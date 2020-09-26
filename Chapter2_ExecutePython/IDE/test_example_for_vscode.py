class A:
    def __init__(self):
        pass

    def f1(self, a):
        b = 1
        c = 2
        result = a**b + a**c
        return result

    def f2(self, a):
        b = 1
        c = 2
        result = a**b + a**c
        return result

    def f3(self, a):
        b = 1
        c = 2
        result = a**b + a**c
        return result

# Lists


#       0   1  2  3  4  5
noten = [
    1, 1, 3,
    4, 2, 1
]

noten.append(6)
noten.append(1)

print(noten)

noten.pop()
noten.pop()

print(noten)

noten.insert(0, 12)

print(noten)

noten.pop(2)

print(noten)

# List Comprehensions
my_list = []

my_list2 = []
for i in range(10):
    my_list2.append(i)
print(my_list2)

my_list2_comp = [i**2 for i in range(100) if i % 2 == 0]
my_list2_comp2 = [i for i in range(100) if i % 2 == 0]
print(my_list2_comp)
print("\n")
print(my_list2_comp2)

# Numpy
import numpy as np


m = np.array([1, 0, 0, 1])
print(m.shape)
print(m)
m = np.reshape(m, (2, 2))
print(m.shape)
print(m)
