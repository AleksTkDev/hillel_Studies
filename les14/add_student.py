from add_human import Human


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return Student(self.record_book == other.record_book,
                       self.first_name == other.first_name,
                       self.last_name == other.last_name,
                       self.age == other.age,
                       self.gender == other.gender)

    def __str__(self):
        resp = super().__str__()
        return f'{self.record_book}: {resp}\n'
