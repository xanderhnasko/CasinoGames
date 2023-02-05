import random

numPlays = 100000
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def dealCard():
    return random.choice(cards)

PlayerWins = 0
DealerWins = 0

def checkForBlackJack(sumHand, soft):
    if sumHand == 21:
        return 1
    elif sumHand == 11 and soft == True:
        return 1
    else:
        return 0


def simulateBlackJack():
    dealerShown = dealCard()
    dealerDown = dealCard()

    # check if dealer got blackjack on first hand
    dealerSum = dealerShown + dealerDown
    dealerSoft = False
    if dealerShown == 1 or dealerDown == 1:
        dealerSoft = True
        
    

    # deal cards to player
    playerFirst = dealCard()
    playerSecond = dealCard()
    sumHand = 0
    soft = False

    # check for player aces
    if playerFirst == 1 and playerSecond == 1:
        sumHand == 12
    elif playerFirst == 1 or playerSecond == 1:

        # case we get blackjack on first hand
        if playerFirst or playerSecond == 10:
            # push case, both dealer and player have blackjack
            if checkForBlackJack(dealerSum, dealerSoft):
                return 0
            # else, player wins
            return 1
        else:
            sumHand = playerFirst + playerSecond + 10
            soft = True

    # check if dealer has blackjack (player doesn't)
    if checkForBlackJack(dealerSum, dealerSoft):
        return -1
    
    while sumHand < 19:

        # case sum is hard
        if not soft:
            if sumHand <= 11:
                # hit on all sums less than 11
                card = dealCard()
                if card == 1:
                    soft == True
                    if sumHand + 11 <= 21:
                        sumHand += 11
                    else:
                        sumHand += 1
                else:
                    sumHand += card
                if checkForBlackJack(sumHand, soft):
                    return 1
                if sumHand > 21:
                    return -1
            elif sumHand == 12:
                if dealerShown <= 3 or dealerShown >= 7:
                    card = dealCard()
                    if card == 1:
                        soft == True
                        if sumHand + 11 <= 21:
                            sumHand += 11
                        else:
                            sumHand += 1
                    else:
                        sumHand += card
                    if checkForBlackJack(sumHand, soft):
                        return 1
                    if sumHand > 21:
                        return -1
                # Player stands if dealer has 4, 5, or 6
                else:
                    break
            elif sumHand >= 13 and sumHand <= 16:
                if dealerShown >= 2 and dealerShown <= 6:
                    # player stands if dealer has 2-6
                    break
                else:
                    card = dealCard()
                    if card == 1:
                        soft == True
                        if sumHand + 11 <= 21:
                            sumHand += 11
                        else:
                            sumHand += 1
                    else:
                        sumHand += card
                    if checkForBlackJack(sumHand, soft):
                        return 1
                    if sumHand > 21:
                        return -1
            else:
                #player stands on all sums greater than 16
                break
        # case sum is hard
        else:
            if sumHand <= 17:
                card = dealCard()
                if card == 1:
                    soft == True
                    if sumHand + 11 <= 21:
                        sumHand += 11
                    else:
                        sumHand += 1
                else:
                    sumHand += card
                if checkForBlackJack(sumHand, soft):
                    return 1
                if sumHand > 21:
                    return -1
            if sumHand == 18:
                if dealerShown == 9 or dealerShown == 10:
                    card = dealCard()
                    if card == 1:
                        soft == True
                        if sumHand + 11 <= 21:
                            sumHand += 11
                        else:
                            sumHand += 1
                    else:
                        sumHand += card
                    if checkForBlackJack(sumHand, soft):
                        return 1
                    if sumHand > 21:
                        return -1
                else:
                    break
            else:
                break
    # dealer hand draws, dealer stands on soft 17
    while (dealerSum < 17):
        if dealerSoft:
            if dealerSum + 10 <= 21 and dealerSum + 10 >= 17:
                dealerSum += 10
                break
        card = dealCard()
        if card == 1:
            dealerSoft = True
            if dealerSum + 11 <= 21:
                dealerSum += 11
            else:
                dealerSum += 1
        else:
            dealerSum += card

    if dealerSum == 21:
        return -1
    elif dealerSum == 22:
        return 0
    if dealerSum > 22:
        return 1

    # compare hands
    if sumHand == dealerSum:
        return 0
    elif sumHand > dealerSum:
        return 1
    else:
        return -1


if __name__ == "__main__":
    i = 0
    numTies = 0
    while i < numPlays:
        if simulateBlackJack() == 1:
            PlayerWins += 1
        elif simulateBlackJack() == -1:
            DealerWins += 1
        else:
            numTies += 1

        i += 1
        


print(f"Player wins: {PlayerWins}")
print(f"Dealer wins: {DealerWins}")
print(f"Ties: {numTies}")
print(f"Player win percentage: {PlayerWins / (PlayerWins + DealerWins + numTies) * 100}%")

    
        
                    





        

        
        
        
    
    
