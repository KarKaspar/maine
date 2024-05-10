# funktsioon võtab 2 listi ja loob uue listi kõigest mis esimeses listis on, aga teises ei ole.
def array_diff(a, b):
    z=[]
    for i in a:
        if i not in b:
            z.append(i)
    print(z)
    return z
