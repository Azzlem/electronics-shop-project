"""Здесь надо написать тесты с использованием pytest для модуля Phone"""

import pytest
from src.phone import Phone, Item


@pytest.fixture
def phone():
    return Phone("phone", 500, 15, 2)


@pytest.fixture
def notebook():
    return Item("notebook", 1000, 50)


def test_init_(phone):
    assert phone.name == "phone"
    assert phone.price == 500
    assert phone.quantity == 15
    assert len(phone.all) == 1
    assert phone.number_of_sim == 2


def test_add_(phone, notebook):
    assert phone + notebook == 65


def test_str_(phone):
    assert repr(phone) == "Phone('phone', 500, 15, 2)"


def test_number_of_sim(phone):
    phone.number_of_sim = 1
    assert phone.number_of_sim == 1