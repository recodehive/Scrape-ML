import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from io import BytesIO
import random
import os
import csv
import time

# Update this line with your Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\kulitesh\Scrape-ML\Tesseract-OCR\tesseract.exe'

# URL to analyze
url_to_analyze = "https://www.myntra.com/"

def take_screenshot_and_analyze(url, num_screenshots=4):
    options = Options()
    options.headless = True 

    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        WebDriverWait(driver, 20).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

        # Create a directory to store screenshots if it doesn't exist
        if not os.path.exists("Screenshots"):
            os.makedirs("Screenshots")

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
            screenshot_path = f"Screenshots/screenshot_{i + 1}.png"
            image.save(screenshot_path)

            # Use Tesseract OCR to extract text
            extracted_text = pytesseract.image_to_string(image)
            print(f"Extracted Text from screenshot {i + 1}:", extracted_text)

            # Add the extracted text to the data list
            data.append({"Screenshot": screenshot_path, "Extracted Text": extracted_text})

        # Write the scraped data to a CSV file
        write_to_csv(data)

    except TimeoutException:
        print("Timed out waiting for page to load")

    finally:
        if 'driver' in locals():
            driver.quit()

def write_to_csv(data):
    # Define CSV file path
    csv_file = "scraped_data.csv"

    # Write data to CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Screenshot", "Extracted Text"])
        writer.writeheader()
        writer.writerows(data)

    print(f"Scraped data written to {csv_file}")

# Perform screenshot and analysis for multiple screenshots
take_screenshot_and_analyze(url_to_analyze)
