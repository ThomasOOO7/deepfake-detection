import os
import time
import numpy as np
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from PIL import Image

from models.load_models import load_all_models
from utils.audio_analyzer import analyze_audio
from utils.video_analyzer import analyze_video
from utils.keyword_spotter import spot_keywords

# === Flask App Setup ===
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB limit
ALLOWED_EXTENSIONS = {'mp4', 'mov', 'avi', 'mp3', 'wav', 'png', 'jpg', 'jpeg'}

# === Load All Models at Startup ===
models = load_all_models()

# === Utility ===
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def safe_delete(filepath):
    if os.path.exists(filepath):
        try:
            os.remove(filepath)
        except PermissionError:
            time.sleep(0.3)
            try:
                os.remove(filepath)
            except Exception as e:
                print(f"[WARN] Could not delete file {filepath}: {e}")

# === Routes ===
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/detect', methods=['POST'])
def detect():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Unsupported file type"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    try:
        ext = filename.rsplit('.', 1)[1].lower()

        if ext in ['mp4', 'avi', 'mov']:
            result = analyze_video(filepath)

        elif ext in ['mp3', 'wav']:
            result = analyze_audio(filepath)

        else:
            # Use your Keras image model (.h5)
            with Image.open(filepath) as img:
                img = img.convert("RGB")
                img = img.resize((128, 128))
                img_array = np.array(img) / 255.0
                img_array = np.expand_dims(img_array, axis=0)

                model = models["image_model"]
                prediction = model.predict(img_array)[0][0]

                verdict = "Fake" if prediction > 0.5 else "Real"
                confidence = round(float(prediction if prediction > 0.5 else 1 - prediction), 4)

                result = {
                    "type": "image",
                    "verdict": verdict,
                    "confidence": confidence
                }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        safe_delete(filepath)

@app.route('/api/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Unsupported file type"}), 400

    keywords = request.form.get("keywords", "")
    if not keywords.strip():
        return jsonify({"error": "No keywords provided"}), 400

    keyword_list = [kw.strip() for kw in keywords.split(',') if kw.strip()]
    if not keyword_list:
        return jsonify({"error": "Invalid keywords format"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    try:
        result = spot_keywords(filepath, keyword_list)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        safe_delete(filepath)

# === Run App ===
if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(host='0.0.0.0', port=5000, threaded=True)
