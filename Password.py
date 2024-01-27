import random

# print two of this list
mychar = ["le", "sa", "ce","be", "na", "ph","re", "ba", "by"]
mychar_one = ["lae", "bsa", "cee","bke", "nia", "phc","nre", "kba", "bdy"]
mychar_two = ["le", "ba", "dy","ke", "na", "ph","ne", "ka", "ny"]

# print two of this list
mynum_one = ['1','2','3','4','5','6','7','8','9']
mynum_two = ['1','2','3','4','5','6','7','8','9']

# print two of this list
mysom_one = ['.#','/$',')%','&*','!(','^?']
mysom_two = ['#','/',')','&','!','^']
# if user input == 9
res = (random.choice(mychar_one) + random.choice(mynum_one) +random.choice( mysom_one) + random.choice(mychar_two) + random.choice(mynum_two) )
# if user input == 8
res_one = (random.choice(mychar) + random.choice(mynum_one) +random.choice( mysom_one) + random.choice(mychar_two) + random.choice(mynum_two) )

# if user input == 6 or == 7
res_two = (random.choice(mychar_two) + random.choice(mynum_two) +random.choice( mysom_two) + random.choice(mynum_two) + random.choice(mychar_two) )

while True:
    char_of_num = int(input("How many characters do you want for your password: "))

    if 7 <= char_of_num <= 9:
        break  # Exit the loop if a valid number is entered
    else:
        print("Please enter a number between 7 and 9.")

if char_of_num == 7:

  print("Your password is: " + res_two)
elif char_of_num == 8:

  print("Your password is: " + res_one)
elif char_of_num == 9:

  print("Your password is: " + res)