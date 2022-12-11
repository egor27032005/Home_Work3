a=float(input())
f=0
while a%1!=0 :
 a=a*10
while a!=0:
 f=f+a%10
 a=a//10
print(int(f))