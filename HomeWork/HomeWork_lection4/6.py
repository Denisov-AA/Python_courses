matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Ввод матрицы можно прикрутить любой другой, если нужно.

def delete_coll(x):
    del_index = -1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if x == matrix[i][j]:
                del_index = j
    if del_index != -1:
        for i in range(len(matrix)):
            del matrix[i][del_index]


delete_coll(1)

print(matrix)
