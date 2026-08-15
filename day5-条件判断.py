score=int(input("请输入分数:"))#input转为字符串，int转为整数
if score < 1 or score > 100:
    print("输入超出范围，请输入 1 到 100 之间的整数")
else:   
    if score >= 90:
        print("优秀")
    elif score >= 80:
        print("良好")
    elif score >= 60:
        print("及格")
    else:
        print("不及格")

year=int(input("请输入年份："))
if year % 4 == 0 and year % 100 != 0:
    print("这是闰年")
elif year % 400 == 0:
    print("这是闰年")
else:
    print("这不是闰年")

a = int(input("第一个数："))
b = int(input("第二个数："))
c = int(input("第三个数："))

if a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
else:
    max_num = c
print("最大的是：", max_num)

