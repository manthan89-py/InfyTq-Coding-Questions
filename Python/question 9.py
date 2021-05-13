# We are given a list and number of elements deletion X.
# We have to delete X elements from the list so that at the end we get minimum unique elemetns in the list.
# Print the final minimum no of unique elements in the list

# Test Case
# 4
# 1 1 1 2 2 3 3 4 5 6
# output : 3

# Test Case
# 2
# 1 1 2 3 4 4
# output : 2


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

