#write your python code here
from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values


ranNums = [] #name your list and make sure it is empty!


# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for index in range(10): #for loop appends 10 numbers to your list, but make sure you name your variable
    ranNums.append(randint(0,50)) #this adds a random number between 1-50 to the list

random_number = randint(1, 50)

if random_number in ranNums:
    print("Number",random_number,"found in the list!")
else:
    print("Number",random_number,"not found in the list.")

print(ranNums) #print the list!