import random

def rogue():
    return random.randint(1, 4) + random.randint(1, 4) + random.randint(1,4)
def warrior():
    return random.randint(1, 8) + 1
def dave_from_accounting():
    return 5

def test_one_hundred_thousand_times(which_class):
    sum = 0
    for i in range(100000):
        sum += which_class()
    return sum / 100000

def main(): 
    print(test_one_hundred_thousand_times(dave_from_accounting))

main()