def dekrübteerimine(sõnum):
    p =53
    q =59
    n = p*q
    with open("privaatne_võti.txt", "r") as b:
        d = [int(line.strip()) for line in b]
    print(d)
    list_num=[]
    list_sõn=[]
    sõnum=list(sõnum)
    #tagastab Unicode koodi vastava numbri jaoks ja dekrüpteerib selle
    for i in range(len(sõnum)):
        C = ord(sõnum[i])
        list_num.append(pow(C, d[-1], n))
    #muutab dekrüpteeritud koodi numbrideks tagasi
    for i in range(len(sõnum)):
        f = chr(list_num[i])
        list_sõn.append(f)
    sõnum="".join(list_sõn)
    print(sõnum)
