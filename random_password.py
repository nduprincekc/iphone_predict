import random
import string


def rand():
    chars = string.ascii_lowercase + string.digits
    size = 3
    return ''.join(random.choice(chars)for x in range(size,27))


t = rand()
print(t)

