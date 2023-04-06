h,w = input().split()
h = int(h)
w = int(w)

m = []
for i in range(h+1) :
  m.append([])
  for j in range(w+1) :
    m[i].append(0)

n = int(input())
for i in range(n) :
  l,d,x,y = input().split()
  if int(d)==0 :
    for j in range(int(l)) :
      m[int(x)-1][int(y)-1+j] = 1
  else :
    for j in range(int(l)) :
      m[int(x)-1+j][int(y)-1] = 1

for i in range(h) :
  for j in range(w) :
    print(m[i][j], end=' ')
  print()
