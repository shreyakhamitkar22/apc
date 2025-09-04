import array as arr
numbers= arr.array('i',[10,20,30])
numbers.append(40)
print(numbers)

import array as arr
numbers= arr.array('i',[30,80,50])
numbers.insert(1,50)
print(numbers)

numbers= arr.array('i',[10,20,30])
numbers.remove(20)
print(numbers)

numbers= arr.array('i',[10,90,30])
numbers.pop(1)
print(numbers)

numbers= arr.array('i',[10,80,30])
print(numbers.index(30))

numbers= arr.array('i',[90,80,70])
numbers.reverse()
print(numbers)

numbers= arr.array('i',[10,10,10,10,10,90,30])
print(numbers.count(10))

numbers= arr.array('i',[10,20,30])
more_numbers= arr.array('i',[40,50,60])
numbers.extend(more_numbers)
print(numbers)

numbers= arr.array('i',[10,80,30])
print(numbers.tolist())