import csv  # for saving words in a CSV file
import os  # for checking if the file exists
from tabulate import tabulate  # for pretty print


class Dictionary:
    FILENAME = 'dictionary.csv'
    FIELDNAMES = ('word', 'translation', 'examples')
    COMMANDS = {'add', 'get', 'edit', 'remove', 'help', 'words', 'translate', 'exit'}

    def __write_to_file(self, data: dict) -> bool:
        """Writes data into a CSV file named dictionary.csv."""
        try:
            file_exists = os.path.isfile(self.FILENAME)
            mode = 'a' if file_exists else 'w'
            with open(self.FILENAME, mode=mode, newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.FIELDNAMES)
                if not file_exists:
                    writer.writeheader()
                writer.writerow(data)
            return True
        except Exception as e:
            print(f"Error writing to file: {e}")
            return False

    def __no_duplicate(self, word):
        """Checks for duplicate words in the dictionary."""
        try:
            with open(self.FILENAME, newline='') as file:
                reader = csv.DictReader(file)
                for el in reader:
                    if el['word'] == word:
                        return True
                return False
        except FileNotFoundError:
            return False
        except Exception as e:
            print(f"Error reading from file: {e}")
            return False

    def no_duplicate(self, word):
        """Public method to check for duplicate words."""
        return not self.__no_duplicate(word)

    def add_word(self, word, translation, examples=''):
        """Adds a new word to the dictionary."""
        data = {
            'word': word,
            'translation': translation,
            'examples': examples
        }
        if self.no_duplicate(word) and self.__write_to_file(data):
            return True
        return False

    def remove_word(self, word):
        """Removes a word from the dictionary."""
        try:
            lines = []
            with open(self.FILENAME, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['word'] != word:
                        lines.append(row)

            with open(self.FILENAME, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.FIELDNAMES)
                writer.writeheader()
                writer.writerows(lines)
            return True
        except Exception as e:
            print(f"Error removing word: {e}")
            return False

    def get_translation(self, word):
        """Retrieve translation and examples for a word."""
        try:
            with open(self.FILENAME) as file:
                reader = csv.DictReader(file)
                for el in reader:
                    if el['word'].lower() == word.lower():
                        return f"Translation: {el['translation']}\nExamples: {el['examples']}"
                return False
        except Exception as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def get_words():
        words = []
        try:
            with open(Dictionary.FILENAME, newline='') as file:
                reader = csv.DictReader(file)
                for el in reader:
                    words.append(el)
            return words
        except FileNotFoundError:
            return "Could not get the words :( Check if the file 'dictionary.csv' exists"


def main():
    my_dict = Dictionary()
    print("""Welcome to the Command-line Dictionary!
Type 'help' to see available commands.""")

    while True:
        command = input("Enter command: ").strip().lower()
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
            elif command.startswith('exit'):
                print("Exiting programm...")
                break
        else:
            print(f"Unknown command {command}. Type 'help' to see available commands")


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
    print(dictionary.get_translation(word))


def get_words_command():
    words_dict = Dictionary.get_words()
    if isinstance(words_dict, list):
        if len(words_dict) == 0:
            print("There are no words yet :(")
        else:

            for el in words_dict:
                word, translation, examples = el.values()
                print(tabulate([[word, translation, examples]],
                               ['Word', 'Translation', 'Examples']))
    else:
        print(words_dict)


def quiz_mode():
    print("Quiz mode is under construction. Check back later!")


if __name__ == '__main__':
    main()
