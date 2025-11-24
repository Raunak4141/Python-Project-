import string
import secrets

# This function creates a random password using letters, numbers, and symbols.
def generate_password(length=12):
    # All characters we can use for the password:
    allowed_characters = string.ascii_letters + string.digits + string.punctuation

    # Build the password one character at a time using secure randomness
    password = ""
    for _ in range(length):
        password += secrets.choice(allowed_characters)

    return password


# This function checks how strong a password is.
def check_strength(password):
    length = len(password)

    # Look for different character types
    has_lower = any(ch.islower() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_symbol = any(ch in string.punctuation for ch in password)

    # Count how many character types the password uses
    score = has_lower + has_upper + has_digit + has_symbol

    # Decide strength based on length + variety
    if length >= 12 and score == 4:
        return "Strong"
    elif length >= 8 and score >= 3:
        return "Moderate"
    else:
        return "Weak"


def main():
    print("=== Friendly Password Generator ===")

    # Ask the user what length they want the password to be
    try:
        length = int(input("How long should the password be? (Try 12 or more): "))
    except ValueError:
        print("That's not a number! I'll use 12 as the length.")
        length = 12

    # Generate the password
    password = generate_password(length)

    # Check the strength of the created password
    strength = check_strength(password)

    # Show results
    print("\nYour new password is:", password)
    print("Password strength:", strength)


# This makes sure the program runs only when executed directly.
if __name__ == "__main__":
    main()
