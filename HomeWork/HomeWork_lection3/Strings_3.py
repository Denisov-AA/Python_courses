# Entering string
s = input("Enter two-words string: ").strip().split()
s.reverse()
s = '-'.join(s)
print("Reversed string:", s)
