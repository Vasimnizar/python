
lis=[]

with open("test.txt",'r') as f:
  #4
  for l in f:
    x=f.readline()
    lis.append(x)
print(lis)
