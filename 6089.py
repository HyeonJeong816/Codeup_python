#6089
a,r,n=map(int,input().split())
#방법1
# for i in range(1,n):
#     a=a*r

#방법2
a=a*(r**(n-1))
print(a)