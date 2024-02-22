# JawnPythias
# date:22/02/2024

"""
创建列表，并且依次打印列表中的元素
"""
names = ["111","222","333"]
print(names[0])
print(names[1])
print(names[2])
"""
为每个元素打印一条消息
"""
greeting = "test elements: "
print(greeting + names[0])
print(greeting + names[1])
print(greeting + names[2])
"""
替换元素
"""
names[1] = "444"
print(names)
"""
增删
"""
names.insert(0,"555")
print(names)
names.insert(2,"666")
print(names)
names.append("777")
print(names)
"""
遍历列表：for loop
"""
for name in names:
    print(name + " testing for-loop")
print("End testing")
"""
数值列表
"""
# 求和：从1到100
total = 0
for i in range(1,101):
    total = total + i
print(total)
# 包含顺序一百万的列表
numbers = []
for num in range(1,1000001):
    numbers.append(num)
for num in numbers:
    print(num)
print(min(numbers))
print(max(numbers))
print(sum(numbers))