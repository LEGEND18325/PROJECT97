import random
print('The Number Guessing Game')
number = random.randint(1,9)
chances=0

print('Guess The Number 1 and 9')

while chances < 5:

   guess=int(input('Enter Your Guess: '))
  
   if (guess==number):
      print("WOW! You Won The game")
      break
   elif (guess>number):
      print('Your Number Is Too High, Try Guessing Lower Than ',guess)
   else:
      print('Your Number Is Too Low, Try Guessing Higher Than ',guess)

      chances=chances+1


if not chances < 5:
    print('Sorry! You Lost The Game And The Number Is ',number)

if (guess>9):
      print("NO! You Should Only Give Numbers Between 1 And 9")

if (guess<1):
      print("NO! You Should Only Give Numbers Between 1 And 9")