import pickle

data = ['aa', 'bb', 'cc']

savePath = 'D:/pickleString.txt'
# dump将python的数据结构转换为pickle数据，并保存在文件中
with open(savePath, 'wb') as f:
    pickle.dump(data, f)
# load将读取文件中的pickle数据，并转换为python数据结构
with open(savePath, 'rb') as f:
    mes = pickle.load(f)
    print(type(mes), ':', mes)

# dumps将python的数据结构转换为pickle数据
p_str_dumps = pickle.dumps(data)
print(type(p_str_dumps), ':', p_str_dumps)
# loads将pickle数据转换为python的数据结构
mes_loads = pickle.loads(p_str_dumps)
print(type(mes_loads), ':', mes_loads)
