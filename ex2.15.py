import random
Up_Alp=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Lo_Alp=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
Num=[1,2,3,4,5,6,7,8,9,0]
SYM = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
ulist=[]
llist=[]
nlist=[]
slist=[]
#ulen=len(ulist)
#llen=len(llist)
#nlen=len(nlist)
#slen=len(slist)
i=0
while(i<=3):
    a=random.choice(Up_Alp)
    #print(a)
    if a not in ulist:
        ulist.append(a)
        #print(ulist)
        i+=1
i=0
while(i<=3):
    a=random.choice(Lo_Alp)
    #print(a)
    if a not in llist:
        llist.append(a)
        #print(llist)
        i+=1
i=0
while(i<=3):
    a=random.choice(SYM)
    #print(a)
    if a not in slist:
        slist.append(a)
        #print(slist)
        i+=1
i=0
while(i<=3):
    a=random.choice(Num)
    #print(a)
    if a not in nlist:
        a=str(a)
        nlist.append(a)
        #print(nlist)
        i+=1
plist=ulist+llist+slist+nlist
#print(plist)
random.shuffle(plist)



def convert(plist):
	new = ""
	for x in plist:
		new += x
	print(new)
print(convert(plist))
