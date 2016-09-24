a = {
    "tournament_id":"550d1d68cd7bd10003000003",     # Id of the current tournament

    "game_id":"550da1cb2d909006e90004b1",           # Id of the current sit'n'go game. You can use this to link a
                                                    # sequence of game states together for logging purposes, or to
                                                    # make sure that the same strategy is played for an entire game

    "round":0,                                      # Index of the current round within a sit'n'go

    "bet_index":0,                                  # Index of the betting opportunity within a round

    "small_blind": 10,                              # The small blind in the current round. The big blind is twice the
                                                    #     small blind

    "current_buy_in": 320,                          # The amount of the largest current bet from any one player

    "pot": 400,                                     # The size of the pot (sum of the player bets)

    "minimum_raise": 240,                           # Minimum raise amount. To raise you have to return at least:
                                                    #     current_buy_in - players[in_action][bet] + minimum_raise

    "dealer": 1,                                    # The index of the player on the dealer button in this round
                                                    #     The first player is (dealer+1)%(players.length)

    "orbits": 7,                                    # Number of orbits completed. (The number of times the dealer
                                                    #     button returned to the same player.)

    "in_action": 1,                                 # The index of your player, in the players array

    "players": [                                    # An array of the players. The order stays the same during the
        {                                           #     entire tournament

            "id": 0,                                # Id of the player (same as the index)

            "name": "Albert",                       # Name specified in the tournament config

            "status": "active",                     # Status of the player:
                                                    #   - active: the player can make bets, and win the current pot
                                                    #   - folded: the player folded, and gave up interest in
                                                    #       the current pot. They can return in the next round.
                                                    #   - out: the player lost all chips, and is out of this sit'n'go

            "version": "Default random player",     # Version identifier returned by the player

            "stack": 1010,                          # Amount of chips still available for the player. (Not including
                                                    #     the chips the player bet in this round.)

            "bet": 320                              # The amount of chips the player put into the pot
        },
        {
            "id": 1,                                # Your own player looks similar, with one extension.
            "name": "piton",
            "status": "active",
            "version": "Default random player",
            "stack": 1590,
            "bet": 80,
            "hole_cards": [                         # The cards of the player. This is only visible for your own player
                                                    #     except after showdown, when cards revealed are also included.
                {
                    "rank": "6",                    # Rank of the card. Possible values are numbers 2-10 and J,Q,K,A
                    "suit": "hearts"                # Suit of the card. Possible values are: clubs,spades,hearts,diamonds
                },
                {
                    "rank": "K",
                    "suit": "hearts"
                }
            ]
        },
        {
            "id": 2,
            "name": "Chuck",
            "status": "out",
            "version": "Default random player",
            "stack": 0,
            "bet": 0
        }
    ],
    "community_cards": [                            # Finally the array of community cards.
        {
            "rank": "4",
            "suit": "hearts"
        },
        {
            "rank": "A",
            "suit": "hearts"
        },
        {
            "rank": "6",
            "suit": "hearts"
        }
    ]
}


class Player:
    VERSION = "Default Python folding player"

# <<<<<<< Updated upstream
    low_cards = ["2", "3", "4", "5", "6", "7", "8"]
    hand = []
#     odds = {"hand": [
#             [{"rank": "A"}, {"rank": "A"},  {"odds": 4}, {"suit": False}],
#             [{"rank": "K"}, {"rank": "K"},  {"odds": 4}, {"suit": False}],
#             [{"rank": "Q"}, {"rank": "Q"},  {"odds": 4}, {"suit": False}],
#             [{"rank": "J"}, {"rank": "J"},  {"odds": 3}, {"suit": False}],
#             [{"rank": "10"}, {"rank": "10"},  {"odds": 3}, {"suit": False}],
#             [{"rank": "9"}, {"rank": "9"},  {"odds": 3}, {"suit": False}],
#             [{"rank": "8"}, {"rank": "8"},  {"odds": 2}, {"suit": False}],
#             [{"rank": "7"}, {"rank": "7"},  {"odds": 2}, {"suit": False}],
#             [{"rank": "6"}, {"rank": "6"},  {"odds": 2}, {"suit": False}],
#             [{"rank": "5"}, {"rank": "5"},  {"odds": 2}, {"suit": False}],
#             [{"rank": "4"}, {"rank": "4"},  {"odds": 2}, {"suit": False}],
#             [{"rank": "3"}, {"rank": "3"},  {"odds": 1}, {"suit": False}],
#             [{"rank": "2"}, {"rank": "2"},  {"odds": 1}, {"suit": False}],
#             [{"rank": "A"}, {"rank": "K"},  {"odds": 3}, {"suit": False}],
#             [{"rank": "A"}, {"rank": "Q"},  {"odds": 3}, {"suit": False}],
#             [{"rank": "A"}, {"rank": "J"},  {"odds": 2}, {"suit": False}],
#             [{"rank": "A"}, {"rank": "10"},  {"odds": 2}, {"suit": False}],
#             [{"rank": "A"}, {"rank": "9"},  {"odds": 2}, {"suit": False}],
#             [{"rank": "A"}, {"rank": "8"},  {"odds": 2}, {"suit": False}],
#             [{"rank": "A"}, {"rank": "7"},  {"odds": 1}, {"suit": False}],
#             [{"rank": "A"}, {"rank": "6"},  {"odds": 1}, {"suit": False}],
#             [{"rank": "A"}, {"rank": "5"},  {"odds": 1}, {"suit": False}],
#             [{"rank": "A"}, {"rank": "4"},  {"odds": 1}, {"suit": False}],
#             [{"rank": "A"}, {"rank": "3"},  {"odds": 1}, {"suit": False}],
#             [{"rank": "A"}, {"rank": "2"},  {"odds": 1}, {"suit": False}],
#             [{"rank": "A"}, {"rank": "K"},  {"odds": 4}, {"suit": True}],
#             [{"rank": "A"}, {"rank": "Q"},  {"odds": 3}, {"suit": True}],
#             [{"rank": "A"}, {"rank": "J"},  {"odds": 3}, {"suit": True}],
#             [{"rank": "A"}, {"rank": "10"},  {"odds": 2}, {"suit": True}],
#             [{"rank": "A"}, {"rank": "9"},  {"odds": 2}, {"suit": True}],
#             [{"rank": "A"}, {"rank": "8"},  {"odds": 2}, {"suit": True}],
#             [{"rank": "A"}, {"rank": "7"},  {"odds": 2}, {"suit": True}],
#             [{"rank": "A"}, {"rank": "6"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "A"}, {"rank": "5"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "A"}, {"rank": "4"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "A"}, {"rank": "3"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "A"}, {"rank": "2"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "K"}, {"rank": "Q"},  {"odds": 2}, {"suit": True}],
#             [{"rank": "K"}, {"rank": "J"},  {"odds": 2}, {"suit": True}],
#             [{"rank": "K"}, {"rank": "10"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "K"}, {"rank": "9"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "K"}, {"rank": "8"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "K"}, {"rank": "7"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "K"}, {"rank": "6"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "K"}, {"rank": "5"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "K"}, {"rank": "4"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "K"}, {"rank": "3"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "Q"}, {"rank": "J"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "Q"}, {"rank": "10"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "Q"}, {"rank": "9"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "Q"}, {"rank": "8"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "Q"}, {"rank": "7"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "J"}, {"rank": "10"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "J"}, {"rank": "9"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "J"}, {"rank": "8"},  {"odds": 1}, {"suit": True}],
#             [{"rank": "J"}, {"rank": "7"},  {"odds": 1}, {"suit": True}]
#             ]}

    def betRequest(self, game_state):
        return self.think(game_state)
# =======
#     low_cards = ["2", "3", "4", "5", "6", "7", "8", "9"]
#     hand = []
#     commun_cards = []
#     handcard1 = []
#     handcard2 = []
#     suit = []
#
#     def betRequest(self, game_state):
#         self.handreturn(game_state)
#         self.communreturn(game_state)
# >>>>>>> Stashed changes
#
#     def showdown(self, game_state):
#        pass
#
#     def handreturn(self, game_state):
#         self.hand = []
#         for player in game_state["players"]:
#             if player["name"] == "piton":
#                 for cards in player["hole_cards"]:
#                     self.hand.append(cards)
#
#     def communreturn(self, game_state):
#         self.commun_cards = []
#         for cards in game_state["community_cards"]:
#             self.commun_cards.append(cards)
#
#     def checkifhandpair(self):
#         if self.hand[0]["rank"] == self.hand[1]["rank"]:
#             return True
#
#     def checkifpair(self):
#         for flop in self.commun_cards:
#             if self.hand[0]["rank"] == flop["rank"]:
#                 self.handcard1.append(flop["rank"])
#             # for card in self.hand:
#             #     for flop in self.commun_cards:
#             #         if card["rank"] == flop["rank"]:
#             #             self.state.append(card)
#             #             self.state.append(flop)
#             # return len(self.state)
#
#     def ifsuit(self):
#         if self.hand[0]["suit"] == self.hand[1]["suit"]:
#             for card in self.hand:
#                 for flop in self.commun_cards:
#                     if card["suit"] == flop["suit"]:
#                         self.suit.append(card)
#         if len(self.suit) >= 5:
#             return True
#
#
#     # def think(self):
#     #     for player in a["players"]:  # PlayerService().game_state
#     #         if player["name"] == "piton":
#     #             for cards in player["hole_cards"]:
#     #                 for card, value in cards.items():
#     #                     if card == "rank":
#     #                         if value in self.low_cards:
#     #                             bet = 0
#     #
#     #     return bet
#
# <<<<<<< Updated upstream
    def think(self, game_state):
        # if len(game_state["community_cards"]) == 0:
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
# =======
# x = Player()
# x.betRequest(a)
# print(x.ifsuit())
# >>>>>>> Stashed changes
