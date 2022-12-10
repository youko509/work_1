import random


def random_code():
    text="abcdefghijklmnopqrstuvwxyz"
    code = random.sample(text,k=20)
    code = ''.join(code)
    print(code)
    return code

random_code()