innum = int(input())

def is_palindrome(number):
    if number == number[::-1]:
        return True
    else:
        return False

# num1 - largest palindrome less then innum
# num2 - smallest palinndrom greater then innum

final_number = 0
num1 = 0
num2 = 0

while innum >= 0:
    num1 = innum - 1
    num2 = innum + 1

    while not (is_palindrome(str(num1))):
        num1 = num1 - 1

    while not (is_palindrome(str(num2))):
        num2 = num2 + 1

    if is_palindrome(str(num1)) and is_palindrome(str(num2)):
        final_number = num1 + num2
        if is_palindrome(str(final_number)):
            print(final_number)
            break
        else:
            innum -= 1

print(f"Final Number:{final_number} : {num1} + {num2}")
