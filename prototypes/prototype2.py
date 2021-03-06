from random import randint

count = 0
coins = [0, 0, 0, 0]
goodPrompts = [0,0,     0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,0,0]
gem = [
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0]
gemName = ['Banded agate', 'Eye agate', 'Moss agate', 'Azurite', 'Blue quartz', 'Hematite', 'Lapis lazuli', 'Malachite', 'Obsidian', 'Rhodochrosite', 'Tiger eye turquoise',
'Freshwater (irregular) pearl', 'Bloodstone', 'Carnelian', 'Chalcedony', 'Chrysoprase', 'Citrine', 'Iolite', 'Jasper', 'Moonstone', 'Onyx', 'Peridot', 'Rock crystal', 'Sard',
'Sardonyx', 'Rose quartz', 'Smoky rose quartz', 'Star rose quartz', 'Zircon', 'Amber', 'Amethyst', 'Chrysoberyl', 'Coral', 'Red garnet', 'Brown-green garnet', 'Jade', 'Jet',
'White pearl', 'Golden pearl', 'Pink pearl', 'Silver pearl', 'Red Spinel', 'Red-brown spinel', 'Deep green spinel', 'Tourmaline', 'Alexandrite', 'aquamarine', 'Violet garnet',
'Black pearl', 'Deep blue spinel', 'Golden yellow topaz', 'Emerald', 'White opal', 'Black opal', 'Fire opal', 'Blue sapphire', 'Fiery yellow corundum', 'Rich purple corundum',
'Blue star sapphire', 'Black star sapphire', 'Star ruby', 'Clearest bright green emerald', 'Blue-white diamond', 'Canary diamond', 'Pink diamond', 'Brown diamond', 'Blue diamond', 'Jacinth']
#Tier 1 gems     0-11   12
#Tier 2 gems     12-28  17
#Tier 3 gems     29-44  16
#Tier 4 gems     45-50  6
#Tier 5 gems     51-59  9
#Tier 6 gems     60-67  8
art = [
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
artName = ['Silver ewer', 'Carved bone statuette', 'Ivory statuette', 'Finely wrought small gold bracelet',
 'Cloth of gold vestments', 'Black velvet mask with numerous citrines', 'Silver chalice with lapis lazuli gems',
 'Large well-done wool tapestry', 'Brass mug with jade inlays', 'Silver comb with moonstones',
 'Silver-plated steel longsword with jet jewel in hilt', 'Carved harp of exotic wood with ivory inlay and zircon gems',
 'Solid gold idol', 'Gold dragon comb with red garnet eye', 'Gold and topaz bottle stopper cork',
 'Ceremonial electrum dagger with a star ruby in the pommel', 'Eyepatch with mock eye of sapphire and moonstone',
 'Fire opal pendant on a fine gold chain', 'Old masterpiece painting', 'Embroidered silk and velvet mantle with numerous moonstones',
 'Sapphire pendant on gold chain', 'Embroidered and bejeweled glove', 'Jeweled anklet', 'Gold music box',
 'Golden circlet with four aquamarines', 'A string of small pink pearls', 'Jeweled gold crown', 'Jeweled electrum ring',
 'Gold and ruby ring', 'Gold cup set with emeralds']
#Tier 1 goods   0-3     4
#Tier 2 goods   4-6     3
#Tier 3 goods   7-8     2
#Tier 4 goods   9-10    2
#Tier 5 goods   11-12   2
#Tier 6 goods   13-15   3
#Tier 7 goods   16-19   4
#Tier 8 goods   20-21   2
#Tier 9 goods   22-24   3
#Tier 10 goods  25-26   2
#Tier 11 goods  27-28   2
#Tier 12 goods  29-30   2

#===Function definitions===

def rollMultipleDice(rmdCount, rmdMax):
    sum = 0
    while rmdCount > 0:
        sum += randint(1,rmdMax)
        rmdCount -= 1
    return sum

#===Program begins here===
while True:
    try:
        count = int(input("What is the number of encounters?"))
    except:
        print("This is not a valid input.")
        continue
    else:
        if count < 0:
            continue
        break

while count > 0:
    loot = randint(1,100)
    if loot >= 96:
        coins[3] += 1
    elif loot >= 53:
        coins[2] += 1
    elif loot >= 30:
        coins[1] += 1
    elif loot >= 15:
        coins[0] += 1

    loot = randint(1,100)
    if loot >= 96:
        goodPrompts[1] += 1
    elif loot >= 91:
        goodPrompts[0] += 1

    count -= 1

#level 1 coin rolls
coins[0] = rollMultipleDice(coins[0], 6) * 1000
coins[1] = rollMultipleDice(2*coins[1], 8) * 100
coins[2] = rollMultipleDice(coins[2], 8) * 10
coins[3] = rollMultipleDice(coins[3], 4) * 10

#==Gem tier rolls
while goodPrompts[0] > 0:
    loot = randint(1,100)
    if loot == 100:
        goodPrompts[7] += 1
    elif loot >= 91:
        goodPrompts[6] += 1
    elif loot >= 71:
        goodPrompts[5] += 1
    elif loot >= 51:
        goodPrompts[4] += 1
    elif loot >= 26:
        goodPrompts[3] += 1
    else:
        goodPrompts[2] += 1
    goodPrompts[0] -= 1

#=Gem individual rolls
while goodPrompts[2] > 0:
    gem[randint(0,11)] += rollMultipleDice(4,4)
    goodPrompts[2] -= 1
while goodPrompts[3] > 0:
    gem[randint(12,28)] += rollMultipleDice(2,4)*10
    goodPrompts[3] -= 1
while goodPrompts[4] > 0:
    gem[randint(29,44)] += rollMultipleDice(4,4)*10
    goodPrompts[4] -= 1
while goodPrompts[5] > 0:
    gem[randint(45,50)] += rollMultipleDice(2,4)*100
    goodPrompts[5] -= 1
while goodPrompts[6] > 0:
    gem[randint(51,59)] += rollMultipleDice(4,4)*100
    goodPrompts[6] -= 1
while goodPrompts[7] > 0:
    gem[randint(60,67)] += rollMultipleDice(2,4)*1000
    goodPrompts[7] -= 1

#=Art tier rolls
while goodPrompts[1] > 0:
    loot = randint(1,100)
    if loot == 100:
        goodPrompts[19] += 1
    elif loot >= 96:
        goodPrompts[18] += 1
    elif loot >= 91:
        goodPrompts[17] += 1
    elif loot >= 86:
        goodPrompts[16] += 1
    elif loot >= 81:
        goodPrompts[15] += 1
    elif loot >= 71:
        goodPrompts[14] += 1
    elif loot >= 61:
        goodPrompts[13] += 1
    elif loot >= 51:
        goodPrompts[12] += 1
    elif loot >= 41:
        goodPrompts[11] += 1
    elif loot >= 26:
        goodPrompts[10] += 1
    elif loot >= 11:
        goodPrompts[9] += 1
    else:
        goodPrompts[8] += 1
    goodPrompts[1] -= 1

#=Art rolls
while goodPrompts[8] > 0:
    art[randint(0,3)] += randint(1,10)*10
    goodPrompts[8] -= 1
while goodPrompts[9] > 0:
    art[randint(4,6)] += rollMultipleDice(3,6)*10
    goodPrompts[9] -= 1
while goodPrompts[10] > 0:
    art[randint(7,8)] += randint(1,6)*100
    goodPrompts[10] -= 1
while goodPrompts[11] > 0:
    art[randint(9,10)] += randint(1,10)*100
    goodPrompts[11] -= 1
while goodPrompts[12] > 0:
    art[randint(11,12)] += rollMultipleDice(2,6)*100
    goodPrompts[12] -= 1
while goodPrompts[13] > 0:
    art[randint(13,15)] += rollMultipleDice(3,6)*100
    goodPrompts[13] -= 1
while goodPrompts[14] > 0:
    art[randint(16,19)] += rollMultipleDice(4,6)*100
    goodPrompts[14] -= 1
while goodPrompts[15] > 0:
    art[randint(20,21)] += rollMultipleDice(5,6)*100
    goodPrompts[15] -= 1
while goodPrompts[16] > 0:
    art[randint(22,24)] += randint(1,4)*1000
    goodPrompts[16] -= 1
while goodPrompts[17] > 0:
    art[randint(25,26)] += randint(1,6)*1000
    goodPrompts[17] -= 1
while goodPrompts[18] > 0:
    art[randint(27,28)] += rollMultipleDice(2,4)*1000
    goodPrompts[18] -= 1
while goodPrompts[19] > 0:
    art[randint(29,30)] += rollMultipleDice(2,6)*1000
    goodPrompts[19] -= 1

#Print results:
#Coins
if coins[0] > 0:
    print("You got",coins[0],"copper coins.")
if coins[1] > 0:
    print("You got",coins[1],"silver coins.")
if coins[2] > 0:
    print("You got",coins[2],"gold coins.")
if coins[3] > 0:
    print("You got",coins[3],"platinum coins.")

print("\n")

#Gems
count = 0
while count < 68:
    if gem[count] != 0:
        print(gem[count],"golds worth of",gemName[count])
    count += 1

print("\n")

#Art
count = 0
while count < 30:
    if art[count] != 0:
        print(art[count],"golds worth of",artName[count])
    count += 1

print("\n")
#Total all rewards
goldSum = 0

goldSum += coins[0]/100
goldSum += coins[1]/10
goldSum += coins[2]
goldSum += coins[3]*10

goldSum += (sum(gem)+sum(art))
print("For a total equivalent to",goldSum,"in gold")




#===ARCHIVE===#
#while(count <= 67):
#    print(count+1, ". ", gemName[count], "\n")
#    count += 1
#
#count = 0
#while(count <= 30):
#    print(count+1, ". ", artName[count], "\n")
#    count += 1
