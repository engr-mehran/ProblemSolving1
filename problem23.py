X=[[2,4,9],
   [8,2,5],
   [3,8,1]]

Y=[[1,0,4,5],
   [7,5,3,1],
   [2,3,6,8]]

result=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
             result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)

