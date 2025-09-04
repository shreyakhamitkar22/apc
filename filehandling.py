
with open("example.txt","w") as file:
    file.write("hello")

with open("example.txt","r") as file:
    print(file.read())

file.seek(6)
print(file.read())


