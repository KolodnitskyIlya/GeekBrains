import random

def random_element(list):
    if len(list) == 0:
        return None
    return random.choice(list)

