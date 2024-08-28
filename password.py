import random
import string

class PasswordGenerator:
    def __init__(self):
        self.include_uppercase = True
        self.include_lowercase = True
        self.include_digits = True
        self.include_special = True

    def get_user_preferences(self):
        print("Password Preferences:")
        self.include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
        self.include_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == "yes"
        self.include_digits = input("Include digits? (yes/no): ").strip().lower() == "yes"
        self.include_special = input("Include special characters? (yes/no): ").strip().lower() == "yes"
        
    def get_password_length(self):
        while True:
            try:
                length = int(input("Enter the desired password length (minimum 6): "))
                if length >= 6:
                    return length
                else:
                    print("Password length must be at least 6.")
            except ValueError:
                print("Please enter a valid number.")

    def generate_password(self, length):

        characters = ''
        if self.include_uppercase:
            characters += string.ascii_uppercase
        if self.include_lowercase:
            characters += string.ascii_lowercase
        if self.include_digits:
            characters += string.digits
        if self.include_special:
            characters += string.punctuation

        if not characters:
            raise ValueError("No character types selected. Cannot generate password.")

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def run(self):
        self.get_user_preferences()
        length = self.get_password_length()
        password = self.generate_password(length)
        print("Generated password:", password)

def main():
    PasswordGenerator.run()

if __name__ == "__main__":
    main()
