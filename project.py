import csv
import os


class Dictionary:

    def __write_to_file(self, data: dict) -> bool:
        """
        Writes data into a CSV file named dictionary.csv
        """
        file_exists = os.path.isfile('dictionary.csv')
        fieldnames = ['word', 'translation', 'examples']
        try:
            mode = 'a' if file_exists else 'w'
            with open('dictionary.csv', mode=mode, newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                if not file_exists:
                    writer.writeheader()
                writer.writerow(data)
            return True
        except Exception as e:
            print(f"Error writing to file: {e}")
            return False

    def __no_duplicate(self, word):
        """ Checks for duplicate words in dictionary"""
        try:
            with open('dictionary.csv', newline='') as file:
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
        """ Public method to check for duplicate words """
        return not self.__no_duplicate(word)

    def add_word(self, word, translation, examples=''):
        """
        Adds a new word to the dictionary
        """
        data = {
            'word': word,
            'translation': translation,
            'examples': examples
        }
        if self.no_duplicate(word) and self.__write_to_file(data):
            return True
        return False

    def remove_word(self, word):
        """ Removes a word from the dictionary """
        try:
            lines = []
            with open('dictionary.csv', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['word'] != word:
                        lines.append(row)

            fieldnames = ['word', 'translation', 'examples']
            with open('dictionary.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(lines)
            return True
        except FileNotFoundError:
            return False
        except Exception as e:
            print(f"Error removing word: {e}")
            return False

    def get_translation(self, word):
        try:
            with open('dictionary.csv') as file:
                reader = csv.DictReader(file)
                for el in reader:
                    if el['word'] == word.lower():
                        return f"Translation: {el['translation']}\nExamples: {el['examples']}"
                return False
        except:
            pass


def main():
    my_dict = Dictionary()
    word = get_word_from_user().lower()
    if my_dict.no_duplicate(word):
        pass
    else:
        print(my_dict.get_translation(word))


def get_word_from_user():
    return input("Enter the word you want to translate: ").strip()


def get_word_translation():
    return input("""The word you entered does not exist in dictionary.
Please, enter the translation of the word to add it to the dictionary or type "exit" to exit the programm""").strip()


if __name__ == '__main__':
    main()
