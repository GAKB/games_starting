import random

money = 100

#Write your game of chance functions here




#Define Coin Flip game function

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




#Define Cho-Han game function

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




#Define Card Pick game function

def card_pick(bet):
  global money
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

    player_1_card = card_deck[random.randint(0,len(card_deck)-1)]
    card_deck.remove(player_1_card)
    player_2_card = card_deck[random.randint(0,len(card_deck)-1)]

    print("You picked the " + player_1_card[1] + " of " + player_1_card[2] + "...")
    print("Player 2 picked the " + player_2_card[1] + " of " + player_2_card[2] + "...")

    if player_1_card[0] > player_2_card[0]:
      print("Your card is higher! You win " + str(bet) + " coins!")
      money += bet

    elif player_1_card[0] < player_2_card[0]:
      print("Your card is lower, you lose " + str(bet) + " coins.")
      money += - bet

    elif player_1_card[0] == player_2_card[0]:
      print("Your cards have equal value, it's a tie! No coins won or lost.")

    print("You have " + str(money) + " coins!")
    print()





#Define Roulette game function
def roulette(guess, bet):
  global money

  if bet < 1:
    print("Bet must not be less than 1!")
    print()

  elif bet > money:
    print("You can't afford to bet " + str(bet) + " coins!")
    print("You only have " + str(money) + " coins.")
    print()

  elif (str(type(guess)) == "<class 'str'>" and guess != "Even" and guess != "Odd") or (str(type(guess)) == "<class 'int'>" and guess != 00 and (guess < 1 or guess > 36)):
    print('Your guess can only be "Even", "Odd", or a number between 0 and 36 inclusive, or 00.')
    print()

  else:  #Game code goes here, incorrect inputs filtered above
    number = random.randint(0,37)

    if str(type(guess)) == "<class 'str'>":
      print("You bet " + str(bet) + " coins on an " + guess + " number...")
      if number == 0:
        print("The ball landed on 0!")
        print("Commiserations, you lose " + str(bet) + " coins.")
        money += - bet

      elif number == 37:
        print("The ball landed on 00!")
        print("Commiserations, you lose " + str(bet) + " coins.")
        money += - bet

      print("The ball landed on " + str(number) + ".")
      
      if number % 2 == 0:
        parity = "Even"
        
      else:
        parity = "Odd"

      print("It's " + parity + "!")

      if guess == parity:
        print("Congratulations! You win " + str(bet) + " coins!")
        money += bet

      else:
        print("Commiserations, you lose " + str(bet) + " coins.")
        money += - bet

    else: #Try to get it working with a guess of 00
      if number == 37:
        result = "00"
        guess = "00"
      else:
        result = number
      
      print("You bet " + str(bet) + " coins on number " + str(guess) + "...")
      print("The ball landed on " + str(result) + "!")

      if guess == result:
        print("Congratulations! You win " + str(bet * 36) + " coins!")
        money += bet * 36

      else:
        print("Commiserations, you lose " + str(bet) + " coins.")
        money += - bet

    print("You have " + str(money) + " coins!")
    print()






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
roulette(25, 5)

print("Testing Roulette with 00 number guess input")
roulette(00, 2)

print("Testing Roulette with 0 number guess input")
roulette(0, 1)
