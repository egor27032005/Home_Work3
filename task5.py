print("Введите длину массива: ")
n=int(input())
list=[]
print("Введите элементы массива: ")
for i in range(n):
    a=int(input())
    list.append(a)
print(list)
from random import randint
def mix(list):
    for i in range(n):
        j=randint(0,n-1)
        per=list[i]
        list[i]=list[j]
        list[j]=per
mix(list)
print(list)


