import os
import random
from time import sleep

SUITS_CARD = {
    0: '♠',
    1: '♣',
    2: '\033[0;31;47m♦\033[0;30;47m',
    3: '\033[0;31;47m♥\033[0;30;47m'
}

RANKS_CARD = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', "A"]


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def view_start_screen():
    star_line = "*" * 50 + "\n"
    print(star_line,
          " BLACK♠JACK ".center(50, "*"), "\n",
          star_line,
          " BEST GAME OF 2020 YEAR ".center(50, "*"), "\n",
          star_line,
          " FOR FIRST VISIT ".center(50, "$"), "\n",
          " PRESENT 50 USA ".center(50, "$"), "\n",
          star_line,
          " press ENTER to play ".center(50, "*"), "\n",
          star_line,
          sep="")


def get_deck():
    new_deck = []
    for rank_card in RANKS_CARD:
        for i in range(4):
            card_value = int(rank_card) if rank_card.isdigit() else (11 if rank_card == "A" else 10)
            new_deck.append({'suit': i, 'rank': rank_card, "card_value": card_value})

    return new_deck


def shuffle_deck(data):
    random.shuffle(data)
    return data


def show_card(data: dict):
    # print(data)
    a = " "
    suit_card = SUITS_CARD[data['suit']]
    rank_card = data['rank']
    empty_line = "|" + a * 9 + "|"
    suit_line = "|" + a * 4 + suit_card + a * 4 + "|"
    a1 = "\033[0;30;47m"
    a2 = "\033[0m"
    print(f"\033[4;30;47m{' ' * 11}{a2}\n"
          f"{a1}|{a * 7}{suit_card}{rank_card}|{a2}\n"
          f"{a1}{empty_line}{a2}\n"
          f"{a1}{suit_line}{a2}\n"
          f"{a1}{empty_line}{a2}\n"
          f"\033[4;30;47m|{rank_card}{suit_card}{a * 7}|{a2}")
    # f"{a1}{first_last_line}{a2}")


def show_cards(data: list):
    try:
        for x in data:
            show_card(x)
    except:
        print("Ooops. Some Problems")


def get_card(data: list):
    return data.pop(), data


def get_cards_total(data: list):
    total = 0
    for x in data:
        total += x.get("card_value")
    return total


if __name__ == '__main__':
    # view_start_screen()

    player_cards = []
    dealer_cards = []
    deck = get_deck()
    shuffle_deck(deck)
    # show_card(deck.pop())

    card, deck = get_card(deck)
    player_cards.append(card)
    card, deck = get_card(deck)
    player_cards.append(card)

    dealer_playing = True
    while True:
        player_total = get_cards_total(player_cards)
        show_cards(player_cards)
        print("Your total: ", player_total)

        if player_total < 21:
            answer = input("More card?")
            if answer in "YyДд":
                card, deck = get_card(deck)
                player_cards.append(card)
                show_cards(card)
                continue
            else:
                break
        elif player_total == 21:
            print("You have Black Jack")
            break
        print("You have more than 21 point. You LOSE!")
        dealer_playing = False
        break
    print()
    card, deck = get_card(deck)
    dealer_cards.append(card)
    card, deck = get_card(deck)
    dealer_cards.append(card)

    while dealer_playing:
        dealer_total = get_cards_total(dealer_cards)
        show_cards(dealer_cards)
        print("Dealer total: ", dealer_total)

        if dealer_total < player_total:
            card, deck = get_card(deck)
            dealer_cards.append(card)
            continue
        elif dealer_total > 21:
            print("Player WIN")
            break
        msg_win = "Player WIN! " if player_total > dealer_total else ("Dealer WIN" if player_total< dealer_total else "DRAW")
        print(msg_win)
        break