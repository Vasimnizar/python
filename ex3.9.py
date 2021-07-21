fname = 'test.txt'
count=0
with open(fname) as file:
    for line in (file.readlines()):
        #print(line)
        count+=1
print(count)
