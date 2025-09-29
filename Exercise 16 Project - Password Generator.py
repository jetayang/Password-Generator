#Exercise 16 Project: Password Generator
import random
import string

pw_strength = str(input("Hello! How strong would you like your new password to be?"))

if pw_strength == "strong":
    pw_length = random.randint(9,12)
elif pw_strength == "medium":
    pw_length = random.randint(6,8)
elif pw_strength == "weak":
    pw_length = random.randint(4,5)

pw_list = []    

for x in range(pw_length):
    typeChance = random.randint(1,3)
    if typeChance == 1:
        randomLetter = random.choice(string.ascii_letters)
        pw_list.append(randomLetter)
    elif typeChance == 2:
        randNum = str(random.randint(0,9))
        pw_list.append(randNum)
    elif typeChance == 3:
        randChara = random.choice(string.punctuation)
        pw_list.append(randChara)
        
    
#Convert new password back to string
new_pw = ''.join(pw_list)

#random code = new_pw

#random code --> random str --> new_pw

#randint(start,stop) = returns a number between start and stop; inclusive
#shuffle() = takes a sequence (like a list) and returns in random order


print("Your new password is:", new_pw)
print("Remember to change your password regularly!")

