import pygame


#Window class that draws the windows in the game to display various stats 
class Window:
    def __init__(self, width, height, posX, posY):
        super(Window, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((71,222,207))
        self.rect = self.surf.get_rect()
        self.posX = posX
        self.posY = posY
        self.rect.move_ip(posX, posY)
        self.font = pygame.font.Font('./Font/pixelated.ttf', int(width/8))
        self.width = width
        self.height = height

        self.rollsMade = []

    #Draws border around the windows
    def drawBorder(self, surface):
        thickness = int(0.02 * self.width)
        top = pygame.Surface((self.width + thickness, thickness))
        left = pygame.Surface((thickness, self.height + thickness))
        bottom = pygame.Surface((self.width + thickness, thickness))
        right = pygame.Surface((thickness, self.height + thickness))
        top.fill((138, 255, 243))
        left.fill((138, 255, 243))
        bottom.fill((1, 110, 95))
        right.fill((1, 110, 95))
        surface.blit(top, (self.posX - thickness/2, self.posY - thickness/2))
        surface.blit(left, (self.posX - thickness/2, self.posY - thickness/2))
        surface.blit(bottom, (self.rect.bottomleft[0] - thickness/2, self.rect.bottomleft[1] - thickness/2))
        surface.blit(right, (self.rect.topright[0] - thickness/2, self.posY - thickness/2))

    #Writes the gievn players name in the rectangle
    def addPlayerName(self, surface, player):
        surface.blit(
            self.font.render(player.getName(),
            True, (0, 0, 0)),
            (self.posX + (self.width/2) - int(self.width*0.3),
            self.posY+ self.height/2 - int(self.height*0.2)))

    #Writes the given players total points in the rectangle
    def addPlayerScore(self, surface, player):
        surface.blit(
            self.font.render(str(player.getScore()),
            True, (0, 0, 0)),
            (self.posX + (self.width/2) - int(self.width*0.3),
            self.posY+ self.height/2 - int(self.height*0.2)))

    #Writes all the players and their total points in the rectangle
    def addScoreboard(self, surface, players, playerCount):
        #for each player get name and score
        #for player count add blit
        for i, player in enumerate(players):
            surface.blit(self.font.render(player.getName() + ' : ' + str(player.getScore()),
            True, (0, 0, 0)),
            (self.posX + int(0.05*self.width), self.posY + i * (self.height/playerCount) + int(self.height*0.05)))
        

    #Writes dice picked in this round in the rectangle
    def addRoundTable(self, surface, points):
        #Show current round score
        surface.blit(self.font.render('Points: '+str(points),
            True, (0, 0, 0)),
            (self.posX + 0.1*self.width, self.posY + 0.04 * self.height))
        
        #Goes through the list of dice picked in this round
        for i, roll in enumerate(self.rollsMade):
            #Adds the dice to a string for display
            dieString = ''
            for die in roll:
                dieString = dieString + ' , ' + str(die)
            dieString = dieString[2:]
            surface.blit(self.font.render(dieString,
            True, (0, 0, 0)),
            (self.posX + 0.1*self.width, self.posY + 0.04 * self.height * i + 0.08 * self.height))

    #Adds a list of dice picked to a list of dice picked this round to be displayed
    def addRoll(self, dieList):
        roll =[]
        for value in dieList:
            roll.append(value.getValue())

        self.rollsMade.append(roll)

    #Reset the picked dice list
    def resetRolls(self):
        self.rollsMade = []


        


