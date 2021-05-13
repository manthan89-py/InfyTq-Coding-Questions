# We are given on list of numbers.
# check of each number if sum of factors of that number present in the list.
# If Present print that number
# otherwise -1

# Test Case
# 0,1,6
# output : 0 1 6


# Sum of factor
def factor(n):
    sum = 0
    if n == 0:
        return
    if n == 1:
        return 1
    for i in range(1,n):
        if n%i == 0:
            sum += i
    return sum

list_of_numbers = list(map (int, input().split(",")))
flag = 0
for number in list_of_numbers:
    if factor(number) in list_of_numbers:
        flag = 1
        print(number)
if flag == 0:
    print("-1")


