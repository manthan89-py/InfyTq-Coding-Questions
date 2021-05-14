# We are given one string.
# If string contain vowel then multiply its index with 5 and store it in result variable.
# Add all even number starting from 1 to result variable. 
# If adition of all even number is in more then two digits then we have to to addition of digits untill answer will not be in single digit.
# After getting the final answer replace vowel with that particular number.
# Print the output string.

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




