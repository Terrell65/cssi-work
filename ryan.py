
import random
import sys

SEA_LENGTH = 20
SHIP_LENGTH = 3
SHIP_COUNT = 3
HASHES_STRING = '#' * (SEA_LENGTH+2)
MAX_RETRIES = 1000


def isValidPlacement(sea, index):
    if index < 0 or index > SEA_LENGTH - SHIP_LENGTH:
        return False

    for i in range(SHIP_LENGTH):
        if (sea[index + i] == '*'):
            return False
    return True


def generateShipPlacements(sea_length, ship_length, ship_count):
  # FYI: lines 9-11 can be shortened to a 'list comprehension' via
  # array = [0 for i in range(sea_length)]
  # but we haven't covered this shorthand :)
  sea = []
  for i in range(sea_length):
    sea.append('0')

  # now that we have our sea, let's fill it with a ship
  count = 0
  retries = 0
  while count < SHIP_COUNT and retries < MAX_RETRIES:
      rand_index = random.randint(0, SEA_LENGTH - SHIP_LENGTH)
      if isValidPlacement(sea, rand_index):
          count += 1
          for i in range(SHIP_LENGTH):
              sea[rand_index + i] = '*'
      else:
          retries += 1
  return sea

def printSea(sea):
    print(HASHES_STRING)
    sys.stdout.write('#')
    for i in sea:
        sys.stdout.write(i)
    print '#'
    print(HASHES_STRING)
#
# '''
# Battleship is a game where you attempt to discover your opponent's ship locations in a hidden sea.
#
# The player has a matching 'sea' where they can track previous attempts to discover a ship.
#
# If a player successfully guesses the location of a ship, the opponent must tell them so that the player can use that information to guess future shots. This is what the player 'sea' board is for.
#
# Objective:
#  Continually ask the user to shoot a slot with a missile
#  If it is a hit, mark that index in 'player_sea' with a *
#  If it is a miss, mark that index in the 'player_sea' with a X so they know not to shoot there again!
#  End the game when all 'ships' have been 'sunk' (when all '*'s in the player_sea board map to the '*'s in the 'opponent_sea')
#  After each choice, you should reprint the player_sea array using printSea function defined above
#
#  STRETCH: Implement the computer AI to take its turn after each choice you make and see who wins.
# '''

########################################
#      YOUR CODE BELOW THIS LINE       #
########################################

# '''
# Q: What are your milestones?
# A: ...
#
# '''
# # this represents the 'hidden' board that you are attempting to shoot
# opponent_sea = generateShipPlacements(SEA_LENGTH, SHIP_LENGTH, SHIP_COUNT)
#
# # this represents the players board which tracks where you
# # have previously attempted to shoot
player_sea = ['-' for i in range(SEA_LENGTH)]
#
# printSea(opponent_sea)
import random
sea_length = 30
SHIP_LENGTH = 3
SHIP_COUNT = 3
HASHES_STRING = '#' * (sea_length+2)
MAX_RETRIES = 2000
opp_guess = generateShipPlacements(sea_length, SHIP_COUNT, SHIP_LENGTH)


def isValidPlacement(sea,index):
    if index <0 or index > sea_length - SHIP_LENGTH:
     return False
    for i in range(ship_length):
        if (sea[index + i] == '*'):
            return False
        return true

def generateShipPlacements(sea_length, SHIP_LENGTH, SHIP_COUNT):
    sea = []
    for i in range(sea_length):
        sea.append('0')
    count = 0
    retries = 0
    while count< SHIP_COUNT and retries < MAX_RETRIES:
        rand_index = random.randint(0,len(sea) - ship_length)
        if isValidPlacement(sea,rand_index):
            count += 1
            for i in range(ship_length):
                sea[rand_index + i] = '*'
            else:
                retries += 1
            return sea
def hit (rell):
    if opp_guess[int(rell)] == '*':
        print "hit"
        return True
    else:
        print " you missed!"
        return False
def bleek():
    for loop in range(0,sea_length-1):
        if opp_guess[loop] == '*':
            if player_sea[loop] != '*':
                print(' loser of round')
                return False
    return True

while True:
    guessString = raw_input("shoot")
    if guessString == "no":
        print('game over !')
        break
    kale = hit(guessString)
    if kale == True:
        player_sea[int(guessString)] = '*'
    else:
        player_sea[int(guessString)] = 'x'
    back = bleek()
    if back == True:
        print("restart")

    bleek()
    printSea(player_sea)
