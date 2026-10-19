import random
from time import sleep
char=['0','1','2','3','4','5','6','7','8','9',' ']
p=[]
while True:
    s=''
    c=0
    for i in range(20):
        x=char[random.randint(0,10)]
        if x==' ':
            c+=1
            if c<10:
                while x!=' ':
                    x=char[random.randint(0,10)]
        s+=x
    sleep(0.1)

    print(s)