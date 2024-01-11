import pygame
import sys
import os


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
    'wall': load_image('void.png'),
    'empty': load_image('escalibur.png'),
    'tuda': load_image('path.png')
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
            tile_width * pos_x + 15, tile_height * pos_y - 16)

        self.pos = (pos_x, pos_y)

    def move(self, x, y):
        self.pos = (x, y)
        self.rect = self.image.get_rect().move(
            tile_width * self.pos[0] + 15, tile_height * self.pos[1] - 16)


player = None

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

level_map = load_level('cave.txt')


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

    elif movement == 'right':
        if x < level_x - 1 and (level_map[y][x + 1] == '.' or level_map[y][x + 1] == '>'
                                or level_map[y][x + 1] == '@'):
            player.move(x + 1, y)


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('tuda', x, y)
                new_player = Player(x, y)
            elif level[y][x] == '>':
                Tile('tuda', x, y)

    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


player, level_x, level_y = generate_level(load_level('cave.txt'))


def start():
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

        screen.fill('black')
        tiles_group.draw(screen)
        player_group.draw(screen)

        pygame.display.flip()
        clock.tick(50)

    pygame.quit()
