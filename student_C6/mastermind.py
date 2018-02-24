# Mastermind.py

import random

def give_feedback(lguess, answer):
    """
    return X's and O's to give feedback on each guess
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
    tries = 10
    colors = ['G', 'R', 'B', 'W', 'Y', 'P']
    answer = [random.choice(colors) for _ in range(4)]
    print("\nInstructions: Guess the right combination of 4 colors in 10 tries")
    print("X means right color, right space | O means right color, wrong space")
    print("Your color choices are Green, Red, Blue, White, Yellow, and Purple\n\n")
    while tries > 0:
        guess = raw_input("Enter 4 colors from G/R/B/W/Y/P, seperate with a space: ")
        lguess = guess.split(' ')
        if len(lguess) == 4 and set(lguess).issubset(set(colors)):
            tries = tries - 1
            if lguess == answer:
                print("you win!!!")
                break
            else:
                feedback = give_feedback(lguess, answer[:])
                print("Guess again: here is your feedback: " + feedback)
                print(str(tries) + " tries left \n")
        else:
            print("Wrong Format, guess again \n")

    print("Answer: " + ' '.join(answer))
