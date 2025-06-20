import pygame
import random
from queue import PriorityQueue

# Инициализация Pygame
pygame.init()

# Константы
WIDTH = 800
GRID_SIZE = 30
CELL_SIZE = WIDTH // GRID_SIZE
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Pathfinding - Вариант 8")

# Цвета
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = col * CELL_SIZE
        self.y = row * CELL_SIZE
        self.color = WHITE
        self.weight = 1
        self.neighbors = []
    
    def get_pos(self):
        return self.row, self.col
    
    def is_barrier(self):
        return self.color == BLACK
    
    def reset(self):
        self.color = WHITE
        self.weight = 1
    
    def make_start(self):
        self.color = ORANGE
    
    def make_end(self):
        self.color = TURQUOISE
    
    def make_barrier(self):
        self.color = BLACK
    
    def make_path(self):
        self.color = PURPLE
    
    def make_closed(self):
        self.color = RED
    
    def make_open(self):
        self.color = GREEN
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, CELL_SIZE, CELL_SIZE))
        if self.weight > 1 and self.color not in [BLACK, ORANGE, TURQUOISE]:
            font = pygame.font.SysFont('Arial', 12)
            text = font.render(str(self.weight), True, BLACK)
            win.blit(text, (self.x + 5, self.y + 5))
    
    def update_neighbors(self, grid):
        self.neighbors = []
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for dr, dc in directions:
            new_row, new_col = self.row + dr, self.col + dc
            if 0 <= new_row < GRID_SIZE and 0 <= new_col < GRID_SIZE:
                neighbor = grid[new_row][new_col]
                if not neighbor.is_barrier():
                    self.neighbors.append(neighbor)

def heuristic(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

def make_grid():
    grid = []
    for i in range(GRID_SIZE):
        grid.append([])
        for j in range(GRID_SIZE):
            cell = Cell(i, j)
            grid[i].append(cell)
    return grid

def draw_grid(win, grid):
    for row in grid:
        for cell in row:
            cell.draw(win)
    
    for i in range(GRID_SIZE):
        pygame.draw.line(win, GREY, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE))
        pygame.draw.line(win, GREY, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH))
    
    pygame.display.update()

def generate_random_grid(grid, weighted=False):
    for row in grid:
        for cell in row:
            cell.reset()
    
    # Фиксированные точки для варианта 8
    start = grid[2][0]
    end = grid[8][9]
    start.make_start()
    end.make_end()
    
    # Случайные препятствия (20%)
    for row in grid:
        for cell in row:
            if random.random() < 0.2 and not cell.is_start() and not cell.is_end():
                cell.make_barrier()
    
    # Случайные веса (1-5)
    if weighted:
        for row in grid:
            for cell in row:
                if cell.color == WHITE:
                    cell.weight = random.randint(1, 5)
    
    return start, end

def main():
    grid = make_grid()
    start = None
    end = None
    
    running = True
    while running:
        draw_grid(WIN, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)
                    a_star_algorithm(lambda: draw_grid(WIN, grid), grid, start, end)
                
                if event.key == pygame.K_r:
                    start, end = generate_random_grid(grid)
                
                if event.key == pygame.K_w:
                    start, end = generate_random_grid(grid, weighted=True)
                
                if event.key == pygame.K_c:
                    grid = make_grid()
                    start = None
                    end = None
            
            if pygame.mouse.get_pressed()[0]:  # ЛКМ
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // CELL_SIZE, pos[0] // CELL_SIZE
                cell = grid[row][col]
                
                if not start and cell != end:
                    start = cell
                    start.make_start()
                elif not end and cell != start:
                    end = cell
                    end.make_end()
                elif cell != end and cell != start:
                    cell.make_barrier()
            
            elif pygame.mouse.get_pressed()[2]:  # ПКМ
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // CELL_SIZE, pos[0] // CELL_SIZE
                cell = grid[row][col]
                cell.reset()
                if cell == start:
                    start = None
                elif cell == end:
                    end = None
    
    pygame.quit()

if __name__ == "__main__":
    main()
  
