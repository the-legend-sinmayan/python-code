import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neon Game Hub")

font = pygame.font.SysFont("Arial", 30)
clock = pygame.time.Clock()

BG = (15, 23, 42)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

state = "menu"

# ================= TIC TAC TOE =================
board = [""] * 9
turn = "X"

def check_win():
    win = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in win:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    return None

def draw_tic():
    screen.fill(BG)

    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, WHITE, (200 + j*100, 150 + i*100, 90, 90), 2)
            idx = i*3 + j
            text = font.render(board[idx], True, WHITE)
            screen.blit(text, (235 + j*100, 180 + i*100))

# ================= SNAKE =================
snake = [(300, 300)]
direction = (20, 0)
food = (200, 200)

def draw_snake():
    screen.fill(BG)

    for s in snake:
        pygame.draw.rect(screen, GREEN, (*s, 20, 20))

    pygame.draw.rect(screen, RED, (*food, 20, 20))

def move_snake():
    global food

    head = snake[0]
    new = (head[0] + direction[0], head[1] + direction[1])

    if new[0] < 0 or new[1] < 0 or new[0] >= WIDTH or new[1] >= HEIGHT:
        reset_snake()

    snake.insert(0, new)

    if new == food:
        food = (random.randint(0, 29)*20, random.randint(0, 29)*20)
    else:
        snake.pop()

def reset_snake():
    global snake, direction
    snake = [(300, 300)]
    direction = (20, 0)

# ================= MENU =================
def draw_menu():
    screen.fill(BG)
    title = font.render("Neon Game Hub", True, WHITE)
    t1 = font.render("Press 1: Tic Tac Toe", True, WHITE)
    t2 = font.render("Press 2: Snake", True, WHITE)

    screen.blit(title, (200, 120))
    screen.blit(t1, (180, 250))
    screen.blit(t2, (180, 300))

snake_timer = 0

# ================= LOOP =================
while True:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # MENU
        if state == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    state = "tic"
                if event.key == pygame.K_2:
                    state = "snake"

        # TIC TAC TOE
        elif state == "tic":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if 200 <= x <= 500 and 150 <= y <= 450:
                    col = (x - 200) // 100
                    row = (y - 150) // 100
                    idx = int(row * 3 + col)

                    if 0 <= idx < 9 and board[idx] == "":
                        board[idx] = turn
                        turn = "O" if turn == "X" else "X"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    board = [""] * 9
                    turn = "X"
                    state = "menu"

        # SNAKE
        elif state == "snake":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = (0, -20)
                if event.key == pygame.K_DOWN:
                    direction = (0, 20)
                if event.key == pygame.K_LEFT:
                    direction = (-20, 0)
                if event.key == pygame.K_RIGHT:
                    direction = (20, 0)
                if event.key == pygame.K_ESCAPE:
                    state = "menu"

    # DRAW STATES
    if state == "menu":
        draw_menu()

    elif state == "tic":
        draw_tic()

        winner = check_win()
        if winner:
            text = font.render(f"{winner} Wins!", True, GREEN)
            screen.blit(text, (220, 500))
            board[:] = [""] * 9
            turn = "X"

    elif state == "snake":
        snake_timer += 1
        if snake_timer % 5 == 0:
            move_snake()
        draw_snake()

    pygame.display.update()