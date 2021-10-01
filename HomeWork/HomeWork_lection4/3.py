l = input("Введите последовательность через пробел: ").strip().split()

for i in range(len(l)):
    minimum = i
    for j in range(i + 1, len(l)):
        if int(l[j]) < int(l[minimum]):
            minimum = j
    l[i], l[minimum] = l[minimum], l[i]

print(l)
