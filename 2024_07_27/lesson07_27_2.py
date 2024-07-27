import random

rn = random.sample(range(1,220),10)
print(rn)

cnt = 0
bnt = 0 
for i in rn:
    if i > 50:
        cnt+=1
        print (cnt,i)
    else:
        bnt+=1
print (bnt )