# Entering string
s = input("Enter string: ").strip()
length = len(s)
ch = input('Which symbol will change:').strip()
ch_count = s.count(ch, 0, length)

# String checking
if length < 3 or ch_count == 0:
    print("String not acceptable. \nTry again.")
else:
    # Changing symbols, except first and last entrance
    s = s.replace(ch, ch.capitalize(), ch_count-1)
    s = s.replace(ch.capitalize(), ch, 1)

    print("Result:", str(s))