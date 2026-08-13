def task1():
    a=" Hello, World!"
    b=a.strip()#首尾空格/换行
    c=b.lower()#全部小写
    d=c.split(",")#用逗号分隔开
    return d
def task2():
    name="yunmeng"
    age=19
    city="四川"
    favorite_word="进步"
    print("个人信息卡")
    print(f"名  字:{name}")
    print(f"年  龄:{age}")
    print(f"城  市:{city}")
    print(f"口头禅:{favorite_word}")
def reverse_upper(s:str):
    return(s[::-1].upper())
print(task1())
task2()
print((reverse_upper("str")))