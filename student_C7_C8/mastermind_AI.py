# Mastermind.py

import random
import time

def all_color_list(color_list):
    all_colors = []
    for color1 in color_list:
        for color2 in color_list:
            for color3 in color_list:
                for color4 in color_list:
                    all_colors.append([color1, color2, color3, color4])
    return all_colors

def one_guess(all_remaining_colors):
    return random.choice(all_remaining_colors)


def try_all_answers(all_remaining_colors, guess, true_feedback):
    remaining = []
    for color_list in all_remaining_colors:
        selective_feedback = give_feedback(guess, color_list[:])
        if true_feedback == selective_feedback:
            remaining.append(color_list)
    return remaining


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
    all_remaining_colors = all_color_list(colors)
    print("\nInstructions: Guess the right combination of 4 colors in 10 tries")
    print("X means right color, right space | O means right color, wrong space")
    print("Your color choices are Green, Red, Blue, White, Yellow, and Purple\n\n")
    while tries > 0:
        guess = one_guess(all_remaining_colors) #raw_input("Enter 4 colors from G/R/B/W/Y/P, seperate with a space: ")
        print("This is the guess for the turn: " + str(guess))
        #lguess = guess.split(' ')
        if len(guess) == 4 and set(guess).issubset(set(colors)):
            tries = tries - 1
            if guess == answer:
                print("you win!!!")
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
            print("Wrong Format, guess again \n")

    print("Answer: " + ' '.join(answer))
