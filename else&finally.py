try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print("Result:", result)
finally:
    print("Program finished.")   # Always runs
