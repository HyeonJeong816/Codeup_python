#6097
h,w=input().split() #격자판의 가로 세로
h=int(h)
w=int(w)
n=int(input()) #막대의 개수

m=[]
#격자판 만들기
for i in range(h):
    m.append([])
    for j in range(w):
        m[i].append(0)

#막대 놓기
# for i in range(n) :
#   l,d,x,y = input().split()
#   if int(d)==0 :
#     for j in range(int(l)) :
#       m[int(x)-1][int(y)-1+j] = 1
#   else :
#     for j in range(int(l)) :
#       m[int(x)-1+j][int(y)-1] = 1
for i in range(n): #막대수 만큼 반복
    l,d,x,y=input().split()#막대의 길이(l), 방향(d), 좌표(x, y)가 입력
    l=int(l)
    d=int(d)
    x=int(x)
    y=int(y)
    for j in range(l):#막대 길이
        if d==0:#막대 가로 놓기
            m[x-1][y-1+j]=1
        else: #막대 세로 놓기
            m[x-1+j][y-1]=1

#격자 출력
for i in range(h):
    for j in range(w):
        print(m[i][j],end=" ")
    print()

