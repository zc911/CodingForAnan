# 第19课练习：面向对象基础

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0
        self.is_finished = False

    def read(self, num_pages):
        self.current_page += num_pages
        if self.current_page >= self.pages:
            self.current_page = self.pages
            self.is_finished = True
            print(f"《{self.title}》读完了！")
        else:
            print(f"《{self.title}》读到第{self.current_page}页（共{self.pages}页）")

    def show_info(self):
        status = "已读完" if self.is_finished else f"读到第{self.current_page}页"
        print(f"《{self.title}》- {self.author}（{self.pages}页）[{status}]")

# 创建几本书试试
book1 = Book("Python入门", "张老师", 100)
book1.read(30)
book1.read(40)
book1.show_info()
