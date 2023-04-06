#6092
n=int(input())#출석 횟수
a=input().split()

stu=[]
for i in range(0,24): #학생을 0으로 초기화
    stu.append(0) #stu[i]=0
for i in range(0,n): #출석횟수를 stu리스트에 저장 
    stu[int(a[i])]+=1

for i in range(1,24):
    print(stu[i],end=' ')
