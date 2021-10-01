class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age


class Worker(User):
    def __init__(self, name, age, salary):
        self.salary = salary
        super().__init__(name, age)

    def getSalary(self):
        return self.salary

    def setSalary(self, salary):
        self.salary = salary


john = Worker(name='John', age=25, salary=1000)
jack = Worker(name='Jack', age=26, salary=2000)

salary_summ = john.getSalary() + jack.getSalary()
print(salary_summ)