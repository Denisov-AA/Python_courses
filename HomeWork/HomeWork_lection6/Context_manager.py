import time


class MyContextManager:

    def __enter__(self):
        self.time_start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Time spent: {time.time() - self.time_start}")
