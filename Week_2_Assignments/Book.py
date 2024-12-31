import json

class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content
        self.current_page = 0

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def turn_page(self):
        if self.current_page < len(self.content) - 1:
            self.current_page += 1

    def get_current_page(self):
        return self.content[self.current_page]

class Library:
    def __init__(self, location):
        self.location = location

    def get_location(self):
        return self.location

class BookSaver:
    @staticmethod
    def save(book, file_path):
        data = {
            "title": book.get_title(),
            "author": book.get_author(),
            "content": book.content,
        }
        with open(file_path, 'w') as file:
            json.dump(data, file)

class PlainTextPrinter:
    def print_page(self, page):
        print(page)

class HtmlPrinter:
    def print_page(self, page):
        print(f'<div style="single-page">{page}</div>')

if __name__ == "__main__":
    book = Book(
        title="A Great Book",
        author="John Doe",
        content=["Page 1 content", "Page 2 content", "Page 3 content"]
    )

    print("Title:", book.get_title())
    print("Author:", book.get_author())

    plain_printer = PlainTextPrinter()
    plain_printer.print_page(book.get_current_page())

    book.turn_page()
    plain_printer.print_page(book.get_current_page())

    saver = BookSaver()
    saver.save(book, "book.json")

    library = Library(location="Shelf 5, Room 2")
    print("Library Location:", library.get_location())
