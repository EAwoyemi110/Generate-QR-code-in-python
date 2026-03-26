# QR Code Generator v1

A simple Python QR code generator built with Tkinter. This project lets a user type text into a small desktop app and generate a QR code that is saved as a PNG image.

This is **version 1** of a bigger idea. Right now, the app focuses on the core functionality: taking user input, creating a QR code, and saving it locally. Later versions can expand on this with a better interface, custom file names, color options, downloadable images, and more advanced QR code features.

## Features

- Simple Tkinter desktop interface
- Text input field for the QR code content
- Button to generate the QR code
- Saves the QR code as a `.png` image
- Beginner-friendly Python project

## Built With

- Python
- Tkinter
- PyQRCode
- pypng

## How It Works

1. The user opens the application
2. The user types text or a link into the input box
3. The app generates a QR code from that input
4. The QR code is saved as `myqr.png`

## Installation

Make sure Python is installed, then install the required libraries:

```bash
pip install pyqrcode pypng
