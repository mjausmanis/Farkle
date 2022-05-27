import pygame

#PopUp class for sprites that show up at certain points as pop-up screen
class PopUp(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font('./Font/pixelated.ttf', int(width/7))
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.surf = pygame.Surface([width, height])
        self.surf.fill((71,222,207))

        self.rect = self.surf.get_rect()

        self.rect.topleft = (x, y)


    #Draws text in to the sprite
    def popUpText(self, surface, text):
        surface.blit(self.font.render(text,
            True, (0, 0, 0)),
            (self.x + int(0.1*self.width), self.y + self.height*0.4))


    #Draws a border around the sprite
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
        surface.blit(top, (self.x - thickness/2, self.y - thickness/2))
        surface.blit(left, (self.x - thickness/2, self.y - thickness/2))
        surface.blit(bottom, (self.rect.bottomleft[0] - thickness/2, self.rect.bottomleft[1] - thickness/2))
        surface.blit(right, (self.rect.topright[0] - thickness/2, self.y - thickness/2))

