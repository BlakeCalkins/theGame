import random

def rogue():
    return random.randint(1, 4) + random.randint(1, 4)
def warrior():
    return random.randint(1, 8) + 1
def strategist():
    return max(random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))
def sharpshooter():
    return random.choice([2, 8])
def dave_from_accounting():
    return 5
def speedster():
    sum = 0
    roll = random.choice([1, 4])
    sum += roll
    if roll == 4:
        while roll == 4:
            roll = random.choice([1, 4])
            sum += roll 
    return sum


def test_one_hundred_thousand_times(which_class):
    sum = 0
    for i in range(100000):
        sum += which_class()
    return sum / 100000

def main(): 
    # print(rogue())
    # print(warrior())
    # print(sharpshooter())
    print("strategist: ", test_one_hundred_thousand_times(strategist))
    return


# print("total is: ", speedster())
main()