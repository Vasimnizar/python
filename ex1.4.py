num =input("enter the number : ")
num=int(num)
print("the divisors of num are :")
for x in range(num,0,-1):
     if (num%x)==0:
         print(x)
     else:
         pass
