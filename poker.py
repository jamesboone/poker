import random
import copy


class Deck(object):
    def __init__(self, deck_qty, custom_suits=None, custom_values=None):
        self.suits = 'HSDC' if not custom_suits else custom_suits
        self.values = '23456789TJQKA' if not custom_values else custom_values
        self.playing_deck = []
        self.deck_qty = deck_qty

    def shuffle(self, deck):
        for v in self.values:
            for s in self.suits:
                deck.append('%s-%s' % (v, s,))

        random.shuffle(deck * self.deck_qty)
        return deck


class Game(object):
    def join(self, player_name, buy_in):
        if player_name not in self.players:
            player = Player(player_name, buy_in)
            self.players.append(player)
        return player

    def play(self):
        if len(self.players) < self.min_players:
            print 'you need more players'
        elif len(self.players) > self.max_players:
            print 'too many players trying to play'
        else:
            if not self.shuffled_deck or len(self.shuffled_deck) < (
                    self.cards_per_player * len(self.players)):
                self.shuffled_deck = self.deck.shuffle(self.deck.playing_deck)

                for i in xrange(self.cards_per_player):
                    for player in self.players:
                        player.hand.append(self.deal())
                print 'deal to play'

    def bet(self):
        for player in self.players:
            print player.name, 'Here is your hand: ', player.hand
            var = raw_input('Please place bet, 0 to pass.')
            if var == 0:
                continue
            else:
                self.pot += int(var)
                player.money -= int(var)
        winner = random.choice(self.players)
        print 'the winner is: ', winner.name
        winner.money += self.pot
        self.pot = 0
        print 'winner\'s new pot is: ', winner.money
        self.collect_cards()
        self.play_another_hand()

    def play_another_hand(self):
        players = copy.copy(self.players)
        for player in players:
            input_msg = "%s play another hand? (y/n)" % (player.name, )
            var = raw_input(input_msg)
            if var not in ['y', 'n']:
                var = raw_input('please indicate with \'y\' or \'n\'')

            if var == 'n':
                player.leave_game(self)

        if self.players:
            print 'playing another hand',
            self.play()

    def deal(self):
        card = random.choice(self.shuffled_deck)
        self.shuffled_deck.remove(card)
        return card


class five_card_stud(Game):
    def __init__(self):
        self.players = []
        self.dealer_name = 'Dave'
        self.dealer = Dealer(self.dealer_name)
        self.name = 'Five Card Stud'
        self.cards_per_player = 5
        self.max_players = 5
        self.min_players = 2
        self.deck_qty = 1
        self.shuffle_after_hand = True
        self.shuffled_deck = None
        self.deck = Deck(self.deck_qty)
        self.pot = 0


class Gambler(object):
    def __init__(self, name):
        self.name = name


class Dealer(Gambler):
    def deal(self):
        print 'deal'

    def shuffle(self, deck):
        print 'shuffle'


class Player(Gambler):
    def __init__(self, name, money, hand=None):
        self.money = money
        self.name = name
        self.hand = []

    def play(self):
        print 'playing player'

    def bet(self):
        print 'betplay'

    def leave_game(self, game):
        game.players.remove(self)
        print 'leave'

if __name__ == "__main__":
    fcs = five_card_stud()
    james = fcs.join('James', 100)
    john = fcs.join('John', 100)
    michael = fcs.join('Michael', 100)
    fcs.play()
    fcs.bet()
