import array
import secrets

arr = array.array('i')

for i in range(1000000000):
    if i % 10000000 == 0:
        print("Progress: {}%".format(i/10000000))

    rndInt = secrets.randbits(16)
    arr.append(rndInt)

with open("rnd-secrets.bin", "wb") as f:
    arr.tofile(f)