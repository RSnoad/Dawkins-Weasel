import random
import string

# Variable storing the choices we need to generate (upper case letters and spaces)
randomCharacterChoices = string.ascii_uppercase + " "

# Function to generate a random string of length 28 with our specified character choices.
def startingString():
    startingstring = ''
    generatedstring = startingstring.join(random.choices(randomCharacterChoices, k=28))
    return generatedstring

# Function that creates a list of copies of the generated string with length 100.
def copiesString():
    return [startingString()] * 100

# Function that takes a string of length 28 and replaces characters with uppercase letters and spaces with a 5% chance.
def mutate(stringToMutate):
    for i in range(0, 28):
        if random.random() < 0.05:
            randomcharacter = ''.join(random.choice(randomCharacterChoices))
            stringToMutate = stringToMutate[:i] + randomcharacter + stringToMutate[i+1:]
    return stringToMutate


# Function that applies mutate function to list (could use map?)
def mutateList(listToMutate):
    for i in range(0, 100):
        listToMutate[i] = mutate(listToMutate[i])
    return listToMutate


# Function that mutates strings, checks their similarity to the target string, and mutates the most similar string
# until the target is reached (seems kind of hard to read, ask how to best clean up and test).
def evolution():
    startingList = copiesString()
    currentString = startingList[0]
    targetString = "METHINKS IT IS LIKE A WEASEL"
    potentialNewString = startingList[0]
    maxScore = 0

# While loop that looks at the current most similar string and terminates once we reach the target string.
    while currentString != targetString:
        startingList = mutateList(startingList)
        # For loop that loops over the list and determines the most suitable string by giving it a score (0-28)
        for listiterator in range(0, 100):
            currentScore = 0
            #For loop that loops over the string to determine the score of that individual string.
            for stringiterator in range(0, 28):
                if startingList[listiterator][stringiterator] == targetString[stringiterator]:
                    currentScore += 1
            if currentScore > maxScore:
                maxScore = currentScore
                potentialNewString = startingList[listiterator]
        if maxScore == 28:
            return potentialNewString
        else:
            startingList = [potentialNewString] * 100
