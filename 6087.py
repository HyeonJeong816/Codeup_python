#6087
a=int(input())
for i in range(1,a+1): #1~a까지 반복 
    #방법1
    # if i%3==0:
    #     continue
    # print(i,end=" ")
    #방법2
    if i%3!=0:
        print(i,end=" ")