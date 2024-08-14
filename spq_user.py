import time
from Okamoto_Uchiyama import enc, modinv
import random
import numpy as np
t = 0.80
def spq_user():
    dfin = []
    with open("enc_rec.txt","r") as res:
        for line in res:
            line = line.strip()
            line = line.split(",")
            dfin.append(line)
    encr = []
    for string in dfin:
        int_array = [int(x) for x in string]
        encr.append(int_array)
    print(encr)
    with open('g.txt', 'r') as file:
        g = file.readlines()
        g = int(''.join(g))
        print(g)
    with open('n.txt', 'r') as file:
        n = file.readlines()
        n = int(''.join(n))
        print(n)
    with open("enc_seq.txt","r") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
    #a = '0000000000'  
    ED = []
    for i in content:
        df = [int(n) for n in i]
        arr=[]
        for j in range(len(df)):
            data = encr[j][df[j]]
            arr.append(data)
            arr = [x for x in arr if x != []]
        #print(arr)

        pk = n,g
        np.asarray(arr)
        prod = (np.prod(arr)) 
        prod = enc(pk, t)*modinv(prod)
        alpha = 2
        enc_beta = enc(pk,1)
        c = pow(prod,alpha,n)
        c = (c*enc_beta)%n
        r = random.randint(1,n)
        ct = pow(c,r**2,n)
        ED.append(ct)
    with open('decrypt.txt', 'w') as f:
        f.write("%s" %str(ED))
start = time.time()        
spq_user()
end = time.time()
print(end-start)
