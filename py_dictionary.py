# JawnPythias
# date:22/02/2024
# dictiionary  key:value
# tuple = ("ele1","ele2")

"""
一个人的信息,用字典存储
"""
friend = {"first_name": "name", "last_name": "Lname", "age": 25, "city": "LA"}
print("Name:" + friend["first_name"] + friend["last_name"])
print("Age:" + str(friend["age"]))
print("City:" + friend["city"])
"""
三个方法：
dict.keys()
dict.values()
dict.items()# 所有键值对
"""
"""
三条河流及国家
"""
rivers = {"nile": "Egypt", "Yangtze": "China",
          "Amazon River": "Brazil"}
for river, nation in rivers.items():
    print("The river " + river + " runs through " + nation)
for river in rivers.keys():
    print(river)
for nation in rivers.values():
    print(nation)
