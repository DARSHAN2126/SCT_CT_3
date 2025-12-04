import string

def check_password_strength(password: str) -> dict:
    """
    Assesses the strength of a password based on five key criteria.

    The overall strength is scored out of 5, where each criterion met
    adds 1 point.

    Criteria:
    1. Length: Must be 8 characters or more.
    2. Uppercase: Must contain at least one uppercase letter.
    3. Lowercase: Must contain at least one lowercase letter.
    4. Digit: Must contain at least one number (0-9).
    5. Special Character: Must contain at least one punctuation mark.

    Args:
        password: The string to be evaluated.

    Returns:
        A dictionary containing boolean results for each criterion, the
        numerical score, and the descriptive strength level.
    """
    # 1. Length Criterion (>= 8 characters)
    length_criteria = len(password) >= 8

    # 2. Uppercase Criterion
    upper_criteria = any(char.isupper() for char in password)

    # 3. Lowercase Criterion
    lower_criteria = any(char.islower() for char in password)

    # 4. Digit Criterion
    digit_criteria = any(char.isdigit() for char in password)

    # 5. Special Character Criterion (uses standard punctuation)
    # string.punctuation includes symbols like !@#$%^&*()_+...
    special_criteria = any(char in string.punctuation for char in password)

    # Calculate the total score
    score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

    # Determine descriptive strength based on the score
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return {
        "length": length_criteria,
        "uppercase": upper_criteria,
        "lowercase": lower_criteria,
        "digits": digit_criteria,
        "special_chars": special_criteria,
        "score": score,
        "strength": strength
    }


def main():
    """
    Runs the main password checker application loop.
    """
    print("=" * 35)
    print("=== P Y T H O N   P A S S W O R D   C H E C K E R ===")
    print("=" * 35)

    try:
        password = input("Enter a password to check: ")

        if not password:
            print("No password entered. Exiting.")
            return

        result = check_password_strength(password)

        print("\n--- Password Strength Report ---")
        print(f"Password: {password}")
        print("-" * 34)
        print(f"| Criterion             | Met? |")
        print("-" * 34)
        print(f"| Length (>=8)          | {'✅' if result['length'] else '❌'}    |")
        print(f"| Uppercase Letter (A-Z)| {'✅' if result['uppercase'] else '❌'}    |")
        print(f"| Lowercase Letter (a-z)| {'✅' if result['lowercase'] else '❌'}    |")
        print(f"| Digit (0-9)           | {'✅' if result['digits'] else '❌'}    |")
        print(f"| Special Char (!@#$...) | {'✅' if result['special_chars'] else '❌'}    |")
        print("-" * 34)
        print(f"Total Score: {result['score']} / 5")
        print(f"\nOverall Strength: {result['strength']}")
        print("\nTip: Aim for 'Strong' or 'Very Strong'!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
