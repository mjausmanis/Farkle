import pygame

#Class for creating input boxes
class InputBox:

    def __init__(self, width, height, x, y, text=''):
        self.COLOR_INACTIVE = pygame.Color((1, 110, 95))
        self.COLOR_ACTIVE = pygame.Color((138, 255, 243))
        self.surf = pygame.Surface((width, height))
        self.FONT = pygame.font.Font('./Font/pixelated.ttf', int(height/2))
        self.rect = pygame.Rect(x, y, width, height)
        self.surf.fill((71,222,207))
        self.color = self.COLOR_INACTIVE
        self.text = text
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.FONT.render(self.text, True, self.color)


    def draw(self, screen):
        # Blit the text.
        screen.blit(self.surf, (self.rect.x, self.rect.y))
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def getText(self):
        return self.text