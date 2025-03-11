import re

def assess_password_strength(password):
    """
    Assesses the strength of a password based on length, character types, and provides feedback.

    Args:
        password: The password to assess.

    Returns:
        A tuple containing the strength score (0-100) and feedback message.
    """

    score = 0
    feedback = []

    # Length criteria
    length = len(password)
    if length >= 12:
        score += 30
        feedback.append("Excellent length!")
    elif 8 <= length < 12:
        score += 20
        feedback.append("Good length.")
    else:
        feedback.append("Consider increasing the password length (at least 8 characters).")

    # Character type criteria
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    if has_upper:
        score += 15
    else:
        feedback.append("Include uppercase letters.")

    if has_lower:
        score += 15
    else:
        feedback.append("Include lowercase letters.")

    if has_digit:
        score += 20
    else:
        feedback.append("Include numbers.")

    if has_special:
        score += 20
    else:
        feedback.append("Include special characters.")

    #Overall strength feedback
    if score >= 90:
        overall_feedback = "Very strong password!"
    elif 70 <= score < 90:
        overall_feedback = "Strong password."
    elif 50 <= score < 70:
        overall_feedback = "Moderate password strength."
    else:
        overall_feedback = "Weak password."

    return score, f"{overall_feedback} {' '.join(feedback)}"

# Example Usage
password = input("Enter your password: ")
strength, feedback = assess_password_strength(password)

print(f"Password Strength: {strength}/100")
print(f"Feedback: {feedback}")