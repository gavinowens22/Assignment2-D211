import random
import string
import os
from datetime import datetime


#this reads the noun file and creates list of words 
with open("top_english_nouns_lower_100000.txt", "r") as file:
    words = file.read().splitlines()


def save_password(password, password_type):
  
    os.makedirs(password_type, exist_ok=True)

    file_path = os.path.join(password_type, "Generated_Passwords.txt")


    current_time = datetime.now().strftime("%A, %B %d, %Y %I:%M:%S %p")

   
    with open(file_path, "a") as file:
        file.write(f"{current_time} - {password}\n")


def memorable_password(num_words, cases):
    passwords = []

    for i in range(num_words):
        random_word = random.choice(words)

        random_case = random.choice(cases)

        if random_case == "upper":
            random_word = random_word.upper()

        random_number = random.randint(0, 9)

        word_with_number = random_word + str(random_number)

        passwords.append(word_with_number)

    final_password = "-".join(passwords)

    save_password(final_password, "Memorable")

    return final_password


def random_password(length, include_punctuation, excluded_characters):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

    if include_punctuation:
        characters += string.punctuation

    #This removes characters that the user does not allow
    for character in excluded_characters:
        characters = characters.replace(character, "")

    password = ""

    for i in range(length):
        password += random.choice(characters)

    save_password(password, "Random")

    return password


def generate_password():
    password_type = input("Would you like a memorable or random password? ").lower()

    if password_type == "memorable":
        num_words = int(input("How many words would you like? "))

        case_choice = input(
            "Enter lower, upper, or both for the available cases: "
        ).lower()

        if case_choice == "upper":
            cases = ["upper"]
        elif case_choice == "lower":
            cases = ["lower"]
        else:
            cases = ["upper", "lower"]

        password = memorable_password(num_words, cases)

        print("Generated password:", password)

    elif password_type == "random":
        length = int(input("How long should the password be? "))

        punctuation_choice = input(
            "Would you like punctuation included? (yes/no): "
        ).lower()

        include_punctuation = punctuation_choice == "yes"

        excluded_characters = input(
            "Enter any characters that are not allowed, or press Enter for none: "
        )

        password = random_password(
            length,
            include_punctuation,
            excluded_characters
        )

        print("Generated password:", password)

    else:
        print("Invalid password type.")


generate_password()
