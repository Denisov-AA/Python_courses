import threading
import time
import random


class Scheduler:
    def __init__(self, runtime=None):
        self.current_time = time.time()
        self.runtime = runtime
        self.func_list = []

    def func_add(self, runperiod, func, args):
        self.func_list.append([runperiod, func, args])

    def starter(self):
        thr = []
        for func in self.func_list:
            t = threading.Timer(func[0], func[1], args=func[2])
            thr.append(t)
            print(f'{func} - {func[0]}')
            t.start()
        for thread in thr:
            thread.join()

    def run(self):

        if self.runtime is None:
            while True:
                self.starter()

        else:
            while self.current_time + self.runtime > time.time():
                self.starter()


def test_func(p):
    return f'{print(f"Test func {p} finished")}'


sched = Scheduler(runtime=20)
for n in range(1, 20):
    print(f"{test_func(n)} - added to Scheduler")
    sched.func_add(func=test_func, runperiod=random.randint(1, 5), args=[n])

sched.run()
