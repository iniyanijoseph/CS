import random


def linemaker(file):
    route = []
    for line in open(file, "r").readlines():
        if line != "":
            route.append(line)
    return route


cinder = linemaker("cinder.txt")
rapunz = linemaker("rapunz.txt")
combt = ""
for element in range(100):
    linechoice = random.randint(1, 100)
    if 1 <= linechoice <= 30:
        combt += random.choice(cinder)
    elif linechoice >= 50:
        combt += random.choice(rapunz)
print(combt)
