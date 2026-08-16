# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i*j}",end=" ")# 打印式子，不换行
#     print()  # 一行打完，换到下一行

# import random# 导入随机数库
# result=random.randint(1,100)#函数.randint随机整数
# count = 0#计数器，循环外为0
# while True:
#     a=int(input("输入1-100内的数字:"))#每轮都重新问一次
#     count += 1
#     if a > result:
#         print("太大")
#     elif a < result:
#         print("太小")
#     else:
#         print(f"猜中用了{count}次")
#         break

total=0
for v in range(1,101,2):
    total += v
print(total)