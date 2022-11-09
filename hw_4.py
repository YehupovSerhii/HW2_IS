#1
n=int(input("Введите ширину треугольника#1 N:"))
while n>=1:
    print ("*"*n)
    n-=1

# #2
n=int(input("Введите ширину треугольника#2 N:"))
i=1
while i<=n:
    print ("*"*i)
    i+=1

#3
n=int(input("Введите ширину треугольника#3 N:"))
i=0
k=n
while i<=n:
    print (" "*i+ "*"*k)
    i+=1
    k-=1

#4
n=int(input("Введите ширину треугольника#4 N:"))
i=n-1
k=1
while k<=n:
    print (" "*i+ "*"*k)
    i-=1
    k+=1