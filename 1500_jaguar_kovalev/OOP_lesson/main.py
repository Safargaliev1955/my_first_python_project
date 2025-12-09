class Player:
    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number
    def action(self):
        print(f"{self.name} играет!")

class HockeyPlayer(Player):
    def action(self):
        print(f"{self.name} играет в хоккей!")


class HockeyTeam():
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def __str__(self):
        return f"Команда {self.name}"

    def add_player(self, player: HockeyPlayer):
        self.players.append(player)
        print(f"В команду {self.name} добавлен {player.name}!")

    @property
    def qty(self) -> int:
        return len(self.players)


class Game():
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def start_game(self):
        print(f"Начинается игра\n{self.team1} в количестве {self.team1.qty}\nVS\n{self.team2.name} в количестве {self.team2.qty}")
        for player in self.team1.players:
            player.action()

        for player in self.team2.players:
            player.action()


if __name__ == "__main__":
    player1 = HockeyPlayer("Иван Кочерыжкин", 15)
    player2 = HockeyPlayer("Ови", 20)
    player3 = HockeyPlayer("Месси", 10)
    team1 = HockeyTeam("ЦСКА")
    team2 = HockeyTeam("Спартак")
    team1.add_player(player1)
    team2.add_player(player2)
    team2.add_player(player3)
    game1 = Game(team1, team2)
    game1.start_game()
