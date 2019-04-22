# Find the sum of the integers with even indexes
# Then multiply this summed number and the final element of the array together.


def even_the_last(data):
    if len(data) < 1:
        return 0
    else:
        return sum(data[::2]) * data[-1]


print(even_the_last([0, 1, 2, 3, 4, 5])) # 30
print(even_the_last([1, 3, 5])) # 30
print(even_the_last([6])) # 36
print(even_the_last([])) # 0
