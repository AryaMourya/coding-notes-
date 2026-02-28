"""Loop question practice"""
##1
i=1
while (i<=10):
    print(i)
    i+=1
##2
i=10
while(i>=1):
    print(i)
    i-=1
##3
num=1
while(num<=50):
    if(num%2==0):
        print(num)
    num+=1
##4 (IMPORTANT)
n=int(input("Please enter the number:"))
sum=0
while(n>=1):
    sum+=n
    n-=1
print("sum=",sum)
##5
n=1
while(n<=4):
    print("*",n)
    n+=1