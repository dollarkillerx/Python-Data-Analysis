db_config = {
    "ip":"127.0.0.1",
    "port":5432,
    "uid":"dollarkiller",
    "pwd":"123456789"
}
print(db_config)

# 遍历所有属性
for key,val in db_config.items():
    print(key," : ",val)

# 遍历所有Key
for key in db_config.keys():
    print(key," : ",db_config[key])

# 遍历所有val
for val in db_config.values():
    print(val)
