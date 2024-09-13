import json
from typing import Optional

class HockeyDataManager:
    def __init__(self) -> None:
        self.__data: list[dict] = []

    def load_file(self, file_path: str):
        with open(file_path, "r") as file:
            self.__data = json.load(file)
            return True

    def num_players(self) -> int:
        return len(self.__data)

    def get_player(self, player_name: str) -> Optional[dict]:
        for player in self.__data:
            if player["name"] == player_name:
                return player
        return None

    def teams(self) -> list[str]:
        return sorted(set([player["team"] for player in self.__data]))

    def countries(self) -> list[str]:
        return sorted(set([player["nationality"] for player in self.__data]))

    def players_in_team(self, team: str) -> list[dict]:
        return sorted(
            filter(lambda player: player["team"] == team, self.__data),
            key=lambda player: player["goals"] + player["assists"],
            reverse=True,
        )

    def players_from_country(self, country: str) -> list[dict]:
        return sorted(
            filter(lambda player: player["nationality"] == country, self.__data),
            key=lambda player: player["goals"] + player["assists"],
            reverse=True,
        )

    def players_by_points(self) -> list[dict]:
        return sorted(
            self.__data,
            key=lambda player: ((player["goals"] + player["assists"]), player["goals"]),
            reverse=True,
        )

    def players_by_goals(self) -> list[dict]:
        return sorted(
            self.__data,
            key=lambda player: (player["goals"], 1 / player["games"]),
            reverse=True,
        )


class Application:
    def __init__(self) -> None:
        self.data_manager = HockeyDataManager()

    def load_file(self) -> None:
        file_name = input("file name: ")
        try:
            self.data_manager.load_file(file_name)
            print(f"read the data of {self.data_manager.num_players()} players")
        except FileNotFoundError:
            print(f"no such file {file_name}")
            self.load_file()

    def print_help(self) -> None:
        print(
            "\n".join(
                [
                    "commands:",
                    "0 quit ",
                    "1 search for player ",
                    "2 teams",
                    "3 countries",
                    "4 players in team",
                    "5 players from country",
                    "6 most points",
                    "7 most goals",
                ]
            )
        )

    def search_for_player(self) -> None:
        player_name = input("name: ")
        player = self.data_manager.get_player(player_name)
        if player != None:
            print()
            self.print_player_stats(player)
        else:
            print(f"no such player {player_name}")

    def print_player_stats(self, player: dict):
        print(
            f"{player['name']:<21}{player['team']}"
            f"{player['goals']:>4d} + {player['assists']:>2d} = "
            f"{(player['goals'] + player['assists']):>3d}"
        )

    def list_teams(self) -> None:
        print("\n".join(self.data_manager.teams()))

    def list_countries(self) -> None:
        print("\n".join(self.data_manager.countries()))

    def players_in_team(self):
        team_name = input("team: ")
        players = self.data_manager.players_in_team(team_name)
        if len(players) > 0:
            print()
            for player in players:
                self.print_player_stats(player)
        else:
            print(f"no players found for team {team_name}")

    def players_in_country(self):
        country_name = input("country: ")
        players = self.data_manager.players_from_country(country_name)
        if len(players) > 0:
            print()
            for player in players:
                self.print_player_stats(player)
        else:
            print(f"no players found in country {country_name}")

    def most_points(self):
        number = int(input("how many: "))
        players_by_points = self.data_manager.players_by_points()

        print()
        for i in range(0, min(number, len(players_by_points))):
            self.print_player_stats(players_by_points[i])

    def most_goals(self):
        number = int(input("how many: "))
        players_by_goals = self.data_manager.players_by_goals()

        print()
        for i in range(0, min(number, len(players_by_goals))):
            self.print_player_stats(players_by_goals[i])

    def execute(self) -> None:
        self.load_file()
        print()
        self.print_help()

        while True:
            print()
            command = input("command: ")
            match command:
                case "0":  # quit
                    break
                case "1":  # search for player
                    self.search_for_player()
                case "2":  # teams
                    self.list_teams()
                case "3":  # countries
                    self.list_countries()
                case "4":  # players in team
                    self.players_in_team()
                case "5":  # players from country
                    self.players_in_country()
                case "6":  # most points
                    self.most_points()
                case "7":  # most goals
                    self.most_goals()


app = Application()
app.execute()
