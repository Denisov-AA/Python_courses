import threading


# Функция суммирования с проверкой
def summation(*args):
    if type(args[0]) is int:
        result = 0
        for arg in args:
            result += arg
        return f'{print(result)}'

    if type(args[0]) is str:
        result = ""
        for arg in args:
            result += arg
        return f'{print(result)}'

    if type(args[0]) is list:
        result = []
        for arg in args:
            result += arg
        return f'{print(result)}'


# Тестовые данные
test_lists = ["akjsdfhajkf", "sadfasdfasdfas"], ["kjfghalkjdfhaskjf"]
test_strings = "qqqqqqqqqq", "aaaaaaaaaaaaaa", "sssssssssssssssssss"
test_ints = 1, 2, 3, 4, 5
threads = []

# Реализуем запуск функции
for data in test_strings, test_lists, test_ints:
    calculate = threading.Thread(target=summation, args=data)
    calculate.start()
    threads.append(calculate)

for thr in threads:
    thr.join()
