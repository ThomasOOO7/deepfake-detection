# utils/audio_analyzer.py

import numpy as np
import librosa

def extract_features(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    mfcc_mean = np.mean(mfcc.T, axis=0)
    return mfcc_mean

def analyze_audio(audio_path):
    from models.load_models import load_all_models
    models = load_all_models()
    model = models["audio"]

    # Extract & normalize features
    features = extract_features(audio_path)
    features = features / np.max(features)
    features = np.expand_dims(features, axis=0)

    prediction = model.predict(features)[0][0]
    verdict = "Fake" if prediction > 0.5 else "Real"
    confidence = round(float(prediction if verdict == "Fake" else 1 - prediction), 4)

    return {
        "type": "audio",
        "verdict": verdict,
        "confidence": confidence
    }
