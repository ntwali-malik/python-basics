num1 = float(input("Enter First number: "))
op = input("Enter an Operator: ")
num2 = float(input("Enter Second Number: "))

if op == '+':
    print("Addition" , num1 + num2)
elif op == '-':
    print("subtraction", num1 - num2)
elif op == '*':
    print("Multiplication", num1 * num2)
elif op == '/':
    print("Division", num1/num2)
else:
    print("Wrong Operator!!")