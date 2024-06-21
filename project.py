import csv
import os


class Dictionary:
    FILENAME = 'dictionary.csv'
    FIELDNAMES = ['word', 'translation', 'examples']

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


def main():
    my_dict = Dictionary()
    while True:
        word = get_word_from_user().lower()
        if word == 'exit':
            print("Exiting program.")
            break

        if my_dict.no_duplicate(word):
            translation = get_word_translation()
            example = get_word_usage_exampe()
            if translation.lower() == 'exit':
                print("Exiting program.")
                break
            if my_dict.add_word(word, translation, example):
                print("Word added successfully.")
            else:
                print("Failed to add the word.")
        else:
            translation = my_dict.get_translation(word)
            if translation:
                print(translation)
            else:
                print(f"The word '{word}' does not exist in the dictionary.")


def get_word_from_user():
    return input("Enter the word you want to translate (type 'exit' to exit): ").strip()


def get_word_translation():
    return input("""The word you entered does not exist in the dictionary.
Please enter the translation of the word to add it to the dictionary or type 'exit' to exit: """).strip()

def get_word_usage_exampe():
    return input("Enter some example(optional, press Enter to skip): ")

if __name__ == '__main__':
    main()
