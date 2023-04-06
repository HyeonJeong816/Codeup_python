r,g,b=map(int,input().split())
sum=0
for i in range(0,r): #0~r-1 반복
    for j in range(0,g): #0~g-1반복
        for k in range(0,b): #0~b-1반복
            print(i,j,k)
            sum=sum+1
print(sum)
