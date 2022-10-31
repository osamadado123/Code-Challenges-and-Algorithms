# Write your test here
from challenge02brackets import validate_brackets
def test_1():
    
    expected = True
    actual = validate_brackets("(g)")

    assert expected == actual


def test_2():

    expected = True
    actual = validate_brackets("({})")

    assert expected == actual

def test_3():

    expected = True
    actual = validate_brackets("()[[Extra Characters]]")

    assert expected == actual

def test_4():

    expected = True
    actual = validate_brackets("(){}[[]]")

    assert expected == actual

def test_5():

    expected = True
    actual = validate_brackets("{}{Code}[Fellows](())")

    assert expected == actual

def test_6():

    expected = False
    actual = validate_brackets("[({}]")

    assert expected == actual
