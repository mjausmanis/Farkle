import pygame


#Button class that adds images, that can be clicked
class Button():
    def __init__(self, width, height, x, y, image, image_clicked):
        self.surf = pygame.Surface((width, height))
        self.regular_image = pygame.transform.scale(image, (int(width), int(height)))
        self.image_clicked = pygame.transform.scale(image_clicked, (int(width), int(height)))
        self.image = self.regular_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.selected = False
        self.width = width
        self.height = height

    def update(self):
        if self.selected == True:
            self.image = self.image_clicked
        else:
            self.image = self.regular_image

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == False:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

    def getClicked(self):
        return self.clicked

    def select(self):
        self.selected = True
        self.update()

    def setSelectedFalse(self):
        self.selected = False
        self.update()