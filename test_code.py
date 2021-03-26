import pytest
from uniqe_char import unique_string

def test_unique_string1():
    string = 'The quick brown fox jumps over the lazy dog'
    assert unique_string(string) == False

def test_unique_string2():
    string = 'I love cats'
    assert unique_string(string) == True

def test_unique_string3():
    string = 'Donald the duck'
    assert unique_string(string) == False