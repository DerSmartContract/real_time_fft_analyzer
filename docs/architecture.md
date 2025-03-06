---

## **📄 2. architecture.md** (Technische Architektur)
📌 **Dateipfad:** `docs/architecture.md`  

```markdown
# Architektur der Echtzeit-FFT-Anwendung

## 📌 Überblick
Diese Applikation nutzt **Fast Fourier Transform (FFT)** zur Umwandlung von **Mikrofon-Audio** in ein Echtzeit-Frequenzspektrum. Die Frequenzen werden analysiert und mit **Matplotlib** visualisiert.

---

## 📂 **Technische Komponenten**
### 🔹 **1. Audioaufnahme (sounddevice)**
- Liest **kontinuierlich Audio-Daten** aus dem Mikrofon.
- Arbeitet mit **blockweise verarbeiteten Samples** (1024 pro Frame).
- Speichert **Rohdaten** für FFT-Analyse.

### 🔹 **2. Signalverarbeitung (NumPy & SciPy)**
- **FFT-Algorithmus zerlegt das Audiosignal** in Frequenzanteile.
- **Normalisierung der Amplitude**, um die Intensität jeder Frequenz sichtbar zu machen.
- Entfernt **Aliasing (Spiegelartefakte)** durch Halbierung der FFT-Daten.

### 🔹 **3. Echtzeit-Visualisierung (Matplotlib)**
- **Live-Update des Frequenzdiagramms** in regelmäßigen Intervallen (~23 ms).
- **X-Achse:** Frequenzen (0 - 22 kHz)
- **Y-Achse:** Amplitude (Signalstärke)

---

## 🔄 **Ablaufdiagramm**
```mermaid
graph TD;
    Start --> |Mikrofonaufnahme| Audio-Stream
    Audio-Stream --> |FFT-Berechnung| Frequenz-Spektrum
    Frequenz-Spektrum --> |Live-Visualisierung| Matplotlib-Graph
    Matplotlib-Graph --> |Aktualisierung alle 23ms| Loop
    Loop --> Audio-Stream