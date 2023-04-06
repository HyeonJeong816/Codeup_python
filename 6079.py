# #6079
# a=int(input())
# i=0
# sum=0
# while(1):
#     sum=sum+i
#     if sum>=a:
#         break
#     i=i+1
# print(i)

#6079
a=int(input()) #정수 하나 입력 
i=0 #1~반복될 변수 
sum=0 #합계저장 
while(sum<a): #조건에 의해서 반복이 끝날 경우 
    i=i+1
    sum=sum+i

print(i) #어디까지 더했는지를 출력 
