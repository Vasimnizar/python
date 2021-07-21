
l = [1,2,3,4,5,6,7,8]
with open('test1.txt', 'w') as f:
    for items in l:
        f.write('%s\n' %items)
    print("File written successfully")
f.close()
f=open('test1.txt','r')
print(f.read())
