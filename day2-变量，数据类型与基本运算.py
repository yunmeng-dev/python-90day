height=1.6
weight=44
age=20
print(height)
print(weight)
print(age)
print(type(height))
print(type(weight))
print(type(age))
bmi=weight/height**2
print(bmi)
if bmi<18.5:#range不支持浮点数 冒号要是英文的
    print("偏廋")
elif bmi>=24:
    print("偏胖")
else:#else后面不加条件
    print("正常")
apple,people=10,3
a=apple//people#每个人能拿多少苹果
b=apple%people#还剩几个苹果
print(a)
print(b)