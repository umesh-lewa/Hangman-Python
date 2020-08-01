#Hangman Python Project

import random
#beginning of the loop
play_again = True
while play_again:
# My words as shown in the word bank
  WORD = ('hangman', 'chairs', 'backpack', 'bodywash', 'clothing', 'computer', 'python', 'program', 'glasses', 'sweatshirt' ,'sweatpants', 'mattress', 'friends', 'clocks', 'biology', 'algebra', 'suitcase', 'knives', 'ninjas', 'shampoo')
  word = random.choice(WORD)
  correct = word
  clue = word[0] + word[(len(word)-1):(len(word))]
  letter_guess = ''
  word_guess = ''
  store_letter = ''
  count = 0
  limit = 7
  name = input("\nWelcome! What is your name?\n")
  print('Welcome' , name , 'to the Game!')
  print('You have 7 attempts at guessing letters in a word!')
  print('After the 7 tries, you have to guess the word. Good luck' , name + '!')
  print('Here is your word bank: hangman, chairs, backpack, bodywash, clothing, computer, python, program, glasses, sweatshirt ,sweatpants, mattress, friends, clocks, biology, algebra, suitcase, knives, ninjas, shampoo')
  print('\n')
  while count < limit:
    letter_guess = input('Guess a letter: ')

    if letter_guess in word:
        print('yes!')
        store_letter += letter_guess
        count += 1

    if letter_guess not in word:
        print('no!')
        count += 1

    if count == 3:
        print('\n')
        clue_request = input('Would you like a clue?')
        if clue_request == 'yes':
            print('\n')
            print('CLUE: The first and last letter of the word is: ', clue)
        if clue_request == 'no':
            print('You\'re very brave!')

  print('\n')
  print('Now its time to guess. You have guessed',len(store_letter),'letters correctly.')
  print('These letters are: ', store_letter)

  word_guess = input('Guess the whole word: ')
  while word_guess:
    if word_guess.lower() == correct:
        print('You got it! Your prize....Nothing')
        break

    elif word_guess.lower() != correct:
        print('Almost had it! The answer was,', word)
        break 
  print("\nWould you like to play again? Type y or yes to play again.")
  response = input("> ").lower()
  if response not in ("yes", "y"):
      play_again = False
#loop end
if __name__ == "__main__":
  main()