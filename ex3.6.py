z=""
with open("test.txt",'r') as f:
  #4
  for l in f:
    x=f.readline()
    z+=x
print(z)
