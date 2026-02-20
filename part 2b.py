#write your python code here
from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values


ranNums = [] #list name 


# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for index in range(10): #for loop appends 10 numbers to your list, but make sure you name your variable
    ranNums.append(randint(0,50)) #this adds a random number between 1-50 to the list


random_number = randint(1, 20) #number to find

comparisons = 0  # Initialize the counter for comparisons
found = False  # if found


for num in ranNums:  # Name your variable in the for loop
    comparisons += 1  # Increment the counter for each comparison
    if num == random_number:
        found = True  # Set found to True if the number is in the list
        break  # Exit the loop early if the number is found

print("the list is",ranNums) #print the list
print("number of comparisons to find", random_number,"was",comparisons) #print the number of comparisons
if random_number in ranNums:
    print("Number",random_number,"found in the list!")
else:
    print("Number",random_number,"not found in the list.")