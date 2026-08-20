# utils/video_analyzer.py

import numpy as np
import cv2
from tensorflow.keras.models import load_model
from PIL import Image

# Load your deepfake detector model
model = load_model("models/deepfake_detectorv.h5")  # Adjust path if needed

def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = image.resize((128, 128))
    image = np.array(image) / 255.0
    return np.expand_dims(image, axis=0)

def analyze_video(filepath):
    try:
        # Preprocess the image
        processed_image = preprocess_image(filepath)

        # Predict using the loaded model
        prediction = model.predict(processed_image)[0][0]

        verdict = "Fake" if prediction > 0.5 else "Real"
        confidence = round(float(prediction if prediction > 0.5 else 1 - prediction), 4)

        return {
            "type": "image",
            "verdict": verdict,
            "confidence": confidence
        }

    except Exception as e:
        return {
            "type": "error",
            "message": f"Error analyzing image: {e}"
        }
