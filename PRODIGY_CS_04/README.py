# Simple Keylogger

This is a basic keylogger created using Python's `pynput` library. It captures keyboard keystrokes and logs them into a file on the user's system. The keylogger is intended for **educational purposes, security testing**, or **personal monitoring**, and it comes with a disclaimer to ensure ethical and legal compliance.

## Features

- **Keylogging**: Captures all keystrokes and special keys pressed.
- **Logs to File**: Keystrokes are logged to a file named `keyloggers.txt` in the user's home directory.
- **Disclaimer and Consent**: The program displays a disclaimer and requires the user to accept the terms before running.
- **Esc Key to Stop**: The keylogger stops running when the `Esc` key is pressed.

## Disclaimer

By using this tool, you acknowledge and accept the following terms and conditions:

1. You confirm that you have explicit permission from the appropriate authorities to capture keystrokes.
2. You agree to use this keylogger solely for educational purposes, security testing, or personal monitoring.
3. You are responsible for ensuring that your use of this tool complies with all applicable laws and regulations.
4. The creators and contributors of this tool accept no responsibility for any consequences resulting from its use.
5. You agree to respect the privacy of all users on the system.

## Installation and Usage

### Prerequisites

- **Python 3.x** installed on your system.
- Install the `pynput` library by running:

    ```bash
    pip install pynput
    ```

### Running the Keylogger

1. Clone or download this repository.
2. Open a terminal or command prompt in the project directory.
3. Run the Python file:

    ```bash
    python Simple_Keylogger.py
    ```

4. You will be prompted to accept the terms and conditions. Type `Yes` to start the keylogger.
5. The program will log all keystrokes to a file named `keyloggers.txt` in your home directory.

### Stopping the Keylogger

Press the `Esc` key at any time to stop the keylogger.

## How It Works

1. **Logging Configuration**: The program sets up logging to save all captured keystrokes into a file.
2. **Keystroke Capture**: Keystrokes are captured using `pynput.keyboard`'s `Listener`. Both regular keys and special keys are logged.
3. **Ethical Use**: A disclaimer is displayed to ensure users acknowledge legal and ethical responsibilities.

## Legal and Ethical Notice

This keylogger is intended for **educational purposes** only. Unauthorized use of keyloggers can violate privacy laws and ethical guidelines. Make sure you have explicit permission to monitor a system before using this tool.

## Future Improvements

- Add encryption to the log file for security.
- Implement a stealth mode to hide the console window.
- Add the ability to email logs or save them to the cloud.

## Credits

Developed by **Sidharth P Nair**

---

**Important**: Please use this tool responsibly and in compliance with all applicable laws and regulations.
