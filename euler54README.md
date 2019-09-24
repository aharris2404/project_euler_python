# Euler Problem \#54 Solution

## Problem

[Project Euler Problem \#54](https://projecteuler.net/problem=54) asks one to read a [large file](euler54_poker.txt) containing two players' hands in <img src="/tex/675eeb554f7b336873729327dab98036.svg?invert_in_darkmode&sanitize=true" align=middle width=32.876837399999985pt height=21.18721440000001pt/> rounds of poker, and determine in how many of those rounds Player One had the winning hand.

## Solution

[Here is the code.](euler54.py)

### Brief Overview

First we clean and enhance the data, storing each card in a hand as a three-digit integer where the first two digits track card rank (2 through Ace) and the final digit tracks card suit. Then we iterate over the number of rounds in the text file, checking at each stage for each player if they had: a straight flush, a flush, a straight, some configuration of cards of repeated rank (pair, triple, four-of-a-kind, two pair, or full house), or nothing at all. If Player One had a hand which outranked Player Two's, we increment our answer by one. If the hands were tied, we check the sorted hands of Player One and two to see who had the higher card, and then increment if that was Player One.

### Somewhat-Less-Brief Overview

The solution will work in the following steps:

1. Read the text file containing each poker hand, storing as a string.
2. *Data cleaning*: Remove spaces and line breaks in the string. Convert into a list-object where the cards are split up into sets of ten (representing a round), which are in turn split up into two lists of five (representing the players in that round).
3. *Data enhancement*: Convert all cards in all hands into a unique three-digit integer (which will be called an *NCA* for numerical card assignment), where the first two digits track card rank, and the last digit tracks card suit.
4. For a particular round, check each player's hand and assign a score based on what rank their hand has (0 through 8).
5. Check if the player has a straight, by sorting the hand, starting from the lowest card, and observing if all remaining cards form a straight (simple to do by taking each NCA and performing `NCA // 10`).
6. Check if the player has a flush by checking if all the NCA's have the same last digit (i.e. `NCA1 % 10 == NCA2 % 10 == ... == NCA5 % 10`)
7. Assign a score of 8 if the player has a straight flush, a score of 5 if the player has a flush, and a score of 4 if the player has a straight.
8. If at least one player has neither a straight nor flush, check if the player has a pair, two pair, three-of-a-kind, full house, or four-of-a-kind. This is easy to do by sorting the hand and checking whether, for example, `hand[i] == hand[i + 1]`. Assign a score of 7 for four-of-a-kind, 6 for full house, 3 for three-of-a-kind, 2 for two pair, 1 for a pair, and 0 otherwise.
9. If players have the same score, check who has the tiebreaking high card by iterating through the sorted hands until one card is decisive over the other.
10. If player one won the hand, increment the answer by one.
11. Loop through steps 4-10 for the number of hands.
12. Return the number of hands won by player one.

### Solution Advantages

* Adheres to black-box paradigm
* Generalizable for different numbers of hands than 1000
* Fast runtime which scales linearly with number of hands

### Solution Disadvantages

* Over 100 lines of code
* Not generalizable for different numbers of players (though could be with some simple modifications)
* Not "smart" enough to clean data in a different format than the specific format used in the provided text file

### Time Complexity

Let <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> be the number of rounds provided.

Since the data-cleaning process iterates over the number of rounds and involves constant-time removal of spaces and linebreaks, and concludes with constant-time assignment of each card to an integer, that phase runs in <img src="/tex/1f08ccc9cd7309ba1e756c3d9345ad9f.svg?invert_in_darkmode&sanitize=true" align=middle width=35.64773519999999pt height=24.65753399999998pt/> time.

For specifically two players with hands of five cards, all the per-hand checks which score the hands and break ties run in constant time. Thus, scoring all the rounds runs in <img src="/tex/1f08ccc9cd7309ba1e756c3d9345ad9f.svg?invert_in_darkmode&sanitize=true" align=middle width=35.64773519999999pt height=24.65753399999998pt/> time.

Thus the total runtime is <img src="/tex/1f08ccc9cd7309ba1e756c3d9345ad9f.svg?invert_in_darkmode&sanitize=true" align=middle width=35.64773519999999pt height=24.65753399999998pt/>.

## Results

For the case given in the problem, this code produces the correct result that Player One won <img src="/tex/ec743f6dfc0334fc2b308bc46ade48bc.svg?invert_in_darkmode&sanitize=true" align=middle width=24.657628049999992pt height=21.18721440000001pt/> hands in total. On my machine, it runs in under one second.
