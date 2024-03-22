class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if value:
            self._first_name = value
        else:
            raise ValueError("First name cannot be empty")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if value:
            self._last_name = value
        else:
            raise ValueError("Last name cannot be empty")

person = Person("Chris", "Southerlin")
print(person.first_name, person.last_name)
person.first_name = "Gigi"
person.last_name = "Bartolomei"
print(person.first_name, person.last_name)