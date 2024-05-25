import os
import cv2
import pytesseract
import numpy as np
from tkinter import Tk, filedialog
from PIL import Image, ImageEnhance, ImageFilter

# Manually specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\kulitesh\Tesseract-OCR\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    # Open the image using PIL
    image = Image.open(image_path)

    # Convert to grayscale
    image = image.convert('L')

    # Increase contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)

    # Apply a median filter to remove noise
    image = image.filter(ImageFilter.MedianFilter(size=3))

    # Convert the image to a NumPy array for OpenCV processing
    image = cv2.cvtColor(np.array(image), cv2.COLOR_GRAY2BGR)

    return image

def segment_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort contours by area (largest first)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    sections = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 50 and h > 50:  # Filter out small contours
            sections.append((x, y, w, h))

    return sections

def extract_text_from_section(image, section):
    x, y, w, h = section
    roi = image[y:y+h, x:x+w]

    # Use Tesseract to extract text with custom configuration
    custom_config = r'--oem 3 --psm 6 -l eng'
    text = pytesseract.image_to_string(roi, config=custom_config)

    return text

def save_extracted_text(image_path, extracted_text):
    base_name = os.path.splitext(image_path)[0]
    text_file_path = base_name + "_extracted_text.txt"

    with open(text_file_path, 'w', encoding='utf-8') as file:
        file.write(extracted_text)
    
    print(f"Extracted text saved to {text_file_path}")

def main():
    # Hide the root window
    Tk().withdraw()

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    screenshots_smart_dir = os.path.join(script_dir, 'screenshots_smart')

    if os.path.exists(screenshots_smart_dir):
        # If screenshots_smart folder exists, ask the user to select an image from there
        image_path = filedialog.askopenfilename(initialdir=screenshots_smart_dir, title="Select a Screenshot", filetypes=[("Image Files", ".png;.jpg;.jpeg;.bmp;*.tiff")])
    else:
        print(f"'screenshots_smart' folder not found in {script_dir}. Please select an image file.")
        # Ask user to add a photo
        image_path = filedialog.askopenfilename(title="Select a Screenshot", filetypes=[("Image Files", ".png;.jpg;.jpeg;.bmp;*.tiff")])

        # If no file is selected, search for images on the Desktop
        if not image_path:
            desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")
            image_files = [f for f in os.listdir(desktop_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
            
            if image_files:
                image_path = os.path.join(desktop_dir, image_files[0])
                print(f"Using image found on Desktop: {image_path}")
            else:
                print("No images found on Desktop.")
                return
    
    # Check if the user selected a file
    if not image_path:
        print("No file selected.")
        return

    # Preprocess the image
    image = preprocess_image(image_path)

    # Segment the image into sections
    sections = segment_image(image)

    # Extract text from each section and aggregate it
    extracted_text = ""
    for section in sections:
        text = extract_text_from_section(image, section)
        if text:
            extracted_text += text + "\n" + "-" * 40 + "\n"

    # Print and save the extracted text
    if extracted_text:
        print("Extracted Text:")
        print(extracted_text)
        save_extracted_text(image_path, extracted_text)
    else:
        print("No text extracted.")

if __name__ == "__main__":
    main()
