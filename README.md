# Assignment2-D211
#Password Generator
#Gavin Owens

# Password Generator

## Purpose


This project is a password generator made in Python that is able to create memorable passwords and random passwords. Memorable passwords are created by the code randomly selecting woords from a provided list of english nouns. After that each word is given a ranom integer. For example if I get the word "engine" then it could be followed by "engine1" or "engine5". The word can be uppercase or lowercase. The words are then joined together using hypens.Random passwords are created by randomly selecting characters from lowercase letters, uppercase letters, numbers, and optionally punctuation symbols. The user can also specify characters that they do not want included in the password. Generated passwords are saved along with the day, date, and time they were created.

## How to Use

Run `password_generator.py` and choose whether you want to generate a memorable or random password.

### Memorable Password Input

The user provides:
- Number of words
- Available cases (uppercase, lowercase, or both)

Example output:

'MOUNTAIN4-engine-POWER1-car2'

Memorable passwords are saved in:
'Memorable/Generated_Passwords.txt'


### Random Password Input

The user provides:
- Length of the password
- Whether punctuation should be included
- Any characters that are not allowed

Example output:

"K8v#2mR!5xQ'

Random passwords are saved in:
'Random/Generated_Passwords.txt'

`

## Modules Used

- "random" - Used to randomly select words, numbers, cases, and characters.
- "string - Provides collections of lowercase letters, uppercase letters, numbers, and punctuation.
- "os" - Used to create directories and file paths.
- "datetime" - Used to record the day, date, and time each password is generated.

## Files

"password_generator.py" - Main Python program.
"top_english_nouns_lower_100000.txt" - List of nouns used to create memorable passwords.
"Memorable/Generated_Passwords.txt" - Stores generated memorable passwords.
"Random/Generated_Passwords.txt" - Stores generated random passwords.
