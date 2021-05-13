# Brackets matching {} () [] 
# If all the brackets are matched then return 0
# Otherwise return Mismatched position of bracket.

# Test Case
# {([])}
# output = 0

# Test Case
# {[[]])}
# output = 6

input = input()
n = len(input)
stack = ['']*n
top = -1
mismatched_position = 0
for i in range(n):
    if input[i]=='{' or input[i]=='[' or input[i] == '(':
        top += 1
        stack[top] = input[i]
    elif (stack[top] == '{' and input[i] == '}') or (stack[top] == '[' and input[i] == ']') or (stack[top] == '(' and input[i] == ')'):
        stack[top] = ''
        top -= 1
    else:
        mismatched_position = i + 1
        break
print(mismatched_position)
