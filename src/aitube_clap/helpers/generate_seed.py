import random

def generate_seed() -> int:
    """ Generate a random seed value """
    return random.randint(0, 2**31 - 1)

