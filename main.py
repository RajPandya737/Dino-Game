import pygame as pg
from sys import exit
pg.init()
WIDTH, HEIGHT = 800, 400
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill('White')
pg.display.set_caption("First Game")
clock = pg.time.Clock()
font = pg.font.Font('Assets/Minecraft.ttf', 30)

velocity = 5
velocity_sky = velocity//4

game_active = 0

player = pg.image.load('Assets/dino_dino.png').convert_alpha()
player_rect = player.get_rect(midbottom = (40, 270))
player_gravity = 0

text_start = font.render('PRESS SPACE TO START', False, 'black')

ground = pg.image.load('Assets/dino_ground.png').convert()
ground_rect = ground.get_rect(topleft = (0, 250))

sky = pg.image.load('Assets/dino_sky.png').convert()
sky_rect = sky.get_rect(topleft = (0, 0))
sky_x = 0


cactus_1 = pg.image.load('Assets/dino_cactus_1.png').convert_alpha()
cactus_1_rect = cactus_1.get_rect(midbottom = (800, 260))



while True:
    if game_active == 0:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                game_active+=1
        screen.blit(sky, sky_rect)
        screen.blit(ground, ground_rect)
        screen.blit(text_start, (300, 50))
        screen.blit(player, player_rect)
        screen.blit(cactus_1, cactus_1_rect)
    elif game_active == 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN and player_rect.bottom == 270:
                if event.key == pg.K_SPACE:
                    player_gravity = -20
        screen.blit(sky, sky_rect)
        screen.blit(ground, ground_rect)
        text_start = font.render('', False, 'black')
        screen.blit(text_start, (300, 50))
        screen.blit(player, player_rect)
        screen.blit(cactus_1, cactus_1_rect)
        cactus_1_rect.x-=velocity
        ground_rect.x-=velocity
        sky_rect.x-=velocity_sky
        if cactus_1_rect.right < -100: cactus_1_rect.x = 900
        if ground_rect.right<800: ground_rect.x = 0
        if sky_rect.right<800: 
            sky_rect.x = 0
            velocity+=2
        player_gravity+=1
        player_rect.y+=player_gravity
        if player_rect.bottom>=270:
            player_rect.bottom = 270 
        if player_rect.colliderect(cactus_1_rect):
            game_active = False
    else:
        pg.quit()
        quit()
    pg.display.update()
    clock.tick(60)
