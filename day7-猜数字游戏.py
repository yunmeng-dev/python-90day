import random
a=random.randint(1,100)
count=0
while True:
    b=int(input("请输入1-100之间的整数:")) 
    count+=1
    if a<b:
        print("太大了")
    elif a>b:
        print("太小了")
    else:
        print(f"猜对了，你猜了{count}次")
        break
