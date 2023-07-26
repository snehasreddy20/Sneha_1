
#  1: Map with Lambda


num = [1, 2, 3, 4, 5]
squared_num = list(map(lambda x: x**2, num))
print(squared_num)

### 2: Zip

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
A = list(zip(names, ages))
print(A)


# 3: Filter
num = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, num))
print(even)


# Example 4: Reduce

from functools import reduce
num = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, num)
print(sum_of_numbers) 
