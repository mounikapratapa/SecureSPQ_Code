

from Okamoto_Uchiyama import dec
import time
start = time.time()



with open('g.txt', 'r') as file:
        g = file.readlines()
        g = int(''.join(g))

with open('sk.txt', 'r') as file:
        sk = file.readlines()
sk =  p,q

EvalScores=[]
with open('decrypt.txt', 'r') as file:
        for c in file:
            c = c.replace("[", "")
            c = c.replace("]", "")
            for ct in c.strip().split(','):
                ct = int(ct)
                result = dec(sk,g,ct)
                es=kronecker(result,p)
                
                EvalScores.append(es)

end = time.time()
print(end-start)       
