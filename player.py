
class Player:
    VERSION = "Default Python folding player"

    low_cards = ["2", "3", "4", "5", "6", "7", "8"]
    hand = []

    def betRequest(self, game_state):
        return self.think(game_state)

    def showdown(self, game_state):
        pass

    def think(self, game_state):
        bet = 1000
        for player in game_state["players"]:
            if player["name"] == "piton":
                for cards in player["hole_cards"]:
                    self.hand.append(cards)
                    for card, value in cards.items():
                        if card == "rank":
                            if value in self.low_cards:
                                bet = 0
        if self.hand[0]["rank"] == self.hand[1]["rank"]:
            bet = 1000
        return bet
