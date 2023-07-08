import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_init_(keyboard):
    assert keyboard.name == "Dark Project KD87A"
    assert keyboard.price == 9600
    assert keyboard.quantity == 5
    assert len(keyboard.all) == 1


def test_str_(keyboard):
    assert str(keyboard) == "Dark Project KD87A"


def test_change_lang(keyboard):
    assert str(keyboard.language) == "EN"
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"
    keyboard.change_lang().change_lang()
    assert str(keyboard.language) == "RU"

