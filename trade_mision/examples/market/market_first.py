import cv2 as cv
from pytesseract import pytesseract
pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# img = cv.imread('teseracttest.png', cv.IMREAD_UNCHANGED)
img = cv.imread('test40.png', cv.IMREAD_UNCHANGED)
text = pytesseract.image_to_string(img)
print(text)