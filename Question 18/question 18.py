# convet decimal number to given base number and
# find maximun continous occuring zeros
# sample input
# 68
# 2
# output = 3

def num_to_base(num,base):
    output = ''
    while num > 0:
        d = int(num%base)
        if d < 10:
            output += str(d)
        else:
            output += chr(ord('A')+d-10)
        num = num // base
        # reverse the string
        # output = output[::-1]
    return output[::-1]

innum = int(input())
inbase = int(input())
converted_number = num_to_base(innum,inbase)
counter = 0
print(converted_number)
for i in range(len(converted_number)-1):
    if converted_number[i] =='0'  and converted_number[i+1]=='0':
        counter += 1
if counter == 0:
    print("-1")
else:
    print(counter)

