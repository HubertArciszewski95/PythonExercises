# check if all elements in the given list are equal.


def all_the_same(elements):
    if all(x == elements[0] for x in elements):
        return True
    return False


print(all_the_same([1, 1, 1])) # True
print(all_the_same([1, 2, 1])) # False
print(all_the_same(['a', 'a', 'a'])) # True
print(all_the_same([])) # True
