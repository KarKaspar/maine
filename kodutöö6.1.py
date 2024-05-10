# funktsioon leiab listis kõik numbrid mis ilmuvad paaritud arvu kaupa
def find_it(seq):
    seto = list(set(seq))
    for i in range(len(seto)):
        if seq.count(seto[i])%2==1:
            return seto[i]
