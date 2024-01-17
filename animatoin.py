import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Game Animation")

player_image = pygame.image.load("player_sprite.png")


player_rect = player_image.get_rect()
player_speed = 5
player_frame = 0
player_animation = [pygame.Rect(0, 0, 32, 48), pygame.Rect(32, 0, 32, 48), pygame.Rect(64, 0, 32, 48)]


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    screen.fill(WHITE)
    screen.blit(player_image, (player_rect.x, player_rect.y), player_animation[player_frame])

    player_frame = (player_frame + 1) % len(player_animation)

    pygame.display.flip()
    clock.tick(30)  # Установка FPS

pygame.quit()
sys.exit()
