
import operator


# 按key排序
def sort_dict(dt, is_sort_by_key = True, is_desc = False):
    """
    字典按键排序
    默认按键升序排
    """
    return dict(sorted(dt.items(), key=lambda x:x[0 if is_sort_by_key else 1], reverse = is_desc))
volumes = {}
volumes['b'] = 3
volumes['a'] = 6
volumes['e'] = 1
volumes = sort_dict(volumes, True, True)
print('按键排序', volumes)
volumes = sort_dict(volumes, False, True)
print('按值排序', volumes)

print('判断是否包含键:')
if 'c' in volumes:
    print('volumes包含a键')

# 遍历
for temp in volumes:
    print(temp)
for key,value in volumes.items():
    print(key, value)

# 按字典值对象中某个属性排序
class Limit():
    def __init__(self,code) -> None:
        self.code = None
        self.up_count = 0
        self.down_count = 0

limit = {}
temp_limit = Limit('a')
temp_limit.up_count = 2
temp_limit.down_count = 3
limit['a'] = temp_limit

temp_limit = Limit('b')
temp_limit.up_count = 1
temp_limit.down_count = 6
limit['b'] = temp_limit

temp_limit = Limit('c')
temp_limit.up_count = 5
temp_limit.down_count = 1
limit['c'] = temp_limit

print('按up_count降序排')
up = dict(sorted(limit.items(), key=lambda x:x[1].up_count, reverse=True))
for code, temp in up.items():
    print(code, temp.up_count)

print('按down_count升序排')
down = dict(sorted(limit.items(), key=lambda x:x[1].down_count))
for code, temp in down.items():
    print(code, temp.down_count)

print('合并字典')
a = {1:'a',2:'b'}
b = {3:'c',4:'d'}
all = {}
all.update(a)
all.update(b)
print(all)

"""
字典转数组
"""
print('字典转数组')
d = {'a':1, 'b':3, 'c':9 }
print('打印字典',d)
print('打印字典的键',list(d.keys()))
print('打印字典的值',list(d.values()))
a = [x for _,x in d.items()]
k = list(d)
print(a)
print(k)


class OpenAmplitude():
    def __init__(self, date, open5, open10) -> None:
        self.date = date
        self.open5_amplitude = open5
        self.open10_amplitude = open10
    def __str__(self) -> str:
        return f'{self.date},{self.open5_amplitude},{self.open10_amplitude}'

amplitudes = {}
amplitudes['2021'] = OpenAmplitude('2021', 1, 2)
amplitudes['2022'] = OpenAmplitude('2022', 3, 4)
amplitudes['2023'] = OpenAmplitude('2023', 5, 6)

# a = []
# for amplitude in amplitudes.values():
#     a.append()
a = ';'.join(list(map(lambda x:str(x), amplitudes.values())))
print(a)