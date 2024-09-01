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

#Write your code below this line 👇

your_choice = input("What do you choose 0 for scisoor,1 for paper,2 for rock: ")
choice_rps= ["rock","paper","scissors"]

random_game = random.choice(choice_rps)
if your_choice == "0":
    print(scissors)
    print("Computer choose:")
    print(random_game)
    if random_game == "rock":
        print(rock)
        print("you loose")
    elif random_game == "paper":
        print(paper)
        print(("You win"))
    else:

        print(scissors)
        print("draw")



elif your_choice =="1":
    print(paper)
    print("Computer choose:")
    print(random_game)
    if random_game == "rock":
        print(rock)
        print("You win")

    elif random_game == "paper":
        print(paper)
        print("Draw")
    else:
        print(scissors)
        print("You loose")
elif your_choice =="2":
    print(rock)
    print("Computer choose:")
    print(random_game)
    if random_game == "rock":
        print(rock)
        print("Draw")
    elif random_game == "paper":
        print(paper)
        print("You loose")
    else:
        print(scissors)
        print("you win")
else:
    print("Invalid choice")
