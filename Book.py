class Book:
    def __init__(self, title, author, pages, is_read: bool):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = is_read
        
    def mark_as_read(self):
        self.is_read = True

    def info(self):
        print(self.title)
        print(self.author)
        print(self.pages)
        print(self.is_read)

erlen_kuben =(Book("מהלך מוטעה","הרלן קובן", 320, False))
erlen_kuben.info()
erlen_kuben.mark_as_read()