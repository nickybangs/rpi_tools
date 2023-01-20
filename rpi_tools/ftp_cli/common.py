import random

def random_char():
    return chr(random.randint(ord('a'), ord('z')))

def random_chars(num):
    return ''.join([random_char() for i in range(num)])
