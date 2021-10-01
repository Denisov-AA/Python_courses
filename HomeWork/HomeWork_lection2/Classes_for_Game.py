class Pers:
    def __init__(self, namevalue, speed=100):
        self.name = namevalue
        self.speed = speed

    def run(self):
        print(f"{self.name} is running, speed {self.speed}")

    def shoot(self):
        print(f"{self.name} is shooting")

    def take_item(self, item):
        item.buff(self)


class Item:
    def buff(self, pers):
        pass


class SpeedUpBuffItem(Item):
    def buff(self, pers):
        pers.speed += 10


class SpeedDownBuffItem(Item):
    def buff(self, pers):
        pers.speed -= 10


# vasya = Pers("Vasya")
forest = Pers("Forest")
forest.run()

nishtyak = SpeedUpBuffItem()
forest.take_item(nishtyak)
forest.run()

