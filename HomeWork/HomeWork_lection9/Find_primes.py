import threading
import multiprocessing
import time

intervals = {3: 10000, 10001: 20000, 20001: 30000}


def find_primes(start=3, stop=10):  # Для нахождения простых чисел используем решето Эрастофена
    numbers = list(range(start, stop + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, stop + 1, number):
                numbers[candidate - start] = 0
    result = list(filter(lambda x: x != 0, numbers))
    return f"{result}"


def benchmark(func):  # Обертка для оценки производительности

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Время выполнения: {end - start} секунд.')

    return wrapper


@benchmark
def primes_consistently():
    for start, stop in intervals.items():
        find_primes(start, stop)


@benchmark
def primes_multithread():
    threads = []
    for start, stop in intervals.items():
        calc = threading.Thread(target=find_primes, args=(start, stop))
        calc.start()
        threads.append(calc)
    for thr in threads:
        thr.join()


@benchmark
def primes_multiprocess():
    processes = []
    for start, stop in intervals.items():
        calc = multiprocessing.Process(target=find_primes, args=(start, stop))
        calc.start()
        processes.append(calc)
    for thr in processes:
        thr.join()


if __name__ == '__main__':
    print("При последовательном запуске")
    primes_consistently()
    print("\n")
    print("При многопоточном запуске")
    primes_multithread()
    print("\n")
    print("При многопроцесовом запуске")
    primes_multiprocess()
