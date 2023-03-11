from random import randint

is_wrong = True

print("Welcome to Python Casino!")
pc_choice = randint(1, 50)

while is_wrong:
  user_choice = int(input("Choose number: "))
  if pc_choice == user_choice:
    print("You Won!")
    is_correct = False
  elif pc_choice > user_choice:
    print("Lower!")
  else:
    print("Higher!")