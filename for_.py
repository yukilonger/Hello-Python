import time


# for循环时有一个值有异常，等待5秒后继续尝试此值
e = 0
def read(i):
    global e
    try:
        for j in range(i,10):
            print(j)
            if j > 3 and e < 3:
                raise Exception('我的异常')
    except Exception as ex:
        print(ex)
        e += 1
        time.sleep(5)
        read(j)

# read(0)

# for的对象不能为None
# a = None
# for i in a:
#     pass

print('倒叙for：')
for i in range(10,-1,-1):
    print(i)


"""
跨i
"""
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
len_a = len(a)
for i in range(0, len_a, 3):
    print(a[i], a[i+2])