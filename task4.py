print('Введите N: ', end="")
n=int(input())
list=[]
sum=1
for i in range(2*n+1):
    list.append(-1*n+i)
print("Введите количество элементов: ", end="")
a=int(input())
for i in range(a):
    print("Введите номер элемента: ", end="")
    f=int(input())
    sum=sum*list[f]
        
print(list)
print(sum)

