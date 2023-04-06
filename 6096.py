#6096
d=[]
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)
#바둑돌 입력하기
for i in range(1,20) :
  a = input().split()
  for j in range(1,20) :
    d[i][j] = int(a[j])
    
#바둑돌 입력받은 수만큼 뒤집기
n=int(input())
for i in range(n):
    x,y=input().split()
    for j in range(1,20):
        if d[j][int(y)]==0:
            d[j][int(y)]=1
        else:
            d[j][int(y)]=0
        if d[int(x)][j]==0:
            d[int(x)][j]=1
        else:
            d[int(x)][j]=0
#바둑돌 출력하기
for i in range(1,20):
    for j in range(1,20):
        print(d[i][j],end=" ")
    print()