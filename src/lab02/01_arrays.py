def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:

    if nums == []:
        raise ValueError("Список пуст")
    """Возвращает ValueError, если список пустой"""

    mini = nums[0]
    for next in nums:
        if next < mini:
            mini = next
    maxi = nums[0]
    for next in nums:
        if next > mini:
            maxi = next

    return mini, maxi
    """В другом случае возвращает минимум и максимум из списка"""


# print('[3, -1, 5, 5, 0] ->', min_max([3, -1, 5, 5, 0]))
# print('[42] ->', min_max([42]))
# print('[-5, -2, -9] ->', min_max([-5, -2, -9]))
# print('[] ->', min_max([]))
# print('[1.5, 2, 2.0, -3.1] ->', min_max([1.5, 2, 2.0, -3.1]))

# def unique_sorted(nums: list[float | int]) -> list[float | int]:

#     nums = list(set(nums))
#     n = len(nums)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]

#                 '''Сортировка пузырьком'''

#     return nums

# print('[3, 1, 2, 1, 3] ->', unique_sorted([3, 1, 2, 1, 3]))
# print('[] ->', unique_sorted([]))
# print('[-1, -1, 0, 2, 2] ->', unique_sorted([-1, -1, 0, 2, 2]))
# print('[1.0, 1, 2.5, 2.5, 0] ->', unique_sorted([1.0, 1, 2.5, 2.5, 0]))


# def flatten(mat: list[list | tuple]) -> list:

#     new_mat = []
#     for elements in mat:
#             if isinstance(elements, tuple | list):
#                 '''Проверяет, список.кортеж ли элемент'''

#                 for element in elements:
#                     new_mat.append(element)
#                 '''Если все элементы удовлетворяют условию, то проходимся по элементам внутри каждого из них'''

#             else:
#                 return TypeError('TypeError')
#             '''Если есть элемент, не являющийся списком/кортежем, выводит ошибку'''

#     return new_mat

# print('[[1, 2], [3, 4]] ->', flatten([[1, 2], [3, 4]]))
# print('([1, 2], (3, 4, 5)) ->', flatten(([1, 2], (3, 4, 5))))
# print('[[1], [], [2, 3]] ->', flatten([[1], [], [2, 3]]))
# print('[[1, 2], "ab"] ->', flatten([[1, 2], "ab"]))
