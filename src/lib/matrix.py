def transpose(mat: list[list[float | int]]) -> list[list]:   #Меняет строки и столбцы

    if not mat:
        return []

    len_row = len(mat[0])
    len_col = len(mat)
    
    for num in range(len(mat) - 1):
        if len(mat[num]) != len(mat[num + 1]):
            return ValueError('Матрица рваная')


    new_mat =[]
    for col_ind in range(len_row):
        new_row = []
        for row_ind in range(len_col):
            new_row.append(mat[row_ind][col_ind])
        new_mat.append(new_row)

    return new_mat

def row_sums(mat: list[list[float | int]]) -> list[float]:
    
    for num in range(len(mat) - 1):
        if len(mat[num]) != len(mat[num + 1]):
            return ValueError('Матрица рваная')
            '''Проверка на одинаковую длину строк'''

    sum_row = []

    for row in mat:
        sum_row.append(sum(row))

    return sum_row


def col_sums(mat: list[list[float | int]]) -> list[float]:    #Считает сумму по столбцу

    len_row = len(mat[0])
    len_col = len(mat)
    
    for num in range(len(mat) - 1):
        if len(mat[num]) != len(mat[num + 1]):
            return ValueError('Матрица рваная)

    sum_col = []
    for col in range(len_row):
        summa = 0
        for row in range(len_col):
            summa += mat[row][col]
        sum_col.append(summa)
    
    return sum_col