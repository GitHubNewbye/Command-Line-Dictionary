from dictionary import Dictionary
from termcolor import colored


class Quiz(Dictionary):

    def __init__(self):
        self.points = 0

    def start(self):
        print("Hi :) With quiz you can check your knowledge of words.\n"
              "It's also helpful to memorize the words if you forgot it.\n"
              "There is two modes: translation mode and match mode.\n"
              "In translation mode you will get a random word from dictionary and must to translate it\n"
              "Every correct answer is 1 point, the wrong answer is 0 point.\n"
              "In match mode you need to match the words with their translations.\n"
              "Every correct answer is 1 point, the wrong answer is 0 point"
              "Type finish when you want to finish the quiz.")

        quiz_mode = input("Type 'translation' or 'match' to start the quiz: ")
        if quiz_mode == 'translation':
            self.translation_mode()
        elif quiz_mode == 'match':
            self.match_mode()

    def translation_mode(self, word):
        pass

    def match_mode(self):
        pass

    def is_correct(self, word):
        return self.get_translation(word) ==

    def finish(self, points):
        pass