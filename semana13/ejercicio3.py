from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        years = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        return years

def only_adults(func):
    def wrapper(user, *args):
        if not isinstance(user, User):
            raise TypeError("First argument must be a User instance")
        if user.age < 18:
            raise Exception("User is not an adult")
        return func(user, *args)
    return wrapper

@only_adults
def enter_club(user):
    print(f"Welcome! User age: {user.age}")

adult = User(date(2000, 1, 1))
minor = User(date(2010, 1, 1))
enter_club(adult)    
enter_club(minor)