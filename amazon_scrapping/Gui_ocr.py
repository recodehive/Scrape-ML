import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from io import BytesIO
import random
import os
import csv
import time
import tkinter as tk
from tkinter import filedialog, messagebox

# Update this line with your Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\kulitesh\Scrape-ML\Tesseract-OCR\tesseract.exe'

def take_screenshot_and_analyze(url, output_csv, save_location, num_screenshots=4):
    options = Options()
    options.headless = True

    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        WebDriverWait(driver, 20).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

        # Create a directory to store screenshots if it doesn't exist
        screenshot_dir = os.path.join(save_location, "Screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        data = []  # List to store scraped data

        for i in range(num_screenshots):
            # Scroll down a random amount
            scroll_amount = random.randint(500, 1000)  # Adjust as needed
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            # Add some waiting time after scrolling
            time.sleep(1)  # Adjust scroll time as needed

            # Capture screenshot
            screenshot = driver.get_screenshot_as_png()
            image = Image.open(BytesIO(screenshot))

            # Save screenshot to file
            screenshot_path = os.path.join(screenshot_dir, f"screenshot_{i + 1}.png")
            image.save(screenshot_path)

            # Use Tesseract OCR to extract text
            extracted_text = pytesseract.image_to_string(image)
            print(f"Extracted Text from screenshot {i + 1}:", extracted_text)

            # Add the extracted text to the data list
            data.append({"Screenshot": screenshot_path, "Extracted Text": extracted_text})

        # Write the scraped data to a CSV file
        write_to_csv(data, output_csv, save_location)

    except TimeoutException:
        print("Timed out waiting for page to load")

    finally:
        if 'driver' in locals():
            driver.quit()

def write_to_csv(data, output_csv, save_location):
    # Define CSV file path
    csv_file = os.path.join(save_location, output_csv)

    # Write data to CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Screenshot", "Extracted Text"])
        writer.writeheader()
        writer.writerows(data)

    print(f"Scraped data written to {csv_file}")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    save_location_entry.delete(0, tk.END)
    save_location_entry.insert(0, folder_selected)

def start_analysis():
    url_to_analyze = url_entry.get()
    output_csv = output_csv_entry.get()
    save_location = save_location_entry.get()
    
    if not url_to_analyze or not output_csv or not save_location:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return
    
    take_screenshot_and_analyze(url_to_analyze, output_csv, save_location)
    messagebox.showinfo("Success", f"Scraped data written to {os.path.join(save_location, output_csv)}")

# Set up the main application window
root = tk.Tk()
root.title("Sentiment Analysis Tool")

# Set window size and background color
root.geometry("600x300")
root.configure(bg="black")

# URL input
tk.Label(root, text="Website URL:", bg="black", fg="white").grid(row=0, column=0, padx=10, pady=5, sticky="e")
url_entry = tk.Entry(root, width=50, bg="white", fg="black")
url_entry.grid(row=0, column=1, padx=10, pady=5)

# Output CSV file name input
tk.Label(root, text="Output CSV File Name:", bg="black", fg="white").grid(row=1, column=0, padx=10, pady=5, sticky="e")
output_csv_entry = tk.Entry(root, width=50, bg="white", fg="black")
output_csv_entry.grid(row=1, column=1, padx=10, pady=5)

# Save location input
tk.Label(root, text="Save Location:", bg="black", fg="white").grid(row=2, column=0, padx=10, pady=5, sticky="e")
save_location_entry = tk.Entry(root, width=50, bg="white", fg="black")
save_location_entry.grid(row=2, column=1, padx=10, pady=5)
browse_button = tk.Button(root, text="Browse", command=browse_folder, bg="white", fg="black")
browse_button.grid(row=2, column=2, padx=10, pady=5)

# Start analysis button
start_button = tk.Button(root, text="Start Analysis", command=start_analysis, bg="white", fg="black")
start_button.grid(row=3, column=1, padx=10, pady=20)

# Start the Tkinter event loop
root.mainloop()
