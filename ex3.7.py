import array
arra=[]

with open("test.txt",'r') as f:
  #4
  for l in f:
    x=f.readline()
    x=str(x)
    arra.append(x)
print(arra)
