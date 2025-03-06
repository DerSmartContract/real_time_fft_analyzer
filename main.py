import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import queue
import logging
from utils.audio_processing import process_audio
from utils.visualization import update_plot

# Logging konfigurieren
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Parameter für die Audioaufnahme
fs = 44100  # Sampling-Rate in Hz (CD-Qualität)
N = 1024  # Anzahl der Samples pro Frame

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
plt.ion()  # Interaktiver Modus für Echtzeit-Updates

# Warteschlange für Audiodaten, um Probleme mit Threads zu vermeiden
audio_queue = queue.Queue()


def audio_callback(indata, frames, time, status):
    """Speichert Audiodaten in einer Warteschlange für den Hauptthread"""
    if status:
        logging.warning(f"Stream-Fehler: {status}")
    audio_queue.put(indata[:, 0])  # Speichert die aktuellen Samples für den Hauptthread


def update_plot_from_queue():
    """Holt Audiodaten aus der Queue und aktualisiert das Plot"""
    while True:
        if not audio_queue.empty():
            audio_data = audio_queue.get()
            spectrum = process_audio(audio_data, N)
            update_plot(line, ax, spectrum, fs, N)
        plt.pause(0.01)  # Matplotlib GUI aktiv halten


# Startet Sound-Stream **im Hauptthread**
with sd.InputStream(callback=audio_callback, channels=1, samplerate=fs, blocksize=N):
    print("✅ Echtzeit FFT-Analyse gestartet. Fenster bleibt offen...")
    update_plot_from_queue()  # Hält GUI aktiv, verarbeitet Audio
