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
    
    print("You have " + str(money) + " coins!")
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

    print("You have " + str(money) + " coins!")
    print()




#Define Card Pick game -------------------------------------

def card_pick(bet):
  global money
  
  if bet < 1:
    print("Bet must not be less than 1!")
    print()

  elif bet > money:
    print("You can't afford to bet " + str(bet) + " coins!")
    print("You only have " + str(money) + " coins.")
    print()

  else:
    print("Two Player Card Pick Game")
    print("You are betting " + str(bet) + " coins that your card will be higher.")
    print("Aces are low, pick a card, any card...")

    player1_card = random.randint(1, 13)
    player2_card = random.randint(1, 13)

    if player1_card > player2_card:
      print("Your card is higher!")
      print("Congatulations! You win " + str(bet) + " coins!")
      money += bet

    elif player1_card == player2_card:
      print("Your cards are equal!")
      print("It's a tie! You do not win or lose any coins.")

    else:
      print("Your card is lower!")
      print("Commiserations, you lose " + str(bet) + " coins.")
      money += -bet

    print("You have " + str(money) + " coins!")
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
coin_flip("Heads", 30)


print("------ Testing Cho-Han ------")
print()

print("Testing Cho-Han with invalid guess input")
cho_han("evens", 25)

print("Testing Cho-Han with invalid bet input")
cho_han("Odd", 0)

print("Testing Cho-Han with valid input")
cho_han("Even", 25)


print("------ Testing Card Pick ------")
print()

print("Testing Card Flip with an invalid bet input")
card_pick(1000)

print("Testing Card Flip with a valid bet input")
card_pick(20)