# Password Complexity Checker

This is a simple Password Complexity Checker implemented in Python. The tool evaluates the strength of a given password based on various criteria, providing feedback on its security.

## Features

- **Password Strength Evaluation**: Analyzes passwords based on length, uppercase letters, lowercase letters, digits, and special characters.
- **Feedback on Password Strength**: Categorizes the strength of the password as **Weak**, **Moderate**, **Strong**, or **Very Strong**.
- **Detailed Recommendations**: Offers specific recommendations for improving password strength.

## How It Works

1. **Input**: The user is prompted to enter a password for evaluation.
2. **Validation**: The password is checked against multiple criteria:
   - Minimum length of 8 characters.
   - At least one uppercase letter.
   - At least one lowercase letter.
   - At least one digit.
   - At least one special character (e.g., @, $, !, %, *).
3. **Output**: The program provides feedback on the strength of the password and any necessary improvements.

## Installation and Usage

### Prerequisites

- **Python 3.x** installed on your system.

### Running the Password Checker

1. Clone or download this repository.
2. Open a terminal or command prompt in the project directory.
3. Run the Python file:

    ```bash
    python Pasword_Complexity_Checker.py
    ```

4. You will be prompted to enter a password. The program will then evaluate its strength and provide feedback.

## Example Output

```bash
==============================Password Complexity Checker====================================
Enter a password to check its Strength: Password123!
Password Strength:  Strong
```

## Future Improvements

- Add a graphical user interface (GUI) for user-friendly interaction.
- Implement password generation suggestions for stronger passwords.
- Store commonly used weak passwords and check against them.

## Credits

Developed by **Sidharth P Nair**

---

**Important**: Please use this tool responsibly and ensure that your passwords meet security standards.

