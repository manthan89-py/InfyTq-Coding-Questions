# remove duplicate and reverse the string

string = input()
d = list(dict.fromkeys(string))
d.reverse()
print(d)
print("".join(d))