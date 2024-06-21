import csv
import os

class Dictionary:

    def __write_to_file(self, data: dict) -> bool:
        """
        Writes data into a CSV file named dictionary.csv
        """
        file_exists = False
        fieldnames = ['word', 'translation', 'examples']
        if os.path.isfile('dictionary.csv'):
            file_exists = True
        try:
            mode = 'a' if file_exists else 'w'
            with open('dictionary.csv', mode=mode) as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                if mode == 'w':
                    writer.writeheader()
                writer.writerow(data)
            return True
        except:
            pass
        return False

    def __no_duplicate(self, word):
        """ Checks for duplicate words in dictionary"""
        try:
            with open('dictionary.csv') as file:
                reader = csv.DictReader(file)
                for el in reader:
                    if word not in el or word not in el.values():
                        return False
                return True
        except:
            pass
        return False


    def no_duplicate(self, word):
        """ Public method to check for duplicate words """
        return self.__no_duplicate(word)

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
        pass


def main():
    my_dict = Dictionary()
    add = my_dict.add_word('hello', 'privet')

    if my_dict.no_dublicate('hello'):
        if add:
            print("Word added")
        else:
            print("Something gone wrong")
    else:
        print(f"The word <hello> already exists")
    print(my_dict)


if __name__ == '__main__':
    main()
