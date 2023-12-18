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


#przykład 2

print((lambda a:a+16)(4))
s = lambda  a,b,z:(a*b-2*z)/(a+b+z)

print(s(3,5,7))

num = [56,7,8,-9,0,.7,13,65,12,99,-100,3,4,12,-34]

nbparz = list(filter(lambda x:x%2==0,num))
print(nbparz)

cube = list(map(lambda x:x**3,num))
print(cube)

kwadraty = [i**2 for i in range(5,50,5)] #list comprehension
print(kwadraty)

#funkcja wyższego rzędu

import bfunkcje
from bfunkcje import konkurs,bonus

def witaj(imie):
    return f'Miło Cię widzieć {imie}'


def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Jan",67,12))
print(osoba(bonus,33,14))
