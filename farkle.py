import pygame, button, player, die, game_methods, window, input, popUp
from pygame.locals import *
pygame.init()

#Game screen resolution
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
#Create the values that will be used to make the game a square, regardless of resolution
if SCREEN_WIDTH > SCREEN_HEIGHT:
    GAMESQUARE_SIDE = SCREEN_HEIGHT
    GAMESQUARE_LEFT = (SCREEN_WIDTH - GAMESQUARE_SIDE)/2
    GAMESQUARE_TOP = 0
else:
    GAMESQUARE_SIDE = SCREEN_WIDTH
    GAMESQUARE_TOP = (SCREEN_HEIGHT - GAMESQUARE_SIDE)/2
    GAMESQUARE_LEFT = 0


#Draws screen and sets window title
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Farkle')

#Loads images that are used in the game
rollButtonImg = pygame.image.load('./Images/roll_button.png')
endTurnImg = pygame.image.load('./Images/end_turn_button.png')
rematchButtonImg = pygame.image.load('./Images/rematchButton.png')
newGameImg = pygame.image.load('./Images/new_game_button.png')
scoreGoalImg = pygame.image.load('./Images/score_goal.png')
fiveKGoalImg = pygame.image.load('./Images/5000.png')
fiveKGoalClickedImg = pygame.image.load('./Images/5000_clicked.png')
tenKGoalImg = pygame.image.load('./Images/10000.png')
tenKGoalClickedImg = pygame.image.load('./Images/10000_clicked.png')
twentyKGoalImg = pygame.image.load('./Images/20000.png')
twentyKGoalClickedImg = pygame.image.load('./Images/20000_clicked.png')
playersCountImg = pygame.image.load('./Images/playersButton.png')
twoPlayerImg = pygame.image.load('./Images/2_player_select.png')
twoPlayerClickedImg = pygame.image.load('./Images/2_player_select_clicked.png')
threePlayerImg = pygame.image.load('./Images/3_player_select.png')
threePlayerClickedImg = pygame.image.load('./Images/3_player_select_clicked.png')
fourPlayerImg = pygame.image.load('./Images/4_player_select.png')
fourPlayerClickedImg = pygame.image.load('./Images/4_player_select_clicked.png')
player1Img = pygame.image.load('./Images/player_1.png')
player2Img = pygame.image.load('./Images/player_2.png')
player3Img = pygame.image.load('./Images/player_3.png')
player4Img = pygame.image.load('./Images/player_4.png')
startGameImg = pygame.image.load('./Images/start_game.png')
titleImg = pygame.image.load('./Images/farkle_title.png')


#Initializes regions where some values are shown when playing the game
currentPlayerRect = window.Window(int((GAMESQUARE_SIDE-0.08*GAMESQUARE_SIDE)/3), int((GAMESQUARE_SIDE-0.1*GAMESQUARE_SIDE)/4), int(0.02*GAMESQUARE_SIDE + GAMESQUARE_LEFT), int(0.02*GAMESQUARE_SIDE + GAMESQUARE_TOP))
totalScoreRect = window.Window(currentPlayerRect.rect.width, currentPlayerRect.rect.height, int((currentPlayerRect.rect.topright[0] + 0.02*GAMESQUARE_SIDE)), int(0.02*GAMESQUARE_SIDE + GAMESQUARE_TOP))
roundScoreRect = window.Window(currentPlayerRect.rect.width, int((GAMESQUARE_SIDE-0.04*GAMESQUARE_SIDE)), int((totalScoreRect.rect.topright[0] + 0.02*GAMESQUARE_SIDE)), int(0.02*GAMESQUARE_SIDE + GAMESQUARE_TOP))


#Initializes the six dice used for the game
die1 = die.Die(int(((GAMESQUARE_SIDE-0.1*GAMESQUARE_SIDE)-totalScoreRect.rect.width)/3), int(((GAMESQUARE_SIDE-0.1*GAMESQUARE_SIDE)-(GAMESQUARE_SIDE-0.08*GAMESQUARE_SIDE)/3)/3), int((0.02*GAMESQUARE_SIDE) + GAMESQUARE_LEFT), int((currentPlayerRect.rect.bottomleft[1] + 0.02*GAMESQUARE_SIDE)))
die2 = die.Die(die1.rect.width, die1.rect.height, int((die1.rect.topright[0] + 0.02*GAMESQUARE_SIDE)), int((currentPlayerRect.rect.bottomleft[1] + 0.02*GAMESQUARE_SIDE)))
die3 = die.Die(die1.rect.width, die1.rect.height, int((die2.rect.topright[0] + 0.02*GAMESQUARE_SIDE)), int((currentPlayerRect.rect.bottomleft[1] + 0.02*GAMESQUARE_SIDE)))
die4 = die.Die(die1.rect.width, die1.rect.height, int((0.02*GAMESQUARE_SIDE) + GAMESQUARE_LEFT), int((die1.rect.bottomleft[1] + 0.02*GAMESQUARE_SIDE)))
die5 = die.Die(die1.rect.width, die1.rect.height, int((die4.rect.topright[0] + 0.02*GAMESQUARE_SIDE)), int((die1.rect.bottomleft[1] + 0.02*GAMESQUARE_SIDE)))
die6 = die.Die(die1.rect.width, die1.rect.height, int((die5.rect.topright[0] + 0.02*GAMESQUARE_SIDE)), int((die1.rect.bottomleft[1] + 0.02*GAMESQUARE_SIDE)))

dieList = [die1, die2, die3, die4, die5, die6]
scoreBoard = window.Window(currentPlayerRect.rect.width, int((GAMESQUARE_SIDE-0.1*GAMESQUARE_SIDE)-currentPlayerRect.rect.height-die1.rect.height*2), int((0.02*GAMESQUARE_SIDE) + GAMESQUARE_LEFT), int((die4.rect.bottomleft[1] + 0.02*GAMESQUARE_SIDE)))
gameObjects = [currentPlayerRect, totalScoreRect, roundScoreRect, scoreBoard]

#Initializes buttons 
rollButton = button.Button(currentPlayerRect.rect.width, int((scoreBoard.rect.height-0.02*GAMESQUARE_SIDE)/2), int((scoreBoard.rect.topright[0] + 0.02*GAMESQUARE_SIDE)), int((die4.rect.bottomleft[1] + 0.02*GAMESQUARE_SIDE)), rollButtonImg, rollButtonImg)
endTurnButton = button.Button(currentPlayerRect.rect.width, int((scoreBoard.rect.height-0.02*GAMESQUARE_SIDE)/2), int((scoreBoard.rect.topright[0] + 0.02*GAMESQUARE_SIDE)), int((rollButton.rect.bottomleft[1] + 0.02*GAMESQUARE_SIDE)), endTurnImg, endTurnImg)
winScreen = popUp.PopUp(int(0.7*GAMESQUARE_SIDE), int(0.8*GAMESQUARE_SIDE), int(GAMESQUARE_LEFT+0.15*GAMESQUARE_SIDE), int(GAMESQUARE_TOP+0.1*GAMESQUARE_SIDE))
rematchButton = button.Button(rollButton.rect.width, rollButton.rect.height, winScreen.rect.bottomleft[0] + 0.05*winScreen.rect.width, winScreen.rect.bottomleft[1] - 0.3 * winScreen.rect.height, rematchButtonImg, rematchButtonImg)
newGameButon = button.Button(rollButton.rect.width, rollButton.rect.height, rematchButton.rect.topright[0] + 0.05*winScreen.rect.width, winScreen.rect.bottomleft[1] - 0.3 * winScreen.rect.height, newGameImg, newGameImg)
mainMenuNewGameButon = button.Button(rollButton.rect.width, rollButton.rect.height, GAMESQUARE_LEFT +  GAMESQUARE_SIDE/2-rollButton.rect.width/2, GAMESQUARE_TOP + GAMESQUARE_SIDE - GAMESQUARE_SIDE/6-rollButton.rect.height/2, newGameImg, newGameImg)

scoreGoalObject = button.Button(int((GAMESQUARE_SIDE-0.16*GAMESQUARE_SIDE)/4), int(((GAMESQUARE_SIDE-0.02*GAMESQUARE_SIDE)/4))/2.5, GAMESQUARE_LEFT+GAMESQUARE_SIDE*0.05, GAMESQUARE_TOP+GAMESQUARE_SIDE*0.05, scoreGoalImg, scoreGoalImg)
fiveKGoalObject = button.Button(int((GAMESQUARE_SIDE-0.16*GAMESQUARE_SIDE)/4), int(((GAMESQUARE_SIDE-0.02*GAMESQUARE_SIDE)/4))/2.5, scoreGoalObject.rect.topright[0]+0.02*GAMESQUARE_SIDE, scoreGoalObject.rect.topright[1], fiveKGoalImg, fiveKGoalClickedImg)
tenKGoalObject = button.Button(int((GAMESQUARE_SIDE-0.16*GAMESQUARE_SIDE)/4), int(((GAMESQUARE_SIDE-0.02*GAMESQUARE_SIDE)/4))/2.5, fiveKGoalObject.rect.topright[0]+0.02*GAMESQUARE_SIDE, scoreGoalObject.rect.topright[1], tenKGoalImg, tenKGoalClickedImg)
twentyKGoalObject = button.Button(int((GAMESQUARE_SIDE-0.16*GAMESQUARE_SIDE)/4), int(((GAMESQUARE_SIDE-0.02*GAMESQUARE_SIDE)/4))/2.5, tenKGoalObject.rect.topright[0]+0.02*GAMESQUARE_SIDE, scoreGoalObject.rect.topright[1], twentyKGoalImg, twentyKGoalClickedImg)

scoreGoalList = [fiveKGoalObject, tenKGoalObject, twentyKGoalObject]

playerCountObject = button.Button(int((GAMESQUARE_SIDE-0.16*GAMESQUARE_SIDE)/4), int(((GAMESQUARE_SIDE-0.02*GAMESQUARE_SIDE)/4)/2.5), GAMESQUARE_LEFT+GAMESQUARE_SIDE*0.05, scoreGoalObject.rect.bottomleft[1]+GAMESQUARE_SIDE*0.05, playersCountImg, playersCountImg)
twoPlayerCountObject = button.Button(int(playerCountObject.rect.height), int(playerCountObject.rect.height), int(fiveKGoalObject.rect.topleft[0] + (fiveKGoalObject.rect.width-playerCountObject.rect.height)/2), int(playerCountObject.rect.topleft[1]), twoPlayerImg, twoPlayerClickedImg)
threePlayerCountObject = button.Button(twoPlayerCountObject.rect.width, twoPlayerCountObject.rect.width, int(tenKGoalObject.rect.topleft[0] + (tenKGoalObject.rect.width-twoPlayerCountObject.rect.width)/2), int(playerCountObject.rect.topleft[1]), threePlayerImg, threePlayerClickedImg)
fourPlayerCountObject = button.Button(twoPlayerCountObject.rect.width, twoPlayerCountObject.rect.width, int(twentyKGoalObject.rect.topleft[0] + (twentyKGoalObject.rect.width-twoPlayerCountObject.rect.width)/2), int(playerCountObject.rect.topleft[1]), fourPlayerImg, fourPlayerClickedImg)

playerCountList = [twoPlayerCountObject, threePlayerCountObject, fourPlayerCountObject]

player1Object = button.Button(playerCountObject.rect.width, playerCountObject.rect.height, GAMESQUARE_LEFT+GAMESQUARE_SIDE*0.05, playerCountObject.rect.bottomleft[1]+GAMESQUARE_SIDE*0.05, player1Img, player1Img)
player2Object = button.Button(playerCountObject.rect.width, playerCountObject.rect.height, GAMESQUARE_LEFT+GAMESQUARE_SIDE*0.05, player1Object.rect.bottomleft[1]+GAMESQUARE_SIDE*0.03, player2Img, player2Img)
player3Object = button.Button(playerCountObject.rect.width, playerCountObject.rect.height, GAMESQUARE_LEFT+GAMESQUARE_SIDE*0.05, player2Object.rect.bottomleft[1]+GAMESQUARE_SIDE*0.03, player3Img, player3Img)
player4Object = button.Button(playerCountObject.rect.width, playerCountObject.rect.height, GAMESQUARE_LEFT+GAMESQUARE_SIDE*0.05, player3Object.rect.bottomleft[1]+GAMESQUARE_SIDE*0.03, player4Img, player4Img)

#Initializes input boxes for setup screen
player1Input = input.InputBox(int(GAMESQUARE_SIDE-player1Object.rect.width-0.12*GAMESQUARE_SIDE), player1Object.rect.height, int(player1Object.rect.topright[0]+0.02*GAMESQUARE_SIDE), player1Object.rect.topright[1], 'Player 1')
player2Input = input.InputBox(player1Input.rect.width, player1Input.rect.height, player2Object.rect.topright[0]+0.02*GAMESQUARE_SIDE, player2Object.rect.topright[1], 'Player 2')
player3Input = input.InputBox(player1Input.rect.width, player1Input.rect.height, player3Object.rect.topright[0]+0.02*GAMESQUARE_SIDE, player3Object.rect.topright[1], 'Player 3')
player4Input = input.InputBox(player1Input.rect.width, player1Input.rect.height, player4Object.rect.topright[0]+0.02*GAMESQUARE_SIDE, player4Object.rect.topright[1], 'Player 4')
startGameButton = button.Button(fiveKGoalObject.rect.width, fiveKGoalObject.rect.height, GAMESQUARE_SIDE - fiveKGoalObject.rect.width - 0.05*GAMESQUARE_SIDE, player4Input.rect.bottomleft[1] + 0.03*GAMESQUARE_SIDE, startGameImg, startGameImg)

inputboxes = [player1Input, player2Input, player3Input, player4Input]

inputLines = [player1Object, player2Object, player3Object, player4Object]

farklePopUp = popUp.PopUp(GAMESQUARE_SIDE * 0.5, GAMESQUARE_SIDE * 0.5,  GAMESQUARE_LEFT + GAMESQUARE_SIDE/4, GAMESQUARE_TOP + GAMESQUARE_SIDE/4)

titleObject = button.Button(mainMenuNewGameButon.rect.width * 3, mainMenuNewGameButon.rect.width*2, int(GAMESQUARE_LEFT +(GAMESQUARE_SIDE - mainMenuNewGameButon.rect.width*3)/2),  int(GAMESQUARE_TOP + (GAMESQUARE_SIDE - mainMenuNewGameButon.rect.width*2)/4), titleImg, titleImg)

#Initializes players that will play the game
player1 = player.Player('Player 1')
player2 = player.Player('Player 2')
player3 = player.Player('Player 3')
player4 = player.Player('Player 4')

playerTurn = 0
playerCount = 0
roundPoints = 0
scoreGoal = 0

#Variables that determine which screen is shown and what is happening
mainMenu = True
gameSetup = False
gameScreen = False

running = True
winnerFound = False
roundFarkled = False

#Method to switch player
def nextPlayer():
    global playerTurn
    playerTurn += 1
    if playerTurn == playerCount:
        playerTurn = 0
    fullDieReset()

#Method that rolls every dice
def rollDice():
    for dice in dieList:
        if dice.isAside() == False:
            dice.roll()
            dice.update()

#Method that fully resets the dice
def fullDieReset():
    for die in dieList:
        die.reset()
        die.unselect()
        die.roll()
        die.update()

#Method for checking if someone has won and who wins
def winCheck():
    if players[playerTurn].getScore() >= scoreGoal:
        global winnerFound
        winnerFound = True



while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if roundFarkled == True:
                roundFarkled = False
        for box in inputboxes:
            box.handle_event(event)
        

    
    screen.fill((100, 150, 255))

    #Main menu screen
    if mainMenu == True:
        titleObject.draw(screen)
        if mainMenuNewGameButon.draw(screen):
            #Changes the screen from main menu to setup 
            mainMenu = False
            gameSetup = True

    #Game setup screen
    if gameSetup == True:
        scoreGoalObject.draw(screen)
        
        #Sets the score goal depending on what button the player clicks
        for i, object in enumerate(scoreGoalList):
            if object.draw(screen):
                if i == 0:
                    scoreGoal = 5000
                elif i == 1:
                    scoreGoal = 10000
                elif i == 2:
                    scoreGoal = 20000
                #Changes the image so that the player can see what was clicked
                if object.getClicked():
                    object.select()
                    for b in range(3):
                        if b != i:
                            scoreGoalList[b].setSelectedFalse()
        
        playerCountObject.draw(screen)

        #Sets how many players will play the game
        for i, object in enumerate(playerCountList):
            if object.draw(screen):
                if i == 0:
                    playerCount = 2
                    players = [player1, player2]
                elif i == 1:
                    playerCount = 3
                    players = [player1, player2, player3]
                elif i == 2:
                    playerCount = 4
                    players = [player1, player2, player3, player4]
                if object.getClicked():
                    object.select()
                    for b in range(3):
                        if b != i:
                            playerCountList[b].setSelectedFalse()
        
        #Shows player name input boxes, depending on how many players have been chosen
        for index, line in enumerate(inputLines):
            if  index < playerCount:
                inputboxes[index].draw(screen)
                line.draw(screen)

        #Shows the start game button if player count and score goal is selected
        if playerCount != 0 and scoreGoal != 0:
            #When the start game button is clicked, sets the player names
            if startGameButton.draw(screen):
                for index, player in enumerate(players):
                    if index < playerCount:
                        player.setName(inputboxes[index].getText())
                #Changes the screen from setup to the game
                gameSetup = False
                gameScreen = True

    #Screen where the game is played
    if gameScreen == True:
        diceInGame = []
        #Check if rolled dice can score, if they can't the players round is over
        for die in dieList:
            if die.isAside() == False:
                diceInGame.append(die)
        if game_methods.hasCombination(diceInGame) == False:
            rollDice()
            fullDieReset()
            roundPoints = 0
            roundScoreRect.resetRolls()
            roundFarkled = True
            nextPlayer()
        
        #Watch dice for clicks and change select when clicked
        for die in dieList:
            if die.draw(screen):
                #Can't select a die that is aside
                if die.isAside() == False:
                    if die.isSelected() == False:
                        die.select()
                    else:
                        die.unselect()
                    die.update()
        selectedDie = []
        unselectedDie = []

        #Roll button
        if rollButton.draw(screen):
            for die in dieList:
                #Populates two lists - one which has the selected die, the other the not-selected
                if die.isSelected():
                    selectedDie.append(die)
                elif die.isAside() == False and die.isSelected() == False:
                    unselectedDie.append(die)
            #Checks if the selected die can score, and there isn't any dice that are not part of combos
            if game_methods.hasCombination(selectedDie) and game_methods.verifySelection(selectedDie):
                #Counts and adds points
                roundPoints += game_methods.countScore(selectedDie)
                roundScoreRect.addRoll(selectedDie)
                #Puts the dice aside for the next roll
                for die in selectedDie:
                    die.setAside()
                    die.update()
                #If all the dice are selected, then roll all 6 again
                if len(unselectedDie) == 0:
                    fullDieReset()
                rollDice()
            else:
                print('cheater!')

        #End turn button
        if endTurnButton.draw(screen):
            for die in dieList:
                if die.isSelected():
                    selectedDie.append(die)
            if game_methods.hasCombination(selectedDie) and game_methods.verifySelection(selectedDie):
                    #Adds the points gotten during the round to the players total score.
                    roundPoints += game_methods.countScore(selectedDie)
                    fullDieReset()
                    roundScoreRect.resetRolls()
                    players[playerTurn].updateScore(roundPoints)
                    roundPoints = 0
                    winCheck()
                    if winnerFound == False:
                        nextPlayer()

        #Draws all objects added to gameObjects on the screen
        for entity in gameObjects:
            screen.blit(entity.surf, entity.rect)
            entity.drawBorder(screen)
        currentPlayerRect.addPlayerName(screen, players[playerTurn])
        totalScoreRect.addPlayerScore(screen, players[playerTurn])
        scoreBoard.addScoreboard(screen, players, playerCount)
        roundScoreRect.addRoundTable(screen, roundPoints)

        #Show a pop-up when the player has no combinations in the rolled dice
        if roundFarkled == True:
            screen.blit(farklePopUp.surf, farklePopUp.rect)
            farklePopUp.popUpText(screen, players[playerTurn-1].getName() + ' farkled!')
            farklePopUp.drawBorder(screen)
        
        #Shows a pop-up if someone wins, has buttons to either play again with the same setup or go back to setup
        if winnerFound == True:
            screen.blit(winScreen.surf, winScreen.rect)
            winScreen.popUpText(screen, players[playerTurn].getName() + ' wins!')
            winScreen.drawBorder(screen)

            #Rematch button, start the game again with the same setup
            if rematchButton.draw(screen):
                for player in players:
                    player.setScore(0)
                fullDieReset()
                roundPoints = 0
                winnerFound = False
            #Go back to setup screen
            if newGameButon.draw(screen):
                for player in players:
                    player.setScore(0)
                fullDieReset()
                roundPoints = 0
                winnerFound = False
                gameScreen = False
                gameSetup = True


        
    pygame.display.flip()

pygame.quit()

