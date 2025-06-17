

## 🛠️ Requirements

- Python 3.6+
- Tesseract OCR engine
- pip packages: `pytesseract`, `Pillow`

---

## 📦 Installation

1. **Install Python dependencies**:

```bash
pip install pillow pytesseract
```

2. **Install Tesseract**:

- **Windows**: [Download Tesseract](https://github.com/tesseract-ocr/tesseract/wiki)
- **macOS**:
  ```bash
  brew install tesseract
  ```
- **Ubuntu/Linux**:
  ```bash
  sudo apt install tesseract-ocr
  ```

3. *(Optional for Windows)*: Set the Tesseract executable path in the script:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

