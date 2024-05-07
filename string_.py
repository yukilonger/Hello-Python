
"""
填充几个空格
"""
len_ = 4
print(len_*' ', 1)


"""
以什么字符开头，以什么字符结束
"""

url= 'http:///'
if url.startswith('http'):
    print('以http开头')
if not url.endswith('http'):
    print('不是以http结尾')