import pygame
import random

# 게임 설정
WIDTH, HEIGHT = 400, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 240, 15  # 폭을 3배로 늘림
BALL_RADIUS = 10
BLOCK_ROWS, BLOCK_COLS = 5, 8
BLOCK_WIDTH = WIDTH // BLOCK_COLS
BLOCK_HEIGHT = 25

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 179, 186), (186, 255, 201), (186, 225, 255), (255, 223, 186), (255, 255, 186)]

class Paddle:
    def __init__(self):
        self.x = WIDTH // 2 - PADDLE_WIDTH // 2
        self.y = HEIGHT - 40
        self.speed = 8

    def move(self, dx):
        self.x += dx * self.speed
        self.x = max(0, min(WIDTH - PADDLE_WIDTH, self.x))

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT))

class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.dx = random.choice([-4, 4])
        self.dy = -4

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, screen):
        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), BALL_RADIUS)

class Block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.alive = True

    def draw(self, screen):
        if self.alive:
            pygame.draw.rect(screen, self.color, (self.x, self.y, BLOCK_WIDTH-2, BLOCK_HEIGHT-2))

def create_blocks():
    blocks = []
    for row in range(BLOCK_ROWS):
        for col in range(BLOCK_COLS):
            x = col * BLOCK_WIDTH
            y = row * BLOCK_HEIGHT + 40
            color = COLORS[row % len(COLORS)]
            blocks.append(Block(x, y, color))
    return blocks

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("블록 깨기")
    clock = pygame.time.Clock()

    paddle = Paddle()
    ball = Ball()
    blocks = create_blocks()
    running = True

    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move(-1)
        if keys[pygame.K_RIGHT]:
            paddle.move(1)

        ball.move()

        # 벽 충돌
        if ball.x < BALL_RADIUS or ball.x > WIDTH - BALL_RADIUS:
            ball.dx *= -1
        if ball.y < BALL_RADIUS:
            ball.dy *= -1

        # 패들 충돌
        if (paddle.y < ball.y + BALL_RADIUS < paddle.y + PADDLE_HEIGHT and
            paddle.x < ball.x < paddle.x + PADDLE_WIDTH):
            ball.dy *= -1
            ball.y = paddle.y - BALL_RADIUS

        # 블록 충돌
        for block in blocks:
            if block.alive:
                if (block.x < ball.x < block.x + BLOCK_WIDTH and
                    block.y < ball.y - BALL_RADIUS < block.y + BLOCK_HEIGHT):
                    block.alive = False
                    ball.dy *= -1
                    break

        # 바닥에 닿으면 게임 오버
        if ball.y > HEIGHT:
            running = False

        # 모든 블록 제거 시 게임 클리어
        if all(not block.alive for block in blocks):
            running = False

        paddle.draw(screen)
        ball.draw(screen)
        for block in blocks:
            block.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
