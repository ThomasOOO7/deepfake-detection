import whisperx
import torch
from typing import List, Dict

# Force CPU with float32 (safe for all systems)
model = whisperx.load_model("base", device="cpu", compute_type="float32")

def spot_keywords(audio_path: str, keywords: List[str]) -> Dict:
    kws = [k.lower() for k in keywords]

    # Step 1: Transcribe
    result = model.transcribe(audio_path)

    # Step 2: Align words for timestamps
    model_a, metadata = whisperx.load_align_model(language_code=result["language"], device="cpu")
    aligned = whisperx.align(result["segments"], model_a, metadata, audio_path, "cpu")

    # Step 3: Match keywords
    matches = []
    for segment in aligned.get("word_segments", []):
        word = segment["word"].lower()
        if word in kws:
            matches.append({
                "keyword": word,
                "start": segment["start"],
                "end": segment["end"]
            })

    return {
        "transcription": result["text"],
        "matches": matches
    }
