
#!/usr/bin/python3

import random

numba = random.randint(-10, 10)

if numba > 0:

    print("{} is positive".format(numba))

elif numba == 0:

    print("{} is zero".format(numba))

else:

    print("{} is negative".format(numba))
