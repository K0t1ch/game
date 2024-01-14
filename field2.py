import pygame
import sys
import os

FPS = 50

money = [0]
health_b = [0]
shield_b = [0]
attack_b = [0]

pygame.init()
size = width, height = 0, 1080
clock = pygame.time.Clock()
screen = pygame.display.set_mode((size), pygame.FULLSCREEN)


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


def terminate():
    pygame.quit()
    sys.exit()


def load_level(filename):
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


tile_images = {
    'wall': load_image('Rock2.png'),
    'empty': load_image('Polier2.png'),
    'bigr': load_image('B_rock2.png'),
    'empty_pole': load_image('E_gard2.png'),
    'treebs': load_image('tree2.png'),
    'water': load_image('water.png'),
    'tuda': load_image('path1.png'),
    'suda': load_image('path2.png'),
    'voin': load_image('voin.png'),
    'a_kto': load_image('a_kto.png')
}
player_image = load_image('allis.png')

tile_width = tile_height = 100


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x - 15, tile_height * pos_y - 2)

        self.pos = (pos_x, pos_y)

    def move(self, x, y):
        self.pos = (x, y)
        self.rect = self.image.get_rect().move(
            tile_width * self.pos[0] - 15, tile_height * self.pos[1] - 2)


player = None

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

level_map = load_level('field_map.txt')


def move(player, movement):
    x, y = player.pos
    if movement == 'up':
        if y > 0 and (level_map[round(y - 0.5)][round(x)] == '.' or level_map[round(y - 0.5)][round(x)] == '$' or
                      level_map[round(y - 0.5)][round(x)] == '@'):
            player.move(x, y - 0.5)

    elif movement == 'down':
        if y < level_y - 1 and (level_map[round(y + 0.5)][round(x)] == '.' or level_map[round(y + 0.5)][round(x)] == '$'
                                or level_map[round(y + 0.5)][round(x)] == '@'):
            player.move(x, y + 0.5)

    elif movement == 'left':
        if x > 0 and (level_map[round(y)][round(x - 0.5)] == '.' or level_map[round(y)][round(x - 0.5)] == '$' or
                      level_map[round(y)][round(x - 0.5)] == '@'):
            player.move(x - 0.5, y)

    elif movement == 'right':
        if x < level_x - 1 and (level_map[round(y)][round(x + 0.5)] == '.'
                                or level_map[round(y)][round(x + 0.5)] == '@'):
            player.move(x + 0.5, y)


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
            elif level[y][x] == '&':
                Tile('empty_pole', x, y)
            elif level[y][x] == '+':
                Tile('bigr', x, y)
            elif level[y][x] == '-':
                Tile('treebs', x, y)
            elif level[y][x] == '~':
                Tile('water', x, y)
            elif level[y][x] == '>':
                Tile('tuda', x, y)
            elif level[y][x] == '<':
                Tile('suda', x, y)
            elif level[y][x] == '!':
                Tile('voin', x, y)
            elif level[y][x] == '?':
                Tile('a_kto', x, y)

    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


player, level_x, level_y = generate_level(load_level('field_map.txt'))


# -------------------------------------------------------------------------------------------------------
def what():
    intro_text = ["Нажмите на любую кнопку чтобы закрыть",
                  "",
                  "",
                  "",
                  "",
                  "Чтобы купить предмет нажмите на цифру,"
                  "соответствующую его позиции"]

    fon = pygame.transform.scale(load_image('rule.png'), (1920, 1080))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 73)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                    return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


# -------------------------------------------------------------------------------------------------------

def shop():
    screen.fill('black')
    fon = pygame.transform.scale(load_image('inside_b.png'), (1920, 1080))
    screen.blit(fon, (0, 0))

    sold_out = pygame.transform.scale(load_image('sold_outc.png'), (150, 180))

    health = pygame.transform.scale(load_image('health_c.png'), (150, 180))

    shield = pygame.transform.scale(load_image('shield_c.png'), (150, 180))

    sword = pygame.transform.scale(load_image('attack_c.png'), (150, 180))

    if health_b[0] == 0:
        screen.blit(health, (110, 670))
    else:
        screen.blit(sold_out, (110, 670))

    if shield_b[0] == 0:
        screen.blit(shield, (410, 670))
    else:
        screen.blit(sold_out, (410, 670))

    if attack_b[0] == 0:
        screen.blit(sword, (710, 670))
    else:
        screen.blit(sold_out, (710, 670))

    font = pygame.font.Font(None, 70)
    text = font.render("Таинственная лавка!", True, (255, 255, 0))
    text_x = 700
    text_y = 170
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (255, 255, 0), (text_x - 10, text_y - 10,
                                             text_w + 20, text_h + 20), 5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # начинаем игру

                elif event.key == pygame.K_1:
                    money[0] -= 30
                    screen.blit(sold_out, (110, 670))
                    health_b.clear()
                    health_b.append(1)

                elif event.key == pygame.K_2:
                    money[0] -= 50
                    screen.blit(sold_out, (410, 670))
                    shield_b.clear()
                    shield_b.append(1)

                elif event.key == pygame.K_3:
                    money[0] -= 100
                    screen.blit(sold_out, (710, 670))
                    attack_b.clear()
                    attack_b.append(1)

        pygame.display.flip()
        clock.tick(FPS)


def inventory():
    screen.fill('black')
    fon = pygame.transform.scale(load_image('inventory.png'), (1920, 1080))
    screen.blit(fon, (0, 0))

    sold_out = pygame.transform.scale(load_image('sold_outc.png'), (150, 180))

    health = pygame.transform.scale(load_image('health_c.png'), (150, 180))

    shield = pygame.transform.scale(load_image('shield_c.png'), (150, 180))

    sword = pygame.transform.scale(load_image('attack_c.png'), (150, 180))

    if health_b[0] == 1:
        screen.blit(health, (110, 670))

    if shield_b[0] == 1:
        screen.blit(shield, (410, 670))

    if attack_b[0] == 1:
        screen.blit(sword, (710, 670))

    sry = 'Инвентарь, пока пусто('
    ok = 'Инвентарь'
    font = pygame.font.Font(None, 70)
    if health_b[0] == shield_b[0] == attack_b[0] == 0:
        text = font.render(sry, True, (255, 255, 0))
    else:
        text = font.render(ok, True, (255, 255, 0))
    text_x = 800
    text_y = 170
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (255, 255, 0), (text_x - 10, text_y - 10,
                                             text_w + 20, text_h + 20), 5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_e:
                    return  # начинаем игру

                elif event.key == pygame.K_1:
                    screen.blit(sold_out, (110, 670))
                    health_b.clear()
                    health_b.append(1)

                elif event.key == pygame.K_2:
                    screen.blit(sold_out, (410, 670))
                    shield_b.clear()
                    shield_b.append(1)

                elif event.key == pygame.K_3:
                    screen.blit(sold_out, (710, 670))
                    attack_b.clear()
                    attack_b.append(1)

        pygame.display.flip()
        clock.tick(FPS)

def letsgo():
    running = True

    while running:
        screen.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

                if event.key == pygame.K_w:
                    move(player, 'up')

                elif event.key == pygame.K_s:
                    move(player, 'down')

                elif event.key == pygame.K_a:
                    move(player, 'left')

                elif event.key == pygame.K_d:
                    move(player, 'right')

                elif event.key == pygame.K_e:
                    inventory()

        screen.fill('black')
        tiles_group.draw(screen)
        player_group.draw(screen)

        font = pygame.font.Font(None, 70)
        text = font.render(f"{money[0]}", True, (255, 255, 0))
        text_x = 1700
        text_y = 1000
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (255, 255, 0), (text_x - 10, text_y - 10,
                                                 text_w + 20, text_h + 20), 5)

        coin = pygame.transform.scale(load_image('монетка.png'), (150, 150))

        screen.blit(coin, (1800, 930))

        pygame.display.flip()
        clock.tick(50)

    pygame.quit()
