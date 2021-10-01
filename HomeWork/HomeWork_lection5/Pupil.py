from Man import Man
import time
import random


class Pupil(Man):

    def __init__(self, name):
        super().__init__(name)

    def solve_task(self):
        print("Wait a second...")
        time.sleep(random.randint(3, 6))
        super().solve_task()
