from unittest.mock import MagicMock

from src.database import Book, FakeDB
from src.main import get_books


def test_get_books():
    database = MagicMock(spec=FakeDB)

    database.get_all_books.return_value = [
        Book(title="test title", description="test description")
    ]

    books = get_books(database)

    assert len(books) == 1
    assert books[0].title == "test title"
    assert books[0].description == "test description"


def test_get_book_by_id():
    class DBTest(FakeDB):
        _books: dict[int, Book] = {
            1: Book(title="test title", description="test description"),
        }

    db = DBTest()

    book = db.get_book_by_id(1)

    assert book is not None
    assert book.title == "test title"
    assert book.description == "test description"
