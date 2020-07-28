# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 12:25:57 2020

@author: mouni
"""

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
import sys
sys.setrecursionlimit(10000)
PtScores =[]
EvalScores=[]
with open('C:/Users/mouni/OneDrive/Desktop/Research MESC/spq/PlaintextED.txt', 'r') as file1:
        for m in file1:
            print(m)
            m = m.replace("[", "")
            m = m.replace("]", "")
            for pt in m.strip().split(','):
                pt = int(pt)
                PtScores.append(pt)
with open('C:/Users/mouni/OneDrive/Desktop/Research MESC/spq/evalres.txt', 'r') as file2:
        for c in file2:
            print(c)
            c = c.replace("[", "")
            c = c.replace("]", "")
            for ct in c.strip().split(','):
                ct = int(ct)
                EvalScores.append(ct)
accuracy=accuracy_score(PtScores,EvalScores)
precision = precision_score(PtScores,EvalScores)
def falsepos(y_actual, y_hat):
    FP = 0
    for i in range(len(y_hat)): 
        if y_hat[i]==1 and y_actual[i]!=y_hat[i]:
           FP += 1
    return FP
print(accuracy)
print(falsepos (PtScores,EvalScores))

                
