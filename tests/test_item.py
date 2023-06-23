"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture
def notebook():
    return Item("notebook", 1000, 50)


def test_init_(notebook):
    assert notebook.name == "notebook"
    assert notebook.price == 1000
    assert notebook.quantity == 50
    assert len(notebook.all) == 1


def test_calculate_total_price(notebook):
    assert notebook.calculate_total_price() == 50000


Item.pay_rate = 0.8


def test_apply_discount(notebook):
    notebook.apply_discount()
    assert notebook.price == 800
