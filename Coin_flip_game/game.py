from random import randint


def info():
    f = open("/home/szymon/PycharmProjects/pythonProject/Coin_flip_game/rules.txt", 'r')
    rules = f.read()
    print(rules)
    f.close()


def smartPayment():
    chance = randint(1, 100)
    if chance % 100 == 0:
        return randint(1000, 5000)
    elif chance % 20 == 0:
        return randint(200, 1000)
    elif chance % 10 == 0:
        return randint(50, 200)
    elif chance % 5 == 0:
        return randint(10, 50)
    else:
        return randint(3, 10)


def throws(rounds):
    # lifes = ((rounds - (rounds % 1000)) / 1000) + 1
    for roundIndex in range(1, rounds):
        if randint(1, 2) % 2 == 0:  # liczby nieparzyste to reszka, parzyste to orzeł => parzysta kończy grę
            price = 2**roundIndex
            print("Orzeł wyrzucony w", roundIndex, "rundzie. Nagroda to", price)
            return price
    price = 2**rounds
    print("Gracz nie wyrzucił orła! Nagroda to", price)
    return price


def game():
    payment = smartPayment()
    # payment = randint(3, 25)
    print("Gracz wpłaca", payment, "zł.")
    return payment - throws(payment)


bilans = 0
info()
amountOfGames = int(input("Podaj liczbę gier, którą chcesz zasymulować: "))
# amountOfGames = 1000000
for i in range(amountOfGames):
    bilans += game()
    print("Po tej grze bilans zysków i strat to", bilans)
print("Po wszystkich grach zyskałeś", bilans, "zł!")
