def my_len(some_list: list):
    len = 0
    for i in some_list:
        len += 1
    return len


print(my_len([1, 3, 5, 6, 7]))
