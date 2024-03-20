class Book: 
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def get_title(self):
        """Print book title."""
        return self.title

    def get_author(self):
        """Print book author."""
        return self.author

    def get_genre(self):
        """Print book genre."""
        return self.genre

# Example usage:
if __name__ == "__main__":
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic Fiction")
    print(f"Title: {book1.get_title()}")
    print(f"Author: {book1.get_author()}")
    print(f"Genre: {book1.get_genre()}\n")   