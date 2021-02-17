# Guided Exploration No. 3
# Abe Busschau
# This code will help us randomize things later.
import random
# This code will work as the accumalater pattern and help us make a list.
possible_names = []
# This will store all the names generated. It is making and opening a file.
outputFile = open('rap-names-output.txt', 'w')
# This is saying that the things in this file, do with dataFile and open the file.
with open('rap-names.txt', 'r') as dataFile:
    # This a definate loop and it is saying for the things in the dataFile variable, do this.
    for name in dataFile:
        # This is adding the generated names to the list possible_names.
        possible_names.append(name.rstrip())
# This is asking the user how many names they want to make.
count = int(input('How many rap names would you like to create? '))
# Now the code is asking the user more specific pieces about the name.
parts = int(input('How many parts should the name contain? '))
# This is going to loop the procesess as many times as the user said to.
for i in range(count):
    # This again is using the accumalator pattern to make a list.
    name_parts = []
    # This is making a loop for how many parts the name has as user said.
    for j in range(parts):
        # This is appending to the list and randomizing the names form the other file.
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])
        # This is going to take the name written and add it to the file and join new ones.
        outputFile.write(f"{' '.join(name_parts)}\n")
        # This is also going to print the names added.
        print(f"{' '.join(name_parts)}")
# This will close the whole file that we made.
outputFile.close()
