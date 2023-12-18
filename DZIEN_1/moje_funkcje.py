#przykład 1
n=100
def policz(a:int,b:float,c:float,y:int=9)->float:
    global n
    n = (a+b)*y-c+n
    return n

print(policz(4,6,2,7))
print(policz(6,8.8,0.22,True))
print(n)
print(policz(4,6,2))

