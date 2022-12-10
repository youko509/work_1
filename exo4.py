import random


def random_code():
    text="abcdefghijklmnopqrstuvwxyz0123456789"
    code = random.sample(text,k=20)
    code = ''.join(code)
    print(code)
    return code

random_code()