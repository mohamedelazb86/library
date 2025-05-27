import random


def generate_code(length):
    data='0123456789QWERTYUIOPLKJHGFDSAZXCVBNM'
    code=''.join(random.choice(data)for _ in range(length))
    return code