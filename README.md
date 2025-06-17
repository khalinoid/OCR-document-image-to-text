# 📝 OCR Document Scanner

This project extracts text from scanned documents using Python and Tesseract OCR. It supports image formats like JPG, PNG, and TIFF.

---

## 📸 Features

- Convert scanned images to editable text
- Supports multiple image formats
- Easy to customize and extend
- Based on Tesseract OCR

---

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

---

## 🚀 Usage

```python
from PIL import Image
import pytesseract

# Load image
image = Image.open('scanned_document.jpg')

# Extract text
text = pytesseract.image_to_string(image)

# Output text
print(text)
```

---

## 📁 Example

```
Input:  scanned_document.jpg  
Output:  "This is a sample scanned document."
```

---

## 📄 License

MIT License
