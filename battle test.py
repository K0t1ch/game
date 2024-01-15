import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Определение размеров окна
WIDTH, HEIGHT = 800, 600

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Card Battle Field")

# Загрузка изображений
player_portrait = pygame.image.load("data/allis.png")
opponent_portrait = pygame.image.load("data/Rock2.png")

# Определение шрифтов
font = pygame.font.Font(None, 36)
# Инициализация игровых параметров
player_mana = 0
player_max_mana = 0
player_health = 30
opponent_health = 30
player_deck_size = 30
player_hand_size = 5
player_card_stock = 0

opponent_deck_size = 30
opponent_hand_size = 5
opponent_card_stock = 0

active_player = "player"  # "player" или "opponent"

# Флаг для определения, был ли уже сделан первый клик мыши
first_click = False

# Функция для начала нового хода
def start_new_turn():
    global player_mana, player_max_mana, player_card_stock, active_player

    if active_player == "player":
        player_max_mana += 1
        player_mana = player_max_mana
        player_card_stock += 1

        active_player = "opponent" if active_player == "player" else "player"

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                first_click = True  # Помечаем, что был сделан первый клик мыши

    if first_click:  # Проверяем, был ли сделан первый клик мыши

        # Очистка экрана
        screen.fill(WHITE)

        # Отрисовка игрока
        screen.blit(player_portrait, (50, 50))
        pygame.draw.rect(screen, BLUE, (50, 300, 100, 30))  # Индикатор манны
        pygame.draw.rect(screen, RED, (50, 350, 100, 30))  # Индикатор здоровья
        text = font.render(f"Mana: {player_mana}/{player_max_mana}", True, BLACK)
        screen.blit(text, (60, 305))
        text = font.render(f"Health: {player_health}", True, BLACK)
        screen.blit(text, (60, 355))
        text = font.render(f"Deck: {player_deck_size}", True, BLACK)
        screen.blit(text, (60, 405))
        text = font.render(f"Hand: {player_hand_size}", True, BLACK)
        screen.blit(text, (60, 455))
        text = font.render(f"Stock: {player_card_stock}", True, BLACK)
        screen.blit(text, (60, 505))

        # Отрисовка оппонента
        screen.blit(opponent_portrait, (WIDTH - 150, 50))
        pygame.draw.rect(screen, BLUE, (WIDTH - 150, 300, 100, 30))  # Индикатор манны
        pygame.draw.rect(screen, RED, (WIDTH - 150, 350, 100, 30))  # Индикатор здоровья
        text = font.render(f"Mana: ?", True, BLACK)
        screen.blit(text, (WIDTH - 140, 305))
        text = font.render(f"Health: {opponent_health}", True, BLACK)
        screen.blit(text, (WIDTH - 140, 355))
        text = font.render(f"Deck: {opponent_deck_size}", True, BLACK)
        screen.blit(text, (WIDTH - 140, 405))
        text = font.render(f"Hand: {opponent_hand_size}", True, BLACK)
        screen.blit(text, (WIDTH - 140, 455))
        text = font.render(f"Stock: {opponent_card_stock}", True, BLACK)
        screen.blit(text, (WIDTH - 140, 505))

        # Отрисовка кнопки "End Turn"
        end_turn_button = pygame.draw.rect(screen, (0, 255, 0), (350, 500, 100, 50))
        text = font.render("End Turn", True, BLACK)
        screen.blit(text, (365, 515))

        # Проверка нажатия на кнопку "End Turn"
        if end_turn_button.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:  # Левая кнопка мыши
                start_new_turn()

        # Обновление экрана
        pygame.display.flip()

# Завершение игры
pygame.quit()
