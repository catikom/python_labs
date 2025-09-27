def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:

    if nums == []:
        return ValueError('ValueError') 
    '''Возвращает ValueError, если список пустой'''

    return (min(nums), max(nums))  
    '''В другом случае возвращает минимум и максимум из списка'''

print('[3, -1, 5, 5, 0] ->', min_max([3, -1, 5, 5, 0]))
print('[42] ->', min_max([42]))
print('[-5, -2, -9] ->', min_max([-5, -2, -9]))
print('[] ->', min_max([]))
print('[1.5, 2, 2.0, -3.1] ->', min_max([1.5, 2, 2.0, -3.1]))