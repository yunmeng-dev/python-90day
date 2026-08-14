shopping=["苹果","李子","芒果"]
shopping.append("桃子")
shopping.insert(0,"荔枝")
shopping[3]="车厘子"
print(shopping)

c=[]
for i in range(1,11):#range后面跟的是()
    if i % 2 == 0:#每一个字符都要空一格
        c.append(i)
print(c)

d=list(range(2,11,2))
print(d)

e=[]
e.append("A")
e.append("B")
e.append("C")
O=e.pop(2)
print(O)
U=e.pop()
print(U)