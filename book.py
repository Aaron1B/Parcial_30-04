class Book:
    def __init__(self, title, author, genre, status="available"):
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status

    def __str__(self):
        return f"'{self.title}' by {self.author} - Genre: {self.genre} - Status: {self.status}"

