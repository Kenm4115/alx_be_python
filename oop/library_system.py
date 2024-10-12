
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"title: {self.title}, Author:{self.author}"


class EBook(Book):
    super().__init__
    # def __init__(self, file_size):
    #     self.file_size = file_size


class PrintBook(Book):
    super().__init__


# class PrintBook(Book):
#     super().__init__(self, page_count):
#         self.page_count = page_count

books = (Book, EBook, PrintBook)
print(books)
