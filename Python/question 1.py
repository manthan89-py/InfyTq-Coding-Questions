# From given number of list assume that 4 always comes first than 7.
# So you have to add all numbers except number between 4 and 7
# You have to concat the numbers between 4 and 7
# add both the number and output it.

input = '3,1,6,4,2,3,7,2'
numbers = input.split(',')

index_4 = numbers.index('4')
index_7 = numbers.index('7')

int_numbers = list(map(int , numbers))
addition = sum(int_numbers[:index_4]) + sum(int_numbers[index_7+1:])

concat_number = int(''.join(numbers[index_4:index_7+1]))

print(addition+concat_number)



