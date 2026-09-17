import random

with open("top_english_nouns_lower_100000.txt", "r") as file:
    words = file.read().splitlines()

passwords = []

num_words = 4

for i in range(num_words):
    random_word = random.choice(words)
    random_number = random.randint(0, 9)
    word_with_number = random_word + str(random_number)
    passwords.append(word_with_number)

final_password = "-".join(passwords)
