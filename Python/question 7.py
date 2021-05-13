# String Rotation

input = input()
list_of_inputs = input.split(',')
new_list = []
for inputs in list_of_inputs:
    sum = 0
    letter, code = inputs.split(":")
    for digit in code:
        sum += int(digit)**2

    if sum % 2 == 0:
        new_list.append(letter[-2:]+letter[:-2])
    else:
        new_list.append(letter[1:]+letter[0])

print(' '.join(new_list))