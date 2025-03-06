import numpy as np
from utils.audio_processing import process_audio


def test_fft():
    """
    Testet die FFT-Berechnung mit einem Sinus-Testsignal.
    """
    fs = 44100
    N = 1024
    t = np.linspace(0, 1, fs, endpoint=False)
    freq = 440  # Testfrequenz (A4-Ton)
    test_signal = np.sin(2 * np.pi * freq * t[:N])  # 1024 Samples eines Sinus

    spectrum = process_audio(test_signal, N)
    assert np.argmax(spectrum) == int(freq / (fs / N)), "Fehlende Spitzenfrequenz!"
