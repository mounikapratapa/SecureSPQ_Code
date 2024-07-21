
import numpy as np
import time
start = time.time()

disp = input("Enter your query sequence:")
inp = [int(i) for i in disp]
a = np.array(inp)

with open("myOutFile.txt","r") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
Distance = []
for i in content:
    df = [int(n) for n in i]
    b = np.array(df)
    dist = np.linalg.norm(a-b)
    Dist = int(dist**2)
    Distance.append((Dist))

print(Distance)
ED = []
for d in Distance:
    if d < 35:
        ED.append(1)
    else:
        ED.append(0)


with open('PlaintextED.txt', 'w') as f:
        f.write("%s"%str(ED))
    
