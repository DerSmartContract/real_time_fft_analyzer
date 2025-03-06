---

## **📄 3. api.md** (Schnittstellenbeschreibung)
📌 **Dateipfad:** `docs/api.md`  

```markdown
# API-Dokumentation für Echtzeit-FFT

## 📌 Überblick
Diese Datei beschreibt die **internen Funktionen** der Anwendung. Alle Module sind **modular aufgebaut** und können leicht erweitert werden.

---

## 📂 **Module & Funktionen**

### **🔹 `audio_processing.py`**
📄 **Funktion:** `process_audio(audio_data, N)`
```python
def process_audio(audio_data: np.ndarray, N: int) -> np.ndarray: