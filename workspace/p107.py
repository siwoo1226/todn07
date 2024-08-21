import random
def rolloing_dice(pip,repeat):
    for r in range(1,repeat+1):
        n=random.randint(1,pip)
        print(r,n)
rolloing_dice(6,5)
