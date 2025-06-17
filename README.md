🛠️ Requirements

    Python 3.6+

    Tesseract OCR engine

    pip packages: pytesseract, Pillow

  📦 Installation

    Install Python dependencies:

pip install pillow pytesseract

    Install Tesseract:

    Windows: Download Tesseract installer

    macOS:

brew install tesseract

Ubuntu/Linux:

    sudo apt install tesseract-ocr

    (Optional for Windows): Set the Tesseract executable path in the script:

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
