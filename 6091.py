#6091
a,b,c=map(int,input().split())
day=1
#방법1
# while day%a!=0 or day%b!=0 or day%c!=0 :
#     day+=1
# print(day)

#방법2
for i in range(1,101):
    if i%a==0 and i%b==0 and i%c==0:
        print(i)