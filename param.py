def get_intersection(*args):
    l = list(args)
    same = set(l[0]).intersection(*l[1:])
    return list(same)


def get_subtraction(*args):
    l = list(args)
    same = set(l[0]).difference(*l[1:])
    return list(same)

a = [1,2,3,7,8]
b = [2,3,4]
c = [3,4,5]

d = get_subtraction(a, b, c)
print('差集',d)
e = get_intersection(a, b, c)
print('交集', e)

print(a,b,c)
