import pygame
import random
import math
import random

pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle Royale Mini")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)

SKY = (90, 160, 255)
GROUND = (70, 170, 80)
WHITE = (255,255,255)
BROWN = (139,69,19)
RED = (220,70,70)
BLUE = (50,100,255)

player = pygame.Rect(100, 450, 40, 60)
velocity_y = 0
on_ground = False
health = 100
score = 0
bullets = []
platforms = [pygame.Rect(0, 510, WIDTH, 90)]
builds = []
enemies = []

for _ in range(5):
    enemies.append(pygame.Rect(random.randint(500, 950), 450, 40, 60))

running = True
while running:
    dt = clock.tick(60)
    # dynamic sky with sun
    for y in range(HEIGHT):
   
        c = (90, min(180 + y//8, 220), 255)
        pygame.draw.line(screen, c, (0, y), (WIDTH, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                velocity_y = -15
            if event.key == pygame.K_q:
                builds.append(pygame.Rect(player.centerx + 30, player.y + 20, 80, 20))

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            bullets.append([player.centerx, player.centery, mx, my])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= 5
    if keys[pygame.K_d]:
        player.x += 5

    velocity_y += 0.7
    player.y += velocity_y
    on_ground = False

    for p in platforms + builds:
        if player.colliderect(p) and velocity_y >= 0:
            player.bottom = p.top
            velocity_y = 0
            on_ground = True

    for bullet in bullets[:]:
        x, y, tx, ty = bullet
        dx = tx - x
        dy = ty - y
        dist = max((dx**2 + dy**2)**0.5, 1)
        bullet[0] += dx / dist * 12
        bullet[1] += dy / dist * 12

        if bullet[0] < 0 or bullet[0] > WIDTH or bullet[1] < 0 or bullet[1] > HEIGHT:
            bullets.remove(bullet)
            continue

        for enemy in enemies[:]:
            if enemy.collidepoint(bullet[0], bullet[1]):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 1
                break

    for enemy in enemies:
        if enemy.x < player.x:
            enemy.x += 1
        else:
            enemy.x -= 1

        if player.colliderect(enemy):
            health -= 0.1

    pygame.draw.rect(screen, GROUND, (0, 510, WIDTH, 90))
    for x in range(0, WIDTH, 40):
        pygame.draw.circle(screen, (90,190,90), (x, 520), 12)

    for b in builds:
        pygame.draw.rect(screen, BROWN, b)

    # player with more stylized look
    pygame.draw.rect(screen, (35,55,170), player, border_radius=8)
    pygame.draw.rect(screen, (255,220,180), (player.x+8, player.y+6, 24, 18), border_radius=6)
    pygame.draw.rect(screen, (20,20,20), (player.x+12, player.y+2, 16, 10), border_radius=4)

    for enemy in enemies:
        pygame.draw.rect(screen, (200,60,70), enemy, border_radius=8)
        pygame.draw.rect(screen, (255,220,180), (enemy.x+8, enemy.y+6, 24, 18), border_radius=6)

    for bullet in bullets:
        pygame.draw.circle(screen, WHITE, (int(bullet[0]), int(bullet[1])), 4)

    screen.blit(font.render(f"Health: {int(health)}", True, WHITE), (20,20))
    screen.blit(font.render(f"Elims: {score}", True, WHITE), (20,55))
    screen.blit(font.render("A/D move  SPACE jump  Mouse shoot  Q build", True, WHITE), (20, 90))

    # inventory bar
    pygame.draw.rect(screen, (30,30,40), (WIDTH//2-220, HEIGHT-70, 440, 50), border_radius=12)
    for i in range(5):
        pygame.draw.rect(screen, (90,90,110), (WIDTH//2-205 + i*85, HEIGHT-60, 70, 30), border_radius=8)

    # sun
    pygame.draw.circle(screen, (255,240,120), (850, 90), 45)

    # clouds
    for cx, cy in [(160,80),(350,120),(620,90)]:
        pygame.draw.circle(screen, (245,245,255), (cx, cy), 25)
        pygame.draw.circle(screen, (245,245,255), (cx+30, cy), 30)
        pygame.draw.circle(screen, (245,245,255), (cx+55, cy), 22)

    # simple trees
    for tx in [120, 280, 760, 910]:
        pygame.draw.rect(screen, (120,80,40), (tx, 455, 14, 60))
        pygame.draw.circle(screen, (40,150,60), (tx+7, 445), 28)

    if health <= 0:
        game_over = font.render("Game Over", True, WHITE)
        screen.blit(game_over, (WIDTH//2 - 80, HEIGHT//2))

    pygame.display.flip()

pygame.quit()

