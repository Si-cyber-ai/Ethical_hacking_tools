print("==============================Password Complexity Checker====================================")
import re

# Function to check password strength
def check_password_strength(password):
    # Regular expression pattern for password strength
    length=len(password) >= 8
    upperis = bool(re.search(r'[A-Z]', password))
    loweris = bool(re.search(r'[a-z]', password))
    digitis = bool(re.search(r'\d', password))
    specialis = bool(re.search(r'[@$!%*?&]', password))
    total=sum([length,upperis,loweris,digitis,specialis])

    # Feedback based on score
    if total == 5 and len(password) >= 16:
        strength = "Very Strong"
    elif total == 5:
        strength = "Strong"
    elif total >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Detailed Feedback
    recommendation = []
    if not length:
        recommendation.append("Password should atleast contain 8 characters")
    if not upperis:
        recommendation.append("Password should atleast contain one uppercase letter")
    if not loweris:
        rcommendation.append("Password should atleast contain one lowercase letter")
    if not digitis:
        recommendation.append("Password should atleast contain one digit")
    if not specialis:
        recommendation.append("Password should atleast contain one special character (e.g., @, $, !, %, *)")
    # Display
    print("Password Strength: ",strength)
    if recommendation:
        print("Feedback: " + ", ".join(recommendation))

# Main Body
password=input("Enter a password to check it's Strength: ")
check_password_strength(password)
