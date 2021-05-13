# Take in input in given format ( string : code )
# check for code digits
# if sum of square of digits is even add last two character at the top of string
# else add first character at the last.

# Test Case
# abcd:1234,bcdgfhf:127836,sdjks:1245
# output : cdab cdgfhfbc kssdj


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
