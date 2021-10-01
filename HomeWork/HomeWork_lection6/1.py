def chargen(string: str):
    for c in string:
        yield c


symbols_string = '01234567895698fghdgd'
words = [c + c for c in chargen(symbols_string)]
print(words)
