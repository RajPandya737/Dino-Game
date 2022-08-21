import pygame as pg
from sys import exit
pg.init()
WIDTH, HEIGHT = 800, 400
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill('White')
pg.display.set_caption("First Game")
clock = pg.time.Clock()
font = pg.font.Font('Assets/Minecraft.ttf', 30)

velocity = 4
velocity_sky = velocity//4

player = pg.image.load('Assets/dino_dino.png').convert_alpha()
player_rect = player.get_rect(midbottom = (40, 270))
player_y = 210

text_start = font.render('PRESS SPACE TO START', False, 'black')

ground = pg.image.load('Assets/dino_ground.png').convert()
ground_rect = ground.get_rect(topleft = (0, 250))

sky = pg.image.load('Assets/dino_sky.png').convert()
sky_rect = sky.get_rect(topleft = (0, 0))
sky_x = 0


cactus_1 = pg.image.load('Assets/dino_cactus_1.png').convert_alpha()
cactus_1_rect = cactus_1.get_rect(midbottom = (800, 260))



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    screen.blit(sky, sky_rect)
    screen.blit(ground, ground_rect)
    screen.blit(text_start, (300, 50))
    screen.blit(player, player_rect)
    screen.blit(cactus_1, cactus_1_rect)
    cactus_1_rect.x-=velocity
    ground_rect.x-=velocity
    sky_rect.x-=velocity_sky
    if cactus_1_rect.right < -100: cactus_1_rect.x = 900
    if ground_rect.right<800: ground_rect.x = 0
    if sky_rect.right<800: sky_rect.x = 0
    if player_rect.colliderect(cactus_1_rect):
        break
    
    pg.display.update()
    clock.tick(60)