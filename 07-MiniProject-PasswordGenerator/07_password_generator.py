# 1. Import necessary functionality
import secrets
import string
import random


# 2. Create a class
class Password:
    # 3. Initialize our class
    def __init__(self, length: int = 12, uppercase: bool = True, symbols: bool = True) -> None:
        self.length = length
        self.use_uppercase = uppercase
        self.use_symbols = symbols

        # 4. Get characters from the string module
        self.base_characters: str = string.ascii_lowercase + string.digits

        # 5. Add symbols and uppercases characters if the user wants them
        if self.use_uppercase:
            self.base_characters += string.ascii_uppercase
        if self.use_symbols:
            self.base_characters += string.punctuation

    # 6. Create a method to generate the password
    def generate(self) -> str:
        password: list[str] = []

        for i in range(self.length):
            password.append(secrets.choice(self.base_characters))

        return ''.join(password)

    # Check the password's strenght
    def password_check(self, password: str) -> str:
        length_ok = len(password) > 15
        has_upper = any(char.isupper() for char in password)
        has_symbol = any(char in string.punctuation for char in password) 
        
        if length_ok and has_upper and has_symbol:
            return "Is Strong"
        elif length_ok or (has_upper and has_symbol):
            return "Is Safe"
        elif length_ok or has_upper or has_symbol:
            return "Is low"
        else:
            return "Is weak"


# 7. Create the main entry point
def main() -> None:

    for i in range(10):
        random_lenght = random.randint(10, 20)
        random_upper = random.choice([True, False])
        random_symbols = random.choice([True, False])


        password: Password = Password(random_lenght, random_upper, random_symbols)
        generated: str = password.generate()
        is_safe = password.password_check(generated)
        
        print(f'{generated} | {(is_safe)}')


# 8. Run the script
if __name__ == '__main__':
    main()

"""
Homework:
1. Create a method in the Password class which checks the passwords strength. 
- check that the password is more than 16 characters long
- check that the password both contains uppercase characters and symbols

"""