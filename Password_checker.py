import re
import math

# Sample dictionary of common weak passwords
weak_passwords = [
    'password', '123456', '12345678', 'admin', 'qwerty', 'letmein', 'welcome',
    'abc123', 'iloveyou', '111111', '123123', 'passw0rd'
]

# Estimate time to crack (returns string with appropriate units)
def estimate_crack_time(entropy, guesses_per_sec=1e10):
    total_combinations = 2 ** entropy
    avg_attempts = total_combinations / 2
    seconds = avg_attempts / guesses_per_sec

    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    elif seconds < 2592000:
        return f"{seconds/86400:.2f} days"
    elif seconds < 31104000:
        return f"{seconds/2592000:.2f} months"
    else:
        return f"{seconds/31104000:.2f} years"

# Check password entropy
def calculate_entropy(password):
    charset = 0
    if re.search(r'[a-z]', password):
        charset += 26
    if re.search(r'[A-Z]', password):
        charset += 26
    if re.search(r'\d', password):
        charset += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        charset += 32
    entropy = len(password) * math.log2(charset) if charset else 0
    return entropy

# Detect common patterns
def has_common_pattern(password):
    patterns = ['1234', 'abcd', 'qwerty', '1111', '0000']
    for pattern in patterns:
        if pattern in password.lower():
            return True
    return False

# Check against weak dictionary passwords
def is_dictionary_word(password):
    return password.lower() in weak_passwords

# Evaluate password
def check_password_strength(password):
    entropy = calculate_entropy(password)
    crack_time = estimate_crack_time(entropy)
    issues = []

    if len(password) < 8:
        issues.append("Use at least 8 characters.")
    if not re.search(r'[A-Z]', password):
        issues.append("Add uppercase letters.")
    if not re.search(r'[a-z]', password):
        issues.append("Add lowercase letters.")
    if not re.search(r'\d', password):
        issues.append("Add numbers.")
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        issues.append("Add special characters.")
    if is_dictionary_word(password):
        issues.append("Avoid common dictionary passwords.")
    if has_common_pattern(password):
        issues.append("Avoid common patterns like '1234' or 'abcd'.")

    # Determine strength level
    if entropy >= 60 and not issues:
        strength = "Very Strong"
    elif entropy >= 50:
        strength = "Strong"
    elif entropy >= 40:
        strength = "Moderate"
    else:
        strength = "Weak"

    print(f"\nPassword: {password}")
    print(f"Entropy: {entropy:.2f} bits")
    print(f"Estimated time to crack: {crack_time}")
    print(f"Strength: {strength}")
    if issues:
        print("Suggestions to improve your password:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("✅ Your password looks good!")

# Run from terminal
if __name__ == "__main__":
    user_password = input("🔐 Enter a password to test: ")
    check_password_strength(user_password)