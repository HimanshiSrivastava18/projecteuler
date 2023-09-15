num=int(input())
fac=1
sum=0
for i in range(1,num+1):
    fac=fac*i
a=(fac)
while a:
    b= a%10
    sum+=b
    a//=10
print(sum)