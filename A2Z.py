# A to Z reminding

# Ch10 practice Getter/Setter + property

class Person:
    def __init__(self, first_name, last_name, input_age):
        self.first_name = first_name
        self.last_name = last_name
        self.hidden_age = input_age

    @property
    def age(self):
        return self.hidden_age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        self.hidden_age = age


person = Person("John", "Doe", 20)
print(person.age)
person.age = person.age + 1
print(person.age)
person.age = 23
print(person.age)
