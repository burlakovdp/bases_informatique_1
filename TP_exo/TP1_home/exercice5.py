import random as r

def random():
    return r.randint(1, 100)

prix = random()
print(prix)
i = 0
while(i < 15):
    prix = random()
    print(prix)
    i = i + 1