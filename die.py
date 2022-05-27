import random, pygame


#Class for the dice
class Die:
    def __init__(self, width, height, x, y):
        self.__value = 0
        self.__aside = False
        self.__selected= False
        self.width = width
        self.height = height

        self.clicked = False

        #Loads images used to show the dice and their status
        self.img1 = pygame.image.load("./Images/1.png")
        self.img1_clicked = pygame.image.load("./Images/1_clicked.png")
        self.img2 = pygame.image.load("./Images/2.png")
        self.img2_clicked = pygame.image.load("./Images/2_clicked.png")
        self.img3 = pygame.image.load("./Images/3.png")
        self.img3_clicked = pygame.image.load("./Images/3_clicked.png")
        self.img4 = pygame.image.load("./Images/4.png")
        self.img4_clicked = pygame.image.load("./Images/4_clicked.png")
        self.img5 = pygame.image.load("./Images/5.png")
        self.img5_clicked = pygame.image.load("./Images/5_clicked.png")
        self.img6 = pygame.image.load("./Images/6.png")
        self.img6_clicked = pygame.image.load("./Images/6_clicked.png")

        #Lists of the images to be iterable through
        self.images = [self.img1, self.img2, self.img3, self.img4, self.img5, self.img6]
        self.images_clicked = [self.img1_clicked, self.img2_clicked, self.img3_clicked, self.img4_clicked, self.img5_clicked, self.img6_clicked]
        self.image_aside = pygame.image.load("./Images/aside.png")
        
        self.roll()
        self.update()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


    #Simple methods to change and return the dies values

    def getValue(self):
        return self.__value

    def isAside(self):
        return self.__aside

    def setAside(self):
        self.__aside = True
        self.__selected = False

    def reset(self):
        self.__aside = False

    def isSelected(self):
        return self.__selected

    def select(self):
        self.__selected = True

    def unselect(self):
        self.__selected = False

    def roll(self):
        self.__value = random.randint(1, 6)

    #Changes the image depending on dies status
    def update(self):
        for number in range(6):
            if self.__value == number + 1:
                if self.__aside:
                    self.image = self.image_aside
                elif self.__selected:
                    self.image = self.images_clicked[number]
                else:
                    self.image = self.images[number]
                self.image = pygame.transform.scale(self.image, (self.width, self.height))

    #Draws the dice and checks for clicks on it, if clicked returns true that can be used in main file
    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        #Checks for clicks
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == False:
            self.clicked = False
            
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action