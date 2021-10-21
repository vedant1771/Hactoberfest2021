num_1 = int(input('Enter your first number: '))
num_2 = int(input('Enter your second number: '))
choice = input('Enter operator: ')
 
if choice == '+':
    print(num_1 + num_2)
 
elif choice == '-':
    print(num_1 - num_2)
 
elif choice == '*':
    print(num_1 * num_2)
 
elif choice == '/':
    print(num_1 / num_2)
 
else:
    print('Enter a valid operator, please run the program again.')

  

print("""
Basic Calculator

Please select an operation
1. Add
2. Substract
3. Multiply
4. Divide
""")
operation = operation = int(input("Operation from 1 to 4: "))
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
result = 0

if(operation == 1):
    result = num_1 + num_2
elif(operation == 2):
    result = num_1 - num_2
elif(operation == 2):
    result = num_1 * num_2
elif(operation == 2):
    result = num_1 / num_2
else:
    print("Invalid operation! please try again.")
    
print(f"The result is {result}")

  
