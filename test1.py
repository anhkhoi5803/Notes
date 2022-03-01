import pygame
import datetime

pygame.init()
clock = pygame.time.Clock()
pygame.font.init()

# Note
finish = 0
leftover = 16

# Font
numb_font = pygame.font.Font('dogicapixelbold.ttf', 14)
text_font = pygame.font.Font('dogicapixelbold.ttf', 16)

color = (233, 248, 215)
active = False

# screen resolution
Width = 800
Height = 600
bg = pygame.image.load('opennote.png')
screen = pygame.display.set_mode((Width, Height))

# Time
time_box = pygame.Rect(250, 63, 50, 30)
date_box = pygame.Rect(221, 27, 50, 30)
# boxes numb
leftover_box = pygame.Rect(265, 105, 30, 30)
finish_box = pygame.Rect(325, 105, 30, 30)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text = text
        self.txt_surface = text_font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                    # Limit characters           -20 for border width
                    if self.txt_surface.get_width() > self.rect.w - 15:
                        self.text = self.text[:-1]

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 10))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, -1)

    def update(self):
        # Re-render the text.
        self.txt_surface = text_font.render(self.text, True, self.color)


def main():
    clock = pygame.time.Clock()
    input_box1 = InputBox(115, 170, 250, 36)
    input_box2 = InputBox(115, 224, 250, 36)
    input_box3 = InputBox(115, 278, 250, 36)
    input_box4 = InputBox(115, 333, 250, 36)
    input_box5 = InputBox(115, 386, 250, 36)
    input_box6 = InputBox(115, 440, 250, 36)
    input_box7 = InputBox(115, 494, 250, 36)
    input_boxes = [input_box1, input_box2, input_box3, input_box4, input_box5, input_box6, input_box7]
    done = False

    while not done:
        # Background
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        now = datetime.datetime.now()
        date_now = now.strftime("%d/%m/%Y")
        time_now = now.strftime("%H:%M:%S")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)
            # Real Time
            # Date
        pygame.draw.rect(screen, 'white', date_box, -1)
        datebox_surface = numb_font.render(date_now, True, color)
        screen.blit(datebox_surface, (date_box.x + 5, date_box.y + 5))
        # Time
        pygame.draw.rect(screen, 'white', time_box, -1)
        timebox_surface = numb_font.render(time_now, True, color)
        screen.blit(timebox_surface, (time_box.x + 5, time_box.y + 5))

        # finish &Leftover
        # finish box
        pygame.draw.rect(screen, 'white', finish_box, -1)
        finishbox_surface = numb_font.render(str(finish), True, color)
        screen.blit(finishbox_surface, finish_box)
        # Leftover box
        pygame.draw.rect(screen, 'white', leftover_box, -1)
        leftover_box_surface = numb_font.render(str(leftover), True, color)
        screen.blit(leftover_box_surface, leftover_box)

        pygame.display.update()
        clock.tick(120)


if __name__ == '__main__':
    main()
    pygame.quit()
