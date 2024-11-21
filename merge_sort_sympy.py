from sympy.combinatorics import Permutation
from sympy import init_printing
init_printing(perm_cyclic=False, pretty_print=False)

integer_array = []

with open("IntegerArray.txt", "r") as reader:
    line = reader.readline()
    while line != '':
        integer_array.append(int(line.rstrip('\n')))
        line = reader.readline()

p = Permutation.from_sequence(integer_array)

print(p.inversions())