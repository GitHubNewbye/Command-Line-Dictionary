from dictionary import Dictionary
from random import choice
from termcolor import colored


class Quiz(Dictionary):

    def __init__(self):
        self.points = 0
        self.__correct_answers = 0
        self.__incorrect_answers = 0
        self.__MINWORDSCOUNT = 6

    def __are_enough_words(self):
        return len(self.get_words()) >= self.__MINWORDSCOUNT

    def start(self):
        if not self.__are_enough_words():
            print(f"There are not enough words to start the quiz. There must be at least {self.__MINWORDSCOUNT} words")
        else:
            print("Hi :) With quiz you can check your knowledge of words.\n"
                  "It's also helpful to memorize the words if you forgot it.\n"
                  "There is two modes: translation mode and match mode.\n"
                  "In translation mode you will get a random word from dictionary and must to translate it.\n"
                  "Every correct answer is 1 point, the wrong answer is 0 point.\n"
                  "In match mode you need to match the words with their translations.\n"
                  "Every correct answer is 1 point, the wrong answer is 0 point.\n"
                  "Type finish when you want to finish the quiz.")

            quiz_mode = input("Type 'translation' or 'match' to start the quiz: ")
            if quiz_mode == 'translation':
                self.translation_mode()
            elif quiz_mode == 'match':
                self.match_mode()

    def translation_mode(self):
        points = 0
        while True:
            word = self.get_random_word()
            word_translation = self.get_translation(word)['Translation']

            user_answer = input(f"Type the translation of the word '{colored(word, attrs=['bold'], color='blue')}' "
            f"or '{colored('finish', 'red', attrs=['bold'])}'  to exit the quiz: ")

            if user_answer == 'finish':
                self.points = self.__correct_answers
                break
            if user_answer == word_translation:
                print(colored("Correct :)", "green"))
                self.__correct_answers += 1
            else:
                print(colored("Incorrect :(", "red"))
                self.__incorrect_answers += 1
        result = f"You got {self.points} points\n" + \
        colored(f"Correct answers: {self.__correct_answers}\n", "green") + \
        colored(f"Incorrect answers: {self.__incorrect_answers}", "red")

        print(result)

    def match_mode(self):
        pass


    def get_random_word(self):
        return choice(self.get_words())['word']
