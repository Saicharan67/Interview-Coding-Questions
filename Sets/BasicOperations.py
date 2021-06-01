x = {1, 1, 1, 1, 2, 2, 3}
y = {1, 1, 1, 2, 3, 4, 4}
print(x.intersection(y))
set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3, 9):
    set2.add(i)

print(set1 ^ set2 == set1.union(set2)-set1.intersection(set2))

# union = addition of two sets - intersection => union  |

# differecnce = set1- set2 => -

# intersection => & only elements in both sets

# precisly in only one set => union-intersection

# disjoint()

# Method 1: Use of discard() method

# The built-in method, discard() in Python, removes the element from the set only if the element is present in the set. If the element is not present in the set, then no error or exception is raised and the original set is printed.
# If the element is present in the set:

# Method 2: Use of remove() method

# The built-in method, remove() in Python, removes the element from the set only if the element is present in the set, just as the discard() method does but If the element is not present in the set, then an error or exception is raised.
# If the element is present in the set:
