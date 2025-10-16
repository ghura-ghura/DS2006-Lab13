import random 

# Dice class for the number of sides of the die and the roll mapping that we had previously
class Die():
    def __init__(self, sides:int):
        if sides < 4 or sides >100:
            raise ValueError("Die must as we asked for have a value between 4 .. 100. Please try again!!! ")
        self.sides = sides 
    
    # Rolling the die 
    def roll_die(self):
         return random.randint(1,self.sides)
    
    # returning the die name that we short circuted with our new verison by just adding sides directly instead of input d1 .. dn    
    def __str__(self):
         return (f"D{self.sides}")


# Define class for Players and their rolling/wins and checking their types as a precaution to avioid errors
class Player():
    def __init__(self, name: str, email: str, country: str, die1: Die, die2: Die):
        self.name = name
        self.email = email
        self.country = country
        self.die1 = die1
        self.die2 = die2
        self.wins = 0 
        self.rollsintotal = []

    # Roll the two dices 
    def make_roll(self):
        roll_1 = self.die1.roll_die()
        roll_2 = self.die2.roll_die()
        total = roll_1 + roll_2
        self.rollsintotal.append(total)
        print(f"{self.name} rolled a {roll_1} and {roll_2} which in total equals {total}")
        return total
    
    # Players wins
    def add_win(self):
        self.wins += 1 

    
# Game controller that runs the game 
class Gamecontroller:
    def __init__(self, players, winning_score=3):
        self.players = players
        self.winning_score = winning_score
        self.rounds_played = 0 
        self.over = False
    
    # Play the game 
    def Play_game(self):
        # Run until we have a winner of our 3 rounds 
        while self.over is not True:
            self.rounds_played += 1 
            print(f"Rounds played for this game {self.rounds_played} ")
        
            # Loop over and do the rolls 
            curr_rolls = {}
            for player in self.players: 
                roll = player.make_roll()
                curr_rolls[player.name] = roll
       
            # Find the max roll value 
            max_roll = max(curr_rolls.values())
        
            winners = []
            for name, roll in curr_rolls.items():
                if roll == max_roll:
                    winners.append(name)

            # Update the winners 
            for player in self.players:
                if player.name in winners:
                    player.add_win()
                    if player.wins >= self.winning_score:
                        print(f"\nOur player, {player.name} is the new champion of our ultimate version of battle of dices\n")
                        self.over = True
                        break
            
            if self.over is True:
                break
        # Test to see if the game works before doing the filewriting part
        """
        print("\n--- Final Scores testprint ---")
        for player in self.players:
            print(f"{player.name}: {player.wins} wins in {len(player.rollsintotal)} rolls total.")
        print(f"\nGame over after {self.rounds_played} rounds!")
        """

    #Save the results to the file 
    def save_results(self, filename):
        with open(filename, "w") as file: 
            #Player info
            file.write("Player information: \n")

            for player in self.players:
                file.write(
                    f"* Name: {player.name}\n"
                    f"* Email: {player.email}\n"
                    f"* Country: {player.country}\n"
                    f"* Wins: {player.wins} \n"
                )
            file.write("\nGame rounds:\n")

            num_rounds = len(self.players[0].rollsintotal)

            # Write each rounds result to the file 
            for round_index in range(num_rounds):
                rolls_results = []

                # Go through each player and build the string step by step 
                for j, player in enumerate(self.players):
                    rolls_results.append(f"{player.name} rolled {player.rollsintotal[round_index]}")
                
                rolls_str = ", ".join(rolls_results)
                 
                # Now write the full round info to the file 
                file.write(f"Round {round_index + 1}:\n {rolls_str}\n")
                

        print("\nGame over! Results saved successfully. ")


## 1. We need to input the number of players that we have along with their info 

# List to store the object info for each player: 
players = []

# The input for how many plyers that we should have 
number_of_players = int(input("Enter how many players that you want to play this game! "))


# Loop over the input so that we can store the objects and get the dies for each player 
for i in range(number_of_players):
    name = input(str(f"What is the name of Player {i+1}? "))
    email = input(str(f"What is the email of Player {i+1}? "))
    country = input(str(f"What is the country of origin of Player {i+1}? "))
    die_1 = Die(int(input(f"Please enter the first die that the player {name} should roll with? \n You can chose from the selection of 4 .. 100 sides? ")))
    die_2 = Die(int(input(f"Please enter the first die that the player {name} should roll with? \n You can chose from the selection of 4 .. 100 sides? ")))
    player = Player(name, email, country, die_1, die_2)
    players.append(player)

## 2. We need to utilize the gamecontroller and run the game 
game = Gamecontroller(players, winning_score=3)
game.Play_game()

## 3. Once we have a winner we need to store the information to a seperate file either we do this in the class or as previously here. 
filename = input("\nEnter the filename to which you want to store the results: ")
game.save_results(filename)
