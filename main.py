import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
score_font = pygame.font.SysFont('comicsans', 60)

class Food:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load('food.png')

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


class Snake:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.direction = 'Right'
        self.image = pygame.image.load('snake.png')
        self.screen = screen
        self.body = [[100, 25],
                     [75, 25],
                     [50, 25]]
    
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.direction != 'Left':
            self.direction = 'Right'
        if keys[pygame.K_LEFT] and self.direction != 'Right':
            self.direction = 'Left'
        if keys[pygame.K_DOWN] and self.direction != 'Up':
            self.direction = 'Down'
        if keys[pygame.K_UP] and self.direction != 'Down':
            self.direction = 'Up'

        self.draw()

    def update(self):
        self.input()

        if self.direction == 'Right':
            self.x += 25
        if self.direction == 'Left':
            self.x -= 25
        if self.direction == 'Down':
            self.y += 25
        if self.direction == 'Up':
            self.y -= 25

        self.body.insert(0, [self.x, self.y])
        self.body.pop()
        self.collision()

    def draw(self):
        for part in self.body:
            self.screen.blit(self.image, (part[0], part[1]))

    def collision(self):
        for part in self.body[1:]:
            if self.x == part[0] and self.y == part[1]:
                return True

        return False
        



snake = Snake(screen, 100, 25)
food = Food(screen, 50, 50)
score = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    screen.fill((0, 0, 0))

    snake.update()
    food.draw()

    if snake.collision():
        print('collision')
        run = False
        pygame.quit()
    print(snake.x, snake.y)

    if snake.body[0][0] >= 800 or snake.body[0][1] >= 800 or snake.body[0][0] <= -25 or snake.body[0][1] <= -25:
        print('game over')
        run = False
        pygame.quit()

    if (snake.x, snake.y) == (food.x, food.y):
        food.x = random.randint(0, 31) * 25
        food.y = random.randint(0, 31) * 25
        snake.body.insert(0, [snake.x, snake.y])
        score += 1

    score_text = score_font.render(f'{score}', False, (255, 255, 255))
    score_text_rect = score_text.get_rect(center = (400, 20))
    screen.blit(score_text, score_text_rect)

    pygame.display.update()
    clock.tick(15)