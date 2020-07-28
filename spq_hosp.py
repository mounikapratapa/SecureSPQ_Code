# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 21:16:23 2020

@author: mouni
"""

import time
from Okamoto_Uchiyama import enc
import random
import numpy as np

def spq_hospital():
    dfin = []
    with open("C:/Users/mouni/OneDrive/Desktop/Research MESC/spq/result.txt","r") as res:
        for line in res:
            line = line.strip()
            line = line.split(",")
            dfin.append(line)
    encr = []
    for string in dfin:
        int_array = [int(x) for x in string]
        encr.append(int_array)
    print(encr)
    with open('C:/Users/mouni/OneDrive/Deskto/spq/g.txt', 'r') as file:
        g = file.readlines()
        g = int(''.join(g))
        print(g)
    with open('C:/Users/mouni/OneDrive/Desktop/spq/n.txt', 'r') as file:
        n = file.readlines()
        n = int(''.join(n))
        print(n)
    with open("C:/Users/mouni/OneDrive/Desktop/spq/seq_100.txt","r") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
    #a = '0000000000'  
    ED = []
    for i in content:
        df = [int(n) for n in i]
        arr=[[]]
        for j in range(len(df)):
            data = encr[j][df[j]]
            arr.append(data)
            arr = [x for x in arr if x != []]
        #print(arr)

        pk = n,g
        np.asarray(arr)
        prod = (np.prod(arr)) 
        #print("prod is:",prod)
        alpha = 42
        enc_beta = enc(pk,11)
        c = pow(prod,alpha,n)
        c = (c*enc_beta)%n
        r = random.randint(1,n)
        ct = pow(c,r**2,n)
        ED.append(ct)
    with open('decrypt.txt', 'w') as f:
        f.write("%s" %str(ED))
start = time.time()        
spq_hospital()
end = time.time()
print(end-start)
