from src.models.book import Book
from src.models.user import User

book1 = Book("Гарри Поттер и Философский камень", "Дж.К.Роулинг", 1997, "978-5-17-080077-7")		
print(book1.get_info())

user1 = User("Женя", 2006, "жен")		
print(user1.get_info())