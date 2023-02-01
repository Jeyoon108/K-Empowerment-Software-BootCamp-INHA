# A to Z reminding

# Ch10 practice Getter/Setter + property-mangling

class Person:
    def __init__(self, first_name, last_name, input_age):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = input_age

    @property
    def age(self):
        print('inside the getter')
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        print('inside the setter')
        self.__age = age


person = Person("John", "Doe", 20)
print(person.age)
# person.age = person.age + 1
print(person.age)
# person.age = 23
print(person.age)
print(person._Person__age)  # 이를 통해 접근할 수는 있긴하지만 inside the getter를 시행하진 않는다.
print(person.__age)  # 네이밍 컨벤션을 통해 __age에 바로 접근할 수 없게 한다.(맹글링)
