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

