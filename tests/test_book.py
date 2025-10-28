from src.models.book import Book

def test_book_borrow_true():
    '''Позитивный тест бронирования книги'''
    book = Book("Алиса в стране чудес", "Льюис Кэрролл", 1865,"242-252-6463-743")
    assert book.borrow()=="Книга Алиса в стране чудес выдана"

