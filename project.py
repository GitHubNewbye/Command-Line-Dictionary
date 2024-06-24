import os
from tabulate import tabulate  # for pretty print
from dictionary import Dictionary  # main class for working with dictionary
from quiz import Quiz  # for quiz mode
from termcolor import colored  # for styling


def main():
    my_dict = Dictionary()
    print(colored("""Welcome to the Command-line Dictionary!
Type 'help' to see available commands.""", "green"))
    quiz_mode = False

    while True:
        command = input(colored("Enter command: ", "green")).strip().lower()
        if command in my_dict.COMMANDS:
            if command.startswith('add'):
                add_word_command(my_dict)
            elif command.startswith('translate'):
                get_translation_command(my_dict)
            elif command.startswith('remove'):
                remove_word_command(my_dict)
            elif command.startswith('words'):
                get_words_command()
            elif command.startswith('help'):
                print_help()
            elif command.startswith('quiz'):
                quiz_mode = True
                break
            elif command.startswith('exit'):
                print("Exiting programm...")
                break
        else:
            print(colored(f"Unknown command {command}. Type 'help' to see available commands", "red"))

    if quiz_mode:
        start_quiz()


def print_help():
    print("""
Available Commands:
- add: Add a new word to the dictionary.
- remove: Remove a word from the dictionary.
- words: Show all words with their translations
- translate: Get translation
- quiz: Enter quiz mode to test your knowledge.
- help: Display available commands
- exit: Exit the program.
""")


def add_word_command(dictionary):
    word = input("Enter the word you want to add: ").strip().lower()
    if dictionary.no_duplicate(word):
        translation = input(f"Enter the translation of '{word}': ").strip()
        examples = input("Enter usage example (optional, press Enter to skip): ").strip()
        if dictionary.add_word(word, translation, examples):
            print(f"'{word}' added to the dictionary.")
        else:
            print(f"Failed to add '{word}' to the dictionary.")
    else:
        print(f"'{word}' already exists in the dictionary.")
        print(dictionary.get_translation(word))


def remove_word_command(dictionary):
    word = input("Enter the word you want to remove: ").strip().lower()
    if dictionary.no_duplicate(word):
        print(f"'{word}' does not exist in the dictionary.")
    elif dictionary.remove_word(word):
        print(f"'{word}' removed from the dictionary.")
    else:
        print(f"Failed to remove '{word}' from the dictionary.")


def get_translation_command(dictionary):
    word = input("Enter the word you want to translate: ")
    translation = dictionary.get_translation(word)
    print(translation if translation else "No such word in dictionary")


def get_words_command():
    words_dict = Dictionary.get_words()
    if isinstance(words_dict, list):
        if len(words_dict) == 0:
            print("There are no words yet :(")
        else:
            for el in words_dict:
                word, translation, examples = el.values()
                print(tabulate([[word, translation, examples]],
                               ['Word', 'Translation', 'Examples'], tablefmt='pretty'))
    else:
        print(words_dict)


def start_quiz():
    quiz = Quiz()
    quiz.start()


if __name__ == '__main__':
    main()
