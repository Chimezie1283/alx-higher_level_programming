
#!/usr/bin/python3

import random

numba = random.randint(-10000, 10000)

digitz = abs(numba) % 10

if numba < 0:

    digitz = -digitz

print("Last digit of {} is {} and is ".format(numba, digitz), end="")

if digitz > 5:

    print("greater than 5")

elif digitz == 0:

    print("0")

else:

    print("less than 6 and not 0")
