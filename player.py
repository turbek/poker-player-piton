
class Player:
    VERSION = "Default Python folding player"

    low_cards = ["2", "3", "4", "5", "6", "7", "8"]
    hand = []
    odds = {"hand": [
            [{"rank": "A"}, {"rank": "A"},  {"odds": 4}, {"suit": False}],
            [{"rank": "K"}, {"rank": "K"},  {"odds": 4}, {"suit": False}],
            [{"rank": "Q"}, {"rank": "Q"},  {"odds": 4}, {"suit": False}],
            [{"rank": "J"}, {"rank": "J"},  {"odds": 3}, {"suit": False}],
            [{"rank": "10"}, {"rank": "10"},  {"odds": 3}, {"suit": False}],
            [{"rank": "9"}, {"rank": "9"},  {"odds": 3}, {"suit": False}],
            [{"rank": "8"}, {"rank": "8"},  {"odds": 2}, {"suit": False}],
            [{"rank": "7"}, {"rank": "7"},  {"odds": 2}, {"suit": False}],
            [{"rank": "6"}, {"rank": "6"},  {"odds": 2}, {"suit": False}],
            [{"rank": "5"}, {"rank": "5"},  {"odds": 2}, {"suit": False}],
            [{"rank": "4"}, {"rank": "4"},  {"odds": 2}, {"suit": False}],
            [{"rank": "3"}, {"rank": "3"},  {"odds": 1}, {"suit": False}],
            [{"rank": "2"}, {"rank": "2"},  {"odds": 1}, {"suit": False}],
            [{"rank": "A"}, {"rank": "K"},  {"odds": 3}, {"suit": False}],
            [{"rank": "A"}, {"rank": "Q"},  {"odds": 3}, {"suit": False}],
            [{"rank": "A"}, {"rank": "J"},  {"odds": 2}, {"suit": False}],
            [{"rank": "A"}, {"rank": "10"},  {"odds": 2}, {"suit": False}],
            [{"rank": "A"}, {"rank": "9"},  {"odds": 2}, {"suit": False}],
            [{"rank": "A"}, {"rank": "8"},  {"odds": 2}, {"suit": False}],
            [{"rank": "A"}, {"rank": "7"},  {"odds": 1}, {"suit": False}],
            [{"rank": "A"}, {"rank": "6"},  {"odds": 1}, {"suit": False}],
            [{"rank": "A"}, {"rank": "5"},  {"odds": 1}, {"suit": False}],
            [{"rank": "A"}, {"rank": "4"},  {"odds": 1}, {"suit": False}],
            [{"rank": "A"}, {"rank": "3"},  {"odds": 1}, {"suit": False}],
            [{"rank": "A"}, {"rank": "2"},  {"odds": 1}, {"suit": False}],
            [{"rank": "A"}, {"rank": "K"},  {"odds": 4}, {"suit": True}],
            [{"rank": "A"}, {"rank": "Q"},  {"odds": 3}, {"suit": True}],
            [{"rank": "A"}, {"rank": "J"},  {"odds": 3}, {"suit": True}],
            [{"rank": "A"}, {"rank": "10"},  {"odds": 2}, {"suit": True}],
            [{"rank": "A"}, {"rank": "9"},  {"odds": 2}, {"suit": True}],
            [{"rank": "A"}, {"rank": "8"},  {"odds": 2}, {"suit": True}],
            [{"rank": "A"}, {"rank": "7"},  {"odds": 2}, {"suit": True}],
            [{"rank": "A"}, {"rank": "6"},  {"odds": 1}, {"suit": True}],
            [{"rank": "A"}, {"rank": "5"},  {"odds": 1}, {"suit": True}],
            [{"rank": "A"}, {"rank": "4"},  {"odds": 1}, {"suit": True}],
            [{"rank": "A"}, {"rank": "3"},  {"odds": 1}, {"suit": True}],
            [{"rank": "A"}, {"rank": "2"},  {"odds": 1}, {"suit": True}],
            [{"rank": "K"}, {"rank": "Q"},  {"odds": 2}, {"suit": True}],
            [{"rank": "K"}, {"rank": "J"},  {"odds": 2}, {"suit": True}],
            [{"rank": "K"}, {"rank": "10"},  {"odds": 1}, {"suit": True}],
            [{"rank": "K"}, {"rank": "9"},  {"odds": 1}, {"suit": True}],
            [{"rank": "K"}, {"rank": "8"},  {"odds": 1}, {"suit": True}],
            [{"rank": "K"}, {"rank": "7"},  {"odds": 1}, {"suit": True}],
            [{"rank": "K"}, {"rank": "6"},  {"odds": 1}, {"suit": True}],
            [{"rank": "K"}, {"rank": "5"},  {"odds": 1}, {"suit": True}],
            [{"rank": "K"}, {"rank": "4"},  {"odds": 1}, {"suit": True}],
            [{"rank": "K"}, {"rank": "3"},  {"odds": 1}, {"suit": True}],
            [{"rank": "Q"}, {"rank": "J"},  {"odds": 1}, {"suit": True}],
            [{"rank": "Q"}, {"rank": "10"},  {"odds": 1}, {"suit": True}],
            [{"rank": "Q"}, {"rank": "9"},  {"odds": 1}, {"suit": True}],
            [{"rank": "Q"}, {"rank": "8"},  {"odds": 1}, {"suit": True}],
            [{"rank": "Q"}, {"rank": "7"},  {"odds": 1}, {"suit": True}],
            [{"rank": "J"}, {"rank": "10"},  {"odds": 1}, {"suit": True}],
            [{"rank": "J"}, {"rank": "9"},  {"odds": 1}, {"suit": True}],
            [{"rank": "J"}, {"rank": "8"},  {"odds": 1}, {"suit": True}],
            [{"rank": "J"}, {"rank": "7"},  {"odds": 1}, {"suit": True}]
            ]}

    def betRequest(self, game_state):
        return self.think(game_state)

    def showdown(self, game_state):
        pass

    def think(self, game_state):
        if len(game_state["community_cards"]) == 0:
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

        # for odd in self.odds:
        #     possible_hand = []
        #     for card in odd[:2]:
        #         possible_hand.append(card)
        #     if (self.hand[0]["rank"] == possible_hand[0]["rank"] and self.hand[1]["rank"] == possible_hand[1]["rank"] or self.hand[1]["rank"] == possible_hand[0]["rank"] and self.hand[0]["rank"] == possible_hand[1]["rank"]) and ((possible_hand[0]["suit"] == possible_hand[1]["suit"]) == suit_check()):
        #             if int(possible_hand[0]["odds"]) > 2:
        #                 bet = 6000
        #                 break
        #             else:
        #                 bet = 50
        #                 break
        #     return bet
        # if len(game_state["community_cards"]) == 0:
    #
    # def suit_check(self):
    #     return self.hand[0]["suit"] == self.hand[1]["suit"]
    #
    # def handreturn(self, game_state):
    #     self.hand = []
    #     for player in game_state["players"]:
    #         if player["name"] == "piton":
    #             for cards in player["hole_cards"]:
    #                 self.hand.append(cards)
    #
    # def communreturn(self, game_state):
    #     self.commun_cards = []
    #     for cards in game_state["community_cards"]:
    #         self.commun_cards.append(cards)
    #
    # def checkpair(self, game_state):
    #     for card in self.hand:
    #         for flop in self.commun_cards:
    #             if card["rank"] == flop["rank"]:
    #                 self.state.append(card)
    #                 self.state.append(flop)
    #     return len(self.state)
    #
    # def ifsuit(self):
    #     if self.hand[0]["suit"] == self.hand[1]["suit"]:
    #         for card in self.hand:
    #             for flop in self.commun_cards:
    #                 if card["suit"] == flop["suit"]:
    #                     self.suit.append(card)
    #     if len(self.suit) >= 5:
    #         return True
