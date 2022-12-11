n=int(input())
sum=0
list=[]
for i in range(1,n+1):
    il=round((1+1/i)**i,2)
    list.append(il)
    sum=sum+il
print(list)
print(sum)