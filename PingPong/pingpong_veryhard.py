import pygame
import os
import sys
import random

os.system("cls")
print("Game is Running!")



SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (20, 60, 120)
ORANGE = (250, 170, 70)
RED = (250, 0, 0)

FPS = 60

class Ball(object):
    def __init__(self, bounce_sound):
        self.rect = pygame.Rect(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2), 12, 12)
        self.bounce_sound = bounce_sound
        self.dx = 0
        self.dy = 5

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left < 0:
            self.dx *= -1
            self.rect.left = 0
            self.bounce_sound.play()

        elif self.rect.right > SCREEN_WIDTH:
            self.dx *= -1
            self.rect.right = SCREEN_WIDTH
            self.bounce_sound.play()

    def reset(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.dx = random.randint(-3, 3)
        self.dy = 5

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

class Player(object):
    def __init__(self, ping_sound):
        self.rect = pygame.Rect(int(SCREEN_WIDTH / 2), SCREEN_HEIGHT - 40, 50, 15)
        self.ping_sound = ping_sound
        self.dx = 0

    def update(self, ball):
        if self.rect.left <= 0 and self.dx < 0:
            self.dx = 0
        elif self.rect.right >= SCREEN_WIDTH and self.dx > 0:
            self.dx = 0

        if self.rect.colliderect(ball.rect):
            ball.dx = random.randint(-5, 5)
            ball.dy *= -1
            ball.rect.bottom = self.rect.top
            self.ping_sound.play()

        self.rect.x += self.dx

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

class Enemy(object):
    def __init__(self, pong_sound):
        self.rect = pygame.Rect(int(SCREEN_WIDTH / 2), 25, 40, 15)
        self.pong_sound = pong_sound

    def update(self, ball):

        if self.rect.centerx > ball.rect.centerx:
            diff = self.rect.centerx - ball.rect.centerx
            if diff <= 4:
                self.rect.centerx = ball.rect.centerx
            else:
                self.rect.x -= 4

        elif self.rect.centerx < ball.rect.centerx:
            diff = ball.rect.centerx - self.rect.centerx
            if diff <= 4:
                self.rect.centerx = ball.rect.centerx
            else:
                self.rect.x += 4

        if self.rect.colliderect(ball.rect):
            ball.dy *= -1
            ball.rect.top = self.rect.bottom
            self.pong_sound.play()

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

class Game(object):
    def __init__(self):
        bounce_path = resource_path("assets/bounce.wav")
        ping_path = resource_path("assets/ping.wav")
        pong_path = resource_path("assets/pong.wav")
        font_path = resource_path("assets/DungGeunMo.ttf")
        bounce_sound = pygame.mixer.Sound(bounce_path)
        ping_sound = pygame.mixer.Sound(ping_path)
        pong_sound = pygame.mixer.Sound(pong_path)
        self.font = pygame.font.Font(font_path, 35)
        self.ball = Ball(bounce_sound)
        self.player = Player(ping_sound)
        self.enemy = Enemy(pong_sound)
        self.player_score = 0
        self.enemy_score = 0

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.dx -= 5
                elif event.key == pygame.K_RIGHT:
                    self.player.dx += 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.dx = 0

        return False

    def run_logic(self):
        self.ball.update()
        self.player.update(self.ball)
        self.enemy.update(self.ball)

        if self.ball.rect.y < 0:
            self.player_score += 1
            self.ball.reset(self.player.rect.centerx, self.player.rect.centery)

        elif self.ball.rect.y > SCREEN_HEIGHT:
            self.enemy_score += 1
            self.ball.reset(self.enemy.rect.centerx, self.enemy.rect.centery)

    def display_message(self, screen, message, color):
        label = self.font.render(message, True, color)
        width = label.get_width()
        height = label.get_height()
        pos_x = int((SCREEN_WIDTH / 2) - (width / 2))
        pos_y = int((SCREEN_HEIGHT / 2) - (height / 2))
        screen.blit(label, (pos_x, pos_y))
        pygame.display.update()

    def display_frame(self, screen):
        screen.fill(BLACK)

        if self.player_score == 10:
            self.display_message(screen, "★ 승 리 ★", WHITE)
            self.player_score = 0
            self.enemy_score = 0
            pygame.time.wait(2000)

        elif self.enemy_score == 10:
            self.display_message(screen, "☆ 패 배 ☆", WHITE)
            self.player_score = 0
            self.enemy_score = 0
            pygame.time.wait(2000)
        else:
            self.ball.draw(screen)
            self.player.draw(screen)
            self.enemy.draw(screen)

            for x in range(0, SCREEN_WIDTH, 24):
                pygame.draw.rect(screen, WHITE, [x, int(SCREEN_HEIGHT / 2), 10, 10])

            enemy_score_label = self.font.render(str(self.enemy_score), True, WHITE)
            screen.blit(enemy_score_label, (10, 260))

            player_score_label = self.font.render(str(self.player_score), True, WHITE)
            screen.blit(player_score_label, (10, 340))

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PingPong [VERY HARD]")
    clock = pygame.time.Clock()
    game = Game()

    done = False
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
