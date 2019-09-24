pokerAssignments = {'2': 20, '3': 30, '4': 40, '5': 50, '6': 60, '7': 70, '8': 80, '9': 90, 'T': 100, 'J': 110, 'Q': 120, 'K': 130, 'A': 140, 'C': 0, 'S': 1, 'H': 2, 'D': 3} #Used to assign each card to a unique three-digit integer

configScoring = {(1, 1): 0, (1, 2): 1, (2, 2): 2, (1, 3): 3, (2, 3): 6, (1, 4): 7} #Tracks hand scores for (respectively) high card, pair, two pair, three-of-a-kind, full house, and four-of-a-kind

scoreValues = {0: 'High Card', 1: 'Pair', 2: '2 Pair', 3: '3 of a Kind', 4: 'Straight', 5: 'Flush', 6: 'Full House', 7: '4 of a Kind', 8: 'Straight Flush'} #This data object is purely to enhance readability by demonstrating what type of hand each hand score corresponds to

def initialize(): #initalizes hands_list, assigns each card in a hand to a unique three-digit integer
    hands_file = open("euler54_poker.txt")
    hands_string = hands_file.read()
    tempList = []
    newString = (hands_string.replace('\n', ' ')).replace(' ', '')

    for i in range(0, len(newString), 2):
        tempList.append(newString[i: i + 2])

    hands_list = []

    for i in range(0, len(tempList), 10): #generates list item for each hand of 10 cards
        new_hand = []

        for j in range(2): #generates list item for each player's cards
            player_hand = []

            for k in range(5):
                player_hand.append(pokerAssignments[tempList[i + 5*j + k][0]] + pokerAssignments[tempList[i + 5*j + k][1]])

            new_hand.append(player_hand)

        hands_list.append(new_hand)

    return hands_list

hands_list = initialize()

def check_flush(hand): # checks if a reverse sorted hand is a flush
    suit = hand[0] % 10

    for i in range(1, 5):
        if hand[i] % 10 != suit:
            return False

    return True

def check_straight(hand): #checks if a reverse sorted hand is a straight

    for i in range(1, 5):

        if hand[i] // 10 != (hand[i - 1] // 10) - 1:
            return False

    return True

def check_copies(hand): #checks if a hand has any pairs, three of a kind, two pair, etc. and sorts it accordingly
    config = []
    hand.sort()

    i = 0
    while i < 5:
        count = 1
        j = 1

        while i + j < 5 and (hand[i + j] // 10) == (hand[i] // 10):
            count += 1
            j += 1

        config.append([count, hand[i] // 10])
        i += j

    if config != []: #sorts for comparison
        config.sort()

        for i in range(len(config)):

            for j in range(5):

                if (hand[j] // 10) == config[i][1]:
                    hand.insert(0, hand[j])
                    hand.pop(j + 1)

    return hand, config[-2][0], config[-1][0]

def score_hand(hand): #returns a number 0-8 for the hand the player has and the hand properly sorted
    hand.sort(reverse = True)
    is_flush = check_flush(hand)
    is_straight = check_straight(hand)

    if is_flush and is_straight:
        return hand, 8

    elif is_flush:
        return hand, 5

    elif is_straight:
        return hand, 4

    else:
        hand, config_one, config_two = check_copies(hand)
        return hand, configScoring[config_one, config_two]

def compare(hand_one, hand_two): #returns the number of the winning player if players have same hand score (who has higher card in tiebreak?)

    for i in range(5):
        if hand_one[i] // 10 > hand_two[i] // 10:
            return 1

        elif hand_two[i] // 10 > hand_one[i] // 10:
            return 2

    return None

def main(hands):
    p_one_wins = 0

    for i in range(len(hands)):
        p_one_hand, p_one_score = score_hand(hands[i][0])
        p_two_hand, p_two_score = score_hand(hands[i][1])

        if p_one_score > p_two_score:
            p_one_wins += 1

        elif p_one_score == p_two_score:
            if compare(p_one_hand, p_two_hand) == 1:
                p_one_wins += 1

    return p_one_wins

print(main(hands_list))
