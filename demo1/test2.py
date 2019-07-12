# 数据基本操作
mylist = ["dollar","killer","hello","world"]
print(mylist)
print(mylist[0])
print(mylist[1])
print(mylist[2].title())

# 修改元素
mylist[0] = "curry seth"
print(mylist)

# 元素增加
mylist.append('dollarkilelr')
print(mylist)

# 初始化
mylist = []
mylist.append("hello")
mylist.append("world")
mylist.append("bbr")
print(mylist)

# 删除元素
del mylist[0]
print(mylist)

# 指名删除
print(mylist)
mylist.remove("bbr")
print(mylist)