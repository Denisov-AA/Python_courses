import random


class Human:

    def __init__(self):
        self.name_list = ['Andrew', 'Julia', "Alexander", 'Maria', 'Alex']
        self.name = random.choice(self.name_list)
        self.age = random.randint(20, 40)
        self.place_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
        self.residence = random.choice(self.place_list)
        print(f"Hi, my name is {self.name}. I'm {self.age}. And I'm from {self.residence}")

    def introduce(self):
        print(f"{self.name} // {self.age} // {self.residence}")
