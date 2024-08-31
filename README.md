# Watermarking App

## Description
This is a simple Python application that allows users to add watermarks to images using a graphical user interface. The app is built using Tkinter for the GUI and Pillow for image processing.

### Features
* Choose an image file to watermark
* Apply a predefined watermark to the chosen image
* Save the watermarked image as a PNG file
* User-friendly graphical interface

### Technologies
* Python

### Python Libs
* Tkinter
* Pillow

## Getting Started
1. Clone this repository.
2. Create virtual environment.
3. Install [requirements](requirements.txt).
4. Run [script](main.py) in Python. 

## Usage
1. Use the "Choose Image" button to select an image file you want to watermark.
2. Click the "Apply Watermark" button to add the watermark to your image.
3. Click the "Save Image" button to save your watermarked image and exit the application.

### File Structure
* `main.py`: The main script containing the application code
* `logo.png`: The logo displayed when the app starts
* `watermark.png`: The watermark image to be applied (should be in the same directory as `main.py`)

### Notes
* The app currently saves the watermarked image as `output.png` in the same directory as the script.
* The watermark is applied at full canvas size, which means it will cover the entire image. You may want to adjust the `apply_watermark()` function to change this behavior.

## Customization
* To change the watermark, replace the `watermark.png` file with your own watermark image.
* You can modify the color scheme by changing the hex color codes at the top of the `main.py` file.
