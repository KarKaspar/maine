def array_diff(a, b):
    z=[]
    for i in a:
        if i not in b:
            z.append(i)
    print(z)
    return z
