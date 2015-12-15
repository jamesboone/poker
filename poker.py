import random


class Deck(object):
    def __init__(self, deck_qty, custom_suits=None, custom_values=None):
        self.suits = 'HSDC' if not custom_suits else custom_suits
        self.values = '23456789TJQKA' if not custom_values else custom_values
        self.deck = []
        self.deck_qty = deck_qty

    def shuffle(self):
        for v in self.values:
            for s in self.suits:
                self.deck.append('%s-%s' % (v, s,))
        return self.deck * self.deck_qty


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
            for i in xrange(self.cards_per_player):
                for player in self.players:
                    player.hand.append(self.deal())
            print 'deal to play'

    def deal(self):
        shuffled_deck = self.deck.shuffle()
        return random.choice(shuffled_deck)


class five_card_stud(Game):
    def __init__(self):
        self.players = []
        self.dealer_name = 'Dave'
        self.dealer = Dealer(self.dealer_name)
        self.name = 'Five Card Stud'
        self.cards_per_player = 5
        self.max_players = 5
        self.min_players = 2
        self.dealer = True
        self.deck_qty = 1
        self.shuffle_after_hand = True
        self.deck = Deck(self.deck_qty)


class Gambler(object):
    def __init__(self, name):
        self.name = name


class Dealer(Gambler):
    def deal(self):
        print 'deal'

    def shuffle(self, deck):
        print 'shuffle'


class Player(Gambler):
    def __init__(self, name, buy_in, hand=None):
        self.buy_in = buy_in
        self.name = name
        self.hand = []

    def play(self):
        print 'playing player'

    def bet(self):
        print 'betplay'

    def leave_game(self):
        print 'leave'


fcs = five_card_stud()
james = fcs.join('james', 100)
john = fcs.join('john', 100)
fcs.play()
