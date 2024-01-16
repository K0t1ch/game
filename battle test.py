import pygame
import sys
import random
import os

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Определение размеров окна
WIDTH, HEIGHT = 1920, 1080
hod = True
# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Card Battle Field")

# Загрузка изображений

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
first_click = True


# Функция для начала нового хода
def load_image(name, colorkey=None):
    fullname = os.path.join("data", name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


fon = pygame.transform.scale(load_image('fight.png'), (1920, 1080))
screen.blit(fon, (0, 0))

cards = ['attack_c.png', 'shield_c.png', 'health_c.png']

x1 = 380
x2 = 680
x3 = 980
x4 = 1280


y1 = y2 = y3 = y4 = 900
xo = x1
xs = x2
xt = x3
xf = x4
numbs = [xo, xs, xt, xf]
numb = random.choice(numbs)
f = random.choice(cards)
s = random.choice(cards)
t = random.choice(cards)
fo = random.choice(cards)

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
    gg = pygame.transform.scale(load_image('gg.png'), (260, 280))

    for event in pygame.event.get():
        first = pygame.transform.scale(load_image(f), (260, 280))
        screen.blit(first, (x1, y1))

        second = pygame.transform.scale(load_image(s), (260, 280))
        screen.blit(second, (x2, y2))

        third = pygame.transform.scale(load_image(t), (260, 280))
        screen.blit(third, (x3, y3))

        fourth = pygame.transform.scale(load_image(fo), (260, 280))
        screen.blit(fourth, (x4, y4))

        alls = [first, second, third, third, third]
        one = random.choice(alls)

        # ---------------------------

        card1 = pygame.transform.scale(load_image('closed.png'), (260, 280))
        screen.blit(card1, (xo, -140))

        card2 = pygame.transform.scale(load_image('closed.png'), (260, 280))
        screen.blit(card2, (xs, -140))

        card3 = pygame.transform.scale(load_image('closed.png'), (260, 280))
        screen.blit(card3, (xt, -140))

        card4 = pygame.transform.scale(load_image('closed.png'), (260, 280))
        screen.blit(card4, (xf, -140))

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_1 and hod:
                screen.blit(gg, (x1, 900))

                x1 += 500
                y1 -= 500
                hod = False
                screen.blit(one, (500, 400))

            elif event.key == pygame.K_2 and hod:
                screen.blit(gg, (x2, 900))
                x2 += 200
                y2 -= 500
                hod = False
                screen.blit(one, (500, 400))

            elif event.key == pygame.K_3 and hod:
                screen.blit(gg, (x3, 900))
                x3 += -100
                y3 -= 500
                hod = False
                screen.blit(one, (500, 400))

            elif event.key == pygame.K_4 and hod:
                screen.blit(gg, (x4, 900))
                x4 += -400
                y4 -= 500
                hod = False
                screen.blit(one, (500, 400))

    if first_click:  # Проверяем, был ли сделан первый клик мыши
        font = pygame.font.Font(None, 70)
        # Отрисовка игрока
        pygame.draw.rect(screen, RED, (50, 45, 258, 75))  # Индикатор здоровья

        text = font.render(f"Health: {player_health}", True, WHITE)
        screen.blit(text, (50, 70))

        text = font.render(f"Deck: {player_deck_size}", True, WHITE)
        screen.blit(text, (50, 400))

        text = font.render(f"Hand: {player_hand_size}", True, WHITE)
        screen.blit(text, (60, 455))

        text = font.render(f"Stock: {player_card_stock}", True, WHITE)
        screen.blit(text, (60, 505))

        att = pygame.transform.scale(load_image('attack_c.png'), (260, 280))
        screen.blit(att, (42, 600))

        opponent_portrait = pygame.transform.scale(load_image('a_kto.png'), (150, 150))

        # Отрисовка оппонента
        screen.blit(opponent_portrait, (WIDTH - 210, 45))
        pygame.draw.rect(screen, RED, (WIDTH - 150, 350, 100, 30))  # Индикатор здоровья
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
