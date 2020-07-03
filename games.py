import random

money = 100

#Write your game of chance functions here




#Define Coin Flip game -------------------------------------

def coin_flip(guess, bet):
  global money
  print("Coin Flip Game")
  
  if guess != "Heads" and guess != "Tails":
    print('Guess must be "Heads" or "Tails"!')
    print()

  elif bet < 1:
    print("Bet must not be less than 1!")
    print()

  elif bet > money:
    print("You can't afford to bet " + str(bet) + " coins!")
    print("You only have " + str(money) + " coins.")
    print()

  else:
    face_num = random.randint(1,2)

    if face_num == 1:
      face_up = "Heads"

    else:
      face_up = "Tails"

    print("You guessed " + guess + ", with a bet of " + str(bet) + " coins...")

    if face_up == guess:
      print("The coin landed on... " + face_up + "!")
      print("Congratulations! You won " + str(bet) + " coins!")
      money += bet
      
    else:
      print("The coin landed on... " + face_up + "!")
      print("Commiserations, you lost " + str(bet) + " coins. Better luck next time!")
      money += - bet
    
    print("You now have " + str(money) + " coins!")
    print()




#Define Cho-Han game -------------------------------------

def cho_han(guess, bet):
  global money
  print("Cho-Han Game")

  if guess != "Even" and guess != "Odd":
    print('Guess must be "Even" or "Odd"!')
    print()

  elif bet < 1:
    print("Bet must not be less than 1!")
    print()

  elif bet > money:
    print("You can't afford to bet " + str(bet) + " coins!")
    print("You only have " + str(money) + " coins.")
    print()

  else:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die_total = die1 + die2

    if die_total % 2 == 0:
      result = "Even"
    else:
      result = "Odd"

    print("You guessed " + guess + " with a bet of " + str(bet) + " coins...")
    print("Die one landed on... " + str(die1) + ".")
    print("Die two landed on... " + str(die2) + ".")
    print("The dice total is " + str(die_total) + "...")
    print("It's " + result + "!")

    if guess == result:
      print("Congratulations! You won " + str(bet) + " coins!")
      money += bet
    
    else:
      print("Commiserations, you lost " +str(bet) + " coins.")
      money += - bet

    print("You now have " + str(money) + " coins!")
    print()




print()
#Call your game of chance functions here


print("------ Testing Coin Flip ------")
print()

print("Testing coin flip with false guess input")
coin_flip("heeds", 3)

print("Testing coin flip with false bet input")
coin_flip("Heads", 120)

print("Testing coin flip with valid input")
pythcoin_flip("Heads", 30)


print("------ Testing Cho-Han ------")
print()

print("Testing Cho-Han with invalid guess input")
cho_han("evens", 25)

print("Testing Cho-Han with invalid bet input")
cho_han("Odd", 0)

print("Testing Cho-Han with valid input")
cho_han("Even", 25)










































