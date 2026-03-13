import random
import string
def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 for better security.")


    # Combine uppercase, lowercase, digits, and punctuation
    all_chars = string.ascii_letters + string.digits + string.punctuation


    # Ensuring that the password contains at least one character from each category
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]


    # Using random choices to fill the remaining
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    
    try:
        length = int(input("Enter desired password length (minimum 4): "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")