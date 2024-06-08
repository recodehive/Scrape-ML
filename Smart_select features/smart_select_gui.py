import os
import cv2
import pytesseract
import numpy as np
from tkinter import Tk, filedialog, Text, Button, Label, Scrollbar, RIGHT, Y, BOTH, END, Frame, Entry, messagebox
from PIL import Image, ImageEnhance, ImageFilter, ImageTk

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

def save_extracted_text(file_path, extracted_text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(extracted_text)
    
    messagebox.showinfo("Saved", f"Extracted text saved to {file_path}")

def gui_main():
    def upload_image():
        file_path = filedialog.askopenfilename(
            initialdir=os.path.join(os.path.expanduser("~"), "Desktop"),
            title="Select an Image from Desktop",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
        )
        
        if file_path:
            try:
                image = preprocess_image(file_path)
                sections = segment_image(image)
                extracted_text = ""
                for section in sections:
                    text = extract_text_from_section(image, section)
                    if text:
                        extracted_text += text + "\n" + "-" * 40 + "\n"

                if extracted_text:
                    text_area.delete('1.0', END)
                    text_area.insert(END, extracted_text)
                    display_image(file_path)
                else:
                    text_area.delete('1.0', END)
                    text_area.insert(END, "No text extracted.")
            except Exception as e:
                text_area.delete('1.0', END)
                text_area.insert(END, f"Error: {str(e)}")

    def display_image(image_path):
        img = Image.open(image_path)
        img.thumbnail((250, 250))
        img = ImageTk.PhotoImage(img)
        panel.config(image=img)
        panel.image = img

    def save_text():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", ".txt"), ("All files", ".*")]
        )
        if file_path:
            extracted_text = text_area.get("1.0", END)
            save_extracted_text(file_path, extracted_text)

    root = Tk()
    root.title("OCR Application")
    root.configure(bg='black')

    frame = Frame(root, bg='black')
    frame.pack(pady=10)

    label = Label(frame, text="Upload an Image for OCR", bg='black', fg='white')
    label.pack(pady=10)

    upload_button = Button(frame, text="Upload Image", command=upload_image, bg='white', fg='black')
    upload_button.pack(pady=5)

    save_button = Button(frame, text="Save Extracted Text", command=save_text, bg='white', fg='black')
    save_button.pack(pady=5)

    text_frame = Frame(root)
    text_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    scrollbar = Scrollbar(text_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    text_area = Text(text_frame, wrap='word', yscrollcommand=scrollbar.set, height=20, bg='black', fg='white', insertbackground='white')
    text_area.pack(fill=BOTH, expand=True)
    scrollbar.config(command=text_area.yview)

    panel = Label(frame, bg='black')
    panel.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    gui_main()
