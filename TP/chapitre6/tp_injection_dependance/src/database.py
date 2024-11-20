from pydantic import BaseModel


class Book(BaseModel):
    title: str
    description: str


class FakeDB:
    _books: dict[int, Book] = {
        1: Book(title="The Great Gatsby", description="A classic American novel"),
        2: Book(title="To Kill a Mockingbird", description="A novel by Harper Lee"),
        3: Book(title="1984", description="A dystopian novel by George Orwell"),
        4: Book(title="Pride and Prejudice", description="A novel by Jane Austen"),
        5: Book(title="The Catcher in the Rye", description="A novel by J.D. Salinger"),
    }

    def __init__(self) -> None:
        print("Database initialized, connexion SUCCESSFUL !")

    def get_all_books(self) -> list[Book]:
        return list(self._books.values())

    def get_book_by_id(self, book_id: int) -> Book | None:
        return self._books.get(book_id)


async def get_db() -> FakeDB:
    return FakeDB()
