import sys

param = sys.argv
if len(param) > 1:
    print(param[1])
else:
    print('没有参数')
print('end argv')