import random
#creat a hangman game  ["apple","chocklate","egg","meat","oregano","chiliflakes"]test cases of program
#greating
print("welcom ato hangman!!")
#wird list
word=["apple","chocklate","egg","meat","oregano","chiliflakes"]

#choose random word from list
secret_word= random.choice(word)
displey_word=[]
for each_letar in secret_word:
    displey_word+="_"
print (displey_word)
num=0
guess_left=5


while "_"  in displey_word:
  guess=input("guess a letter").lower()
  if guess  in secret_word:
      for position in range(len(secret_word)):
       if secret_word[position]==guess:
         displey_word[position]=guess
  elif guess not in secret_word:
    num+=1
    guess_left-=num
      
  if num>=5:displey_word="you loosae" 
  elif "_" not in displey_word: print ("you winn")

    #celse: displey_word="gameover"
#chake if letar is in word or not
  print(displey_word,"guess_left",guess_left)
    