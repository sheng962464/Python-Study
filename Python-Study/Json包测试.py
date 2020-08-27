import json

Data = [100, "Python3", {"www": 1, "pythontab.com": 2, "Python3": 3}]

filePath = 'D:/jsonString.txt'
# dump将python的数据结构转换为json数据，并保存在文件中
with open(filePath, 'w') as f:
    json.dump(Data, f)
# load将读取文件中的json数据，并转换为python数据结构
with open(filePath, 'r') as f:
    mes = json.load(f)
    print(type(mes), mes)

# dumps将python的数据结构转换为json数据
p_str_dumps = json.dumps(Data)
print(type(p_str_dumps), p_str_dumps)
# loads将json数据转换为python的数据结构
mes_loads = json.loads(p_str_dumps)
print(type(mes_loads), mes_loads)
