num1 = input("Please input number 1 :")
opr = input("Please input operator : ")
num2 = input("Please input number 2 :")

num1_float = False
num2_float = False

if num1.find(".") != -1:
    num1_float = True
    num1 = float(num1)
else:
    num1 = int(num1)

if num2.find(".") != -1:
    num2_float = True
    num2 = float(num2)
else:
    num2 = int(num2)


result = 0
if opr == "+":
    result = num1 + num2
elif opr == "-":
    result = num1 - num2
elif opr == "*":
    result = num1 * num2
elif opr == "/":
    result = num1 / num2
elif opr == "%":
    result = num1 % num2
elif opr == "**":
    result = num1 ** num2
elif opr == "//":
    result = num1 // num2
else:
    result = "Invalid operator !!!"

print("result = " + str(result))




