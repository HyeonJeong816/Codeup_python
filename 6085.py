#6085
# w가로 h세로 b비트 
# 비트->MB 변환 /8/1024/1024
w,h,b=input().split()
w=int(w)
h=int(h)
b=int(b)
a=w*h*b
b=a/8/1024/1024
print('%.2f'%b,"MB")