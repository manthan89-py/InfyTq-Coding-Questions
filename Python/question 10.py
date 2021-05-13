# Check vertically , horizontly and diagonaly in Matrix. 
# If any number repeat 4 times then add that number in list.
# At the end return minimum from that list.
# If you will not find any number like that then return -1

row , col = list(map(int, input().split()))
answers = []
Matrix = []
for i in range(row):
    full_row = list(map(int,input().split()))
    Matrix.append(full_row)

for i in range(row):
    for j in range(col):
        # Horizontol
        if j < col-3:
            if Matrix[i][j] == Matrix[i][j+1]==Matrix[i][j+2]==Matrix[i][j+3]:
                answers.append(Matrix[i][j])
        # Vertical
        if i < row-3:
            if Matrix[i][j] == Matrix[i+1][j] == Matrix[i+2][j] == Matrix[i+3][j]:
                answers.append(Matrix[i][j])
        # Diagonal  Right -> Left
        if j < col-3 and i >= 3:
            if Matrix[i][j] == Matrix[i-1][j+1] == Matrix[i-2][j+2] == Matrix[i-3][j+3]:
                answers.append(Matrix[i][j])

        # Diagonal Left -> Right
        if j >= 3 and i >= 3:
            if Matrix[i][j] == Matrix[i-1][j-1]==Matrix[i-2][j-2]==Matrix[i-3][j-3]:
                answers.append(Matrix[i][j])

if len(answers) == 0:
    print("-1")
else:
    print(min(answers))

