def add(x, y):
    print(x + y)

def sub(x, y):
    print(x - y)

def mul(x, y):
    print(x * y)

def div(x, y):
    print(x / y)


num_1 = int(input("enter number 1 : "))
num_2 = int(input("enter number 2 : "))

print("choose the following commands to perform the calculation")
print("1 to add")
print("2 to subtract")
print("3 to multiply")
print("4 to divide")

operation = int(input("enter the repesctive number to perform the opertation : "))

if operation == 1:
   add(num_1, num_2)

elif operation == 2:
   sub(num_1, num_2)

elif operation == 3:
   mul(num_1, num_2)


elif operation == 4:
   div(num_1, num_2)




 
