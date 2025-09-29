#Exercise 16 Project: Password Generator
import random
import string

pw_strength = str(input("Hello! How strong would you like your new password to be?"))

#Vary the potential pw length
if pw_strength == "strong":
    pw_length = random.randint(9,12)
elif pw_strength == "medium":
    pw_length = random.randint(6,8)
elif pw_strength == "weak":
    pw_length = random.randint(4,5)

#Creating random pw based on length
pw_list = [] 

for x in range(pw_length):
    randomItem = random.choice(string.ascii_letters + str(random.randint(0,9)) + string.punctuation)
    pw_list.append(randomItem)  
   
#Convert new password back to string
new_pw = ''.join(pw_list)


print("Your new password is:", new_pw)
print("Remember to change your password regularly!")

