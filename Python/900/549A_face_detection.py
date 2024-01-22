def face_detection(arr,n,m):
    if n == 1 or m == 1:
        return 0
    face = {'f','a','c','e'}
    faces=0
    for i in range(0,n-1):
        for j in range(0,m-1):
            square = set(arr[k][l] for l in range(j,j+2) for k in range(i,i+2))
            print(square)
            if square ==  face:
                faces+=1
    return faces

n,m = [int(x) for x in input().split()]
arr = []
for ii in range(n):
    arr.append(list(input()))
print(face_detection(arr,n,m))