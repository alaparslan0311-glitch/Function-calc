def add(a , b):
    return(a + b)
def subtract(a , b):
    return(a - b)
def multiply(a , b):
    return(a * b)
def divide(a , b):
    return(a / b)

try:
  number1 = float(input("Enter the first number: "))
  number2 = float(input("Enter the second number: "))

  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")

  choice = input("Enter an operation: ")
  if choice == "1":
    print("The sum is:", add(number1, number2))
  elif choice == "2":
    print("The result is:", subtract(number1, number2))
  elif choice == "3":
    print("the result is:", multiply(number1, number2))
  elif choice == "4":
    print("The result is:", divide(number1, number2))
  else:
    print("Invalid choice.")
    
except ValueError:
  print("please enter a number only!")
except ZeroDivisionError:
  print("Cannot divide by zero!")


    