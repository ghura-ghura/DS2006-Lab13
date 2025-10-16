#Task14
import random

def rollD6():
    return random.randint(1, 6)

def rollD20():
    return random.randint(1, 20)

num_players = int(input("Enter number of players: "))
players = []

for i in range(num_players):
    name = input(f"Enter name for Player {i+1}: ")
    players.append({"name": name, "wins": 0})

rounds = 0

while max(p["wins"] for p in players) < 3:
    rounds += 1
    print(f"\nRound {rounds}:")
    for player in players:
        score = rollD6() + rollD20()
        player["last_score"] = score
        print(f"{player['name']} rolled {score}")

    max_score = max(p["last_score"] for p in players)
    winners = [p for p in players if p["last_score"] == max_score]

    if len(winners) == 1:
        winners[0]["wins"] += 1
        print(f"--> {winners[0]['name']} wins this round!")
    else:
        print("Tie round!")

champion = max(players, key=lambda x: x["wins"])
print(f"\n🏆 {champion['name']} is the champion after {rounds} rounds! 🏆")
