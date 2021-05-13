# remove duplicate and reverse the string

# Test Case
# google
# output : elog

# Test Case
# infosys
# ysofni

string = input()
d = list(dict.fromkeys(string))
d.reverse()
print(d)
print("".join(d))
