# a = int(input("Enter a number: "))

# if a % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# option = input("Enter an operator (+, -, *, /): ")

# if option == "+":
#     print(num1 + num2)
# elif option == "-":
#     print(num1 - num2)
# elif option == "*":
#     print(num1 * num2)
# elif option == "/":
#     if num2 != 0:
#         print(num1 / num2)
#     else:
#         print("Error: Division by zero is not allowed.")


# cal = 0
# for i in range(1, 101):
#     if i % 2 == 1 :
#         cal = cal + i
# print (cal)

# print('&&'.join(sorted("ping")))


cart = ["Rice", "Beans", "Sugar", "Salt", "Oil"]

cart.append("Flour")

cart.insert(2, "Tea")
print(cart)