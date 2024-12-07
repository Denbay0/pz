import random
import string

def print_random_characters():
    """
    1) Составить функцию, которая напечатает сорок любых символов.
    """
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=40))
    print(f"Случайные символы: {random_chars}")

if __name__ == "__main__":
    print_random_characters()
