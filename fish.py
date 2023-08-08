import pygame
import os
import sys
import random

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

WHITE = (255, 255, 255)
SEA = (80, 180, 220)
GROUND = (140, 120, 40)
DARK_GROUND = (70, 60, 20)
FPS = 60
class Fish():
    def __init__(self):
        self.image = pygame.image.load(resource_path('assets/fish.png'))
        self.sound = pygame.mixer.Sound(resource_path('assets/swim.wav'))
        self.rect = self.image.get_rect()
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.reset()

    def reset(self):
        self.rect.x = 250
        self.rect.y = 250
        self.dx = 0
        self.dy = 0

    def swim(self):
        self.dy = -10
        self.sound.play()

    def update(self):
        self.dy += 0.5
        self.rect.y += self.dy
        if self.rect.y <= 0:
            self.rect.y = 0

        if self.rect.y + self.height > SCREEN_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - self.height
            self.dy = 0

        if self.dy > 20:
            self.dy = 20

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Pipe():
    def __init__(self):
        self.lpipe = pygame.image.load(resource_path('assets\pipe01.png'))
        self.lpipe_rect = self.lpipe.get_rect()
        self.lpipe_width = self.lpipe.get_rect().width
        self.lpipe_height = self.lpipe.get_rect().height
        pipes = ('assets\pipe02.png', 'assets\pipe03.png', \
                 'assets\pipe04.png', 'assets\pipe05.png', 'assets\pipe06.png')
        self.spipe = pygame.image.load(resource_path(random.choice(pipes)))
        self.spipe_rect = self.spipe.get_rect()
        self.spipe_width = self.spipe.get_rect().width
        self.spipe_height = self.spipe.get_rect().height
        self.set_pos()

    def set_pos(self):
        if random.randint(0, 1):
            self.lpipe_rect.x = SCREEN_WIDTH
            self.lpipe_rect.y = -2
            self.spipe_rect.x = SCREEN_WIDTH
            self.spipe_rect.y = SCREEN_HEIGHT - self.spipe_height + 2

        else:
            self.spipe_rect.x = SCREEN_WIDTH
            self.spipe_rect.y = -2
            self.lpipe_rect.x = SCREEN_WIDTH
            self.lpipe_rect.y = SCREEN_HEIGHT - self.lpipe_height + 2

    def update(self):
        self.lpipe_rect.x -= 4
        self.spipe_rect.x -= 4

    def out_of_screen(self):
        if self.spipe_rect.x + self.spipe_width <= 0:
            return True
        return False

    def check_crash(self, fish):

        if (self.lpipe_rect.x + self.lpipe_width > fish.rect.x) and \
            (self.lpipe_rect.x < fish.rect.x + fish.width) and \
            (self.lpipe_rect.y < fish.rect.y + fish.height) and \
            (self.lpipe_rect.y + self.lpipe_height > fish.rect.y):
            return True

        elif (self.spipe_rect.x + self.spipe_width > fish.rect.x) and \
            (self.spipe_rect.x < fish.rect.x + fish.width) and \
            (self.spipe_rect.y < fish.rect.y + fish.height) and \
            (self.spipe_rect.y + self.spipe_height > fish.rect.y):
            return True
        else:
            return False

    def draw(self, screen):
        screen.blit(self.lpipe, self.lpipe_rect)
        screen.blit(self.spipe, self.spipe_rect)

class Game():
    def __init__(self):
        self.praytime = 0
        self.hiscore = 0
        font_path = resource_path('assets\DungGeunMo.ttf')
        self.font = pygame.font.Font(font_path, 34)
        pygame.mixer.music.load(resource_path("assets\gm.mp3"))
        self.fish = Fish()
        self.pipes = []
        self.pipes.append(Pipe())
        self.pipe_pos = 100

        self.score = 0

        self.menu_on = True

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if self.menu_on:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.play(-1)
                        self.score = 0
                        self.menu_on = False
                        self.fish.reset()
                        self.pipes = []
                        self.pipes.append(Pipe())

            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.fish.swim()
        return False

    def run_logic(self, screen):
        for pipe in self.pipes:

            if pipe.spipe_rect.x == self.pipe_pos:
                self.pipes.append(Pipe())
                self.score += 1

            if pipe.out_of_screen():
                del self.pipes[0]
                self.pipe_pos = random.randrange(200, 300, 4)

            if pipe.check_crash(self.fish):
                pygame.mixer_music.stop()
                self.menu_on = True

    def draw_text(self, screen, text, font, x, y, main_color):
        text_obj = font.render(text, True, main_color)
        text_rect = text_obj.get_rect()
        text_rect.center = x, y
        screen.blit(text_obj, text_rect)

    def display_menu(self, screen):
        center_x = (SCREEN_WIDTH / 2)
        center_y = (SCREEN_HEIGHT / 2)
        rect = (center_x - 220, center_y - 50, 440, 100)
        pygame.draw.rect(screen, GROUND, rect)
        pygame.draw.rect(screen, DARK_GROUND, rect, 4)
        self.draw_text(screen, "Press Space Key to Play",
                       self.font, center_x, center_y, DARK_GROUND)

    def display_frame(self, screen):
        screen.fill(SEA)
        pygame.draw.rect(screen, GROUND,
                         (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50))
        pygame.draw.line(screen, DARK_GROUND,
                         (0, SCREEN_HEIGHT - 50), (SCREEN_WIDTH, SCREEN_HEIGHT - 50), 4)
        self.fish.update()
        self.fish.draw(screen)
        for pipe in self.pipes:
            pipe.update()
            pipe.draw(screen)
        if self.score > self.hiscore:
            self.hiscore = self.score
        self.praytime += 0.018
        self.draw_text(screen, "점수: " + str(self.score), self.font, 100, 50, WHITE)
        self.draw_text(screen, "최고 점수: " + str(self.hiscore), self.font, 145, 100, WHITE)
        self.draw_text(screen, "플레이 시간: " + str(int(self.praytime)), self.font, 160, 150, WHITE)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("나는 '새'")
    clock = pygame.time.Clock()
    game = Game()
    done = False
    while not done:
        done = game.process_events()
        if game.menu_on:
            game.display_menu(screen)
        else:
            game.run_logic(screen)
            game.display_frame(screen)
        

        pygame.display.flip()
        clock.tick(FPS)
        
    pygame.quit()

if __name__ == '__main__':
    main()