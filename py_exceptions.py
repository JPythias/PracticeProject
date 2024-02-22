# JawnPythias
# date:22/02/2024

user_input1 = input("请输入第一个数字：")
user_input2 = input("请输入第二个数字：")

try:
    result = int(user_input1) + int(user_input2)
except ValueError:
    print("请输入合理数字！")
else:
    print(result)