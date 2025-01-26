#When you compare two values, the expression is evaluated and Python returns the Boolean answer:
print(10 > 9)
print(10 == 9)
print(10 < 9)

#When you run a condition in an if statement, Python returns True or False:
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#Most Values are True
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#Some value are false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#Function that returns a Boolean Value:
def myFunction() :
  return True

print(myFunction())

#Print "YES!" if the function returns True, otherwise print "NO!":
if myFunction():
  print("YES!")
else:
  print("NO!")

#Function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))
