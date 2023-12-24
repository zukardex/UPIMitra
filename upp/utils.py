# upp/utils.py
import cv2
import pytesseract
import base64
import numpy as np

def capture_and_ocr():
    # Open a connection to the webcam (usually 0 for the default webcam)
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None

    # Capture a photo from the webcam
    ret, frame = cap.read()

    # Check if the photo is captured successfully
    if not ret:
        print("Error: Could not capture photo.")
        cap.release()
        return None

    # Convert the photo to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform OCR on the grayscale image
    text = pytesseract.image_to_string(gray)

    # Release the webcam
    cap.release()

    return text
