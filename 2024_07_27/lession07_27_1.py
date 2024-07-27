import random
v=''
cho = []
for i in range(1,30):
    print (random.randrange(0,10) ,end = ' ')
    o = random.randint(1,10)
    v = v+ '  ' + str(o)
    cho.append (o)
print ()
c = random.choice(cho)
print (cho) 
print (v)
print ('幸運中選的號碼是',c)
random.shuffle(cho)
print (cho)
