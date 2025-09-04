ints=[1,2,3,4,5]
print(ints)
print(type(ints[0]))

floats=[1.4,2.5,3.6,4.7]
print(floats)
print(type(floats[0]))

strings=["apple","banana","mango","grapes"]
print(strings)
print(type(strings[0]))

booleans=[True ,False ,True ,False]
print(booleans)
print(type(booleans[0]))

nums = [5, 10, 15, 20]
print(sum(nums))         
print(max(nums))         
print(min(nums))        
print(nums[1] + nums[2]) 

marks = [88.5, 76.2, 92.8, 81.0]
avg = sum(marks) / len(marks)
print("Average:", avg)     
print(round(avg, 2))       

fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print(fruits)              
print(" & ".join(fruits))  
print(fruits[0].upper())   

flags = [True, False, True, True]
print(all(flags))  
print(any(flags))
print(flags.count(True))  
