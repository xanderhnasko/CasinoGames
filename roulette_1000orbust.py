import random
import matplotlib.pyplot as plt

x = []
y = []
num_plays = 1000000
reds = [i + 1 for i in range(18)]
blacks = [i + 1 for i in range(18, 36)]
money = 0
bet = 1
thousand_bet = False
negative_profit = False

for i in range(num_plays):
    spin = random.randint(-1, 36)
    color_bet = random.randint(0, 1)

    if (color_bet == 0 and spin in reds) or (color_bet == 1 and spin in blacks):

        money += bet
        if money < 0:
            negative_profit = True
        else:
            negative_profit = False
            thousand_bet = False

        if thousand_bet and negative_profit:
            bet = 1000
        else:
            bet = 1
    else:
        money -= bet
        if bet >= 512:
            thousand_bet = True
            bet = 1000
        else:
            bet *= 2
    x.append(i + 1)
    y.append(money)

plt.plot(x, y)
plt.xlabel("Games Played")
plt.ylabel("Profit ($)")
plt.show()
