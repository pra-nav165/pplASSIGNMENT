import random
#data types
#1string(str)
#print(type("hi their")) 

#2intiger
#3float
#boolean
#true or false
'''marks=int(input("enter your marks"))
if marks>=90:
    print("A Grade")
elif 90>marks>=80:
    print("B Grade")
elif 80>marks>=70:
    print("c Grade")
elif 70>marks>=60:
    print("D Grade")
else:print("F grade")'''

#function
'''def greating(name):
    print("hello",name)
greating("pranav")'''
#project1
#creat a hangman game 
#greating
print("welcom ato hangman!!")
#wird list
word=["apple","chocklate","egg","meat","oregano","chiliflakes"]

#choose random word from list
secret_word=random.choice(word)
displey_word=[]
for each_letar in secret_word:
    displey_word+="_"
print (displey_word)
num=0
guess_left=5


while "_"  in displey_word:
  guess=input("guess a letter").lower()
  len(guess)==1
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
    