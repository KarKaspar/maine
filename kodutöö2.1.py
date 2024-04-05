def dig_pow(n, p):
    l=list(str(n))
    null=0
    for i in range(len(l)):
        null=null+(int(l[i]))**(p+i)
    if null/n==int(null/n):
        return (null/n)
    else:
        return (-1)
