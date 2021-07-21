thisset = {1,2,3,4,5,6}
a=input("Enter the number to be deleted : ")
a=int(a)
if a in thisset:
    thisset.remove(a)

print(thisset)
