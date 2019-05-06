print("hello world python")

# 单行注释

'''
多行注释1
'''

"""
多行注释2
"""

# 数据类型
print()
print("###########")
print("# 数据类型 #")
myInt = 1
myString = "my str"
myBoolean = True
myFloat = 1.2

print(type(myInt))
print(type(myString))
print(type(myBoolean))
print(type(myFloat))

# 基本运算
print()
print("###########")
print("# 基本运算 #")
num1 = 10
num2 = 5
print(num1 + num2)
print(num1 - num2)
print(num2 - num1)
print(num1 * num2)
print(num1 / num2)

# 取模
print()
print("###########")
print("取模 : " + str(num1 % num2))
print("取模 : " + str(num2 % num1))
# 幂运算
print("幂运算 : " + str(4 ** 3))
# 取整
print("取整 : " + str(4 // 3))

# 赋值运算符
print()
print("###########")
print("赋值运算符")
num1 = 2
num1 += 5
print("num1 = 2, num1 += 5 : " + str(num1))
num1 = 10
num1 %= 2
print("num1 = 10, num1 %= 2 : " + str(num1))

# 进制运算
# 十进制 -> X进制
i = 16
print()
print("###########")
print("进制运算")
print("十进制 -> X进制")
print("十进制 : " + str(i))
print("二进制 : " + str(bin(i)))
print("八进制 : " + str(oct(i)))
print("十六进制 : " + str(hex(i)))

# X进制 -> 十进制
i = "100"
print()
print("X进制 -> 十进制")
print("二进制 : " + str(int(i, 2)))
print("八进制 : " + str(int(i, 8)))
print("十六进制 : " + str(int(i, 16)))

# 位运算
print()
print("###########")
print("位运算")
i = 3  # 00011
j = 10  # 00110
print("i :" + str(i) + " ---- " + str(bin(i)))
print("j :" + str(j) + " ---- " + str(bin(j)))
print("按位 与 : ")
print("i & j : " + str(i & j))
print("按位 或 : ")
print("i | j : " + str(i | j))
print("按位 异或 : ")
print("i ^ j : " + str(i ^ j))
print("按位 取反 (-i-1) : ")
print("~i : " + str(~i))
print("左移 运算符 :")
print("i << 2 : " + str(i << 2))
print("右移 运算符 :")
print("i >> 2 : " + str(i >> 2))

# 条件控制
print()
print("###########")
print("条件控制")
'''
形式一
if condition :
    statement

形式二
if condition:
    statement
else:
    statement

形式三
if condition:
    statement
elif condition:
    statement
elif condition:
    statement
(else:
    statement)   

'''
i = int(input("请输入数字 : "))
if i > 0:
    print("positive")
elif i < 0:
    print("negative")
elif i == 0:
    print("zero")
else:
    print("invalid")

