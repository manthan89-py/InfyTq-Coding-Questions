# pronic number
import math

inputarr = input()
temp = set()

# finding substring
for i in range(len(inputarr)):
    for j in range(i, len(inputarr)):
        temp.add(int(inputarr[i:j+1]))

temp = sorted(list(temp))

# check for pronic number
outarr = []

for number in temp:
    for n in range(1, int(math.sqrt(number)) + 1):
        if n*(n+1) == number:
            outarr.append(number)
            break

print(outarr)


