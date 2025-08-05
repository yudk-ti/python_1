#cmd
#pip install pygame

import pygame
import random

# 게임 설정
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
COLUMNS = WIDTH // BLOCK_SIZE
ROWS = HEIGHT // BLOCK_SIZE

# 파스텔톤 색상
PASTEL_COLORS = [
    (255, 179, 186),  # 연핑크
    (186, 255, 201),  # 연녹색
    (186, 225, 255),  # 연파랑
    (255, 223, 186),  # 연주황
    (255, 255, 186),  # 연노랑
]

# 블럭 타입 (5개)
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
]

class Block:
    def __init__(self):
        self.type = random.randint(0, len(SHAPES) - 1)
        self.shape = SHAPES[self.type]
        self.color = PASTEL_COLORS[self.type]
        self.x = COLUMNS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

class Tetris:
    def __init__(self):
        self.board = [[(0, (0,0,0)) for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.block = Block()
        self.game_over = False

    def valid(self, shape, offset_x, offset_y):
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    nx, ny = x + offset_x, y + offset_y
                    if nx < 0 or nx >= COLUMNS or ny < 0 or ny >= ROWS:
                        return False
                    if self.board[ny][nx][0]:
                        return False
        return True

    def freeze(self):
        for y, row in enumerate(self.block.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.block.y + y][self.block.x + x] = (1, self.block.color)
        self.clear_lines()
        self.block = Block()
        if not self.valid(self.block.shape, self.block.x, self.block.y):
            self.game_over = True

    def clear_lines(self):
        new_board = [row for row in self.board if not all(cell[0] for cell in row)]
        lines_cleared = ROWS - len(new_board)
        for _ in range(lines_cleared):
            new_board.insert(0, [(0, (0,0,0)) for _ in range(COLUMNS)])
        self.board = new_board

    def move(self, dx, dy):
        if self.valid(self.block.shape, self.block.x + dx, self.block.y + dy):
            self.block.x += dx
            self.block.y += dy
            return True
        return False

    def rotate(self):
        old_shape = self.block.shape
        self.block.rotate()
        if not self.valid(self.block.shape, self.block.x, self.block.y):
            self.block.shape = old_shape

    def drop(self):
        if not self.move(0, 1):
            self.freeze()

    def drop_to_bottom(self):
        # 블럭을 바닥까지 즉시 떨어뜨림
        while self.move(0, 1):
            pass
        self.freeze()

def draw_board(screen, game):
    screen.fill((240, 240, 240))
    # 보드 그리기
    for y in range(ROWS):
        for x in range(COLUMNS):
            if game.board[y][x][0]:
                pygame.draw.rect(
                    screen, game.board[y][x][1],
                    (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                )
    # 현재 블럭 그리기
    for y, row in enumerate(game.block.shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(
                    screen, game.block.color,
                    ((game.block.x + x) * BLOCK_SIZE, (game.block.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                )
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("파스텔 테트리스")
    clock = pygame.time.Clock()
    game = Tetris()
    fall_time = 0

    # 방향키 누른 시간 추적용
    key_hold = {
        pygame.K_LEFT: 0,
        pygame.K_RIGHT: 0,
        pygame.K_DOWN: 0,
        pygame.K_UP: 0,
    }
    key_pressed = {
        pygame.K_LEFT: False,
        pygame.K_RIGHT: False,
        pygame.K_DOWN: False,
        pygame.K_UP: False,
    }

    while not game.game_over:
        dt = clock.tick(60)
        fall_time += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key in key_hold:
                    key_pressed[event.key] = True
                if event.key == pygame.K_LEFT:
                    game.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    game.move(1, 0)
                elif event.key == pygame.K_DOWN:
                    game.drop()
                elif event.key == pygame.K_UP:
                    game.rotate()
            elif event.type == pygame.KEYUP:
                if event.key in key_hold:
                    key_pressed[event.key] = False
                    key_hold[event.key] = 0

        # 방향키가 눌린 상태면 시간 누적
        for k in key_hold:
            if key_pressed[k]:
                key_hold[k] += dt
                # 2초(2000ms) 이상 누르면 블럭을 끝까지 떨어뜨림
                if key_hold[k] > 2000:
                    if not game.game_over:
                        game.drop_to_bottom()
                    key_hold[k] = 0
                    key_pressed[k] = False

        if fall_time > 500:
            game.drop()
            fall_time = 0
        draw_board(screen, game)
    pygame.quit()

if __name__ == "__main__":
    main()