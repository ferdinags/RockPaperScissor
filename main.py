import random

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

game_images = [rock, paper, scissors] # 0,1,2

user_choices = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choices >= 0 and user_choices <= 2:
    print(game_images[user_choices])

computer_choices = random.randint(0, 2)
print("Computer choice:")
print(game_images[computer_choices])

if user_choices >= 3 or user_choices < 0:
    print("Invalid input, You lose!")
elif user_choices == 0 and computer_choices == 2:
    print("You win!")
elif computer_choices == 0 and user_choices == 2:
    print("You lose!")
elif user_choices > computer_choices:
    print("You win!")
elif computer_choices > user_choices:
    print("You lose!")
elif user_choices == computer_choices:
    print("It's a draw!!")
