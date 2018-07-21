class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def print_catalog(self):
        for key in self.books:
            print(key)

    def print_users(self):
        for key in self.users:
            print(key)

    def most_read_books(self):
        v = list(self.books.values())
        k = list(self.books.keys())
        return k[v.index(max(v))]

    def most_positive_user(self):
        v = list(self.users.values())
        k = list(self.books.keys())
        return k[v.indec(max(v))]

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Your e-mail has been updated!")

    def __repr__(self):
        return 'User %s, email: %s, books read %s' %(self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user:
            return 'These are the same user'

    def read_book(self, book, rating='None'):
        self.book[book] = rating

    def get_average_rating(self):
        for key, value in self.books:
            key_num += 1
            values += value
        average = values/key_num
        return average



class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("The book's ISBN has been updated successfully!")

    def add_rating(self, rating):
        if 4 >= rating >= 0:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other):
        if self.title == other.get_title and self.isbn == other.get_isbn():
            return "These are the same book"

    def get_average_rating(self):
        for key, value in self.ratings:
            key_num += 1
            values += value
        average = values/key_num
        return average

class Fiction(Book):
    def __init__(self, title, author, isbn):
        Book.__init__(self, title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return '%s by %s' %(self.title, self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        Book.__init__(self, title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return '%s, a %s manual on %s' %s(self.title, self.level, self.subject)
