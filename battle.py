import pygame
import sys
import random
import os
from field2 import health_b, attack_b, shield_b, money


def start_new_turn(kartonochka, plus_m):
    f = open('money.txt', 'w')
    f.write(str(plus_m[0]))
    f.close()
    game(kartonochka)


def game(kartonochka):
    global player_health
    plus_m = [0]

    f_card = [0]
    s_card = [0]
    t_card = [0]
    fo_card = [0]

    k = 0

    fa = 500
    sa = 500
    ta = 500
    foa = 500

    f_card_en = [0]
    s_card_en = [0]
    t_card_en = [0]
    fo_card_en = [0]
    # Инициализация Pygame
    pygame.init()

    # Определение цветов
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)


    # Определение размеров окна
    WIDTH, HEIGHT = 1920, 1080
    hod1 = True
    hod2 = True
    hod3 = True
    hod4 = True
    # Создание окна
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Card Battle Field")

    # Загрузка изображений

    # Определение шрифтов
    font = pygame.font.Font(None, 36)
    # Инициализация игровых параметров

    if shield_b[0] == 0 and health_b[0] == 0:
        player_health = 30

    elif shield_b[0] == 1:
        player_health = 40

    elif health_b[0] == 1:
        player_health = 35

    if attack_b[0] == 1:
        damage = 25
    else:
        damage = 20
    opponent_health = 30

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

    cards = ['attack_c.png', 'shield_c.png', 'health_c.png', 'attack_c.png', 'attack_c.png']

    x1 = 380
    x2 = 680
    x3 = 980
    x4 = 1280

    y2 = y3 = y4 = 900
    xo = x1
    xs = x2
    xt = x3
    xf = x4

    f = random.choice(cards)
    s = random.choice(cards)
    t = random.choice(cards)
    fo = random.choice(cards)

    alls = ['attack_c.png', 'shield_c.png', 'health_c.png']
    one1 = random.choice(alls)
    one2 = random.choice(alls)
    one3 = random.choice(alls)
    one4 = random.choice(alls)

    # Основной цикл игры
    running = True
    while running:

        for event in pygame.event.get():
            first = pygame.transform.scale(load_image(f), (260, 280))
            first.set_alpha(fa)
            screen.blit(first, (380, 900))

            second = pygame.transform.scale(load_image(s), (260, 280))
            second.set_alpha(sa)
            screen.blit(second, (x2, y2))

            third = pygame.transform.scale(load_image(t), (260, 280))
            third.set_alpha(ta)
            screen.blit(third, (x3, y3))

            fourth = pygame.transform.scale(load_image(fo), (260, 280))
            fourth.set_alpha(foa)
            screen.blit(fourth, (x4, y4))

            sbros1 = pygame.transform.scale(load_image(f), (260, 280))
            sbros2 = pygame.transform.scale(load_image(s), (260, 280))
            sbros3 = pygame.transform.scale(load_image(t), (260, 280))
            sbros4 = pygame.transform.scale(load_image(fo), (260, 280))

            one1_card = pygame.transform.scale(load_image(one1), (260, 280))
            screen.blit(one1_card, (xo, -140))

            one2_card = pygame.transform.scale(load_image(one2), (260, 280))
            screen.blit(one2_card, (xs, -140))

            one3_card = pygame.transform.scale(load_image(one3), (260, 280))
            screen.blit(one3_card, (xt, -140))

            one4_card = pygame.transform.scale(load_image(one4), (260, 280))
            screen.blit(one4_card, (xf, -140))

            # определяем первую карту врага
            if one1 == 'attack_c.png':
                f_card_en.clear()
                f_card_en.append('att')

            elif one1 == 'shield_c.png':
                f_card_en.clear()
                f_card_en.append('def')

            else:
                f_card_en.clear()
                f_card_en.append('heal')

            # определяем вторую карту врага
            if one2 == 'attack_c.png':
                s_card_en.clear()
                s_card_en.append('att')

            elif one2 == 'shield_c.png':
                s_card_en.clear()
                s_card_en.append('def')

            else:
                s_card_en.clear()
                s_card_en.append('heal')

            # определяем третью карту врага
            if one3 == 'attack_c.png':
                t_card_en.clear()
                t_card_en.append('att')

            elif one3 == 'shield_c.png':
                t_card_en.clear()
                t_card_en.append('def')

            else:
                t_card_en.clear()
                t_card_en.append('heal')

            # определяем четвёртую карту врага
            if one4 == 'attack_c.png':
                fo_card_en.clear()
                fo_card_en.append('att')

            elif one4 == 'shield_c.png':
                fo_card_en.clear()
                fo_card_en.append('def')

            else:
                fo_card_en.clear()
                fo_card_en.append('heal')

            # ---------------------------

            card1 = pygame.transform.scale(load_image('closed.png'), (260, 280))
            screen.blit(card1, (xo, -140))

            card2 = pygame.transform.scale(load_image('closed.png'), (260, 280))
            screen.blit(card2, (xs, -140))

            card3 = pygame.transform.scale(load_image('closed.png'), (260, 280))
            screen.blit(card3, (xt, -140))

            card4 = pygame.transform.scale(load_image('closed.png'), (260, 280))
            screen.blit(card4, (xf, -140))

            # определяем первую карту
            if f == 'attack_c.png':
                f_card.clear()
                f_card.append('att')

            elif f == 'shield_c.png':
                f_card.clear()
                f_card.append('def')

            else:
                f_card.clear()
                f_card.append('heal')

            # определяем вторую карту
            if s == 'attack_c.png':
                s_card.clear()
                s_card.append('att')

            elif s == 'shield_c.png':
                s_card.clear()
                s_card.append('def')

            else:
                s_card.clear()
                s_card.append('heal')

            # определяем третью карту
            if t == 'attack_c.png':
                t_card.clear()
                t_card.append('att')

            elif t == 'shield_c.png':
                t_card.clear()
                t_card.append('def')

            else:
                t_card.clear()
                t_card.append('heal')

            # определяем четвёртую карту
            if fo == 'attack_c.png':
                fo_card.clear()
                fo_card.append('att')

            elif fo == 'shield_c.png':
                fo_card.clear()
                fo_card.append('def')

            else:
                fo_card.clear()
                fo_card.append('heal')

            if player_health <= 0:
                hod2 = hod3 = hod4 = hod1 = False

            elif opponent_health <= 0:
                opponent_health = 0
                hod2 = hod3 = hod4 = hod1 = False
                while k != 1:
                    k += 1
                    plus_m.clear()
                    plus_m.append(k)

            if event.type == pygame.QUIT:
                plus_m.clear()
                plus_m.append(0)
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

                elif event.key == pygame.K_1 and hod1:
                    if player_health <= 0 or opponent_health <= 0:
                        player_health = opponent_health = 0
                        hod2 = hod3 = hod4 = False
                    screen.blit(fon, (0, 0))
                    pygame.display.update()
                    fa -= 500

                    screen.blit(sbros1, (800, 400))
                    one1_card.set_alpha(0)
                    one3_card.set_alpha(0)
                    one4_card.set_alpha(0)
                    hod1 = False
                    screen.blit(one2_card, (500, 400))
                    if f_card[0] == 'att':
                        if s_card_en[0] == 'att':
                            player_health -= damage
                            opponent_health -= damage

                        elif s_card_en[0] == 'def':
                            pass

                        else:
                            opponent_health -= 10

                    # если атака--------------------------------------------------------------------------------

                    elif f_card[0] == 'def':
                        if s_card_en[0] == 'att':
                            pass

                        elif s_card_en[0] == 'def':
                            pass

                        else:
                            opponent_health += 5

                    # если защита--------------------------------------------------------------------------------

                    else:
                        if s_card_en[0] == 'att':
                            player_health -= 10

                        elif s_card_en[0] == 'def':
                            player_health += 5

                        else:
                            player_health += 5
                            opponent_health += 5
                # если хилл--------------------------------------------------------------------------------

                elif event.key == pygame.K_2 and hod2:
                    if player_health <= 0 or opponent_health <= 0:
                        player_health = opponent_health = 0
                        hod3 = hod4 = hod1 = False
                    screen.blit(fon, (0, 0))
                    pygame.display.update()
                    sa -= 500
                    screen.blit(sbros2, (800, 400))
                    one2_card.set_alpha(0)
                    one3_card.set_alpha(0)
                    one4_card.set_alpha(0)
                    hod2 = False
                    screen.blit(one1_card, (500, 400))
                    if s_card[0] == 'att':
                        if f_card_en[0] == 'att':
                            player_health -= damage
                            opponent_health -= damage

                        elif f_card_en[0] == 'def':
                            pass

                        else:
                            opponent_health -= 10
                    # если атака--------------------------------------------------------------------------------

                    elif s_card[0] == 'def':
                        if f_card_en[0] == 'att':
                            pass

                        elif f_card_en[0] == 'def':
                            pass

                        else:
                            opponent_health += 5

                    # если защита--------------------------------------------------------------------------------

                    else:
                        if f_card_en[0] == 'att':
                            player_health -= 10

                        elif f_card_en[0] == 'def':
                            player_health += 5

                        else:
                            player_health += 5
                            opponent_health += 5

                # если хилл--------------------------------------------------------------------------------

                elif event.key == pygame.K_3 and hod3:
                    if player_health <= 0 or opponent_health <= 0:
                        player_health = opponent_health = 0
                        hod2 = hod4 = hod1 = False
                    screen.blit(fon, (0, 0))
                    pygame.display.update()
                    ta -= 500
                    screen.blit(sbros3, (800, 400))
                    hod3 = False
                    one1_card.set_alpha(0)
                    one3_card.set_alpha(0)
                    one2_card.set_alpha(0)
                    screen.blit(one4_card, (500, 400))
                    if t_card[0] == 'att':
                        if fo_card_en[0] == 'att':
                            player_health -= damage
                            opponent_health -= damage

                        elif fo_card_en[0] == 'def':
                            pass

                        else:
                            opponent_health -= 10

                    # если атака--------------------------------------------------------------------------------

                    elif t_card[0] == 'def':
                        if fo_card_en[0] == 'att':
                            pass

                        elif fo_card_en[0] == 'def':
                            pass

                        else:
                            opponent_health += 5

                    # если защита--------------------------------------------------------------------------------

                    else:
                        if fo_card_en[0] == 'att':
                            player_health -= 10

                        elif fo_card_en[0] == 'def':
                            player_health += 5

                        else:
                            player_health += 5
                            opponent_health += 5
                # если хилл--------------------------------------------------------------------------------

                elif event.key == pygame.K_4 and hod4:
                    if player_health <= 0 or opponent_health <= 0:
                        player_health = opponent_health = 0
                        hod2 = hod3 = hod1 = False
                    screen.blit(fon, (0, 0))
                    pygame.display.update()
                    foa -= 500
                    screen.blit(sbros4, (800, 400))
                    one1_card.set_alpha(0)
                    one2_card.set_alpha(0)
                    one4_card.set_alpha(0)
                    hod4 = False
                    screen.blit(one3_card, (500, 400))
                    if fo_card[0] == 'att':
                        if t_card_en[0] == 'att':
                            player_health -= damage
                            opponent_health -= damage

                        elif t_card_en[0] == 'def':
                            pass

                        else:
                            opponent_health -= 10
                    # если атака--------------------------------------------------------------------------------

                    elif fo_card[0] == 'def':
                        if t_card_en[0] == 'att':
                            pass

                        elif t_card_en[0] == 'def':
                            pass

                        else:
                            opponent_health += 5
                    # если защита--------------------------------------------------------------------------------

                    else:
                        if fo_card_en[0] == 'att':
                            player_health -= 10

                        elif fo_card_en[0] == 'def':
                            player_health += 5

                        else:
                            player_health += 5
                            opponent_health += 5
                # если хилл--------------------------------------------------------------------------------
        end_turn_button = pygame.draw.rect(screen, (0, 255, 0), (0, 1000, 300, 75))
        text = font.render("Заново", True, BLACK)
        screen.blit(text, (10, 1020))

        if end_turn_button.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:  # Левая кнопка мыши
                start_new_turn(kartonochka, plus_m)

        font = pygame.font.Font(None, 50)
        pygame.draw.rect(screen, RED, (50, 45, 258, 75))  # Индикатор здоровья

        text = font.render(f"Здоровье: {player_health}", True, WHITE)
        screen.blit(text, (50, 70))

        att = pygame.transform.scale(load_image('attack_c.png'), (260, 280))
        screen.blit(att, (42, 600))

        opponent_portrait = pygame.transform.scale(load_image(f'{kartonochka}'), (150, 150))

        # Отрисовка оппонента
        screen.blit(opponent_portrait, (WIDTH - 210, 45))
        pygame.draw.rect(screen, RED, (1600, 350, 1620, 75))  # Индикатор здоровья
        text = font.render(f"Здоровье: {opponent_health}", True, WHITE)
        screen.blit(text, (1630, 370))

        pygame.display.flip()

    pygame.quit()
