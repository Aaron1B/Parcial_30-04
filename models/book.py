from enums.book_genre import BookGenre

class Book:
    def __init__(self, title: str, author: str, genre: BookGenre, is_borrowed: bool = False):
        self._title = title
        self._author = author
        self._genre = genre
        self._is_borrowed = is_borrowed

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_genre(self):
        return self._genre

    def set_title(self, title):
        self._title = title

    def set_author(self, author):
        self._author = author

    def set_genre(self, genre):
        if isinstance(genre, BookGenre):
            self._genre = genre

    def borrow(self):
        self._is_borrowed = True

    def return_book(self):
        self._is_borrowed = False

    def is_available(self):
        return not self._is_borrowed
