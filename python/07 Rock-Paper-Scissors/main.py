import random
#Sorry if it looks more visual than what was required.
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
print('''
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀''')
options = ["R", "P", "S"]

while True:
  #Computer randomly pick a choice at each loop.
  computer_choice = random.choice(options)
  user_choice = input('Please pick an option between "R", "P" or "S" select "Q" to Quit or CTRL + C: ').upper() # Exception handling for lowercase input
  #Game logic goes here
  if user_choice == "S" and computer_choice == "P":
    print("You choose: ")
    print(scissors)
    print("Computer chooses: ")
    print(paper)
    print("You won!")
  elif user_choice == "S" and computer_choice == "R":
    print("You choose: ")
    print(scissors)
    print("Computer chooses: ")
    print(rock)
    print("You lose!")
  elif user_choice == "S" and computer_choice == "S":
    print("You choose: ")
    print(scissors)
    print("Computer chooses: ")
    print(scissors)
    print("It's a tie!")

    
  elif user_choice == "R" and computer_choice == "P":
    print("You choose: ")
    print(rock)
    print("Computer chooses: ")
    print(paper)
    print("You lose!")
  elif user_choice == "R" and computer_choice == "S":
    print("You choose: ")
    print(rock)
    print("Computer chooses: ")
    print(scissors)
    print("You won!")
  elif user_choice == "R" and computer_choice == "R":
    print("You choose: ")
    print(rock)
    print("Computer chooses: ")
    print(rock)
    print("It's a tie!")

    
  elif user_choice == "P" and computer_choice == "R":
    print("You choose: ")
    print(paper)
    print("Computer chooses: ")
    print(rock)
    print("You won!")
  elif user_choice == "P" and computer_choice == "S":
    print("You choose: ")
    print(paper)
    print("Computer chooses: ")
    print(scissors)
    print("You lose!")
  elif user_choice == "P" and computer_choice == "P":
    print("You choose: ")
    print(paper)
    print("Computer chooses: ")
    print(paper)
    print("It's a tie!")

  elif user_choice == "Q":
      break

    #User must have typed in an invalid input, warn them
  else:
    print("Invalid input, please try again 😁")
    
