#with default arguments
def add(a,b,c=0):
    return a+b+c

print(add(2,3))
print(add(2,3,4))


#using arguments
def add(*args):
    return sum(args)

print(add(2,3))
print(add(2,3,4,5))


    