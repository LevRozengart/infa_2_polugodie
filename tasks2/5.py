class Library:
    book_list = list()
    def add_book(self, title):
        self.book_list.append(title)
        print(self.book_list)
        return self.book_list
    def del_book(self, naz):
        self.book_list.pop(self.book_list.index(naz))
        print(self.book_list)
        return self.book_list
    def find_book(self, title):
        print(str(self.book_list.index(title)) + ' - индекс')
        return self.book_list.index(title)

a = Library()
a.add_book('Война и мир')
a.del_book('Война и мир')
a.add_book('Гена')
a.add_book('Волк')
a.find_book('Волк')
