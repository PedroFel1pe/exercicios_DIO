#Crie uma classe Livro com atributos como título, autor, ano de publicação e um método para mostrar os dados completos do livro.
class Book:
    def __init__(self, title, author, publication_date):
        self.title = title
        self.author = author
        self.publication_date = publication_date
    def full_book_details(self):
        return f"Title: {self.title}, Author: {self.author}, Publication: {self.publication_date}"

information = Book("One Piece", "Oda", "22/07/1997")
print(information.full_book_details())