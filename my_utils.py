import ffmpeg
import numpy as np
import os

def load_audio(file, sr):
    try:
        file = file.strip(" ").strip('"').strip("\n").strip('"').strip(" ")
        print(f"[DEBUG] Attempting to load audio: '{file}'")
        print("[DEBUG] File exists:", os.path.exists(file))
        if os.path.exists(file):
            print("[DEBUG] File size:", os.path.getsize(file), "bytes")

        out, _ = (
            ffmpeg.input(file, threads=0)
            .output("-", format="f32le", acodec="pcm_f32le", ac=1, ar=sr)
            .run(cmd=["ffmpeg", "-nostdin"], capture_stdout=True, capture_stderr=True)
        )
    except Exception as e:
        raise RuntimeError(f"Failed to load audio: {e}")

    return np.frombuffer(out, np.float32).flatten()
