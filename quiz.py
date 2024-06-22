from dictionary import Dictionary
class Quiz(Dictionary):

    def start(self):
        print("Hi :) With quiz you can check your knowledge of words.\n"
        "It's also helpful to memorize the words if you forgot it.\n"
        "There is two modes: translation mode and match mode.\n"
        "In translation mode you will get a random word from dictionary and must to translate it\n"
        "Every correct answer is 1 point, the wrong answer is 0 point.\n"
        "In match mode you need to match the words with their translations.\n"
        "Every correct answer is 1 point, the wrong answer is 0 point")

    def translate(self, word):
        pass