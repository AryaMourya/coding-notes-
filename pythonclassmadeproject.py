#TRANSLATOR 
'''Giraffe language
vowels=>"g"
------------------
dog=dgg
cat=cgt'''

def translate(phrase):
    translation=""
    for letter in phrase:
        if letter.lower() in "aioue":
            if letter.isupper():
             translation=translation+"G"
            else:
               translation=translation+"g"

        else:
            translation=translation + letter
    return translation

print(translate(input("Enter the phase:")))
'''to quit this translations type quit'''
print(input("do you want to quit ?"))

# Guessing Game:-
secret_word = "giraffe"
guess =""
guess_count=0
guess_limit=3
out_of_guesses=False
hint_taken=False
while guess !=secret_word and not out_of_guesses:
    if guess_limit > guess_count:
      guess = input("Enter guess: ")
      guess_count+=1
      if not hint_taken and guess !=secret_word:
         hint=input("DO you want hints? (Yes/No):")
         if hint=="Yes":
           print ("wild animal," \
                   "eat grass," \
                   "has long neck")
         elif hint=="No":
              print("OK!")
    else:
        out_of_guesses=True
       
if out_of_guesses==True:
 print("You lose!")
else:
  print("You Win!")