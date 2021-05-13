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

