def count_symbol(string: str, symbol: str):
    n = 0
    for first in range(len(string) - len(symbol) + 1):
        if string[first:first + len(symbol)] == symbol:
            n += 1
    return n


print(count_symbol("asdasddasd", "d"))
