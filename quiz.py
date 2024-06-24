from dictionary import Dictionary
from random import choice, shuffle
from termcolor import colored


class Quiz(Dictionary):

    def __init__(self):
        super().__init__()
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

            quiz_mode = input("Type 'translation' or 'match' to start the quiz: ").strip().lower()
            if quiz_mode == 'translation':
                self.translation_mode()
            elif quiz_mode == 'match':
                self.match_mode()
            else:
                print(colored("Invalid mode selected. Please try again.", "red"))

    def translation_mode(self):
        while True:
            word = self.get_random_word()
            word_translation = self.get_translation(word)['Translation']

            user_answer = input(f"Type the translation of the word '{colored(word, attrs=['bold'], color='blue')}' "
                                f"or '{colored('finish', 'red', attrs=['bold'])}' to exit the quiz: ").strip()

            if user_answer.lower() == 'finish':
                break
            if user_answer == word_translation:
                print(colored("Correct :)", "green"))
                self.__correct_answers += 1
            else:
                print(colored("Incorrect :(", "red"))
                self.__incorrect_answers += 1

        self.points = self.__correct_answers
        self.display_results()

    def match_mode(self):
        print("""Type the first word's and the second word's numbers separated by space to match the words.
Example: 1 7 """)

        words = [el['word'] for el in self.get_words()]
        translations = [self.get_translation(word)['Translation'] for word in words]

        shuffled_words = words[:]
        shuffled_translations = translations[:]
        shuffle(shuffled_words)
        shuffle(shuffled_translations)

        answers = {'correct_answers': [], 'incorrect_answers': []}

        for i in range(len(words)):
            print(f"{i + 1}. {shuffled_words[i]}".ljust(20), f"{i + 1}. {shuffled_translations[i]}".ljust(20))

        i = 1

        while True:
            user_input = input("Enter the nums of pairs or 'finish' to exit the quiz: ").strip()
            if user_input.lower() == 'finish' or i == len(words):
                break
            try:
                i += 1
                word_num, translation_num = map(int, user_input.split())
                if 1 <= word_num <= len(words) and 1 <= translation_num <= len(translations):
                    word = shuffled_words[word_num - 1]
                    translation = shuffled_translations[translation_num - 1]
                    actual_translation = self.get_translation(word)['Translation']
                    if actual_translation == translation:
                        print(colored("Correct :)", "green"))
                        self.__correct_answers += 1
                        answers['correct_answers'].append(f"{word} - {translation}")
                    else:
                        print(colored("Incorrect :(", "red"))
                        self.__incorrect_answers += 1
                        answers['incorrect_answers'].append(f"{word} - {translation}")
                else:
                    print(colored("Invalid numbers. Please try again.", "red"))
            except ValueError:
                print(colored("Invalid input format. Please enter numbers separated by space.", "red"))

        self.points = self.__correct_answers
        self.display_results(answers)

    def get_random_word(self):
        return choice(self.get_words())['word']

    def display_results(self, answers=None):
        if answers is None:
            answers = {'correct_answers': [], 'incorrect_answers': []}

        print(f"You got {self.points} points")
        print(colored(f"Correct answers: {self.__correct_answers}", "green", attrs=['bold']))

        if answers['correct_answers']:
            for correct_answer in answers['correct_answers']:
                print(colored(correct_answer, "green"))

        print(colored(f"Incorrect answers: {self.__incorrect_answers}", "red", attrs=['bold']))

        if answers['incorrect_answers']:
            for incorrect_answer in answers['incorrect_answers']:
                print(colored(incorrect_answer, "red"))
