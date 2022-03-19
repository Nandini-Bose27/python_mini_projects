print("Select Operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
operation=input("Enter operation number")

if operation=="1":
     num1=input("Enter first number:")
     num2=input("Enter second number:")
     print("The sum is",int(num1)+int(num2))
     
elif operation=="2":
     num1=input("Enter first number:")
     num2=input("Enter second number:")
     print("The subtraction is", int(num1)-int(num2))
     

elif operation=="3":
     num1=input("Enter first number:")
     num2=input("Enter second number:")
     print("The multiplication is" ,int(num1)*int(num2))
     

elif operation=="4":
     num1=input("Enter first number:")
     num2=input("Enter second number:")
     print("The division is",int(num1)/int(num2))
     
else:
     print("Invalid")
 
     


