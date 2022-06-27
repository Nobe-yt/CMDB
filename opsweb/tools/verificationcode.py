import random

class rcode:
    for i in range(1):
        rcode = ''
        for j in range(4):
            if random.randint(0, 1) == 0:
                rcode += str(random.randint(0, 9))
            else:
                rcode += chr(random.randint(65, 90))
        print(rcode)
