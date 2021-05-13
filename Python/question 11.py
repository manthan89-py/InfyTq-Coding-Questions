# Find Largest subset from array that contains elements which are fibonaci number
# If more then two elements exist in the list then print its length otherwise -1.

# Test Case
# 3,2,5,8,9,10,11
# output : 5

input_arr = list(map(int, input().split()))
input_arr.sort()
max_element = input_arr[-1]
fib_series = []
num1 = 0
num2 = 1
fib_series.append(num1)
fib_series.append(num2)
while num2 < max_element:
    sum = num1 + num2
    num1 = num2
    num2 = sum
    fib_series.append(sum)
print(fib_series)
length = 0
for i in input_arr:
    if i in fib_series:
        length += 1

if length  > 2:
    print(length)
else:
    print("-1")

