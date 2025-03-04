import array
import random

arr = array.array('i')

r = random.Random()
for i in range(1000000000):
    if i % 10000000 == 0:
        print("Progress: {}%".format(i/10000000))

    rndInt = r.randint(0, 1000)
    arr.append(rndInt)

with open("rnd-random.bin", "wb") as f:
    arr.tofile(f)