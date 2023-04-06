a,b=input().split()
x=bool(int(a))
y=bool(int(b))
print((x and not(y)) or (not(x) and y))