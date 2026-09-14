import random
import pygame
import sys

class Block:
    def __init__(self):
        self.is_wall = False
        self.is_coin = False

class Player:
    def __init__(self):
        self.xpos = 1
        self.ypos = 1
        self.is_alive = True
        self.score = 0
        self.face = "North"

    def move(self, direction, grid):
            if direction == "North" and grid[self.ypos - 1][self.xpos].is_wall == False:
                self.ypos -= 1
            elif direction == "South" and grid[self.ypos + 1][self.xpos].is_wall == False:
                self.ypos += 1
            elif direction == "West" and grid[self.ypos][self.xpos - 1].is_wall == False:
                self.xpos -= 1
            elif direction == "East" and grid[self.ypos][self.xpos + 1].is_wall == False:
                self.xpos += 1

        ## use the portal 
            if self.xpos == 27 and self.ypos == 14 and direction == "East":
                self.xpos = 1
                self.ypos = 14

            if self.xpos == 0 and self.ypos == 14 and direction == "West":
                self.xpos = 26
                self.ypos = 14

    def score_up(self):
        if grid[self.ypos][self.xpos].is_coin:
            grid[self.ypos][self.xpos].is_coin = False
            self.score += 1

class Ghost:
    def __init__(self, name, color, xpos, ypos):
        # super().__init__() Ich glaube, das ist doof, weil ich es auch nicht brauche
        # und ich die Punktzahl nicht von den Geistern bekommen will.
        self.name = name
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        self.is_alive = True
        self.face = "North"

    def move(self, direction):
        pass
    def find_player(self, player):
        pass


grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 3, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 3, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 3, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 3, 1],
    [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1],
    [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# den objecten in der liste zuweisen
for ypos in range(len(grid)):
    for xpos in range(len(grid[ypos])):
        if grid[ypos][xpos] == 1:
            block = Block()
            block.is_wall = True
            grid[ypos][xpos] = block
        elif grid[ypos][xpos] == 2:
            block = Block()
            block.is_coin = True
            grid[ypos][xpos] = block
        else:
            block = Block()
            grid[ypos][xpos] = block

MAIN_FONT_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)
YELLOW = (255, 255, 0)
FPS = 60

pygame.init()
pygame.font.init()
MAIN_FONT = pygame.font.SysFont("Arial", MAIN_FONT_SIZE)
pygame.display.set_caption("Pacman")

screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
player = Player()

GHOSTS_PINK = Ghost("Pink", "Pink", 13, 14)
GHOSTS_PINK.color = "Pink"
GHOSTS_PINK.xpos = 13
GHOSTS_PINK.ypos = 14

# Position the grid in the center of the screen
SREEN_MID_X = screen.get_width() //4
SREEN_MID_Y = screen.get_height() //12

SCALE = 30

while running:
    for event in pygame.event.get():
        # general keyboard input
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.face = "North"
                player.move(player.face, grid)
                player.score_up()
            elif event.key == pygame.K_s:
                player.face = "South"
                player.move(player.face, grid)
                player.score_up()
            elif event.key == pygame.K_a:
                player.face = "West"
                player.move(player.face, grid)
                player.score_up()
            elif event.key == pygame.K_d:
                player.face = "East"
                player.move(player.face, grid)
                player.score_up()

    screen.fill(WHITE)
    clock.tick(FPS)

    #draw the grid
    for ypos in range(len(grid)):
        for xpos in range(len(grid[ypos])):
            block = grid[ypos][xpos]
            if block.is_wall:
                pygame.draw.rect(screen, BLACK, (xpos * SCALE + SREEN_MID_X , ypos * SCALE + SREEN_MID_Y , SCALE, SCALE))
            elif block.is_coin:
                pygame.draw.circle(screen, BLUE, (xpos * SCALE + SREEN_MID_X + SCALE // 2, ypos * SCALE + SREEN_MID_Y + SCALE // 2), 5)

        pygame.draw.rect(screen, YELLOW , (player.xpos * SCALE + SREEN_MID_X, player.ypos * SCALE + SREEN_MID_Y, SCALE, SCALE))
        pygame.draw.rect(screen, PINK, (GHOSTS_PINK.xpos * SCALE + SREEN_MID_X, GHOSTS_PINK.ypos * SCALE + SREEN_MID_Y, SCALE, SCALE))

    killed = False
    if player.xpos == GHOSTS_PINK.xpos and player.ypos == GHOSTS_PINK.ypos:
        player.is_alive = False
        print("Der Spieler ist gestorben!")
        killed = True
        running = False


    won = False
    if player.score == 240:
        print("Der Spieler hat gewonnen!")
        running = False
        won = True

    #draw the player score
    draw_player_count = MAIN_FONT.render(f"Score: {player.score}", True, BLACK)
    screen.blit(draw_player_count, (10, 10))
    pygame.display.flip()

if won:
    print("Der Spieler hat gewonnen!")
    screen.fill(WHITE) # spielfeld leeren

    gewonnen = pygame.font.SysFont("Arial", 50)
    gewonnen_text = gewonnen.render("Du hast gewonnen!", True, BLACK)

    screen.blit(gewonnen_text, (screen.get_width() // 2 - gewonnen_text.get_width() // 2, screen.get_height() // 2 - gewonnen_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(3000)
if killed:
    print("Der Spieler ist gestorben!")
    screen.fill(WHITE) # spielfeld leeren

    verloren = pygame.font.SysFont("Arial", 50)
    verloren_text = verloren.render("Du hast verloren!", True, BLACK)

    screen.blit(verloren_text, (screen.get_width() // 2 - verloren_text.get_width() // 2, screen.get_height() // 2 - verloren_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(3000)
    
pygame.quit()
sys.exit()

    