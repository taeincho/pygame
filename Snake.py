import pygame, os, sys, random
from time import sleep

# 게임 스크린 전역변수
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 게임 화면 전역변수
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRID_SIZE

# 방향 전역변수
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# 색상 전역변수
WHITE = (255, 255, 255)
ORANGE = (250, 150, 0)
GRAY = (100, 100, 100)

# 뱀 객체
class Snake():
    def __init__(self):
        self.create()
    
    def create(self): # 뱀 생성
        self.length = 2
        self.positions = [(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
    
    def control(self, xy):
        if(xy[0] * -1, xy[1] * -1) == self.direction:
            return
        else:
            self.direction = xy

    def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = (cur[0] + (x * GRID_SIZE)), (cur[1] + (y * GRID_SIZE))
        if new in self.positions[2:]:
            sleep(1)
            self.create()
        elif new[0] < 0 or new[0] >= SCREEN_WIDTH or \
             new[1] < 0 or new[1] >= SCREEN_HEIGHT:
            sleep(1)
            self.create()
        else:
            self.positions.insert(0, new)
            if len(self.positions) >> self.length:
                self.positions.pop()
    
    def eat(self):
        self.length += 1
    
    def draw(self, screen):
        red, green, blue = 50 / (self.length - 11), 1500, 150 / (self.length -1)
        for i, p in enumerate(self.positions):
            color = (100 + red * i, green, blue * i)
            rect = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, color, rect)
    
class Feed():
    def __init__(self):
        self.position = (0, 0)
        self.color = ORANGE
        self.create()
        
    def create(self):
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        self.position = x * GRID_SIZE, y * GRID_SIZE
        
    def draw(self, screen):
        rect = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.color, rect)

class Game():
    def __init__(self):
        self.snake = Snake()
        self.feed = Feed()
        self.speed = 5
    
    def process_evennts(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.control(UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.control(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.control(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.control(RIGHT)
        return False
    
    def run_logic(self):
        self.snake.move()
        self.check_eat(self.snake, self.feed)
        self.speed = (10 + self.snake.length) /2
    
    def check_eat(snake, feed):
        if snake.positions[0] == feed.position:
            snake.eat()
            feed.create()
    
    def draw_info(self, lenght, speed, screen):
        info = "Length: " + str(lenght) + "        " + "Speed: " + str(round(speed, 2))
        font = pygame.font.SysFont('맑은 고딕', 30, False, False)
        text_obj = font.render(info, True, GRAY)
        text_rect = text_obj.get_rect()
        text_rect.x, text_rect.y = 10, 10
        screen.blit(text_obj, text_rect)

    def display_frame(self, screen):
        screen.fill(WHITE)
        self.draw_info(self.snake.length, self.speed, screen)
        self.snake.draw(screen)
        self.feed.draw(screen)
        screen.blit(screen, (0, 0))
    
    def main():
        pygame.init()
        pygame.display.set_caption("Snake Game")
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        game = Game()
        clock = pygame.time.Clock()
        done = False
        while not done:
            done = game.process_evennts()
            game.run_logic()
            game.display_frame(screen)
            pygame.display.flip()
            clock.tick(game.speed)
pygame.quit()