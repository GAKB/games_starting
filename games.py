import random

money = 100

#Write your game of chance functions here




#Define the Coin Flip game

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

    elif face_num == 2:
      face_up = "Tails"

    print("You guessed " + guess + ", with a bet of " + str(bet) + " coins...")

    if face_up == guess:
      print("The coin landed on... " + face_up + "!")
      print("Congratulations! You won " + str(bet) + " coins!")
      money += bet
      print("You now have " + str(money) + " coins!")
      print()

    else:
      print("The coin landed on... " + face_up + "!")
      print("Commiserations, you lost " + str(bet) + " coins. Better luck next time!")
      money += - bet
      print("You now have " + str(money) + " coins left.")
      print()


#Test coin flip using valid and invalid inputs
print()

print("Testing coin flip false guess input")
coin_flip("heeds", 3)

print("Testing coin flip false bet input")
coin_flip("Heads", 120)

print("Testing coin flip valid input")
coin_flip("Heads", 30)




#Define Cho-Han game







#Call your game of chance functions here














































