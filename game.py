import random
import statistics

class Archetype:
    def __init__(self):
        self.default_life = 20
        self.life = self.default_life
        self.name = "Archetype"
    def show_life(self):
        print(f"{self.name}'s life is {self.life}")
    def take_dmg(self, dmg):
        self.life -= dmg
    def reset_life(self):
        self.life = self.default_life
    def show_name(self):
        print(self.name)

class Rogue(Archetype):
    def __init__(self, name="Rogue"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn=None):
        return random.randint(1, 4) + random.randint(1, 4)
    
class Warrior(Archetype):
    def __init__(self, name="Warrior"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn=None):
        return random.randint(1, 8) + 1

class Strategist(Archetype):
    def __init__(self, name="Strategist"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn=None):
            return max(random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))
    
class Musketeer(Archetype):
    def __init__(self, name="Musketeer"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn):
        if turn % 2 == 0:
            return random.randint(1, 20)
        if turn % 2 == 1:
            return 0
        
class Bard(Archetype):
    def __init__(self, name="Bard"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn=None):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        return max(0, abs(a-b) - 2)
    
class Gambler(Archetype):
    def __init__(self, name="Gambler"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn=None):
        dmg_given = 0
        dmg_received = 0
        roll = random.randint(1, 20)
        print(roll)
        if roll % 2 == 0:
            dmg_given += roll
        else: 
            dmg_received += roll
        roll = random.randint(1, 20)
        print(roll)
        if roll % 2 == 0:
            dmg_given += roll
        else: 
            dmg_received += roll
        self.take_dmg(dmg_received)
        return dmg_given
    
class Forcer(Archetype):
    def __init__(self, name="Forcer"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn):
        sum = 0
        for i in range(turn+2):
            if random.randint(1, 20) == 20:
                sum = 50
        return sum
    
class Paladin(Archetype):
    def __init__(self, name="Paladin"):
        super().__init__()
        self.name = name
        self.default_life = 30
    def calc_dmg(self, turn=None):
        return random.randint(1, 6) 

class Parasite(Archetype):
    def __init__(self, name="Parasite"):
        super().__init__()
        self.name = name
    def heal(self, amt):
        self.life += amt
    def calc_dmg(self, turn=None):
        dmg_gain = random.randint(1, 4)
        self.heal(dmg_gain)
        return dmg_gain

class Sharpshooter(Archetype):
    def __init__(self, name="Sharpshooter"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn=None):
        return random.choice([2, 8])

class Dave_from_HR(Archetype):
    def __init__(self, name="Dave_from_HR"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn=None):
        return 5

class Weapons_Dealer(Archetype):
    def __init__(self, name="Weapons_Dealer"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn=None):
        arr = []
        arr.append(random.randint(1, 2))
        arr.append(random.randint(1, 4))
        arr.append(random.randint(1, 6))
        arr.append(random.randint(1, 8))
        arr.append(random.randint(1, 10))
        arr.append(random.randint(1, 12))
        arr.append(random.randint(1, 20))
        return statistics.median(arr)

class Broker(Archetype):
    def __init__(self, name="Broker"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn):
        return random.randint(1, 6) + turn

class Speedster(Archetype):
    def __init__(self, name="Speedster"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn=None):
        sum = 0
        roll = random.choice([1, 4])
        sum += roll
        if roll == 4:
            while roll == 4:
                roll = random.choice([1, 4])
                sum += roll 
        return sum

class Wild_Mage(Archetype):
    def __init__(self, name="Wild_Mage"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn=None):
        roll = random.randint(1, 20)
        if roll == 1:
            self.take_dmg(random.randint(1, 4))
            return 0 
        elif 2 <= roll <= 7:
            return random.randint(1, 4)
        elif 8 <= roll <= 14:
            return random.randint(1, 4) + random.randint(1, 4)
        elif 15 <= roll <= 19:
            return random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4)
        else:
            return 50
        
    
def run_game(archetype_a, archetype_b, verbose=True):
    archetype_b.life += 5
    turn = 1
    while archetype_a.life > 0 and archetype_b.life > 0:
        if verbose:
            print(f"turn {turn}:")
        a_dmg = archetype_a.calc_dmg(turn)
        if verbose:
            print(f"{archetype_a.name} deals {a_dmg} to {archetype_b.name}.")
        archetype_b.take_dmg(a_dmg)
        if archetype_b.life <= 0:
            break
        if verbose:
            print(f"{archetype_b.name}'s life is now {archetype_b.life}")
        b_dmg = archetype_b.calc_dmg(turn)
        if verbose:
            print(f"{archetype_b.name} deals {b_dmg} to {archetype_a.name}")
        archetype_a.take_dmg(b_dmg)
        if verbose:
            print(f"{archetype_a.name}'s life is now {archetype_a.life}")
        turn += 1
    if archetype_a.life <= 0 and archetype_b.life > 0:
        if verbose:
            print(f"{archetype_b.name} wins!")
        archetype_a.reset_life()
        archetype_b.reset_life()
        return 1
    elif archetype_b.life <= 0 and archetype_a.life > 0:
        if verbose:
            print(f"{archetype_a.name} wins!") 
        archetype_a.reset_life()
        archetype_b.reset_life()
        return 0
    else:
        if verbose:
            print(f"{archetype_a.name} wins!")
        archetype_a.reset_life()
        archetype_b.reset_life()
        return 0

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

def test_one_hundred_thousand_games(a_a, a_b):
    first_half_wins_a = 0
    first_half_wins_b = 0
    for i in range(50000):
        if run_game(a_a, a_b, verbose=False) == 0:
            first_half_wins_a += 1
        else:
            first_half_wins_b += 1
    print(f"{a_a.name} won {first_half_wins_a} games, {round((first_half_wins_a/50000)*100, 2)}% of all it's games going first.")
    print(f"{a_b.name} won {first_half_wins_b} games, {round((first_half_wins_b/50000)*100, 2)}% of all it's games going second.")
    second_half_wins_a = 0
    second_half_wins_b = 0
    for i in range (50000):
        if run_game(a_b, a_a, verbose=False) == 0:
            second_half_wins_b += 1
        else:
            second_half_wins_a += 1
    print(f"{a_a.name} won {second_half_wins_a} games, {round((second_half_wins_a/50000)*100, 2)}% of all it's games going second.")
    print(f"{a_b.name} won {second_half_wins_b} games, {round((second_half_wins_b/50000)*100, 2)}% of all it's games going first.")

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
    s = Strategist()
    w = Warrior()
    # print(run_game(s, w, verbose=True))
    test_one_hundred_thousand_games(s, w)


    return

main()