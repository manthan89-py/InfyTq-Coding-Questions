# Largest even number possible from given string.
# If not able to find any even number return -1.

# Test Case
# asdf@75483
# output : 87534

# Test Case
# infytq@13579
# output : -1

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
