# we are given string which contains at lease one special character , one even digit and one odd digit.
# then count no of special character.
# if count is even then print all even and odd digits alternatively. First take the even digit.
# else all odd and even digits alternatively. First take the odd digit.

# Test Case
# A5c67r21i@p#8t
# output : 652781

input = input()
even = []
odd = []
special_character_count = 0
for i in input:
    if not(i.isalnum()):
        special_character_count += 1

for i in input:
    if i.isdigit():
        if int(i)%2 == 0:
            even.append(int(i))
        else:
            odd.append(int(i))

if special_character_count%2 != 0:
    odd, even = even, odd

for b in range(max(len(odd),len(even))):
    if b < len(even):
        print(even[b] , end="")
    if b < len(odd):
        print(odd[b] , end="")

