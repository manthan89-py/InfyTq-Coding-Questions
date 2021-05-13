# longest prefix and suffix conditions are both are equal and not overlapped
# print the length of suffix or prefix

# Test Case 
# abcdabc
# output : 3

# Test Case 
# ababa
# output : 2


input = input()
length = len(input)

mid = length // 2

for i in range(mid, 0, -1):
    prefix = input[:i]
    suffix = input[length-i:]
    if prefix == suffix:
        print(len(prefix))
        break

