import random
import numpy as np
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
        self.default_life = 18
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

    
class Forcer(Archetype):
    def __init__(self, name="Forcer"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn):
        sum = 0
        for i in range(turn+1):
            if d20() == 20:
                sum = 25
        return sum
    
class Paladin(Archetype):
    def __init__(self, name="Paladin"):
        super().__init__()
        self.name = name
        self.default_life = 30
    def calc_dmg(self, turn=None):
        return d6()

class Academic(Archetype):
    def __init__(self, name="Academic"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn):
        if turn == 1:
            return d6()
        if turn == 2:
            return d8()
        if turn == 3:
            return d10()
        if turn == 4:
            return d12()
        else:
            return d20()

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

class Irradiated(Archetype):
    def __init__(self, name="Irradiated"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn):
        if turn == 1:
            return d4() + d4() + d4() + d4() + d4()
        if turn == 2:
            return d4() + d4() + d4()
        if turn == 3:
            return d4() + d4()
        else:
            return d4()

class Werewolf(Archetype):
    def __init__(self, name="Werewolf"):
        super().__init__()
        self.name = name
        self.werewolf = False
    def calc_dmg(self, turn=None):
        if self.werewolf:
            return d12()
        else:
            if d4() == 4:
                self.werewolf = True
            return d8()

class Needler(Archetype):
    def __init__(self, name="Needler"):
        super().__init__()
        self.name = name
    def calc_dmg(self, turn=None):
        dmg = 0
        for _ in range(12):
            if d6() == 1 or d6() == 2:
                dmg += 1
        return dmg

        
    
def run_game(archetype_a, archetype_b, verbose=True):
    archetype_b.life += 2
    turn = 1
    damages = []
    if verbose:
        print(f"{archetype_a.name}'s life is {archetype_a.life}")
        print(f"{archetype_b.name}'s life is {archetype_b.life}")
    while archetype_a.life > 0 and archetype_b.life > 0:
        if verbose:
            print(f"turn {turn}:")
        a_dmg = archetype_a.calc_dmg(turn)
        damages.append(a_dmg)
        if verbose:
            print(f"{archetype_a.name} deals {a_dmg} to {archetype_b.name}.")
        archetype_b.take_dmg(a_dmg)
        if archetype_b.life <= 0:
            break
        if verbose:
            print(f"{archetype_b.name}'s life is now {archetype_b.life}")
        b_dmg = archetype_b.calc_dmg(turn)
        damages.append(b_dmg)
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
        return 1, np.mean(damages), turn
    elif archetype_b.life <= 0 and archetype_a.life > 0:
        if verbose:
            print(f"{archetype_a.name} wins!") 
        archetype_a.reset_life()
        archetype_b.reset_life()
        return 0, np.mean(damages), turn
    else:
        if verbose:
            print(f"{archetype_a.name} wins!")
        archetype_a.reset_life()
        archetype_b.reset_life()
        return 0, np.mean(damages), turn

def test_one_hundred_thousand_times(which_class):
    sum = 0
    for _ in range(100000):
        sum += which_class.calc_dmg()
    return sum / 100000

def test_one_hundred_thousand_times_turns(which_class):
    sum = 0
    for _ in range(100000):
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
    damages = []
    turns = []
    for _ in range(50000):
        win, dmg, trn = run_game(a_a, a_b, verbose=False)
        damages.append(dmg)
        turns.append(trn)
        if win == 0:
            first_half_wins_a += 1
        else:
            first_half_wins_b += 1
    print(f"{a_a.name} first", file=output)
    print(f"{first_half_wins_a}", file=output)
    print(f"{a_b.name} second", file=output)
    print(f"{first_half_wins_b}", file=output)
    second_half_wins_a = 0
    second_half_wins_b = 0
    for _ in range (50000):
        win, dmg, trn = run_game(a_b, a_a, verbose=False)
        damages.append(dmg)
        turns.append(trn)
        if win == 0:
            second_half_wins_b += 1
        else:
            second_half_wins_a += 1
    print(f"{a_a.name} second", file=output)
    print(f"{second_half_wins_a}", file=output)
    print(f"{a_b.name} first", file=output)
    print(f"{second_half_wins_b}", file=output)
    # print("Average Damage:", file=output)
    # print(np.mean(damages), file=output)
    # print("Average turns:", file=output)
    # print(np.mean(turns), file=output)

def archetype_averages():
    rog = Rogue()
    war = Warrior()
    stg = Strategist()
    msk = Musketeer()
    brd = Bard()
    frc = Forcer()
    pal = Paladin()
    acd = Academic()
    shs = Sharpshooter()
    dav = Dave_from_HR()
    spd = Speedster()
    wim = Wild_Mage()
    ndl = Needler()
    wer = Werewolf()
    rad = Irradiated()
    print("rogue: ", test_one_hundred_thousand_times(rog))
    print("warrior: ", test_one_hundred_thousand_times(war))
    print("strategist: ", test_one_hundred_thousand_times(stg))
    print("musketeer turns: ", test_one_hundred_thousand_times_turns(msk))
    print("bard: ", test_one_hundred_thousand_times(brd))
    # print("gambler_dmg_received: ", test_one_hundred_thousand_times(gambler_dmg_received))
    print("forcer turns: ", test_one_hundred_thousand_times_turns(frc))
    print("paladin turns: ", test_one_hundred_thousand_times_turns(pal))
    print("academic: ", test_one_hundred_thousand_times(acd))
    print("sharpshooter: ", test_one_hundred_thousand_times(shs))
    print("dave_from_human_resources: ", test_one_hundred_thousand_times(dav))
    print("Speedster: ", test_one_hundred_thousand_times(spd))
    print("wild_mage: ", test_one_hundred_thousand_times(wim))
    print("needler: ", test_one_hundred_thousand_times(ndl))
    print("werewolf: ", test_one_hundred_thousand_times(wer))
    print("irradiated: ", test_one_hundred_thousand_times(rad))

def main(): 
    rog = Rogue()
    war = Warrior()
    stg = Strategist()
    msk = Musketeer()
    brd = Bard()
    frc = Forcer()
    pal = Paladin()
    acd = Academic()
    shs = Sharpshooter()
    dav = Dave_from_HR()
    spd = Speedster()
    wim = Wild_Mage()
    ndl = Needler()
    wer = Werewolf()
    rad = Irradiated()
    archetypes = [rog, war, stg, msk, brd, frc, pal, acd, shs, dav, ndl, wer, rad, spd, wim]
    matchups = 0
    with open("patch_10", "w") as f:
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
    frc1 = Forcer("Forcer A")
    frc2 = Forcer("Forcer B")
    pal1 = Paladin("Paladin A")
    pal2 = Paladin("Paladin B")
    acd1 = Academic("Academic A")
    acd2 = Academic("Academic B")
    shs1 = Sharpshooter("Sharpshooter A")
    shs2 = Sharpshooter("Sharpshooter B")
    dav1 = Dave_from_HR("Dave Kinkade")
    dav2 = Dave_from_HR("Dave Calkins")
    spd1 = Speedster("Speedster A")
    spd2 = Speedster("Speedster B")
    wim1 = Wild_Mage("Wild_Mage A")
    wim2 = Wild_Mage("Wild_Mage B")
    rad1 = Irradiated("Irradiated A")
    rad2 = Irradiated("Irradiated B")
    ndl1 = Needler("Needler A")
    ndl2 = Needler("Needler B")
    wer1 = Werewolf("Werewolf A")
    wer2 = Werewolf("Werewolf B")

    with open("patch_10", "a") as f:
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

        print(f"Testing {frc1.name} vs {frc2.name}", file=f)
        print(f"Testing {frc1.name} vs {frc2.name}")
        test_one_hundred_thousand_games(frc1, frc2, output=f)
        print(file=f)

        print(f"Testing {pal1.name} vs {pal2.name}", file=f)
        print(f"Testing {pal1.name} vs {pal2.name}")
        test_one_hundred_thousand_games(pal1, pal2, output=f)
        print(file=f)

        print(f"Testing {acd1.name} vs {acd2.name}", file=f)
        print(f"Testing {acd1.name} vs {acd2.name}")
        test_one_hundred_thousand_games(acd1, acd2, output=f)
        print(file=f)

        print(f"Testing {shs1.name} vs {shs2.name}", file=f)
        print(f"Testing {shs1.name} vs {shs2.name}")
        test_one_hundred_thousand_games(shs1, shs2, output=f)
        print(file=f)

        print(f"Testing {dav1.name} vs {dav2.name}", file=f)
        print(f"Testing {dav1.name} vs {dav2.name}")
        test_one_hundred_thousand_games(dav1, dav2, output=f)
        print(file=f)

        print(f"Testing {spd1.name} vs {spd2.name}", file=f)
        print(f"Testing {spd1.name} vs {spd2.name}")
        test_one_hundred_thousand_games(spd1, spd2, output=f)
        print(file=f)

        print(f"Testing {wim1.name} vs {wim2.name}", file=f)
        print(f"Testing {wim1.name} vs {wim2.name}")
        test_one_hundred_thousand_games(wim1, wim2, output=f)
        print(file=f)

        print(f"Testing {rad1.name} vs {rad2.name}", file=f)
        print(f"Testing {rad1.name} vs {rad2.name}")
        test_one_hundred_thousand_games(rad1, rad2, output=f)
        print(file=f)

        print(f"Testing {ndl1.name} vs {ndl2.name}", file=f)
        print(f"Testing {ndl1.name} vs {ndl2.name}")
        test_one_hundred_thousand_games(ndl1, ndl2, output=f)
        print(file=f)

        print(f"Testing {wer1.name} vs {wer2.name}", file=f)
        print(f"Testing {wer1.name} vs {wer2.name}")
        test_one_hundred_thousand_games(wer1, wer2, output=f)
        print(file=f)





def fr():
    frc = Forcer()
    # print(we_de.calc_dmg())
    print(test_one_hundred_thousand_times_turns(frc))


main()
mirrors()
# archetype_averages()
# fr()