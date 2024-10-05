# Caesar Cipher

This is a simple implementation of the Caesar Cipher in Python. The Caesar Cipher is a classic encryption technique that shifts each letter in the plaintext by a fixed number of positions down the alphabet.

## Features

- **Encryption**: Converts plaintext into ciphertext using a specified shift value.
- **Decryption**: Converts ciphertext back into plaintext using the same shift value.
- **User-Friendly Interface**: Prompts the user for input and displays the results clearly.

## How It Works

1. **Input**: The user is prompted to enter a message, a shift value, and whether to encrypt or decrypt the message.
2. **Processing**:
   - For **encryption** (`E`), each letter in the message is shifted by the specified value.
   - For **decryption** (`D`), the shift is reversed, returning the original message.
3. **Output**: The program outputs the encrypted or decrypted message based on the user's choice.

## Installation and Usage

### Prerequisites

- **Python 3.x** installed on your system.

### Running the Caesar Cipher

1. Clone or download this repository.
2. Open a terminal or command prompt in the project directory.
3. Run the Python file:

    ```bash
    python Implement_Caesar_Cipher.py
    ```

4. Follow the prompts to enter your message, shift value, and choose to encrypt or decrypt.

## Example Usage

```bash
===============Implement Caesar Cipher===============
Enter the Message: Hello, World!
Enter the Shift value: 3
Enter 'E' for encrypt or 'D' for decrypt: E
Encrypted Message:  Khoor, Zruog!
```
## Future Improvements

- **Input Validation**: Add input validation to ensure the shift value is within a valid range.
- **Support for Non-Alphabetical Characters**: Implement support for non-alphabetical characters in the input.
- **Uppercase/Lowercase Options**: Allow the user to specify whether to use uppercase, lowercase, or both.

## Credits

Developed by **Sidharth P Nair**

---

**Important**: Please use this tool responsibly and be aware that while the Caesar Cipher is a fun exercise, it is not secure for real-world applications.
