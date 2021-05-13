# Largest even number possible from given string.

import itertools
input = input()
list_of_numbers = []
for i in list(set(input)):
    if i.isnumeric():
        list_of_numbers.append(i)

permuations = list(itertools.permutations(list_of_numbers))
max_even_value = -1
for p in permuations:
    value = int(''.join(p))
    if value % 2 == 0 and value > max_even_value:
        max_even_value = value

print(max_even_value)