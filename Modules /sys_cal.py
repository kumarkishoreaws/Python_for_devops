import sys

def add(num1,num2):
  Addition = num1+num2
  return "Addition of two numbers is :" + str(Addition)

def sub(num1,num2):
 Subtraction = num1-num2 
 return "Subtraction of two numbers is :" + str(Subtraction)

def mul(num1,num2):
  Multiplication = num1*num2
  return "Multiplication of two numbers is :" + str(Multiplication)

def div(num1,num2):
   Division = num1 / num2
   return "Division of two nymbers is :" + str(Division)

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "+":
  print(add(num1,num2))

elif operation == "-":
  print(sub(num1,num2))

elif operation == "mul":
   print(mul(num1,num2))

elif operation == "/":
  print(div(num1,num2))

else:
  print("Invalid operation")