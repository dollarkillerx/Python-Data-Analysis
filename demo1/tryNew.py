try:
    print(10/0)
except:
    print("除0错误")
else: # 没有错误执行
    print("正常处理")
finally: # 不管有没有错误都执行
    print('end')