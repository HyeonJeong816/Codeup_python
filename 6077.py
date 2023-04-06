#6077
a=int(input())
sum=0
# for i in range(1,a+1):
#     if i%2==0:
#         sum=sum+i
# print(sum)

for i in range(0,a+1,2):
    sum=sum+i
print(sum)
