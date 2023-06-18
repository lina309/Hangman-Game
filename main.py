import random
import hman_art as art
import hman_words as words
from replit import clear

print("Welcome to")
print(art.logo)
wrd = words.word_list

character_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
                 'u','v','w','x','y','z']

chosen_word = random.choice(wrd)
chosen_word_len = len(chosen_word)

print("_ " * chosen_word_len)
user_word = "_" * chosen_word_len
# print(chosen_word)

#Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
def indexes2(my_list, desired_element):
    for index, element in enumerate(my_list):
        if element == desired_element:
            yield index

chosen_word = list(chosen_word)
count_lives = 0
indexes=[]
user_word = list(user_word)

while count_lives!=7 and user_word!=chosen_word:
  guess = input("\nGuess a letter:").lower()
  clear()
  if guess not in character_list:
    print(f"You have already guessed letter: {guess}")
    continue
  else:
    character_list.remove(guess)
    if guess in chosen_word:
      print("You are on the right track!\n")
      for i in indexes2(chosen_word, guess):
        user_word[i] = guess
      print(" ".join(user_word))
    else:
      print()
      print(" ".join(user_word))
      print(art.stages[count_lives])
      print(f"Oops! The letter {guess} is not present in the word.")
      count_lives+=1

if count_lives==7:
  print("You lose! Hangman is dead")
else:
  print("You win!!! Hooray!")
    
