# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:24:23 2020

@author: mouni
"""

from Okamoto_Uchiyama import dec
import time
start = time.time()
p = 70404470836673456642937968870480997199552877944781723511551237182454544842985007390607138146394452777
q=816923218412868614402781105203
sk =  p,q



with open('C:/Users/mouni/OneDrive/Desktop/spq/g.txt', 'r') as file:
        g = file.readlines()
        g = int(''.join(g))

'''with open('C:/Users/mouni/OneDrive/Desktop/spq/sk.txt', 'r') as file:
        sk = file.readlines()'''
EvalScores=[]
with open('C:/Users/mouni/OneDrive/Desktop/spq/decrypt.txt', 'r') as file:
        for c in file:
            c = c.replace("[", "")
            c = c.replace("]", "")
            for ct in c.strip().split(','):
                ct = int(ct)
                result = dec(sk,g,ct)
                es=kronecker(result,p)
                
                EvalScores.append(es)
with open('evalres.txt', 'w') as f:
        f.write("%s" %str(EvalScores))
end = time.time()
print(end-start)       
