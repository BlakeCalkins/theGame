import random

def rogue(turn):
    return random.randint(1, 4) + random.randint(1, 4)
def warrior(turn):
    return random.randint(1, 8) + 1
def strategist(turn):
    return max(random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))
def musketeer(turn):
    if turn % 2 == 0:
        return random.randint(1, 20)
    if turn % 2 == 1:
        return 0
def bard(turn):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    return max(0, abs(a-b) - 2)
def gambler_dmg_given(turn):
    sum = 0
    roll = random.randint(1, 20)
    if roll % 2 == 0:
        sum += roll
    roll = random.randint(1, 20)
    if roll % 2 == 0:
        sum += roll
    return sum
def gambler_dmg_received(turn):
    sum = 0
    roll = random.randint(1, 20)
    if roll % 2 == 1:
        sum += roll
    roll = random.randint(1, 20)
    if roll % 2 == 1:
        sum += roll
    return sum
def forcer(turn):
    sum = 0
    for i in range(turn+2):
        if random.randint(1, 20) == 20:
            sum = 50
    return sum
def paladin(turn):
    return random.randint(1, 6) 
def parasite(turn):
    return random.randint(1, 4)
def sharpshooter(turn):
    return random.choice([2, 8])
def dave_from_accounting(turn):
    return 5
def speedster(turn):
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
        sum += which_class(1)
    return sum / 100000

def test_one_hundred_thousand_times_turns(which_class):
    sum = 0
    for i in range(100000):
        sum += num_turns(which_class)
    return sum / 100000

def num_turns(which_class):
    turn = 1 
    total = 0
    while total < 20:
        total += which_class(turn)
        if total >= 20:
            return turn
        turn += 1


def main(): 
    # print("rogue: ", test_one_hundred_thousand_times(rogue))
    # print("warrior: ", test_one_hundred_thousand_times(warrior))
    # print("strategist: ", test_one_hundred_thousand_times(strategist))
    # print("bard: ", test_one_hundred_thousand_times(bard))
    # print("gambler_dmg_given: ", test_one_hundred_thousand_times(gambler_dmg_given))
    # print("gambler_dmg_received: ", test_one_hundred_thousand_times(gambler_dmg_received))
    # print("forcer: ", test_one_hundred_thousand_times_turns(forcer))
    # print("paladin: ", test_one_hundred_thousand_times_turns(paladin))
    print("parasite: ", test_one_hundred_thousand_times(parasite))
    # print("sharpshooter: ", test_one_hundred_thousand_times(sharpshooter))
    # print("dave_from_accounting: ", test_one_hundred_thousand_times(dave_from_accounting))
    # print("musketeer: ", test_one_hundred_thousand_times_turns(musketeer))
    # print("turns it took: ", num_turns(musketeer))
    # print("turns it took: ", num_turns(musketeer))
    # print("turns it took: ", num_turns(musketeer))
    # print("turns it took: ", num_turns(musketeer))



    return


# print("total is: ", speedster())
main()