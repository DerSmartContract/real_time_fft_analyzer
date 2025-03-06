import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
from utils.audio_processing import process_audio
from utils.visualization import update_plot

# Parameter für die Audioaufnahme
fs = 44100  # Sampling-Rate in Hz (CD-Qualität)
N = 1024  # Anzahl der Samples pro Frame
time_window = 50  # Zeitfenster für Visualisierung (in ms)

# Frequenzachse für die Darstellung
freqs = np.fft.rfftfreq(N, d=1 / fs)

# Echtzeit-Plot vorbereiten
fig, ax = plt.subplots()
(line,) = ax.plot(freqs, np.zeros_like(freqs))
ax.set_xlim(0, fs // 2)  # Nur positive Frequenzen anzeigen
ax.set_ylim(0, 1)  # Dynamische Skalierung wird später gesetzt
ax.set_xlabel("Frequenz (Hz)")
ax.set_ylabel("Amplitude")
ax.set_title("Echtzeit Frequenzanalyse (FFT)")


def audio_callback(indata, frames, time, status):
    """Wird für jedes Audio-Frame aufgerufen und aktualisiert das Frequenzspektrum"""
    if status:
        print(status)
    spectrum = process_audio(indata[:, 0], N)  # FFT berechnen
    update_plot(line, ax, spectrum, fs, N)  # fs und N übergeben


# Stream starten
with sd.InputStream(callback=audio_callback, channels=1, samplerate=fs, blocksize=N):
    plt.show()
