import pytest
from singleton import Singleton


@pytest.fixture(autouse=True)
def reset_singleton():
    Singleton.reset()


def test_singleton_default_value():
    # On initialise le singleton sans paramètre
    singleton = Singleton()
    # On vérifie que la valeur par défaut est 0
    assert singleton.get_value() == 0


def test_singleton_set_value():
    # On initialise le singleton sans paramètre
    singleton = Singleton()
    # On change la valeur du singleton
    singleton.set_value(5)
    # On vérifie que la valeur a changé
    assert singleton.get_value() == 5


def test_singleton_init_value():
    # On initialise le singleton avec 42
    singleton = Singleton(42)
    # On vérifie que la valeur est 42
    assert singleton.get_value() == 42
