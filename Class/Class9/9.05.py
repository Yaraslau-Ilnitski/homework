from functools import reduce
nums = [1, 3, 9]
b = reduce(lambda x, y: x * y,filter(lambda x: x % 3 == 0, nums))  # в конце берем уже отфильтрованный списко по делимости на 3

print(b)
