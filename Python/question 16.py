# Consider MxN matrix m1 and PxQ matrix M2 cosisting of positive integers. Create and print outmatrix based ont that below logic.
# For every number num1 from M1 at row r1 and column c1 :
# (1) Multiply with each of the numbers num2 of M2 such that num2 is in (r1,r1) , (r1,c1) , (c1,c1) , (c1,r1) if exists.
# (2) Identify and add the product that occurs maximum number of times to outmatirx at row r1 and column c1.
# (3) If there are multiple product with maximum occurence then minimum value will be added yo row r1 anc column c1.
# (4) if both row and column in M2 doesn't exist equal to r1 and c1 then add -1 in the outmatrix at row r1 and column c1.


from collections import Counter
try:
    m = int(input())
    n = int(input())
    a = []
    for i in range(m):
        a.append(list(map(int, input().split())))
    lm = len(a[0])
    b = []
    for i in range(n):
        b.append(list(map(int, input().split())))
    ln = len(b[0])
    ans = [[-1 for _ in range(lm)] for _ in range(m)]
    for i in range(m):
        for j in range(lm):
            flag = 0
            tmp = []
            # print('i ',i)
            # print('j ',j)
            # print('ln ',ln)
            # print('n ',n)
            # ln -column length b array
            # n - row length of b array
            if (i < ln and i < n):
                tmp.append(a[i][j]*b[i][i])
                flag = 1
            if (i < ln and j < n):
                tmp.append(a[i][j]*b[j][i])
                flag = 1
            if (j < ln and i < n):
                tmp.append(a[i][j]*b[i][j])
                flag = 1
            if (j <ln and j < n):
                tmp.append(a[i][j]*b[j][j])
                flag = 1
            # print('tmp ',tmp)
            if flag == 1:
                tc = Counter(tmp)
                val = 0
                # print('tc ',tc)
                for k in tc.keys():
                    val = max(tc[k],val)
                tp = []
                for k in tc.keys():
                    if tc[k] == val:
                        tp.append(k)
                print('tp ',tp)
                ans[i][j] = min(tp)
    for i in range(m):
        print(*ans[i])
except EOFError as e:
    pass
