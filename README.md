# Command-line Dictionary Application

#### Video Demo:  <URL HERE>

## Overview

Command-line Dictionary application is a simple tool for easy creating your own simple dictionary of words. There is
also a quiz mode included which will help you to memorize the words and their translations. The main thing is that the
adding of words is completely depended on the user and the user decides which word he would like to add to his
dictionary. You also can add some examples of usage of the words. So with this Command-line Dictionary, you can

1. #### Add Words and Their Translations:

Add new words to your dictionary along with their translations and optional usage examples.

2. #### Remove Words and Their Translations:

Remove words from your dictionary when they are no longer needed.

3. #### Get All Existing Words and Their Translations:

Display all the words currently stored in your dictionary along with their translations and usage examples.

4. #### Test Your Knowledge by Playing Quiz Mode:

Enter quiz mode to test your knowledge and reinforce your learning.

## Requirements

1. `Python 3.x`
2. `tabulate` library(can be installed via pip)
3. `termcolor` library(can be installed via pip)

Check out the `requirments.txt` to see the needed versions of these libraries

## How to use it

The project contains the following files:

1. `project.py`
2. `quiz.py`
3. `dictionary.py`
4. `test_project.py`

You can run either `quiz.py` or `project.py` via terminal or IDE to start using the application, but
consider that you can't play quiz if there is no `dictionary.csv` file, or it contains less than 6 words.
`test_project.py` contains unit tests for testing the application. You can add custom tests there.

### Starting via terminal

#### Windows

```cmd
python project.py
```

```cmd
python quiz.py
```

#### Linux

```
python3 project.py
```

```
python3 quiz.py
```

### Starting in IDE

Check out your IDE tutorials to see how to run python scripts.

VS Code: https://code.visualstudio.com/docs/python/python-tutorial

PyCharm: https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html

## Project.py

`project.py` is the entry point of the application. In this file are several functions:

1. `main()`: Main function initializes the Dictionary class and starts the interactive mode

2. `add_word_command()`: Handles `add` command to add words to the dictionary using the methods of Dictionary class

3. `remove_word_command()`: Handles `remove` to remove words from Dictionary

4. `get_words_command()`: Handles `words` command to get the list of the words from the dictionary

5. `get_translation_command()`: Handles `translate` command to translate the given word

6. `start_quiz()`: Starts the quiz mode using the Quiz class

## Dictionary.py

`dictionary.py` contains the `Dictionary` class which is used to *add*, *remove*, *get*, and *translate* the words. This
class works with `dictionary.csv` file which must be in the same directory. If there is no such file it will be created
automatically. It contains the following public methods:

1. `add_word()` method adds the given word with its translation and usage example to the dictionary and returns True if
   the word was added else returns False. This method ignores the duplicate words

2. `remove_word()` method removes the word with its translation and usage examples from the dictionary. Returns False if
   the deletion was not successful

3. `get_translation()` method retrieves the translation and usage examples of the given word and returns a dictionary
   with keys `Translation` and `Examples`

4. `no_dublicate` method checks if the given word already exists in the dictionary. This method is used by `add_word()`

## Quiz.py

The quiz mode allows you to test your knowledge of words and their translations.

`quiz.py` contains the `Quiz` class which implements the quiz functionality. It contains three public methods:

1. `translation_mode()`
2. `match_mode()`
3. `start()`

`start()` method starts the quiz session. First you will see a welcome text

```chatinput
Enter command: quiz
Hi :) With quiz you can check your knowledge of words.
It's also helpful to memorize the words if you forgot it.
There is two modes: translation mode and match mode.
In translation mode you will get a random word from dictionary 
and must to translate it.
Every correct answer is 1 point, the wrong answer is 0 point.
In match mode you need to match the words with their translations.
Every correct answer is 1 point, the wrong answer is 0 point.
Type finish when you want to finish the quiz.
Type 'translation' or 'match' to start the quiz: 

```

After typing `translation` or `match` the corresponded mode will be started.

### Translate mode

In the `translation mode` you will get a random word from dictionary until you type `finish`.
After, finishing you will the count of correct and incorrect answers:

```chatinput
You got 1 points
Correct answers: 1
Incorrect answers: 1
```

### Match mode

In match mode the `match_mode()` method will generate a shuffled pairs of words and their translations. You must match
them by their numbers. At the end of game you will see your results as a points, correct and incorrect answers

```chatinput
You got 4 points
Correct answers: 4
pajaro - bird
flor - flower
sol - sun
luna - moon
Incorrect answers: 0
```