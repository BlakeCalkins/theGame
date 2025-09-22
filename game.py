import random
import sys

def d2():
    return random.randint(1, 2)
def d4():
    return random.randint(1, 4)
def d6():
    return random.randint(1, 6)
def d8():
    return random.randint(1, 8)
def d10():
    return random.randint(1, 10)
def d12():
    return random.randint(1, 12)
def d20():
    return random.randint(1, 20)

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
        return d4() + d4()
    
class Warrior(Archetype):
    def __init__(self, name="Warrior"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn=None):
        return d8() + 1

class Strategist(Archetype):
    def __init__(self, name="Strategist"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn=None):
            return max(d6(), d6(), d6())
    
class Musketeer(Archetype):
    def __init__(self, name="Musketeer"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn):
        if turn % 2 == 0:
            return d20()
        if turn % 2 == 1:
            return 0
        
class Bard(Archetype):
    def __init__(self, name="Bard"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn=None):
        a = d20()
        b = d20()
        return max(0, abs(a-b) - 2)
    
class Gambler(Archetype):
    def __init__(self, name="Gambler"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn=None):
        dmg_given = 0
        dmg_received = 0
        roll = d20()
        if roll % 2 == 0:
            dmg_given += roll
        else: 
            dmg_received += roll
        roll = d20()
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
        for i in range(turn+1):
            if d20() == 20:
                sum = 50
        return sum
    
class Paladin(Archetype):
    def __init__(self, name="Paladin"):
        super().__init__()
        self.name = name
        self.default_life = 30
    def calc_dmg(self, turn=None):
        return d6()

class Parasite(Archetype):
    def __init__(self, name="Parasite"):
        super().__init__()
        self.name = name
    def heal(self, amt):
        self.life += amt
    def calc_dmg(self, turn=None):
        dmg_gain = d4()
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
        arr.append(d2())
        arr.append(d4())
        arr.append(d6())
        arr.append(d8())
        arr.append(d10())
        arr.append(d12())
        arr.append(d20())
        s_arr = sorted(arr)
        first_five = s_arr[:5]
        last_two = s_arr[-2:]
        return max(0, (sum(last_two) - sum(first_five)))

class Broker(Archetype):
    def __init__(self, name="Broker"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn):
        return d4() + turn

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
        roll = d20()
        if roll == 1:
            self.take_dmg(d4())
            return 0 
        elif 2 <= roll <= 7:
            return d4()
        elif 8 <= roll <= 14:
            return d4() + d4()
        elif 15 <= roll <= 19:
            return d4() + d4() + d4()
        else:
            return 50
        
    
def run_game(archetype_a, archetype_b, verbose=True):
    archetype_b.life += 2
    turn = 1
    if verbose:
        print(f"{archetype_a.name}'s life is {archetype_a.life}")
        print(f"{archetype_b.name}'s life is {archetype_b.life}")
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
        sum += which_class.calc_dmg()
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
        total += which_class.calc_dmg(turn)
        if total >= 20:
            return turn
        turn += 1

def test_one_hundred_thousand_games(a_a, a_b, output=sys.stdout):
    first_half_wins_a = 0
    first_half_wins_b = 0
    for i in range(50000):
        if run_game(a_a, a_b, verbose=False) == 0:
            first_half_wins_a += 1
        else:
            first_half_wins_b += 1
    print(f"{a_a.name} first", file=output)
    print(f"{first_half_wins_a}", file=output)
    print(f"{a_b.name} second", file=output)
    print(f"{first_half_wins_b}", file=output)
    second_half_wins_a = 0
    second_half_wins_b = 0
    for i in range (50000):
        if run_game(a_b, a_a, verbose=False) == 0:
            second_half_wins_b += 1
        else:
            second_half_wins_a += 1
    print(f"{a_a.name} second", file=output)
    print(f"{second_half_wins_a}", file=output)
    print(f"{a_b.name} first", file=output)
    print(f"{second_half_wins_b}", file=output)

def main(): 
    # print("rogue: ", test_one_hundred_thousand_times(rogue))
    # print("warrior: ", test_one_hundred_thousand_times(warrior))
    # print("strategist: ", test_one_hundred_thousand_times(strategist))
    # print("musketeer turns: ", test_one_hundred_thousand_times_turns(musketeer))
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
    #speedster
    #print("wild_mage: ", test_one_hundred_thousand_times(wild_mage))


    rog = Rogue()
    war = Warrior()
    stg = Strategist()
    msk = Musketeer()
    brd = Bard()
    gmb = Gambler()
    frc = Forcer()
    pal = Paladin()
    par = Parasite()
    shs = Sharpshooter()
    dav = Dave_from_HR()
    wed = Weapons_Dealer()
    bro = Broker()
    spd = Speedster()
    wim = Wild_Mage()
    archetypes = [rog, war, stg, msk, brd, gmb, frc, pal, par, shs, dav, wed, bro, spd, wim]
    matchups = 0
    with open("patch_3", "w") as f:
        for i, type1 in enumerate(archetypes):
            for type2 in archetypes[i+1:]:
                print(f"Testing {type1.name} vs {type2.name}", file=f)
                test_one_hundred_thousand_games(type1, type2, output=f)
                print(file=f)
                matchups+=1
                print(matchups)


    # print(run_game(b, b2, verbose=True))
    # test_one_hundred_thousand_games(b, b2)


    return

def mirrors():
    rog1 = Rogue("Rogue A")
    rog2 = Rogue("Rogue B")
    war1 = Warrior("Warrior A")
    war2 = Warrior("Warrior B")
    stg1 = Strategist("Strategist A")
    stg2 = Strategist("Strategist B")
    msk1 = Musketeer("Musketeer A")
    msk2 = Musketeer("Musketeer B")
    brd1 = Bard("Bard A")
    brd2 = Bard("Bard B")
    gmb1 = Gambler("Gambler A")
    gmb2 = Gambler("Gambler B")
    frc1 = Forcer("Forcer A")
    frc2 = Forcer("Forcer B")
    pal1 = Paladin("Paladin A")
    pal2 = Paladin("Paladin B")
    par1 = Parasite("Parasite A")
    par2 = Parasite("Parasite B")
    shs1 = Sharpshooter("Sharpshooter A")
    shs2 = Sharpshooter("Sharpshooter B")
    dav1 = Dave_from_HR("Dave Kinkade")
    dav2 = Dave_from_HR("Dave Calkins")
    wed1 = Weapons_Dealer("Weapons_Dealer A")
    wed2 = Weapons_Dealer("Weapons_Dealer B")
    bro1 = Broker("Broker A")
    bro2 = Broker("Broker B")
    spd1 = Speedster("Speedster A")
    spd2 = Speedster("Speedster B")
    wim1 = Wild_Mage("Wild_Mage A")
    wim2 = Wild_Mage("Wild_Mage B")

    with open("patch_3", "a") as f:
        print(f"Testing {rog1.name} vs {rog2.name}", file=f)
        print(f"Testing {rog1.name} vs {rog2.name}")
        test_one_hundred_thousand_games(rog1, rog2, output=f)
        print(file=f)

        print(f"Testing {war1.name} vs {war2.name}", file=f)
        print(f"Testing {war1.name} vs {war2.name}")
        test_one_hundred_thousand_games(war1, war2, output=f)
        print(file=f)

        print(f"Testing {stg1.name} vs {stg2.name}", file=f)
        print(f"Testing {stg1.name} vs {stg2.name}")
        test_one_hundred_thousand_games(stg1, stg2, output=f)
        print(file=f)

        print(f"Testing {msk1.name} vs {msk2.name}", file=f)
        print(f"Testing {msk1.name} vs {msk2.name}")
        test_one_hundred_thousand_games(msk1, msk2, output=f)
        print(file=f)

        print(f"Testing {brd1.name} vs {brd2.name}", file=f)
        print(f"Testing {brd1.name} vs {brd2.name}")
        test_one_hundred_thousand_games(brd1, brd2, output=f)
        print(file=f)

        print(f"Testing {gmb1.name} vs {gmb2.name}", file=f)
        print(f"Testing {gmb1.name} vs {gmb2.name}")
        test_one_hundred_thousand_games(gmb1, gmb2, output=f)
        print(file=f)

        print(f"Testing {frc1.name} vs {frc2.name}", file=f)
        print(f"Testing {frc1.name} vs {frc2.name}")
        test_one_hundred_thousand_games(frc1, frc2, output=f)
        print(file=f)

        print(f"Testing {pal1.name} vs {pal2.name}", file=f)
        print(f"Testing {pal1.name} vs {pal2.name}")
        test_one_hundred_thousand_games(pal1, pal2, output=f)
        print(file=f)

        print(f"Testing {par1.name} vs {par2.name}", file=f)
        print(f"Testing {par1.name} vs {par2.name}")
        test_one_hundred_thousand_games(par1, par2, output=f)
        print(file=f)

        print(f"Testing {shs1.name} vs {shs2.name}", file=f)
        print(f"Testing {shs1.name} vs {shs2.name}")
        test_one_hundred_thousand_games(shs1, shs2, output=f)
        print(file=f)

        print(f"Testing {dav1.name} vs {dav2.name}", file=f)
        print(f"Testing {dav1.name} vs {dav2.name}")
        test_one_hundred_thousand_games(dav1, dav2, output=f)
        print(file=f)

        print(f"Testing {wed1.name} vs {wed2.name}", file=f)
        print(f"Testing {wed1.name} vs {wed2.name}")
        test_one_hundred_thousand_games(wed1, wed2, output=f)
        print(file=f)

        print(f"Testing {bro1.name} vs {bro2.name}", file=f)
        print(f"Testing {bro1.name} vs {bro2.name}")
        test_one_hundred_thousand_games(bro1, bro2, output=f)
        print(file=f)

        print(f"Testing {spd1.name} vs {spd2.name}", file=f)
        print(f"Testing {spd1.name} vs {spd2.name}")
        test_one_hundred_thousand_games(spd1, spd2, output=f)
        print(file=f)

        print(f"Testing {wim1.name} vs {wim2.name}", file=f)
        print(f"Testing {wim1.name} vs {wim2.name}")
        test_one_hundred_thousand_games(wim1, wim2, output=f)
        print(file=f)





def fr():
    frc = Forcer()
    # print(we_de.calc_dmg())
    print(test_one_hundred_thousand_times_turns(frc))


main()
mirrors()
# fr()