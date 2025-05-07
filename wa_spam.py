# Installation: pip install pyautogui pynput keyboard

import pyautogui, time
import os
from pynput import keyboard

# Variable to track if stop key is pressed
stop_program = False

def on_press(key):
    global stop_program
    # Stop program when Escape key is pressed
    if key == keyboard.Key.esc:
        print("\nEmergency stop activated!")
        stop_program = True
        return False  # Stop listener

# Start keyboard listener in a separate thread
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Get the current directory and construct path to spam.txt
current_dir = os.path.dirname(os.path.abspath(__file__))
spam_file = os.path.join(current_dir, "spam.txt")

# Read message from file
with open(spam_file, 'r', encoding='utf-8') as f:
    msg = f.read().strip()

# Get frequency from user
x = int(input("Frequency: "))

print(f"Will send message from spam.txt ({len(msg)} characters) {x} times.")
print("Starting in 5 seconds... Click where you want to type.")
print("Press ESC key to stop the program at any time.")
time.sleep(5)

for i in range(x):
    if stop_program:
        print("Program stopped by user.")
        break
    pyautogui.write(msg)
    pyautogui.press("enter")
    time.sleep(0.1)

# Clean up
if listener.is_alive():
    listener.stop()