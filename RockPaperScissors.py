import random

while True:
 print("Rock Paper Scissors")
 print("type S for Scissors, R for Rock and P for paper")

 playerchoice = input("type here ---->").upper()

 choices= ['R', 'P', 'S']
 computerchoice = random.choice(choices)
 print(f"Computer chose {computerchoice}!")
 win= 1
 if computerchoice == playerchoice :
    print("Tie!")
    win=0
 elif computerchoice=='R' and playerchoice=='P':
        print("Player Wins!")
 elif computerchoice=='S' and playerchoice=='R':
        print("Player Wins!")
 elif computerchoice=='P' and playerchoice=='S':
    print("Player Wins")
 else :
    print("Computer Wins!")
    win=0
    
    
 repeat= input("Want to play again? (yes/no) --->").lower()

 if repeat =="yes" :
    if win==0 :
        print("Maybe you'll win this time?")
    else :
        print("Keep up the good work!")
 elif win==0:
    print("Dont be such a sore loser! Try again!")
 else: 
     print("Smart, quit while you're ahead")
     break
  