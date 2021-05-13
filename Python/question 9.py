
target = int(input())
list_num = list(map(int , input().split(" ")))
unique = set(list_num)
# print(unique)
frequency_list = []
for i in unique:
    frequency_list.append(list_num.count(i))
length = len(frequency_list)
frequency_list.sort()
# print(frequency_list)
for count in frequency_list:
    if target >= count:
        target -= count
        length -= 1
    else:
        break

print(length)

