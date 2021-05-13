# Take input from user in given format ( name : code )
# find the maximum digit from code which is less then or equal to the length of name and put the place
# char in the final string if there is no any digit found which satisfies above condition then put 'X' in the
# final String
# Test Case :
# Anchal :23581,Aman:57568,Sonakshi:34848,Ria:14585
# Output = aXiR

input = input()
list_of_inputs = list(input.split(','))
final_string = ''
for key_pair in list_of_inputs:
    x , y = key_pair.split(':')
    max = 0
    length_of_x = len(x)
    for  number in y:
        if int(number) <= length_of_x and  int(number) > max:
            max = int(number)
    if max == 0:
        final_string += 'X'
    else:
        final_string += x[max-1]
print(final_string)
