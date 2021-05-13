instr = input()
outstr = ''
vowels = ['A','E','I','O','U','a','e','i','o','u']
for i in range(len(instr)):
    temp = instr[i]
    if instr[i] in vowels:
        res = i*5
        outnum = 0
        for num in range(1,res+1):
            if num%2 != 0:
                outnum += num
        if outnum >= 10:
            while outnum >= 10:
                outnum = sum(list(map(int, str(outnum))))

        temp = str(outnum)
    outstr += temp

print(outstr)




