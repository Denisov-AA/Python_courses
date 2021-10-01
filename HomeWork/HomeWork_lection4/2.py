number = list(input("Введите число: ").strip())

for i in range(0, len(number)):
    print(f"{i+1}-ая цифра равна {number[i]}")
