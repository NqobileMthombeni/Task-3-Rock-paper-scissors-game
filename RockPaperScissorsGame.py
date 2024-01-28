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

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))

computer_choice = random.randint(0, 2)

user_choice_graphics = ""
computer_choice_graphics = ""

if user_input == 0:
    user_choice_graphics = rock
elif user_input == 1:
    user_choice_graphics = paper
elif user_input == 2:
    user_choice_graphics = scissors

if computer_choice == 0:
    computer_choice_graphics = rock
elif computer_choice == 1:
    computer_choice_graphics = paper
elif computer_choice == 2:
    computer_choice_graphics = scissors

print(f"Your choice:\n{user_choice_graphics}")
print(f"Computer's choice:\n{computer_choice_graphics}")

if user_input == computer_choice:
    print("It's a draw!")
elif (user_input == 0 and computer_choice == 2) or \
     (user_input == 1 and computer_choice == 0) or \
     (user_input == 2 and computer_choice == 1):
    print("You win!")
elif (user_input == 0 and computer_choice == 1) or \
     (user_input == 1 and computer_choice == 2) or \
     (user_input == 2 and computer_choice == 0):
    print("You lose!")
else:
    print("Invalid input. Please choose 0 for Rock, 1 for Paper, or 2 for Scissors.")
