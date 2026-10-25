
import string
common_passwords = [
    "123456",
    "password",
    "12345678",
    "qwerty",
    "abc123",
    "password123",
    "admin",
    "111111"
]
def check_password(password):
    if password.lower() in common_passwords:
        print("Warning: This is a common password!")
        return

    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter")

    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add at least one number")

    if any(not c.isalnum() for c in password):
        score += 1
    else:
        suggestions.append("Add at least one special character")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    print("\nPassword Strength:", strength)

    if suggestions:
        print("Suggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("Your password meets all the basic checks!")


password = input("Enter a password to analyze: ")
check_password(password)