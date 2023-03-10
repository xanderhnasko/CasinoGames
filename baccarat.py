import random

#code to simulate a game of baccarat with an infinite deck of cards 


def draw_card():
    return random.randint(1,13)

def check_natural(player, banker):
    if player == 8:
        if banker == 8:
            return -1
        elif banker == 9:
            return 0
        else: 
            return 1
    elif player == 9:
        if banker == 9:
            return -1
        else:
            return 1
    elif banker == 8 or banker == 9:
        return 0
    else:
        return None
    

def play_game():
    GOLDEN_DRAGON = 0
    LOW_TIE_MAX = 0

    player_cards = [draw_card(), draw_card()]
    banker_cards = [draw_card(), draw_card()]
    player = player_cards[0] + player_cards[1]
    banker = banker_cards[0] + banker_cards[1]
    banker_drawn = 2
    player_drawn = 2

    if player > 9:
        player = player % 10
    if banker > 9:
        banker = banker % 10
    
    # natural cases
    if check_natural(player, banker) in [-1,0,1]:
        return check_natural(player, banker), GOLDEN_DRAGON, LOW_TIE_MAX

    
    # player draws a third card
    if player < 6:
        player_cards.append(draw_card())
        player += player_cards[2]
        player_drawn += 1
        if player > 9:
            player = player % 10
        
        # banker draws a third card
        if banker < 3:
            banker_drawn += 1
            banker_cards.append(draw_card())
            banker += banker_cards[2]
            if banker > 9:
                banker = banker % 10
        elif banker == 3 and player != 8:
            banker_drawn += 1
            banker_cards.append(draw_card())
            banker += banker_cards[2]
            if banker > 9:
                banker = banker % 10
        elif banker == 4:
            if player in [2,3,4,5,6,7]:
                banker_drawn += 1
                banker_cards.append(draw_card())
                banker += banker_cards[2]
                if banker > 9:
                    banker = banker % 10
        elif banker == 5:
            if player in [4,5,6,7]:
                banker_drawn += 1
                banker_cards.append(draw_card())
                banker += banker_cards[2]
                if banker > 9:
                    banker = banker % 10
        elif banker == 6:
            if player in [6,7]:
                banker_drawn += 1
                banker_cards.append(draw_card())
                banker += banker_cards[2]
                if banker > 9:
                    banker = banker % 10
        # banker stands on 7 and above
    elif banker < 6:
            # banker draws a third card
            banker_drawn += 1
            banker_cards.append(draw_card())
            banker += banker_cards[2]
            if banker > 9:
                banker = banker % 10
        # banker stands on 6 and above
    

    if check_natural(player, banker) in [-1,0,1]:
        return check_natural(player, banker), GOLDEN_DRAGON, LOW_TIE_MAX
    else:
        if player > banker:
            return 1, GOLDEN_DRAGON, LOW_TIE_MAX
        elif player < banker:
            if banker == 7 and banker_drawn == 3:
                GOLDEN_DRAGON = 1
            return 0, GOLDEN_DRAGON, LOW_TIE_MAX
        else:
            
            if check_low_tie(player_cards) and check_low_tie(banker_cards):
                LOW_TIE_MAX = 1
            return -1, GOLDEN_DRAGON, LOW_TIE_MAX

def check_low_tie(player_cards):
    for card in player_cards:
        if card > 5 and card < 10:
            return False
    return True
    

if __name__ == "__main__":
    player_wins = 0
    banker_wins = 0
    ties = 0
    num_games = 1000000
    dragon_count = 0
    low_tie_count = 0
    for i in range(num_games):
        result, gd, ltm = play_game()
        dragon_count += gd
        low_tie_count += ltm
        if result == 1:
            player_wins += 1
        elif result == 0:
            banker_wins += 1
        else:
            ties += 1
    print("Number of games: ", num_games)
    print("Player wins: ", player_wins)
    print("Banker wins: ", banker_wins)
    print("Ties: ", ties)
    print("Player win percentage: ", player_wins/num_games)
    print("Banker win percentage: ", banker_wins/num_games)
    print("Tie percentage: ", ties/num_games)
    print ("Golden Dragon count: ", dragon_count)
    print("Golden Dragon percentage: ", dragon_count/num_games)
    print ("Low Tie Max count: ", low_tie_count)
    print("Low Tie Max percentage: ", low_tie_count/num_games)




    