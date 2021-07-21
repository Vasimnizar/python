f = open('test.txt')
z=0
for word in f.read().split():
    x=len(word)
    if x>z:
        z=x
        y=word
    else:
        pass
print(z)
print(y)
