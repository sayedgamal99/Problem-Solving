class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}")
    def display(self):
        print(f"Age: {self.age}")

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age,salary=1000):
        super().__init__(name, age)
        self._salary = salary
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self._salary}")

    

class Family(Person):
    def __init__(self, name, age,position='Father'):
        super().__init__(name, age)
        self.__position = position

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Position: {self.__position}")



person = Person('Sayed',20)
print(person.name,person.age)
person.display()

print('='*50)

employee = Employee('Sayed',21,1500)
print(employee.name,employee.age,employee._salary)
employee.display()

print('='*50)

member = Family('Sayed',22,'Son')
try:
    print(member.name,member.age,member.__position)
except AttributeError:
    print("Can't access private attribute-> Position")

try:
    member.display()
except AttributeError:
    print("Can't access private attribute inside Display function")

