# We are given two list find the sum of the list first.
# Then find pair from list1 and list2 that make both sum equal.
# After find that pair print first the pair which product is even number.
# After that print the odd number.
# Make sure print even and odd number with , seprated.
# If pair doesn't exist then return -1.

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

sum1 = sum(list1)
sum2 = sum(list2)
output = []

for i in list1:
    for j in list2:
        if sum1-i+j == sum2+i-j:
            output.append((i, j))
ans = []
for pair in output:
    if (pair[0]*pair[1])%2 == 0:
        ans.append(pair[0])
        ans.append(pair[1])

for pair in output:
    if (pair[0]*pair[1]) % 2 != 0:
        ans.append(pair[0])
        ans.append(pair[1])

if len(ans) == 0:
    print("-1")
else:
    for n in range(len(ans)-1):
        print(ans[n], end=',')
print(ans[len(ans)-1])


