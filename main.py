from PIL import Image
import pytesseract

# Load the image
image = Image.open('./image.jpg')  # image file path

# Perform OCR
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
