import random, string

def startingString():
    startingstring = ''
    generatedstring = startingstring.join(random.choices(string.ascii_uppercase + " ", k = 28))
    return generatedstring

def copiesString():
    return [startingString()] * 100

# def mutate():



print(startingString())

print(copiesString())
