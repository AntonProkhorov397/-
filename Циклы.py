t=0 #количество чисел
q=0 #int
while t<1:
    t+=1
    a=float(input("sisesta arv:"))
    if a==round(a): q+=1
print("Täisarvude kogus:",q)
#1
t=0
q=0
for t in range(1):
    a=float(input("sisesta arv:"))
    if a==round(a): q+=1
print("Täisarvude kogus:",q)
#2
A=4
s=0
for arv in range(1,a+1):
    s+=arv
print("Summa:",s)

#3
from random import *
korrutis=1
for i in range(8):
    B=randint(-100,100)
    print(B)
    if B>0: korrutis*=B
print("Korrutis on",korrutis)
#4
for a in range(10,20):
    print(a**2)
#6
p=0
from random import *
N=int(input("Mitu: "))
p=n=o=0
while N>0:
    N-=1
    B=randint(-100,100)
    print(B)
    if B>0:
        p+=1
    elif B<0:
        n+=1
    else:
        o+=1
print("Pos:",p)
print("Neg:",n)
print("Nul:",0)
#Задача:Купи слона!
loom=input("Купи слона")
while loom.title()!="Слон":
    loom=input("Все говорят"+loom+"!А ты купи!!!")
#17
Z=int(input("Sisesta arv "))
for i in range(1,10):
    print(Z,"*",i,"=",Z*i)
#15
for j in range(0,10):
    for i in range(0,10):
        print(i,end=" ")
    print()

for j in range(1,10):
    for i in range(1,10):
        print(f"{(j*i):2}",end=" ")
    print()
#16
for j in range(0,10):
    for i in range(0,10):
        if j==i:
            print(i,end=" ")
        else:
            print("0",end=" ")
    print()

import random
a=random.randint(1,10)
while True:
    text=input("Введите число или стоп для выхода: ")
    if text=="стоп":
        print("Выход из программы! До встречи! Загадано было",a)
        break
    elif text==a:
        print("Победа")
        break
    else:
        print("Попробуйте еще")





print("FOR".center(60,"$"))
for i in range(5):
    print("Hello world!!!")
print("WHILE TRUE")
k=0
while True:
    k+=1
    print("Hello world!!!")
    if k==5: break
print("WHILE Tingimusega")
k=0
while k<5:
    print("Hello world!!!")
    k+=1

