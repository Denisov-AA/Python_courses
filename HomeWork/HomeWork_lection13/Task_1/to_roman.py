class NonValidInput(Exception):
    def __init__(self, text: str):
        self.txt = text


def to_roman(n):
    if isinstance(n, int) is True:
        pass
    else:
        raise NonValidInput('Wrong data format')

    if 0 < n < 5000:
        result = ''
        for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                                 'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
            result += n // arabic * roman
            n %= arabic
        return result

    else:
        print('Your number should be in 0 - 5000')
        return 1


#print(to_roman("asd"))
