# 前后补0
for i in range(20):
    # 前补0
    print(f'第{"{:0>2}".format(i)}集')
    # 后补0
    print(f'第{"{:0<2}".format(i)}集')


x = 123456789.87654321

# 保留两位小数
r1 = format(x,"0.2f")
print(r1)
# 123456789.88

# 金额用,隔开
r2 = format(round(x),",")
print(r2)
# 123,456,789.87654321

# 使用 e 的科学计数法
r3 = format(x,"e")
print(r3)
# 1.234568e+08

# 使用 E 的科学计数法
r4 = format(x,"0.2E")
print(r4)
# 1.23E+08