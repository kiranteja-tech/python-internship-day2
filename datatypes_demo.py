#declaration of variables of different datatypes
a=10
a2=20
b=10.2
c="kiran"
d=True
#printing type of each variable
print(type(a))
print(type(b))
print(type(c))
print(type(d))
#arthematic operations on integer variables
print("Arthematic operations")
print(a+b)#add
print(a-b)#sub
print(a/b)#div
print(a*b)#mul
print(a%b)
print(a//b)#floordiv
print(a**b)#square
#converting string input to int and float
user_input = input("Enter a number: ")
try:
    # Convert string input to integer
    number_int = int(user_input)
    print("Integer value:", number_int)
    # Convert string input to float
    number_float = float(user_input)
    print("Float value:", number_float)
except ValueError:
    # Handles invalid input such as alphabets or symbols
    print("Error: Invalid input! Please enter a numeric value.")
print("-" * 40)
#  String and number concatenation
score = 95
#convert number to string
message = "Your score is " + str(score)
print(message)
#  Demonstrating Dynamic Typing

value = 100          # Initially an integer
print("Value:", value, "| Type:", type(value))
value = "Hundred"    # Reassigned to string
print("Value:", value, "| Type:", type(value))
value = 100.50       # Reassigned to float
print("Value:", value, "| Type:", type(value))

