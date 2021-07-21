with open('first.txt','r') as firstfile, open('second.txt','a') as secondfile:
    for line in firstfile:
             secondfile.write(line)
f=open('second.txt','r')
print(f.read())
