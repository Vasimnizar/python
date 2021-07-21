l1=["1",1,"hi",'hello']
print(l1)
print(l1[1:3])
print(l1[:4])
print(l1[0:])

for x in l1:
	print(x)
if 1 in l1:
	print("yes its available")
else:
	print("NO its not available")
print(len(l1))
l1.append("entahlla")
print(l1)

course = ['Python', 'PHP', 'C#', 'Javascript', 'Java']
course.pop()
print(course)


x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
print(x[0], x[2], x[4])
#x[1] and x[3] are sublists.
print(x[1]) 
print(x[3])

t1=(1,"python",2,[1,"java",2],(1,3,"hi"),3)
print(t1)



my_tuple = ("hello")
print(type(my_tuple))
my_tuple = ("hello",)
print(type(my_tuple))
my_tuple = "hello",
print(type(my_tuple))

t1=1,"python",2,[1,"java",2],(1,3,"hi"),3
print(type(t1))


# Accessing tuple elements using indexing
my_tuple = ('p','e','r','m','i','t')

print(my_tuple[0])   # 'p' 
print(my_tuple[5])   # 't'

# IndexError: list index out of range
# print(my_tuple[6])

# Index must be an integer
# TypeError: list indices must be integers, not float
# my_tuple[2.0]

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])       # 's'
print(n_tuple[1][1])       # 4


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[-1:-4])



course = {
  "language": "Python",
  "framework": "Django",
  "version": 2.0
}
print(course)