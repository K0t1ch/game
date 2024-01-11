import pygame
import sys
import os
from itertools import cycle
from cave import start

FPS = 50

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
    'store': load_image('Store2.png'),
    'bigr': load_image('B_rock2.png'),
    'hole': load_image('Enter2.png'),
    'empty_pole': load_image('E_gard2.png'),
    'treebs': load_image('tree2.png'),
    'water': load_image('water.png'),
    'tuda': load_image('path1.png'),
    'suda': load_image('path2.png')
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
            tile_width * pos_x + 15, tile_height * pos_y + 5)

        self.pos = (pos_x, pos_y)

    def move(self, x, y):
        self.pos = (x, y)
        self.rect = self.image.get_rect().move(
            tile_width * self.pos[0] + 15, tile_height * self.pos[1] + 5)


player = None

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

level_map = load_level('map.txt')


def move(player, movement):
    x, y = player.pos
    if movement == 'up':
        if y > 0 and (level_map[y - 1][x] == '.' or level_map[y - 1][x] == '$' or level_map[y - 1][x] == '>' or
                      level_map[y - 1][x] == '@'):
            player.move(x, y - 1)

    elif movement == 'down':
        if y < level_y - 1 and (level_map[y + 1][x] == '.' or level_map[y + 1][x] == '$' or level_map[y + 1][x] == '>'
                                or level_map[y + 1][x] == '@'):
            player.move(x, y + 1)

    elif movement == 'left':
        if x > 0 and (level_map[y][x - 1] == '.' or level_map[y][x - 1] == '$' or level_map[y][x - 1] == '>' or
                      level_map[y][x - 1] == '@'):
            player.move(x - 1, y)

        elif x > 0 and level_map[y][x - 1] == '*':
            start()

    elif movement == 'right':
        if x < level_x - 1 and (level_map[y][x + 1] == '.' or level_map[y][x + 1] == '>'
                                or level_map[y][x + 1] == '@'):
            player.move(x + 1, y)

        elif x < level_x - 1 and level_map[y][x + 1] == '$':
            what()
            shop()


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
            elif level[y][x] == '$':
                Tile('store', x, y)
            elif level[y][x] == '&':
                Tile('empty_pole', x, y)
            elif level[y][x] == '*':
                Tile('hole', x, y)
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

    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


player, level_x, level_y = generate_level(load_level('map.txt'))


class LoadSceneOne:
    def __init__(self):
        pass

    def draw(self, screen):
        fon = pygame.transform.scale(load_image('load_screen.jpg'), (1920, 1080))
        screen.blit(fon, (0, 0))

        intro_text = ["Аллистар: Посмертная афера", "",
                      "Beta 1.0.3",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "Нажмите на любую кнопку чтобы начать"]

        font = pygame.font.Font(None, 100)
        text_coord = 70
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color(10, 18, 143))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

    def update(self, dt, events):
        pass


class LoadSceneTwo:
    def __init__(self):
        pass

    def draw(self, screen):
        fon = pygame.transform.scale(load_image('load_screen2.jpg'), (1920, 1080))
        screen.blit(fon, (0, 0))

        intro_text = ["Аллистар: Посмертная афера", "",
                      "Beta 1.0.3",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "Нажмите на любую кнопку чтобы начать"]

        font = pygame.font.Font(None, 100)
        text_coord = 70
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

    def update(self, dt, events):
        pass


class LoadSceneThree:
    def __init__(self):
        pass

    def draw(self, screen):
        fon = pygame.transform.scale(load_image('load_screen3.jpg'), (1920, 1080))
        screen.blit(fon, (0, 0))

        intro_text = ["Аллистар: Посмертная афера", "",
                      "Beta 1.0.3",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "Нажмите на любую кнопку чтобы начать"]

        font = pygame.font.Font(None, 100)
        text_coord = 70
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

    def update(self, dt, events):
        pass


class Fader:
    def __init__(self, scenes):
        self.scenes = cycle(scenes)
        self.scene = next(self.scenes)
        self.fading = None
        self.alpha = 0
        sr = pygame.display.get_surface().get_rect()
        self.veil = pygame.Surface(sr.size)
        self.veil.fill((0, 0, 0))

    def next(self):
        if not self.fading:
            self.fading = 'OUT'
            self.alpha = 0

    def draw(self, screen):
        self.scene.draw(screen)
        if self.fading:
            self.veil.set_alpha(self.alpha)
            screen.blit(self.veil, (0, 0))

    def update(self, dt, events):
        self.scene.update(dt, events)

        if self.fading == 'OUT':
            self.alpha += 8
            if self.alpha >= 255:
                self.fading = 'IN'
                self.scene = next(self.scenes)
        else:
            self.alpha -= 8
            if self.alpha <= 0:
                self.fading = None


def start_screen():
    screen_width, screen_height = 1920, 1080
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    dt = 0
    fader = Fader([LoadSceneOne(), LoadSceneTwo(), LoadSceneThree()])

    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.MOUSEMOTION:
                fader.next()

            if e.type == pygame.KEYDOWN:
                return

        fader.draw(screen)
        fader.update(dt, events)

        pygame.display.flip()
        dt = clock.tick(30)


# -------------------------------------------------------------------------------------------------------
def what():
    intro_text = ["Нажмите на любую кнопку чтобы закрыть",
                  "",
                  "",
                  "",
                  "",
                  "Чтобы купить предмет нажмите на цифру,"
                  "соответствующую его позиции"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (1920, 1080))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 73)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
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


start_screen()
def go():
    running = True

    while running:
        screen.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_w:
                    move(player, 'up')

                elif event.key == pygame.K_s:
                    move(player, 'down')

                elif event.key == pygame.K_a:
                    move(player, 'left')

                elif event.key == pygame.K_d:
                    move(player, 'right')

        screen.fill('black')
        tiles_group.draw(screen)
        player_group.draw(screen)

        pygame.display.flip()
        clock.tick(50)

    pygame.quit()

go()