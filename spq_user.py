# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 20:00:04 2020

@author: mouni
"""

from Okamoto_Uchiyama import enc,keys
import time
start = time.time()
precomp = [[0,1,4],[1,0,1],[4,1,0]]
def spq_encrypt(query,pk):
        c = enc(pk,query)
        return c
def spq_user():
    disp = str(input("Please enter your input query sequence:"))
    pk, sk = keys(100)
    n,g = pk
    with open('g.txt', 'w') as f:
        f.write("%s" %str(g))
    with open('sk.txt', 'w') as f:
        f.write("%s" %str(sk))
    with open('n.txt', 'w') as f:
        f.write("%s" %str(n))
    df = [int(n) for n in disp]
    print(df)
    res =[]
    for i in df:
        data = [spq_encrypt(x,pk) for x in precomp[i]]
        res.append(data)
    print(res)
    with open('result.txt', 'w') as f:
        f.write("%s" %str(res))
spq_user()
end = time.time()
total = end - start
print(total)    
