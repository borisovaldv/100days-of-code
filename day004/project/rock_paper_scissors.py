rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

def play():
    rps = [rock, paper, scissors]
    user_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

    if 0 <= user_input <= 2:
        print(rps[user_input])
        comp_choice = random.randint(0, 2)
        print('Computer chose:')
        print(rps[comp_choice])

        if user_input == 1:
            if comp_choice == 0:
                print('You win!')
            elif comp_choice == 1:
                print("It's a draw")
            elif comp_choice == 2:
                print('You lose')

        elif user_input == 0:
            if comp_choice == 0:
                print("It's a draw")
            elif comp_choice == 1:
                print("You lose")
            elif comp_choice == 2:
                print('You win!')

        elif user_input == 2:
            if comp_choice == 0:
                print("You lose")
            elif comp_choice == 1:
                print('You win!')
            elif comp_choice == 2:
                print("It's a draw")
    else:
        print('Error. Type 0, 1 or 2.')

play()
again = input('Want to play again? y/n\n')
while again == 'y':
    play()
    again = input('Want to play again? y/n\n')
else:
    print('Thanks for playing!')