def unique_in_order(sequence):
    alist = list(sequence)
    if len(alist)==0:
        return []
    else:
        anolist = [sequence[0]]
        for i in range(1,len(sequence)):
            if sequence[i-1] == sequence[i]:
                a=1
            else:
                anolist.append(sequence[i])
        return (anolist)
