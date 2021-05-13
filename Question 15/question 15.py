m = int(input())
M = []
for i in range(m):
    M.append(list(map(int, input().split())))
n = len(M[0])
no_of_total_elements = m * len(M[0])

zero_count = 0
for i in range(m):
    zero_count += M[i].count(0)
non_zero_element = no_of_total_elements - zero_count

if non_zero_element > zero_count:
    print("-1")
else:
    rowsum = 0
    colsum = 0
    for i in range(m):
        if non_zero_element > zero_count:
            break
        for j in range(n):
            if non_zero_element > zero_count:
                break
            if M[i][j] == 0:
                rowsum = sum(M[i])
                for k in range(m):
                    colsum += M[k][j]
                if rowsum <= colsum:
                    num = 1
                    while True:
                        if (rowsum + num) %2 == 0:
                            M[i][j] = num
                            non_zero_element += 1
                            zero_count -= 1
                            colsum = 0
                            break
                        else:
                            num += 1
                else:
                    num = 1
                    while True:
                        if(rowsum+num) %3==0:
                            M[i][j] = num
                            non_zero_element+=1
                            zero_count-= 1
                            colsum = 0
                            break
                        else:
                            num += 1

print(M)
