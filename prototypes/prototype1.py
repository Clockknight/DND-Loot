from random import randint

count, loot = 0, 0
coin = [0,0,0,0]

#works VVV
def rollMultipleDice(dieCount, dieNumber):
    sum = 0
    while dieCount > 0:
        sum += randint(1, int(dieNumber))
        dieCount -= 1
    return sum

#works VVV
while True:
    try:
        count = int(input("What is the number of encounters?"))
    except ValueError:
        print("This is not an integer.")
        continue
    else:
        break

#works VVV
while count > 0:
    loot = randint(1,100)
    if (loot > 14 and loot < 30):
        coin[0] += 1
    elif (loot >= 30 and loot < 53):
        coin[1] += 1
    elif (loot >= 53 and loot < 96):
        coin[2] += 1
    elif loot >= 96:
        coin[3] += 1
    count -= 1

coin[0] = rollMultipleDice(coin[0], 6) * 1000
coin[1] = rollMultipleDice(coin[1], 8) * 100
coin[2] = rollMultipleDice(2*coin[2], 8) * 10
coin[3] = rollMultipleDice(coin[3], 4) * 10

print (coin[0], "cp,", coin[1], "sp,", coin[2], "gp,", coin[3], "pp.")
