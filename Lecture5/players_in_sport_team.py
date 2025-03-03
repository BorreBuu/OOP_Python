class Player:
    def __init__(self, name: str, goals: int):
        self.name = name
        self.goals = goals

    def __str__(self):
        return f"{self.name} ({self.goals} goals)"

class Team:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def add_player(self, player: Player):
        self.players.append(player)

    #Practice with keyword None
    #If player is not found, program returns None
    def find_player(self, name: str):
        for player in self.players:
            if player.name == name:
                return player
        return None

    def summary(self):
        goals = []
        for player in self.players:
            goals.append(player.goals)
        print("Team:", self.name)
        print("Players:", len(self.players))
        print("Goals scored by each player:", goals)

ca = Team("Campus Allstars")
ca.add_player(Player("Eric", 10))
ca.add_player(Player("Emily", 22))
ca.add_player(Player("Andy", 1))
#ca.summary()
player1 = ca.find_player("Andy")
print(player1)
player2 = ca.find_player("Charlie")

if player2 is not None:
    print(f"Goals by Charlie: {player2.goals}")
else:
    print(f"Charlie doesn't play in Campus Allstars :(")