"""
AUTHOR: Ashley Maynez
DATE: 09-04-2019
CLASS: CS 4500-001


PROGRAM DESCRIPTION:
This program is designed to implement the following game:
    1. Place a magnetic marker in circle #1, and put a check mark in circle #1. The circle where the marker resides is
        called the “current circle.”
    2. Randomly choose among the out arrows in the current circle. (If there is only one out arrow, that choice is
        trivial.) In this selection, all the out arrows should be equally likely to be picked.
    3. Move the marker to the circle pointed to by the out arrow. This becomes the new current circle.
    4. Put a check mark in the current circle.
    5. If all the circles have at least one check mark, stop the game. If not, go to step 2 and repeat.

This program reads in a number N, the number of circles used in this game.  It reads in a number K, the
number of arrows that will be drawn between two circles.  It reads in the following K lines, each line
consisting of 2 numbers: the first number is the backend of the arrow and the second number is the frontend of
the arrow.  The two numbers are separated by a white space character.

This program utilizes lists to iterate over the data from an input file.  It stores the arrows' backend numbers
in a list called 'positionStart'.  The frontend numbers are stored in a list called 'positionEnd'.  A variety of
operations are performed on the lists in order to gain the number of total checks, average check, and max check.
The results are outputted to a text-file called 'HW1maynezOutfile.txt'.
"""


import random
import collections

# Variable to store reference to output file.
outputFile = open("HW1maynezOutfile.txt", "w")

# Clears the file by writing a blank character to that file.
outputFile.write("")

# Closes previous output file after clearing.
outputFile.close()

# Reads in all lines from 'HW1infile.txt' and stores them in separate elements in list 'gameList'.
with open('HW1infile.txt') as f:
    gameList = []
    for line in f:
        line = line.split()
        if line:
            line = [int(i) for i in line]
            gameList.append(line)


# Pulls number of circles from 'gameList'.
N = gameList[0][0]

# Pulls number of text-lines of arrows from 'gameList'.
K = gameList[1][0]

# List of backend numbers.
positionStart = []

# List of frontend numbers.
positionEnd = []

# List of circles passed or "check-marked".
pastCircles = []

# Appends backend and frontend numbers to appropriate lists in the order they're given in the text-file.
counter = 2
while counter < len(gameList):
    positionStart.append(gameList[counter][0])
    positionEnd.append(gameList[counter][1])
    counter += 1

# Appends starting circle to passed circles list.
currentIndex = 0
pastCircles.append(positionStart[currentIndex])

# Current circle position.
current = positionStart[currentIndex]

# Initializing of list that will contain all unique numbers in backend numbers list.
uniqueList = []

# Traverses 'positionStart' list and appends all unique numbers to uniqueList.
for i in positionStart:
    if i not in uniqueList:
        uniqueList.append(i)

# Sorts 'uniqueList'.
uniqueList.sort()

# Gets rid of duplicate elements, if any.
uniqueList = list(set(uniqueList))

# Temporary list to store indexes of duplicate backend numbers.
tempList = []

# Counts arrows.
arrowCounter = 0

# Counts checks
checkCounter = [0] * N


# While the number of elements in 'uniqueList' do not equal the elements of pastCircles:
while uniqueList != pastCircles:

    # Current circle set to frontend number.
    current = positionEnd[currentIndex]

    # Sorts 'pastCircles' list.
    pastCircles.sort()

    # Resets 'tempList' to blank list.
    tempList = []

    # Traverse through every element in 'positionStart' list.
    for i in range(0, len(positionStart)):

        # If current frontend number equals a backend number:
        if current == positionStart[i]:

            # Append the value to 'tempList'
            tempList.append(i)

            # Selects random traversal from 'tempList'.
            a = random.choice(tempList)

            # Counts number of checks.
            checkCounter[positionStart[a] - 1] += 1

            # Append passed circle to 'pastCircles'.
            pastCircles.append(positionStart[a])

            # Counts arrows.
            arrowCounter += 1

            # Removes duplicates from 'pastCircles' list.
            pastCircles = list(set(pastCircles))

            # Sets 'currentIndex' to current index of for loop.
            currentIndex = i

# Variable to write to output file.
outputFile = open("HW1maynezOutfile.txt", "a")

# Outputs data to file in readable format.
outputFile.write("Number of circles that were used in this game: %d\n" % N)
outputFile.write("Number of arrows that were used in this game: %d\n" % K)
outputFile.write("Number of checks on all circles: %d\n" % arrowCounter)
outputFile.write("Average number of checks in a circle marked in this game: %d\n" % (sum(checkCounter) / len(checkCounter)))
outputFile.write("Maximum number of checks in a circle marked in this game: %d\n" % max(checkCounter))

# Closes output file.
outputFile.close()
