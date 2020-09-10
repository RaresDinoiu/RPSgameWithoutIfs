import random

while True:
    choice = str(input("Choose your weapon! "))
    choice = choice.lower()
    print("You chose : ", choice)

    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    print("Computer chose: ", computer_choice)

    choice_dict = {'rock': 0, 'paper': 1, 'scissors': 2}

    choice_index = choice_dict.get(choice, 3)
    computer_index = choice_dict.get(computer_choice)
    #print('COMPUTER choice index', computer_index)

    result_matrix = [[0,2,1], #to be explained below
                     [1,0,2],
                     [2,1,0],
                     [3,3,3]]

    result_index = result_matrix[choice_index][computer_index]

    result_messages = ['It\'s a tie', 'You Win! :) ', 'You lose! :(', 'Wait! That\'s illegal! Choose again!']

    result = result_messages[result_index]
    print(result)
    print()


    #matrix explaining:
    # indexes: 0 = rock, 1 = paper, 2 = scissors
    # rows = player choices.
    # columns = computer choices.
    # row with index 3 = invalid options.

    # rules
    # Scissors cuts Paper
    # Paper covers Rock
    # Rock crushes Lizard
    # Lizard poisons Spock
    # Spock smashes Scissors
    # Scissors decapitates Lizard
    # Lizard eats Paper
    # Paper disproves Spock
    # Spock vaporizes Rock
    # (and as it always has) Rock crushes Scissors