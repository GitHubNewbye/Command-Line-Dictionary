from dictionary import Dictionary

my_dict = Dictionary()
def test_add_word():
    assert my_dict.add_word("palabra", "word") == True
    assert my_dict.add_word("luna", "moon") == True
    assert my_dict.add_word("luna", "moon") == False


def test_remove_word():
    assert my_dict.remove_word('luna') == True
    # assert my_dict.remove_word('luna') == False


def test_get_words():
    assert isinstance(my_dict.get_words(), list)
