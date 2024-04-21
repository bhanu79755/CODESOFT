import secrets
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_punctuation=False):
    """Generate a randomly generated password."""
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    punctuations = string.punctuation if use_punctuation else ''
    combined_chars = lowercase_letters + uppercase_letters + digits + punctuations
    return ''.join(secrets.choice(combined_chars) for _ in range(length))

# Get user input for password length & complexity
pw_len = int(input("Please enter the desired password length: "))
use_uppercase = bool(int(input("Use UPPERCASE letters? (y/n): ")))
use_digits = bool(int(input("Use DIGITS? (y/n): ")))
use_punctuation = bool(int(input("Use PUNCTUATION? (y/n): ")))

# Generate & Display Password
generated_passwd = generate_password(pw_len, use_uppercase, use_digits, use_punctuation)
print(f"\nGenerated Password: {generated_passwd}\n")