a = [1,2,3,4,5]

r = a[::-1]
print('数组反转', r)

print(a[3:8])
print('end可以越界')

print('正反截取:',a[1:-2])

print(a[8:])
print(a[-3:-1])
print(a[-3:1])
print(a[-2:])
print('start为负，end必须为负，否则返回空')
print('start为负若越界=索引0', a[-10:-1])


# print('数组不可越界：', a[8])


b = [6]
c= (b+a)[:-1]
print('合并数组', c)

print('正向反向截取', a[1:-2])


"""
对象数组排序
"""
# class Stock():
#     def __init__(self, code, name) -> None:
#         self.code = code
#         self.name = name

# stocks = []
# stocks.append(Stock(1, 'whl'))
# stocks.append(Stock(2, 'lzj'))
# stocks.append(Stock(3, 'xxx'))

# temp_stock = max(stocks, key=lambda x:x.code)
# print(stocks.index(temp_stock))
# print(temp_stock.name)

"""
['1','2','3'] -> [1,2,3]
"""
str_arr = ['1','2','3']
print(str_arr)
print('列表可以直接拼接到字符串里打印：')
print(f'a {str_arr}')
int_arr = list(map(int, str_arr))
print('map', int_arr)
int_arr = [int(x) for x in str_arr]
print('int', int_arr)


# 索引
def index_of(arr, obj):
    if obj in arr:
        return arr.index(obj)
    return -1

print(2,index_of(int_arr,2))
print(4,index_of(int_arr,4))


# 插入元素到数组开头
a = [1,2,3]
a.insert(0, 5)
print(f'a:{a}')

# 数组移除元素
print('数组移除元素:')
a = [1,2,3]
b = [2,3,4]
for e in b:
    if e in a:
        a.remove(e)
print(a)

# 去重
a = [1,1,3,3,4,5]
b = list(set(a))
print('去重', b)

# 差集
a = [1,2,3,4,7]
b = [2,3,9]
c = [3,4,5,6]
d = list(set(a)-set(b)-set(c))
print('差集',d)


