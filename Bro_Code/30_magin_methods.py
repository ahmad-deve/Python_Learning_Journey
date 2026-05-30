class book:
    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    def __str__(self):
        return f"Title: {self.title} | Num of Pages: {self.num_pages}"
    def __eq__(self, other):
        self.num_pages == other.num_pages
    def __contains__(self, keyword):
        return keyword in self.author or keyword in self.author
    def __lt__(self, other):
        return self.num_pages < other.num_pages
book1 = book("Rich dad poor dad","Robert.James",22)
book2 = book("Think and grow rich","Robert",125)
# print(book1.num_pages == book2.num_pages)
# print("Ahmad" in book1)
print(book1<book2)