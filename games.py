import random

money = 100

#Define instruction list
def help():
  print()
  print("------ G's Game Room ------")
  print()
  print("You can play the following games by typing the functions below:")
  print()
  print('''    To play Coin Flip:
        type coin_flip("Heads" or "Tails", bet amount) and press Enter''')
  print()
  print('''    To play Cho-Han:
        type cho_han("Even" or "Odd", bet amount) and press Enter''')
  print()
  print('''    To play Card Pick:
        type card_pick(bet amount) and press Enter''')
  print()
  print('''    To play Roulette:
        type roulette(guess, bet amount) and press Enter
            Guesses can be "Even", "Odd", any number from 0 to 36 inclusive, or to bet on 00 input 37.''')
  print()
  print("To see this list again, type help()")
  print()
  print("Good luck!")
  print()
  print("You have " + str(money) + " coins, what would you like to play?")

#Print instruction list in console for player to reference
help()




#Write your game of chance functions here




#Define Coin Flip game function

def coin_flip(guess, bet):
  
  global money    #Allow update of global money variable to use as running total
  print("------ Coin Flip Game ------")
  
  if guess != "Heads" and guess != "Tails":    #Catch incorrect guess input
    print('Guess must be "Heads" or "Tails"!')
    print()

  elif bet < 1:    #Catch incorrect guess input
    print("Bet must not be less than 1!")
    print()

  elif bet > money:    #Ensure user can't bet more than they have
    print("You can't afford to bet " + str(bet) + " coins!")
    print("You only have " + str(money) + " coins.")
    print()

  else:
    face_num = random.randint(1,2)    #Generate random number and define "Heads" and "Tails"
    if face_num == 1:
      face_up = "Heads"
    else:
      face_up = "Tails"

    print("You guessed " + guess + ", with a bet of " + str(bet) + " coins...")

    if face_up == guess:    #Win
      print("The coin landed on... " + face_up + "!")
      print("Congratulations! You won " + str(bet) + " coins!")
      money += bet
      
    else:    #Loss
      print("The coin landed on... " + face_up + "!")
      print("Commiserations, you lost " + str(bet) + " coins. Better luck next time!")
      money += - bet
    
    print("You have " + str(money) + " coins!")    #Print remaining funds for next game
    if money < 0:
      print("You're in debt!")
      print()




#Define Cho-Han game function

def cho_han(guess, bet):
  
  global money
  print("------ Cho-Han Game ------")

  if guess != "Even" and guess != "Odd":    #Catch incorrect guess input
    print('Guess must be "Even" or "Odd"!')
    print()

  elif bet < 1:    #Catch incorrect bet input
    print("Bet must not be less than 1!")
    print()

  elif bet > money:    #Ensure user can't bet more than they have
    print("You can't afford to bet " + str(bet) + " coins!")
    print("You only have " + str(money) + " coins.")
    print()

  else:
    die1 = random.randint(1, 6)    #Generate die rolls and define variables
    die2 = random.randint(1, 6)
    die_total = die1 + die2

    if die_total % 2 == 0:    #Check if die total is even and define result
      result = "Even"
    else:
      result = "Odd"

    print("You guessed " + guess + " with a bet of " + str(bet) + " coins...")
    print("Die one landed on... " + str(die1) + ".")
    print("Die two landed on... " + str(die2) + ".")
    print("The dice total is " + str(die_total) + "...")
    print("It's " + result + "!")

    if guess == result:   #Win
      print("Congratulations! You won " + str(bet) + " coins!")
      money += bet
    
    else:    #Loss
      print("Commiserations, you lost " +str(bet) + " coins.")
      money += - bet

    print("You have " + str(money) + " coins!")    #Print remaining funds for next game
    if money < 0:
      print("You're in debt!")
      print()



#Define Card Pick game function

def card_pick(bet):
  
  global money
  print("------ Card Pick Game ------")
  #Assign a list for a complete deck of cards
  suit_diamonds = ["Diamonds", "Diamonds", "Diamonds", "Diamonds", "Diamonds", "Diamonds", "Diamonds", "Diamonds", "Diamonds", "Diamonds", "Diamonds", "Diamonds", "Diamonds"]
  suit_clubs = ["Clubs", "Clubs", "Clubs", "Clubs", "Clubs", "Clubs", "Clubs", "Clubs", "Clubs", "Clubs", "Clubs", "Clubs", "Clubs"]
  suit_hearts = ["Hearts", "Hearts", "Hearts", "Hearts", "Hearts", "Hearts", "Hearts", "Hearts", "Hearts", "Hearts", "Hearts", "Hearts", "Hearts"]
  suit_spades = ["Spades", "Spades", "Spades", "Spades", "Spades", "Spades", "Spades", "Spades", "Spades", "Spades", "Spades", "Spades", "Spades"]
  card_names = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
  card_values = list(range(1, 14))
  card_diamonds = list(zip(card_values, card_names, suit_diamonds))
  card_clubs = list(zip(card_values, card_names, suit_clubs))
  card_hearts = list(zip(card_values, card_names, suit_hearts))
  card_spades = list(zip(card_values, card_names, suit_spades))
  card_deck = card_diamonds + card_clubs + card_hearts + card_spades
  card_deck.sort()

  if bet < 1:    #Catch incorrect bet input
    print("Bet must not be less than 1!")
    print()

  elif bet > money:   #Ensure user can't bet more than they have
    print("You can't afford to bet " + str(bet) + " coins!")
    print("You only have " + str(money) + " coins.")
    print()

  else:
    print("You are betting " + str(bet) + " coins that your card will be higher.")
    print("Aces are low, pick a card, any card...")

    player_1_card = card_deck[random.randint(0,len(card_deck)-1)]    #User card picked from deck of 52 cards
    card_deck.remove(player_1_card)    #Remove picked card from deck
    player_2_card = card_deck[random.randint(0,len(card_deck)-1)]    #Player 2 card picked from deck of 51 cards

    print("You picked the " + player_1_card[1] + " of " + player_1_card[2] + "...")
    print("Player 2 picked the " + player_2_card[1] + " of " + player_2_card[2] + "...")

    if player_1_card[0] > player_2_card[0]:    #Win
      print("Your card is higher! You win " + str(bet) + " coins!")
      money += bet

    elif player_1_card[0] < player_2_card[0]:    #Lose
      print("Your card is lower, you lose " + str(bet) + " coins.")
      money += - bet

    elif player_1_card[0] == player_2_card[0]:    #Tie
      print("Your cards have equal value, it's a tie! No coins won or lost.")

    print("You have " + str(money) + " coins!")    #Print remaining funds for next game
    if money < 0:
      print("You're in debt!")
      print()




#Define Roulette game function
def roulette(guess, bet):
  
  global money
  print("------ Roulette Game ------")
  
  if bet < 1:    #Catch incorrect bet input
    print("Bet must not be less than 1!")
    print()

  elif bet > money:    #Ensure user can't bet more than they have
    print("You can't afford to bet " + str(bet) + " coins!")
    print("You only have " + str(money) + " coins.")
    print()

  elif (str(type(guess)) == "<class 'str'>" and guess != "Even" and guess != "Odd") or (str(type(guess)) == "<class 'int'>" and (guess < 1 or guess > 37)):
    print('Your guess can only be "Even", "Odd", a number between 0 and 36 inclusive, or to bet on 00 input 37.')
    print()    #Check that the guess input is valid

  else:
    number = random.randint(0,37)    #Generate number the ball lands on, 37 becomes 00

    if str(type(guess)) == "<class 'str'>":   #If guess is a string run this code
      print("You bet " + str(bet) + " coins on an " + guess + " number...")
      
      if number == 0:    #Betting on Even or Odd results in loss if ball lands on 0 or 00
        print("The ball landed on 0!")
        print("Commiserations, you lose " + str(bet) + " coins.")
        money += - bet

      elif number == 37:
        print("The ball landed on 00!")
        print("Commiserations, you lose " + str(bet) + " coins.")
        money += - bet

      print("The ball landed on " + str(number) + ".")
      
      if number % 2 == 0:    #Defining variable to store parity of the number
        parity = "Even"
        
      else:
        parity = "Odd"

      print("It's " + parity + "!")

      if guess == parity:    #Win
        print("Congratulations! You win " + str(bet) + " coins!")
        money += bet

      else:    #Lose
        print("Commiserations, you lose " + str(bet) + " coins.")
        money += - bet

    else:    #If guess is an integer run this code
      if guess == 37:
        guess = "00"    #Ensures 00 prints correctly
        
      if number == 37:
        result = "00"    #Ensures 00 prints correctly and matches guess if it is also 00
        
      else:
        result = number
      
      print("You bet " + str(bet) + " coins on number " + str(guess) + "...")
      print("The ball landed on " + str(result) + "!")

      if guess == result:
        print("Congratulations! You win " + str(bet * 36) + " coins!")
        money += bet * 36

      else:
        print("Commiserations, you lose " + str(bet * 36) + " coins.")
        money += - bet * 36

    print("You have " + str(money) + " coins!")    #Print remaining funds for next game
    if money < 0:
      print("You're in debt!")
      print()


'''

#Call your game of chance functions here
print()

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

print("------ Testing Roulette ------")
print()

print("Testing Roulette with invalid parity guess input")
roulette("boo", 15)

print("Testing Roulette with invalid numer guess")
roulette(100, 20)

print("Testing Roulette with invalid bet input")
roulette("Even", 1000)

print("Testing Roulette with valid parity guess input")
roulette("Even", 25)

print("Testing Roulette with valid number guess input")
roulette(25, 1)

print("Testing Roulette with 00 number guess input")
roulette(00, 1)

print("Testing Roulette with 0 number guess input")
roulette(0, 20)

'''
