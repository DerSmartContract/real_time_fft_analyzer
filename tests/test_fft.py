import pytest
import numpy as np
from utils.audio_processing import process_audio


def test_fft_processing():
    """
    Testet die FFT-Verarbeitung.
    """
    N = 1024
    t = np.arange(N) / N  # Gleichmäßige Abtastwerte für eine exakte Periode
    test_signal = 0.5 * np.sin(2 * np.pi * t)  # Sinuswelle mit Amplitude 0.5
    spectrum = process_audio(test_signal, N)

    assert spectrum is not None, "Die FFT-Berechnung liefert keine Werte!"
    assert len(spectrum) == (
        N // 2 + 1
    ), "Die FFT hat die falsche Anzahl an Frequenzkomponenten!"

    # Erwartete Amplitude für eine Sinuswelle mit Amplitude 0.5 ist exakt 0.5
    fundamental_freq_index = 1  # Die Grundfrequenz liegt bei Index 1
    assert np.allclose(
        spectrum[fundamental_freq_index], 0.5, atol=1e-3
    ), f"Die Amplitude der Grundfrequenz ist falsch: {spectrum[fundamental_freq_index]}"

    # Alle anderen Frequenzanteile sollten nahezu null sein
    assert np.allclose(
        spectrum[2:], 0, atol=1e-3
    ), "Es gibt unerwartete hohe Amplituden!"
