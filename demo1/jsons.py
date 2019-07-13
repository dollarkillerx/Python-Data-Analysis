import json

filename = "data.json"
mydata = {
    "title":"我的测试数据",
    "lesson":{
        "python":"学习中",
        'vue':"学习完毕",
        "golang":"基本精通"
    },
    "games":{
        "GAT":"一年没有玩了"
    },
}

# 文件写入
with open(filename,'w',encoding="utf-8") as data:
    # 数据,文件句柄,json缩进空格数
    json.dump(mydata,data,indent=4)

# 读文件
with open(filename,'r',encoding='utf-8') as data:
    # 句柄
    rdata = json.load(data)
    print(rdata)
