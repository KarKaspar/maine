# võtmete genereerimine
p =53
q =59
n = p*q
f = (p-1)*(q-1)
#avalik võti
e = 17
print(e)
#privaatne võti
d = pow(e, -1, f)
print(d)
#võtmete salvestamine faili
with open("avalik_võti.txt", "w") as f:
    f.write(str(e)+ "\n")
    f.close()
with open("privaatne_võti.txt", "w") as f:
    f.write(str(d)+ "\n")
    f.close()
