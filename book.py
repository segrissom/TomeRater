# This is part of my solution for TomeRater
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
