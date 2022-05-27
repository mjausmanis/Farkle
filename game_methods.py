#File that contains methods for game logic 

#Checks if the given dice contain a combination by calling the other methods
def hasCombination(diceList):
    values = []
    for die in diceList:
        values.append(die.getValue())

    if checkForOneOrFive(values):
        return True
    elif checkForOfAKind(values):
        return True
    elif checkForPairs(values):
        return True
    elif checkForStraights(values):
        return True
    else:
        return False

#Checks for 1s or 5s
def checkForOneOrFive(values):
    if values.__contains__(1) or values.__contains__(5):
        return True
    else:
        return False

#Checks if there are three or more of kind
def checkForOfAKind(values):
    ones = values.count(1)
    twos = values.count(2)
    threes = values.count(3)
    fours = values.count(4)
    fives = values.count(5)
    sixes = values.count(6)
    if ones >= 3:
        return True
    elif twos >= 3:
        return True
    elif threes >= 3:
        return True
    elif fours >= 3:
        return True
    elif fives >= 3:
        return True
    elif sixes >= 3:
        return True
    else:
        return False

#Checks if there are 3 pairs
def checkForPairs(values):
    ones = values.count(1)
    twos = values.count(2)
    threes = values.count(3)
    fours = values.count(4)
    fives = values.count(5)
    sixes = values.count(6)
    countList = []
    countList.append(ones)
    countList.append(twos)
    countList.append(threes)
    countList.append(fours)
    countList.append(fives)
    countList.append(sixes)
    #Checks if there are 3 values that appear twice
    if countList.count(2) == 3:
        return True
    else:
        return False

#Checks if there is a straight
def checkForStraights(values):
    if values.__contains__(1) and values.__contains__(2) and values.__contains__(3) and values.__contains__(4) and values.__contains__(5):
        return True
    elif values.__contains__(2) and values.__contains__(3) and values.__contains__(4) and values.__contains__(5) and values.__contains__(6):
        return True
    else:
        return False

#Counts the score gotten from the given dice List.
def countScore(diceList):
    #Gets the values of the dice
    values = []
    for die in diceList:
        values.append(die.getValue())
    points = 0
    #Counts points from straights (minus 1s and 5s that will be added later)
    if checkForStraights(values):
        if values.__contains__(1) and values.__contains__(2) and values.__contains__(3) and values.__contains__(4) and values.__contains__(5) and values.__contains__(6):
            points += 1350
        elif values.__contains__(1) and values.__contains__(2) and values.__contains__(3) and values.__contains__(4) and values.__contains__(5):
            points += 350
        elif values.__contains__(2) and values.__contains__(3) and values.__contains__(4) and values.__contains__(5) and values.__contains__(6):
            points += 700
        
    #Counts points from 3 pairs
    if checkForPairs(values):
        points += 1000
        if values.__contains__(1):
            points -= 200
        if values.__contains__(5):
            points -= 100

    #Counts points from 3 or more of a kind
    if checkForOfAKind(values):
        #Gets the count of all dice values and puts them in a list
        ones = values.count(1)
        twos = values.count(2)
        threes = values.count(3)
        fours = values.count(4)
        fives = values.count(5)
        sixes = values.count(6)
        countList = [ones, twos, threes, fours, fives, sixes]
        #Point variable used to calculate points from of a kind combinations
        localPoints = 0
        #Goes through the list of counts. 
        for i, count in enumerate(countList):
            #Point variable for this specific value
            thisPoints = 0
            #Checks if there is 3 or more of a kind, if so times the value of the 
            #dice with a hundred to get the 3 of a kind point value.
            #Ones have a 1000 for 3 of a kind, so it needs to be separate
            if i != 0 and count >= 3:
                thisPoints = (i + 1) * 100
            elif count >= 3:
                thisPoints = 1000
            #Checks for mroe of a kind, then times it with the corresponding value.
            if count == 4:
                thisPoints = thisPoints * 2
            elif count == 5:
                thisPoints = thisPoints * 4
            elif count == 6:
                thisPoints = thisPoints * 8
            #If its a 1 or 5 and scores, takes off the value of individual dice that gets added later
            if i == 0 and count >= 3:
                thisPoints -= count * 100
            if i == 4 and count >= 3:
                thisPoints -= count * 50
            localPoints += thisPoints
        points += localPoints

    #Counts the values from 1s and 5s
    if checkForOneOrFive(values):
        ones = values.count(1)
        fives = values.count(5)

        points += ones * 100
        points += fives * 50

    return points

#Check if all the dice selected are able to score.
def verifySelection(diceList):
    values = []
    for die in diceList:
        values.append(die.getValue())

    ones = values.count(1)
    twos = values.count(2)
    threes = values.count(3)
    fours = values.count(4)
    fives = values.count(5)
    sixes = values.count(6)
    countList = [ones, twos, threes, fours, fives, sixes]
    #If there are 3 pairs, only the pairs can be selected - no false dice
    if checkForPairs(values):
        return True
    #If there are no straights, the selected dice have to be 3 or more of a kind, or 1 or 5
    if checkForStraights(values) == False:
        for i, count in enumerate(countList):
            #if not 1 or 5
            if i != 0 and i != 4:
                #if there is only 1 or 2 dice fail verification
                if count == 1 or count == 2:
                    return False
    #If there is a straight, then check that there isn't another dice added that isn't 1 or 5
    if checkForStraights(values):
        for i, count in enumerate(countList):
            if i != 0 and i != 4:
                if count == 2:
                    return False
    #If the ifs all failed, then the list should be correct
    return True


