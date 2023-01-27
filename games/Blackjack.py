import random, sys

HEARTS   = chr(9829)
DIAMONDS = chr(9830)
SPADES   = chr(9824)
CLUBS    = chr(9827)

BACKSIDE = 'backside'

def main():
    print(''' BlackJack
    Rules:
        Intenta obtener o acercarte a 21 sin pasarte.
        Reyes, reinas, and sotas valen 10 puntos.
        Aces pueden valer tanto 1 como 11 puntos.
        Desde el 2 al 10 valen el numero de la cara.
        (I)ntentar para pedir otra carta.
        (P)arar para dejar de pedir.
        En tu primera jugada puedes (D)uplicar para incrementar tu apuesta
        pero debes pedir al menos una vez mas otra carta.
        En caso de empate la apuesta se le devuelve.
        El dealer deja de intentar cuando asoma a 17.''')

    money = 5000
    while True:
        if money <= 0:
            print('¡Estas quebrado!')
            print('Menos mal que no juegas con dinero real')
            print('Gracias por jugar.')
            sys.exit()

        print('Dinero: ',money)
        bet = getBet(money)

        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        print('Apuesta:', bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()
            if getHandValue(playerHand) > 21:
                break
            move = getMove(playerHand, money - bet)

            if move == 'D':
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Apuesta incrementada en {}.'.format(bet))
                print('Apuesta: ', bet)

            if move in ('I', 'D'):

                newCard = deck.pop()
                rank, suit = newCard
                print('Tu obtuviste un {} de {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                      continue
            if move in ('P', 'D'):
                break

        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print('Dealer tiene ...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break
                input('Presiona Enter para continuar')
                print('\n\n')

        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        if dealerValue > 21:
            print('Dealer se pasó, tu ganaste ${}'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('¡Perdiste!')
            money -= bet
        elif playerValue > dealerValue:
            print('¡Tu ganaste! ${}'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('Es un empate, la apuesta vuelve a tu billetera')

        input('Presiona Enter para continuar')
        print('\n\n')

def getBet(maxBet):
    while True:
        print('¿De cuanto es la apuesta? (1-{}, o salir)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'salir':
            print('Gracias por jugar')
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1<= bet <= maxBet:
            return bet

def getDeck():
    deck = []
    for suit in ( HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print('DEALER: ', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        displayCards([BACKSIDE] + dealerHand[1:])

    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    value = 0
    numberOfAces = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    return value

def displayCards(cards):
    rows = ['', '', '', '', '']

    for i, card in enumerate(cards):
        rows[0] += ' ___  '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank,suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    for row in rows:
        print(row)

def getMove(playerHand, money):
    while True:
        moves = ['(I)ntentar', '(P)arar']

        if len(playerHand) == 2 and money > 0:
            moves.append('(D)uplicar')

        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('I', 'P'):
            return move
        if move == 'D' and '(D)uplicar' in moves:
            return move

if __name__ == '__main__':
    main()
            
        
