import random
lis=[]

with open("test.txt",'r') as f:
  for l in f:
    x=f.readline()
    lis.append(x)
#print(lis)
print("the random line is : ")
print(random.choice(lis))
