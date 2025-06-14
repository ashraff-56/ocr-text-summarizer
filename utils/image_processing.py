import cv2
import easyocr
import numpy as np

def preprocess_image_opencv(image, enhance_quality=True):
    """Enhanced image preprocessing using OpenCV"""
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image.copy()
    
    if enhance_quality:
        gray = cv2.GaussianBlur(gray, (1, 1), 0)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        gray = clahe.apply(gray)
    
    height, width = gray.shape
    if width < 1000:
        scale_factor = 1000 / width
        new_width = 1000
        new_height = int(height * scale_factor)
        gray = cv2.resize(gray, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
    
    return gray

def extract_text_with_easyocr(image, enhance_quality=True):
    reader = easyocr.Reader(['en'], gpu=False)
    processed_image = preprocess_image_opencv(image, enhance_quality)
    results = reader.readtext(processed_image)
    filtered_results = [(bbox, text, conf) for bbox, text, conf in results if conf > 0.3]
    text = "\n".join([item[1] for item in filtered_results])
    return text.strip(), filtered_results, processed_image