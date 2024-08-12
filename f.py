import os
import random
import time


def roll(sides):
  result = random.randint(1,sides)
  return result
def roll_6_and_12():
  roll_6_sided_dice = roll(6)
  roll_8_sided_dice = roll(12)
  healthbar = (roll_6_sided_dice * roll_8_sided_dice) / 2 + 10
  return healthbar
def roll_6_and_8():
   roll_6_sided_dice = roll(6)
   roll_8_sided_dice = roll(12)
   healtbar = (roll_6_sided_dice * roll_8_sided_dice) / 2 + 12
   return healtbar

while True:
  print("Character builder")
  n = input("Name your legendary character:")
  f = input("What's your character's race?(Human, Elf, Wizard, Orc, Dwarf, Knight, Hero)")
  if f != "Human" and f != "Elf" and f != "Wizard" and f != "Orc" and f != "Dwarf" and f != "Knight" and f != "Hero":
      print("please choose a valid race")
      time.sleep(2)
      os.system("clear")
      continue
  print(n)
  print("Race:", f)
  print("Health:", roll_6_and_12())
  print("Strength:", roll_6_and_8())
  print("May your Character's name go down in legend...")
  f2 = input("Do you want to go another instance?")
  if f2 == "yes" or f2 =="Yes":
    continue
  elif f2 == "no" or f2 =="No":
    exit()
  else:
    print("please choose a correct option.")
    time.sleep(2)
    os.system("clear")
    exit()
    
    












