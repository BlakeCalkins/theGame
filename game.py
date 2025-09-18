import random
import statistics

class Archetype:
    def __init__(self):
        self.life = 20
    def show_life(self):
        print(f"life is {self.life}")
    def take_dmg(self, dmg):
        self.life -= dmg

class Rogue(Archetype):
    def __init__(self):
        super().__init__()
    def calc_dmg(self, turn=None):
        return random.randint(1, 4) + random.randint(1, 4)
    
class Warrior(Archetype):
    def __init__(self):
        super().__init__()
    def calc_dmg(self, turn=None):
        return random.randint(1, 8) + 1



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
def dave_from_human_resources(turn):
    return 5
def weapons_dealer(turn):
    arr = []
    arr.append(random.randint(1, 2))
    arr.append(random.randint(1, 4))
    arr.append(random.randint(1, 6))
    arr.append(random.randint(1, 8))
    arr.append(random.randint(1, 10))
    arr.append(random.randint(1, 12))
    arr.append(random.randint(1, 20))
    return statistics.median(arr)
def broker(turn):
    return random.randint(1, 6) + turn
def speedster(turn):
    sum = 0
    roll = random.choice([1, 4])
    sum += roll
    if roll == 4:
        while roll == 4:
            roll = random.choice([1, 4])
            sum += roll 
    return sum
def wild_mage(turn):
    roll = random.randint(1, 20)
    if roll == 1:
        return 0 
    elif 2 <= roll <= 7:
        return random.randint(1, 4)
    elif 8 <= roll <= 14:
        return random.randint(1, 4) + random.randint(1, 4)
    elif 15 <= roll <= 19:
        return random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4)
    # elif 16 <= roll <= 19:
    #     return random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4)
    else:
        return 50
    
def run_game(class_a, class_b):
    a_life = 20
    b_life = 25
    if class_a  == paladin:
        a_life = 30
    if class_b == paladin:
        b_life = 35
    turn = 1
    while a_life > 0 and b_life > 0:
        print(f"turn {turn}:")
        a_dmg = class_a(turn)
        print(f"{class_a.__name__} deals {a_dmg} to {class_b.__name__}.")
        b_life -= a_dmg
        if b_life <= 0:
            break
        print(f"{class_b.__name__}'s life is now {b_life}")
        b_dmg = class_b(turn)
        print(f"{class_b.__name__} deals {b_dmg} to {class_a.__name__}")
        a_life -= b_dmg
        print(f"{class_a.__name__}'s life is now {a_life}")
        turn += 1
    if a_life <= 0 and b_life > 0:
        print(f"{class_b.__name__} wins!")
    elif b_life <= 0 and a_life > 0:
        print(f"{class_a.__name__} wins!")
    else:
        print(f"{class_a.__name__} wins!")

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
    # print("forcer turns: ", test_one_hundred_thousand_times_turns(forcer))
    # print("paladin turns: ", test_one_hundred_thousand_times_turns(paladin))
    # print("parasite: ", test_one_hundred_thousand_times(parasite))
    # print("sharpshooter: ", test_one_hundred_thousand_times(sharpshooter))
    # print("dave_from_human_resources: ", test_one_hundred_thousand_times(dave_from_human_resources))
    # print("weapons_dealer: ", test_one_hundred_thousand_times(weapons_dealer))
    # print("broker turns: ", test_one_hundred_thousand_times_turns(broker))
    # print("musketeer turns: ", test_one_hundred_thousand_times_turns(musketeer))
    # print("wild_mage: ", test_one_hundred_thousand_times(wild_mage))

    # run_game(warrior, rogue)
    r = Rogue()
    print(r.calc_dmg())
    r.show_life()
    r.take_dmg(1)
    r.show_life()


    return

main()