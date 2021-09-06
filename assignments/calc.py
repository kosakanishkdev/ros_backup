number_1 = int(input("enter number 1 : "))
number_2 = int(input("enter number 2 : "))

print("choose the following commands to perform the calculation")
print("1 to add")
print("2 to subtract")
print("3 to multiply")
print("4 to divide")

operation = int(input("enter the repesctive number to perform the opertation : "))

if operation == 1:
  sum = number_1 + number_2
  print(sum)

elif  operation == 2:
   sub = number_1 - number_2
   print(sub)

elif  operation == 3:
   mul = number_1 * number_2
   print(mul)

elif  operation == 4:
   div = number_1 / number_2
   print(div)

