#6094
n=int(input())
num=input().split()
min=100
for i in range(n):
    if min>int(num[i]):
        min=int(num[i])
print(min)
