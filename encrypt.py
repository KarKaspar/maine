def krübteerimine(sõnum):
    p =53
    q =59
    n = p*q
    with open("avalik_võti.txt", "r") as b:
        e = [int(line.strip()) for line in b]
    print(e)
    b.close()
    list_num=[]
    list_sõn=[]
    sõnum=list(sõnum)
    #tagastab Unicode koodi vastava numbri jaoks ja krüpteerib selle
    for i in range(len(sõnum)):
        M = ord(sõnum[i])
        list_num.append(pow(M, e[-1], n))
    #muutab krüpteeritud koodi numbrideks tagasi
    for i in range(len(sõnum)):
        f = chr(list_num[i])
        list_sõn.append(f)
    krüpt="".join(list_sõn)
    print(krüpt)
    #salvestab faili
    with open("krübteeritud_sõnum.txt", "w", encoding="utf-8") as f:
        f.write(str(krüpt)+ "\n")
        f.close()
