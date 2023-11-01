X=[[2,4,8],
   [8,2,9],
   [3,8,1]]

Y=[[1,0,4],
   [7,5,3],
   [2,3,6]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j]=X[i][j]+Y[i][j]

for r in result:
    print (r)