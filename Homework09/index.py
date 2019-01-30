"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    help_arr = [0,0,0,0,0,0,0]
    for dice in hand:
        if dice == 1:
            help_arr[1] += 1
        elif dice == 2:
            help_arr[2] += 2
        elif dice == 3:
            help_arr[3] += 3
        elif dice == 4:
            help_arr[4] += 4
        elif dice == 5:
            help_arr[5] += 5
        elif dice == 6:
            help_arr[6] += 6
    #print max(help_arr)        
    return max(help_arr)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    all_rolls = gen_all_sequences((range(1,(num_die_sides+1))),num_free_dice)
    all_hands = [hand + held_dice for hand in all_rolls]    
    outcomes = float(len(all_rolls))
    expect = 0   
    for hand in all_hands:
        expect += (1/outcomes)*score(hand)
    return expect
   


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.
    
    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    holds = set([()])
    for dummy in range(len(hand) + 1):
        temp = set()
        for part in holds:
            ans = list(hand)
            for ele in part:
                ans.remove(ele)
            for item in ans:
                new = list(part)
                new.append(item)
                temp.add(tuple(sorted(new)))
        holds.update(temp)

    return holds



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.
    
    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    expected_values = []
    for item in gen_all_holds(hand):
        expected_values.append((expected_value(item, num_die_sides, len(hand) - len(item)), item))
    values = tuple([idx[0] for idx in expected_values])
    index = values.index(max(values))
    return expected_values[index]


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    score(hand)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)