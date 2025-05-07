# Keyboard Input Spammer

A simple Python utility that automatically types text from a file multiple times. Useful for quickly sending repetitive messages in chat applications, forms, or any text input field.

## Features

- Reads custom message content from an external text file
- Allows you to specify how many times to repeat the message
- 5-second delay before starting to give you time to select the input field
- Emergency stop with ESC key
- Works with any application that accepts keyboard input

## Requirements

- Python 3.6 or higher
- PyAutoGUI
- Pynput
- Keyboard

## Installation

1. Make sure you have Python installed on your system
2. Install the required packages:

```
pip install pyautogui pynput keyboard
```

## How to Use

1. Rename your `input.txt` file to `spam.txt` (or update the script to use input.txt)
2. Edit the `spam.txt` file with the message you want to send repeatedly
3. Run the script:

```
python spam_input.py
```

4. Enter how many times you want to repeat the message when prompted for "Frequency"
5. Click on the text input field where you want the text to be typed within the 5-second countdown
6. The program will automatically type your message and press Enter after each message
7. Press ESC at any time to stop the program

## Warning

This tool is meant for personal use in appropriate situations. Please use responsibly and be aware that:

- Sending too many messages in quick succession might get you rate-limited or banned on some platforms
- Some applications or websites may have policies against automated messaging
- Respect others' boundaries when sending messages

## How It Works

The script reads your custom message from the text file, then uses PyAutoGUI to simulate keyboard input. It sends the exact text from your file, followed by pressing Enter, repeating this process based on your specified frequency.

A keyboard listener runs in the background to detect if you press ESC, allowing you to stop the program immediately if needed.