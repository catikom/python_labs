def transpose(mat: list[list[float | int]]) -> list[list]:

    if not mat:
        return []
        '''Проверка наличия элементов в матрице'''
    len_row = len(mat[0])
    len_col = len(mat)
    
    for num in range(len(mat) - 1):
        if len(mat[num]) != len(mat[num + 1]):
            return ValueError('ValueError')
            '''Проверка на одинаковую длину строк'''

    new_mat =[]
    for col_ind in range(len_row):
        new_row = []
        '''С каждым запуске цикла создаётся ряд, рядов столько, сколько столбцов в изначальной матрице'''
        for row_ind in range(len_col):
            new_row.append(mat[row_ind][col_ind])
            '''Элементов в ряд добавляется столько, сколько столбцов в изначальной матрице'''
        new_mat.append(new_row)
        '''Ряд добавляется в новую матрицу'''

    return new_mat


print('[[1, 2, 3]] ->', transpose([[1, 2, 3]]))
print('[[1], [2], [3]] ->', transpose([[1], [2], [3]]))
print('[[1, 2], [3]] ->', transpose([[1, 2], [3, 4]]))
print('[] ->', transpose([]))
print('[[1, 2], [3]] ->', transpose([[1, 2], [3]]))