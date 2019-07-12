mylist = ["curry","hidden","pps","ok"]

# 数组循环
print("Start.")
for name in mylist:
    print("\t",name)
print('End.')



# enumerate() 变成可枚举的对象
print("Start.")
for k,v in enumerate(mylist):
    print(k," : ",v)
print('End.')