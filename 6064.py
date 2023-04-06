a, b ,c= input().split()
a = int(a)  #변수 a에 저장되어있는 값을 정수로 바꾸어 다시 변수 a에 저장
b = int(b)
c = int(c)
d =a if (a<=b) else b
d=d if (d<=c) else c
print(d)
"""if a<b:
    print(a)
else:
    print(b)

#print(int(c))"""