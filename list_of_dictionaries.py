books = [
    {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "year": 1979},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954},
    {"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "year": 1997}
]

# Print the title of the second book in the list
print(books[1]["title"])

# Print the year the third book was published
print(books[2]["year"])

# Iterate over the list and print out each book's title and author
for book in books:
    print(book["title"], "by", book["author"])