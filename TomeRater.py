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
        if user == other_user:
            return 'These are the same user'

    