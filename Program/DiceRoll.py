# Collection of functions to simulate a dice roll

import random

# function to roll a single dice of a certain number of sides
def rollDice(sides):
  return randrange(1, sides + 1)

# Function to roll attributes for a character 
# Uses "standard" method (4d6, drop lowest)
def standardAS():
  for ability in range (1, 7):
    for rolls in range (1, 5):
      seperateRolls.append(rollDice(6))
    lowestRoll = 6
    for roll in seperateRolls:
      if roll < lowestRoll:
        lowestRoll = roll
    score = 0
    seenLowRoll = False
    for roll in seperateRolls:
      if roll == lowestRoll and !seenLowRoll:
        seenLowRoll = True
      else:
        score += roll
    abilityScores.append(score)
  return abilityScores
 

# Function to roll attributes for a character
# Uses "classic" method (3d6, no dropping)
def classicAS():
  for ability in range (1,7):
    score = 0
    for rolls in range (1,4):
      score += rollDice(6)
    abilityScores.append(score)
  return abilityScores
      
    
    
    
    
