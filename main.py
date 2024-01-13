import random

class Character:
    def __init__(self, name, lmoves, mmoves, hmoves, health, stamina, dodge):
        self.name=name
        self.lmoves=lmoves
        self.mmoves=mmoves
        self.hmoves=hmoves
        self.health=health
        self.stamina=stamina
        self.dodge=dodge

#for random numbas rolf
def rand_list(a_list):
    a=max(a_list)
    b=min(a_list)
    c=random.randint(b,a)
    return c

#attack functions
def l_attack(p1, p2):
    p2.health-=rand_list(p1.lmoves)
    return p2.health
def m_attack(p1, p2):
    p2.health-=rand_list(p1.mmoves)
    return p2.health
def h_attack(p1, p2):
    p2.health-=rand_list(p1.hmoves)
    return p2.health

#move sequences
def l_s(p1,p2):
    p1.stamina-=5
    if p2.health<=0:
        print(f"{p2.name} was defeated by {p1.name}'s light attack!\n{p1.name} was victorious!")
    else:
        print(f"{p1.name} has chosen their light attack! {p2.name} has {p2.health} health! {p1.name} has {p1.stamina} stamina remaining!")
def m_s(p1,p2):
    p1.stamina-=7
    if p2.health<=0:
        print(f"{p2.name} was defeated by {p1.name}'s medium attack!\n{p1.name} was victorious!")
    else:
        print(f"{p1.name} has chosen their medium attack! {p2.name} has {p2.health} health! {p1.name} has {p1.stamina} stamina remaining!")
def h_s(p1,p2):
    p1.stamina-=10
    if p2.health<=0:
        print(f"{p2.name} was defeated by {p1.name}'s heavy attack!\n{p1.name} was victorious!")
    else:
        print(f"{p1.name} has chosen their heavy attack! {p2.name} has {p2.health} health! {p1.name} has {p1.stamina} stamina remaining!")

#dodge and stam regen
def dodge(p1, a_list):
    a=rand_list(a_list)
    if a <= p1.dodge:
        return True
    
def stam_reg(p1,a):
    p1.stamina=a

dd=[1,100]    

slmoves=[10,15]
smmoves=[22,15]
shmoves=[22,30]

hlm=[5,10]
hmm=[10,15]
hhm=[15,20]

dlm=[10,13]
dmm=[13,18]
dhm=[18,24]

blm=[8,12]
bmm=[12,16]
bhm=[16,20]

wlm=[15,20]
wmm=[20,25]
whm=[25,30]

clm=[50,100]
cmm=[100,175]
chm=[175,1000]

characters=[
    Character("salman", slmoves, smmoves, shmoves, 100, 30, 20),
    Character("huzaifa", hlm, hmm, hhm, 50, 50, 60),
    Character("woody", dlm, dmm, dhm, 65, 40, 40),
    Character("brudda", blm, bmm, bhm, 75, 50, 30),
    Character("Wick", wlm, wmm, whm, 200, 100, 50),
    Character("Mr.Cheating", clm, cmm, chm, 1000, 666, 100)
]

print("""
Welcome to Nexus Warfare!
      Presented by:
      Salman Saif
      Huzaifa Shafiq(gay man incredibile lover)
      """)
l=input("""Main Menu:
Character Select(a)\nLore(b)\n""")

b=""
while b!="yes":
    p1=input("Please select a character:\nsalman(a)\nhuzaifa(b)\nwoody(c)\nbrudda(d)\nWick(w)\nMr.Cheating(downfall)\n")
    
    if p1=="a":
        p1=characters[0]
    elif p1=="b":
        p1=characters[1]
    elif p1=="c":
        p1=characters[2]
    elif p1=="d":
        p1=characters[3]
    elif p1=="w":
        p1=characters[4]  
    elif p1=="downfall":
        p1=characters[5]

    p2=input("Player 2, please select your character:\nsalman(a)\nhuzaifa(b)\nwoody(c)\nbrudda(d)\nWick(w)\nMr.Cheating(downfall)\n")
    
    if p2=="a":
        p2=characters[0]
    elif p2=="b":
        p2=characters[1]
    elif p2=="c":
        p2=characters[2]
    elif p2=="d":
        p2=characters[3]  
    elif p2=="w":
        p2=characters[4]
    elif p2=="downfall":
        p2=characters[5]
    
    print("These are your chosen characters' stats:")
    print(f"Player 1:\n{p1.name}\nLight Attack damage: {p1.lmoves}\nMedium Attack Damage: {p1.mmoves}\nHeavy Attack damage: {p1.hmoves}\nHealth: {p1.health}\nStamina: {p1.stamina}\nDodge Chance: {p1.dodge}%")
    print(f"Player 2:\n{p2.name}\nLight Attack damage: {p2.lmoves}\nMedium Attack Damage: {p2.mmoves}\nHeavy Attack damage: {p2.hmoves}\nHealth: {p2.health}\nStamina: {p2.stamina}\nDodge Chance: {p2.dodge}%")
    b=input("Are you satisfied with your character choices?\nyes\nno\n")

stam1=p1.stamina
stam2=p2.stamina

while p1.health>0 or p2.health>0:
    c1=input(f"{p1.name}, choose your move:\nLight Attack(a)\nMedium Attack(b)\nHeavy Attack(c)\nRegenerate Stamina(d)\n")
    if p2.stamina<=0:
        print(f"{p2.name} is out of stamina!")
        p2.stamina=stam2
    else:
        a=dodge(p2,dd)
        if  a is True:
            print(f"{p2.name} dodged the attack!")
        else:
    #attack sequence p1
            if c1=="a":
                l_attack(p1,p2)
                l_s(p1,p2)
                if p2.health<=0:
                    break

            elif c1=="b":
                m_attack(p1,p2)
                m_s(p1,p2)
                if p2.health<=0:
                    break
            elif c1=="c":
                h_attack(p1,p2)
                h_s(p1,p2)
                if p2.health<=0:
                    break
    if c1=="d":
        stam_reg(p1,stam1)
        print(f"{p1.name} has regenerated their stamina! They now have {p1.stamina} stamina left")

    c2=input(f"{p2.name}, choose your move:\nLight Attack(a)\nMedium Attack(b)\nHeavy Attack(c)\nRegenerate Stamina(d)\n")
    if p2.stamina<=0:
        print(f"{p2.name} is out of stamina!")
        p2.stamina=stam2
    else:
        b=dodge(p1,dd)
        if  b is True:
            print(f"{p1.name} dodged the attack!")
        else:
    #attack sequence p2
            if c2=="a":
                l_attack(p2,p1)
                l_s(p2,p1)
                if p1.health<=0:
                    break
            elif c2=="b":
                m_attack(p2,p1)
                m_s(p2,p1)
                if p1.health<=0:
                    break
            elif c2=="c":
                h_attack(p2,p1)
                h_s(p2,p1)
                if p1.health<=0:
                    break
    if c2=="d":
        stam_reg(p2,stam2)
        print(f"{p2.name} has regenerated their stamina! They now have {p2.stamina} stamina left")
















