import numpy as np


def process_audio(audio_data, N):
    """
    Berechnet die FFT eines Audiosignals.

    :param audio_data: Eingangs-Audio als NumPy-Array
    :param N: Anzahl der Samples für die FFT
    :return: Amplitudenspektrum
    """
    spectrum = np.abs(np.fft.rfft(audio_data, n=N)) / N  # RFFT für reale Signale nutzen
    return spectrum
