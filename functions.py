def greet():
    print("Hello, welcome to python!")
greet()



def add(a,b):
   return a+b

result=add(5,3)
print(result)



def add(a,b=5):
    print(a+b)

add(10)
add(10,3)


def input(n1,n2):
  print("number 1 is:",n1)
  print("number 2 is:",n2)

print("call to function")
input(50,30)


def function(n1,n2=20):
    print("number 1 is:",n1)
    print("number 2 is:",n2)
function(50)
function(40,30)