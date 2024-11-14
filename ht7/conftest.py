from pytest import fixture
import random

@fixture
def generate_numbers():
    randomlist = random.sample(range(0,100), 10)
    return randomlist
