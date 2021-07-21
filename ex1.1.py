import datetime
name=input("enter your name : ")
age=input("enter your age : ")
age=int(age)
print("Dear %s your current age is %d" %(name,age))
newage=100-age

x=datetime.datetime.now()
hyear=x.year+newage
print("Dear %s you will become hundred years old on %d "%(name,hyear))
