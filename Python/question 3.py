# For given list take the number at even places only. Square that number in list and
# Output First Four Digits.

# Test Case
# 5624381275
# output: 3616

input = input()
list_of_numbers = list(map(int , list(input)))
new_list = []
for i in range(1,len(list_of_numbers) , 2):
    new_list.append(list_of_numbers[i]**2)

print(''.join(str(new_list[0])+str(new_list[1])))

