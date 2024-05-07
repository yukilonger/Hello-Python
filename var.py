def add(i):
    i += 1
    return i

i = 1
for j in range(10):
    i = add(i)
    print(i)
