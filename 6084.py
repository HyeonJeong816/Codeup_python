#6084
#횟수:h , 비트수 :b , 채널 : c , 초:s
#저장용량 = 음질(횟수)*비트수*채널수*초
#비트수 => MB 변환 = 저장용량/8/1024/1024
h,b,c,s=input().split()
h=int(h)
b=int(b)
c=int(c)
s=int(s)
a=h*b*c*s
b=a/8/1024/1024
print(round(b,1),"MB")