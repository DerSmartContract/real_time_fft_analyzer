import pytest
import sounddevice as sd
import numpy as np


def test_audio_stream():
    """
    Testet, ob das Mikrofon Daten aufnimmt.
    """
    fs = 44100
    duration = 1  # 1 Sekunde aufnehmen
    audio_data = sd.rec(int(fs * duration), samplerate=fs, channels=1, dtype="float32")
    sd.wait()  # Warten, bis die Aufnahme beendet ist
    assert audio_data is not None, "Keine Audiodaten aufgenommen!"
    assert np.any(audio_data), "Das Mikrofon hat nur Stille aufgenommen!"
