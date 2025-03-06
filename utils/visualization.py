import numpy as np
import matplotlib.pyplot as plt


def update_plot(line, ax, spectrum, fs, N):
    """
    Aktualisiert das Frequenzspektrum im Plot.

    :param line: Matplotlib-Linienobjekt
    :param ax: Matplotlib Achsen-Objekt
    :param spectrum: FFT-Werte zur Darstellung
    :param fs: Sampling-Rate in Hz
    :param N: Anzahl der Samples
    """
    freqs = np.fft.rfftfreq(N, d=1 / fs)  # Frequenzachse neu berechnen

    if len(freqs) != len(spectrum):  # Falls Shapes nicht übereinstimmen, trimmen
        min_len = min(len(freqs), len(spectrum))
        freqs = freqs[:min_len]
        spectrum = spectrum[:min_len]

    line.set_xdata(freqs)  # Frequenzachse aktualisieren
    line.set_ydata(spectrum)  # Spektrum aktualisieren

    ax.set_xlim(0, fs // 2)  # Frequenzbereich von 0 bis Nyquist-Frequenz
    ax.set_ylim(
        0, max(spectrum) * 1.2 if max(spectrum) > 0 else 1
    )  # Dynamische Skalierung

    ax.relim()
    ax.autoscale_view()
    plt.pause(0.01)
