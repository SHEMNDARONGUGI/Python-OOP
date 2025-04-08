
from book import Book

class DigitalBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size
        
    def stream(self):
        # simulated streaming of the digital book
        return f"streaming {self.title} - Size: {self.file_size}MB"
    
    def borrow(self):
        #overrides the borrow method to reflect digital availability
        return f"{self.title}"