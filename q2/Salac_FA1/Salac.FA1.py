class Publication:
    def __init__(self, title:str, author:str):
        self.__title = title
        self.__author = author

    def get_title(self):
            return self.__title

    def get_author(self):
            return self.__author
        
    def set_title(self, new_title):
            self.__title = new_title

    def set_author(self, new_author):
            self.__author = new_author

    def display_info(self):
            print("Title:", self.__title)
            print("Author:", self.__author)

class Book(Publication):
    def __init__(self, title, author, number_of_pages: int):
        super().__init__(title, author)
        self.number_of_pages = None
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self):
        return self.number_of_pages

    def set_number_of_pages(self, new_number_of_pages):
        if new_number_of_pages > 0:
            self.number_of_pages = new_number_of_pages
        else:
            print("Number of pages must be positive.")

    def display_info(self):
        super().display_info()
        print("Number of pages:", self.number_of_pages)

class Magazine(Publication):
    def __init__(self, title, author, issue_number: int):
        super().__init__(title, author)
        self.issue_number = None
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.issue_number

    def set_issue_number(self, new_issue_number):
        if new_issue_number > 0:
                self.issue_number = new_issue_number
        else:
            print("The issue number must be positive.")

    def display_info(self):
        super().display_info()
        print("Issue number:", self.issue_number)

pub1 = Publication("Vince", "Vince Collado")
book1 = Book("Jerrick", "Jerrick Jaralve", 310)
mag1 = Magazine("Vinson", "Vinson Digal", 202)

print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()

print("\nMagazine Information:")
mag1.display_info()
