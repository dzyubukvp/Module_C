user_peter = {
    "name": "Peter",
    "email": "peterrobertson@mail.com",
    "created_at": "2019-05-05",
    "is_email_verified": True,
    "purchases": ["Egg", "Spam", "Hat", "Knife", "Shield", "Book of Knight secrets"],
}

user_julia = {
    "name": "Julia Donaldson",
    "email": "juliadonaldson@mail.com",
    "created_at": "2019-06-13",
    "is_email_verified": True,
    "purchases": ["Egg", "Spam", "Magic Brush"],
}

product_eggs = {
    "name": "Egg",
    "category": "food",
    "is_available": False,
    "quantity_in_stock": 0,
    "vendor": "Dark Knight LTD",
    "manager": "William The Conqueror",
}

class User:
    def __init__(self, name, email, purchases):
        self.name = name
        self.email = email
        self.purchases = purchases

peter = User(name="Peter Robertson", email="peterrobertson@mail.com", purchases = ["Egg", "Spam", "Hat", "Knife", "Shield", "Book of Knight secrets"])



print(peter.name, peter.email, peter.purchases)
