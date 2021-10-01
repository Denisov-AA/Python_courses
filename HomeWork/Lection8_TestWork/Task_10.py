class Money:
    def __init__(self, ruble: int, penny: int):
        self.ruble = ruble
        self.penny = penny
        self.sum = self.ruble * 100 + self.penny

    def __add__(self, other):
        return f"{(self.sum + other.sum) // 100}, {(self.sum + other.sum) % 100}"

    def __sub__(self, other):
        return f"{(self.sum - other.sum) // 100}, {(self.sum - other.sum) % 100}"

    def __truediv__(self, n):
        return f"{(int(self.ruble / n))}, {int(self.sum / n - int(self.ruble / n) * 100)}"

    def __gt__(self, other):
        return f"{print(self.sum > other.sum)}"

    def __lt__(self, other):
        return f"{print(self.sum < other.sum)}"

    def __ge__(self, other):
        return f"{print(self.sum >= other.sum)}"

    def __le__(self, other):
        return f"{print(self.sum <= other.sum)}"

    def __eq__(self, other):
        return f"{print(self.sum == other.sum)}"

    def __ne__(self, other):
        return f"{print(self.sum != other.sum)}"

    def get_money(self):
        return f"{print(f'{self.ruble}, {self.penny}')}"

    def set_course(self, course):
        self.course = course

    def get_currency(self):
        self.currency = (self.sum / (self.course * 100))
        return f"{print(self.currency)}"


bablo = Money(6500, 65)

# Test
bablo.get_money()
bablo.set_course(65)
bablo.get_currency()
