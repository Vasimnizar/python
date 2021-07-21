_a=7
b5="rough"
print(type(_a))
print(b5)
b='mashupstack'
print(b)
a,b,c="python",1,"vasim"
print(a)
print(b)
print(c)

a=b=c="mashupstack"
print(a)
print(b)
print(c)

a="python"
b="Django"

print(type(a))
print("keywords")

a=["apple",1,"pineapple"]
print(a)
print(type(a))
a=("apple","oarange","banana")
print(a)
print(type(a))
import random
print(random.randrange(1,10))

x=int(2)
y=int(2.1)
z=int("2")
print(type(x))

a="aaaaaaaaaaaaaaasdsdqwdcqwcvcQC"

print(a[10])

for x in a:
	print(x)

print(len(a))
txt="The best things iin life are free!"
if "free" in txt:
	print("free is present in txt")
txt="The best things iin life are free!"
print("expensive" in txt)


b="Hello, world"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:2])
print(b.upper())
print(b.strip())
print(b.replace("H","J"))
print(b.split(","))

c="hai"

print(c+b)

a =b+ " " +c
print(a)
a="dogs"
print("I love {0}".format(a))
print("I love %s" %(a))
print(1<2)
print(1==1)
print(1>2)


print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))