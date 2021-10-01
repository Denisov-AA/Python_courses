def my_range(stop: int, start=0, step=1):
    result = []
    result.append(start)
    if step == 0:
        return start
    else:
        pass
    if step > 0:
        i = 1
        while i < stop:
            result.append(start + step * i)
            if result[i] > stop:
                break
            i += 1

        return result
    else:
        i = -1
        while i > stop + step * start:
            result.append(start - step * i)
            if result[i] < stop:
                break
            i -= 1
        return result


print(my_range(10, 1, 1))
t = range(1, 10, 2)
