# CasinoGames
Simulations of various strategies in casino games like Blackjack and Roulette

**Blackjack_sim.py**
Simulates an inputted number of Blackjack games (default = 1000000) wherein the player uses the most mathematically optimal strategy and the dealer always stands on soft 17s. Calculates the total number of player wins, dealer wins, and pushes (ties). 

**roulette_1000orbust.py**
Simulates a roulette strategy where the player bets the max limit ($1000) upon a loss until (if ever) they are back in profit

**roulette_1000max.py**
Simulates a roulette strategy where the player cuts their losses, doubling down upon a loss until their bet would be over 1000, in which case they bet only $1. 

**roulette.py**
Simulates the double-down roulette strategy with unlimited capital and no max-bet cap, where a player doubles down upon a loss until winning. 
