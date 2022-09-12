import pygame
from pygame.constants import BLEND_SUB, K_DOWN, K_LEFT, K_RIGHT, K_UP
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)

BLOCK_DIMENSIONS = 20
WIDTH, HEIGHT = 600, 600
ROWS, COLUMNS = WIDTH/BLOCK_DIMENSIONS, HEIGHT/BLOCK_DIMENSIONS

FPS = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake game")

class snake(object):
    def __init__(self):
        self.positions = [[0, 280],[20, 280], [40, 280], [60, 280]]
        self.xspeed = 1
        self.yspeed = 0

    def update(self):
        for _ in range(len(self.positions)-1):
            self.positions[_] = self.positions[_ + 1]
        del(self.positions[-1])

        self.positions.append([self.positions[-1][0] + self.xspeed * BLOCK_DIMENSIONS, self.positions[-1][1] + self.yspeed * BLOCK_DIMENSIONS])
        if self.positions[-1][0] > WIDTH - BLOCK_DIMENSIONS:
            self.dead()
        if self.positions[-1][0] < 0:
            self.dead()
        if self.positions[-1][1] > HEIGHT - BLOCK_DIMENSIONS:
            self.dead()
        if self.positions[-1][1] < 0:
            self.dead()
        for j in self.positions[:-1]:
            if j[0] == self.positions[-1][0] and j[1] == self.positions[-1][1]:
                Snake.dead()

    def direction(self, x, y):
        self.xspeed = x
        self.yspeed = y
    
    def show(self):
        for i in self.positions:
            pygame.draw.rect(screen, BLACK, (i[0], i[1], BLOCK_DIMENSIONS, BLOCK_DIMENSIONS))
    
    def eat(self, foodx, foody):
        if self.positions[-1][0] == foodx and self.positions[-1][1] == foody:
            self.positions.insert(0, [self.positions[0][0] - self.xspeed, self.positions[0][1]-self.yspeed])
            return True
        else:
            return False
    
    def dead(self):
        self.positions = [[0, 280],[20, 280], [40, 280], [60, 280]]
        self.xspeed = 1
        self.yspeed = 0


class food(object):
    def __init__(self):
        self.posX = round(random.randint(0, WIDTH - 10), -1)
        if self.posX % 20 != 0:
            self.posX -= 10
        self.posY = round(random.randint(0, HEIGHT - 10), -1)
        if self.posY % 20 != 0:
            self.posY -= 10
    
    def show(self):
        pygame.draw.rect(screen, RED, (self.posX, self.posY, BLOCK_DIMENSIONS, BLOCK_DIMENSIONS))
    
    def pickLocation(self):
        self.posX = round(random.randint(0, WIDTH - 10), -1)
        if self.posX % 20 != 0:
            self.posX -= 10
        self.posY = round(random.randint(0, HEIGHT - 10), -1)
        if self.posY % 20 != 0:
            self.posY -= 10


Snake = snake()
Food = food()

def keypress():
    keys = pygame.key.get_pressed()

    if keys[K_RIGHT]:
        if Snake.xspeed != -1:
            Snake.direction(1, 0)
    if keys[K_LEFT]:
        if Snake.xspeed != 1:
            Snake.direction(-1, 0)
    if keys[K_DOWN]:
        if Snake.yspeed != -1:
            Snake.direction(0, 1)
    if keys[K_UP]:
        if Snake.yspeed != 1:
            Snake.direction(0, -1)

def draw_screen():
    screen.fill(CYAN)
    Snake.show()
    Food.show()
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keypress()
        Snake.update()
        if Snake.eat(Food.posX, Food.posY):
            Food.pickLocation()

        draw_screen()
main()

if __name__ == "__main__":
    main()
