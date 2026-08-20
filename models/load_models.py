# models/load_models.py

import os
from tensorflow.keras.models import load_model

def load_all_models():
    models_dict = {}

    # Load image model
    image_model_path = os.path.join("models", "deepfake_detectorv.h5")
    if os.path.exists(image_model_path):
        models_dict["image_model"] = load_model(image_model_path)
        print("[INFO] Image model loaded.")
    else:
        print("[WARNING] Image model not found.")

    # Load audio model
    audio_model_path = os.path.join("models", "deepfake_audio_model.h5")
    if os.path.exists(audio_model_path):
        models_dict["audio"] = load_model(audio_model_path)
        print("[INFO] Audio model loaded.")
    else:
        print("[WARNING] Audio model not found.")

    return models_dict
