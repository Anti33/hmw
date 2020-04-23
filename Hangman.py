import time

display = []

word_from_user = input("Enter word to use: ")
split_word = list(word_from_user)
amount = len(word_from_user)
time.sleep(0.5)
print("Your word has "+str(amount)+" letters")
print()
time.sleep(1)
display.extend(split_word)

print("_ " * amount)
#print the words the get correct
correct_counter = 0
incorrect_counter = 0
while correct_counter < 3 and incorrect_counter < 3:
  for i in range(amount):
    guess = input("Guess a letter or word: ")
    if split_word[i] in guess:
      display[i] = guess
      print("Correct")
      correct_counter += 1
    else:
      print("Incorrect letter, try again")
      incorrect_counter += 1

if correct_counter > incorrect_counter:
  print("You have guessed the correct word")
elif incorrect_counter > correct_counter:
  print("You have lost, thanks for playing!")
