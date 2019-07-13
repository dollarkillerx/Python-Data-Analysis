filename = "try.py"
content = ""
# 文件读取
with open(filename,"r",encoding="utf-8") as myfile:
    content = myfile.read()

# 文件写入
newFileName = "tryNew.py"
with open(newFileName,"w",encoding="utf-8") as newfile:
    newfile.write(content)
