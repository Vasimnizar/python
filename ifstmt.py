num = 5
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
else:
    print(num, "is a negative number.")
print("This is also always printed.")




num = 3.14
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")



# To take input from the user,
n = int(input("Enter n: "))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1  
print("The sum is", sum)