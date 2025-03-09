


import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]  # J
]

# Colors for shapes
SHAPE_COLORS = [CYAN, MAGENTA, RED, GREEN, YELLOW, ORANGE, BLUE]

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Clock
clock = pygame.time.Clock()

class Tetris:
    def __init__(self):
        self.grid = [[BLACK for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
        self.current_shape = self.get_new_shape()
        self.next_shape = self.get_new_shape()
        self.score = 0
        self.game_over = False

    def get_new_shape(self):
        shape = random.choice(SHAPES)
        color = SHAPE_COLORS[SHAPES.index(shape)]
        return {'shape': shape, 'color': color, 'x': SCREEN_WIDTH // BLOCK_SIZE // 2 - len(shape[0]) // 2, 'y': 0}

    def draw_grid(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                pygame.draw.rect(screen, self.grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
                pygame.draw.rect(screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

    def draw_shape(self, shape):
        for y, row in enumerate(shape['shape']):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, shape['color'], ((shape['x'] + x) * BLOCK_SIZE, (shape['y'] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

    def move_shape(self, dx, dy):
        self.current_shape['x'] += dx
        self.current_shape['y'] += dy
        if self.check_collision():
            self.current_shape['x'] -= dx
            self.current_shape['y'] -= dy
            return False
        return True

    def rotate_shape(self):
        shape = self.current_shape['shape']
        rotated_shape = [[shape[y][x] for y in range(len(shape))] for x in range(len(shape[0]) - 1, -1, -1)]
        original_x = self.current_shape['x']
        self.current_shape['x'] = max(0, min(self.current_shape['x'], SCREEN_WIDTH // BLOCK_SIZE - len(rotated_shape[0])))
        self.current_shape['shape'] = rotated_shape
        if self.check_collision():
            self.current_shape['shape'] = shape
            self.current_shape['x'] = original_x

    def check_collision(self):
        shape = self.current_shape['shape']
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    if (self.current_shape['y'] + y >= len(self.grid) or
                        self.current_shape['x'] + x < 0 or
                        self.current_shape['x'] + x >= len(self.grid[0]) or
                        self.grid[self.current_shape['y'] + y][self.current_shape['x'] + x] != BLACK):
                        return True
        return False

    def lock_shape(self):
        shape = self.current_shape['shape']
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_shape['y'] + y][self.current_shape['x'] + x] = self.current_shape['color']
        self.clear_lines()
        self.current_shape = self.next_shape
        self.next_shape = self.get_new_shape()
        if self.check_collision():
            self.game_over = True

    def clear_lines(self):
        lines_to_clear = [y for y, row in enumerate(self.grid) if all(cell != BLACK for cell in row)]
        for y in lines_to_clear:
            del self.grid[y]
            self.grid.insert(0, [BLACK for _ in range(SCREEN_WIDTH // BLOCK_SIZE)])
        self.score += len(lines_to_clear)

    def update(self):
        if not self.move_shape(0, 1):
            self.lock_shape()

    def draw(self):
        self.draw_grid()
        self.draw_shape(self.current_shape)
        self.draw_shape(self.next_shape)

def main():
    tetris = Tetris()
    fall_time = 0
    fall_speed = 0.5
    fast_fall_speed = 0.05
    fast_fall = False

    running = True
    while running:
        screen.fill(BLACK)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fast_fall:
            current_fall_speed = fast_fall_speed
        else:
            current_fall_speed = fall_speed

        if fall_time / 1000 >= current_fall_speed:
            fall_time = 0
            tetris.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetris.move_shape(-1, 0)
                if event.key == pygame.K_RIGHT:
                    tetris.move_shape(1, 0)
                if event.key == pygame.K_DOWN:
                    fast_fall = True
                if event.key == pygame.K_UP:
                    tetris.rotate_shape()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    fast_fall = False

        tetris.draw()
        pygame.display.update()

        if tetris.game_over:
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()
