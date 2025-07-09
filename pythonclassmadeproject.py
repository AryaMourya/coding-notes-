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