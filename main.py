import requests
import json


class Player:

    def __init__(self, platform, region, battletag):
        self.platform = platform
        self.region = region
        self.battletag = battletag
        # grabs profile
        response = requests.get(f"https://ow-api.com/v1/stats/{self.platform}/{self.region}/{self.battletag}/profile")
        self.data = json.loads(response.text)


    def get_name(self):
        return self.data['name']


    def get_total_level(self):
        return str(self.data['prestige']) + str(self.data['level'])


    def get_rating(self):
        return self.data['rating']


    def get_loss(self):
        return int(self.data['competitiveStats']['games']['played']) - int(self.data['competitiveStats']['games']['won'])


    def get_win(self):
        return self.data['competitiveStats']['games']['won']


    def get_rank(self):
        rating = self.data['rating']
        if rating < 1500:
            rank = "Bronze"
        elif rating in range(1500, 2000):
            rank = "Silver"
        elif rating in range(2000, 2500):
            rank = "Gold"
        elif rating in range(2500, 3000):
            rank = "Platinum"
        elif rating in range(3000, 3500):
            rank = "Diamond"
        elif rating in range(3500, 4000):
            rank = "Master"
        elif rating >= 4000:
            rank = "Grandmaster"
        return rank


if __name__ == "__main__":
    # TODO: ASK FOR INPUT for PLATFORM, REGION, NAME
    # IF NAME IS ENTERED WITH '#' INSTEAD OF '-', SWITCH IT TO THAT

    player = Player("pc", "us", "nebula-11571")
    print('Name: ', player.get_name())
    print('Level: ', player.get_total_level())
    print('Rating: ', player.get_rating())
    print('Losses: ', player.get_loss())
    print('Wins: ', player.get_win())    








