def multiplier(m=1, source=(1, 2, 3)):
    result = list(source)
    for i, x in enumerate(result):
        result[i] *= m

    return result

