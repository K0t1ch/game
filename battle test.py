import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Инициализация экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Card Game")

# Инициализация переменных
player_mana = 0
player_health = 100
bot_health = 100

# Инициализация колоды и колоды сброса
deck = ["Card1", "Card2", "Card3", "Card4", "Card5"]
discard_pile = []

# Функция для выдачи карт
def deal_cards(num_cards):
    return random.sample(deck, num_cards)

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отрисовка фона
    screen.fill(WHITE)

    # Отрисовка индикатора маны
    pygame.draw.rect(screen, BLUE, (10, 10, player_mana * 10, 20))

    # Отрисовка колоды
    pygame.draw.rect(screen, RED, (10, 50, 50, 80))

    # Отрисовка колоды сброса
    pygame.draw.rect(screen, RED, (80, 50, 50, 80))

    # Выдача карт игроку и боту
    player_hand = deal_cards(3)
    bot_hand = deal_cards(3)

    # Отображение карт на экране
    for i, card in enumerate(player_hand):
        pygame.draw.rect(screen, BLUE, (10 + i * 60, 150, 50, 80))
        font = pygame.font.Font(None, 36)
        text = font.render(card, True, WHITE)
        screen.blit(text, (20 + i * 60, 170))

    for i, card in enumerate(bot_hand):
        pygame.draw.rect(screen, RED, (10 + i * 60, 350, 50, 80))

    # Отрисовка счетчиков здоровья
    font = pygame.font.Font(None, 36)
    player_health_text = font.render(f"Player Health: {player_health}", True, BLACK)
    screen.blit(player_health_text, (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 50))

    bot_health_text = font.render(f"Bot Health: {bot_health}", True, BLACK)
    screen.blit(bot_health_text, (20, 20))

    # Обновление экрана
    pygame.display.flip()

# Завершение Pygame
pygame.quit()