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
avail_choices = [rock, paper, scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice = random.randint(0,2)
if user_choice==0 or user_choice==1 or user_choice==2:
    print(avail_choices[user_choice])
    print("Computer chose:")
    print(avail_choices[comp_choice])
    if user_choice==comp_choice:
        print("It's a draw")
    elif (comp_choice==0 and user_choice==1) or (comp_choice==2 and user_choice==0) or (comp_choice==1 and user_choice==2):
        print("You win!")
    else:
        print("You lose")
else:
    print("You typed an invalid number, you lose!")
