# Mastermind.py

import random
import itertools
import time
import numpy as np

INSTRUCTIONS = """\nInstructions:
                  Guess the right combination of colors in a limited tries,
                  X means right color, right space.
                  O means right color, wrong space.
                  Your color choices are Green, Red,
                  Blue, White, Yellow, and Purple\n\n"""

def try_all_answers(all_remaining_colors, guess, true_feedback):
    """
    This is for the Artificial Intelligence answering mechanism.

    After making a random guess we search all answers that produce the
    same feedback with the original guess. This results in a smaller set
    of remaining answers. These answers repeat the random guessing pattern,
    and take the feedback to produce another, smaller, subset in which
    the true answer must be contained.
    """

    remaining = []
    for maybe_answer in all_remaining_colors:
        filter_feedback = give_feedback(guess, maybe_answer[:])
        if true_feedback == filter_feedback:
            remaining.append(maybe_answer)
    return remaining

def give_feedback(lguess, answer):
    """
    return X's and O's to give feedback on each guess

    called by the game for the player to respond with a follow-up guess
    """

    correct = ''
    idx_list = []
    for i in range(4):
        if lguess[i] == answer[i]:
            correct = correct + 'X'
        else:
            idx_list.append(i)
    for j in idx_list:
        for k in idx_list:
            if j != k and lguess[j] == answer[k]:
                correct = correct + 'O'
                answer[k] = ''
                break
    return correct

if __name__ == "__main__":
#number_of_guesses = []
#failed_attempts = 0
#for game in range(100):
    tries = 10
    answer_length = 4
    colors = ['G', 'R', 'B', 'W', 'Y', 'P']
    answer = random.sample(colors, answer_length)
    all_remaining_colors = list(map(list, itertools.product(colors,
                                            repeat=answer_length)))
    print(INSTRUCTIONS)
    while tries > 0:
        guess = random.choice(all_remaining_colors)
        print("This is the guess for the turn: " + str(guess))
        if len(guess) == answer_length and set(guess).issubset(set(colors)):
            tries = tries - 1
            if guess == answer:
                print("you win!!!")
                #number_of_guesses += [10 - tries]
                break
            else:
                feedback = give_feedback(guess, answer[:])
                all_remaining_colors = try_all_answers(all_remaining_colors,
                                                        guess, feedback)
                print("Guess again: here is your feedback: " + feedback)
                print(str(tries) + " tries left \n")
                print("answers remaining: " + str(len(all_remaining_colors)))
                time.sleep(5)
        else:
            pass
            print("Wrong Format, guess again \n")
    else:
        print("You Lost.")
        #failed_attempts += 1

    print("Answer: " + ' '.join(answer))

#all_guesses = np.array(number_of_guesses)
#print("mean all guess: " + str(np.mean(all_guesses)))
#print("standard deviation all guess: " + str(np.std(all_guesses)))
#print("games lost: " + str(failed_attempts))
