#6088
a,d,n=map(int,input().split())
#방법1
for i in range(1,n):#1~n-1까지 반복
    a=a+d
print(a)
# #방법2
# a=a+(n-1)*d
# print(a)
