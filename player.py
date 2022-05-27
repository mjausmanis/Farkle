
#Player class that is used to store the name and points
class Player:
    def __init__(self, name):
        self.__playerName = name
        self.__score = 0

    def getName(self):
        return self.__playerName

    def getScore(self):
        return self.__score

    def setScore(self, value):
        self.__score = value

    def updateScore(self, points):
        self.__score = self.__score + points

    def setName(self, name):
        self.__playerName = name