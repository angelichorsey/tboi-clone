import random
import sys
import pygame as pg
from mixins import BoundAwareSprite
from player import Player
from enemy import Enemy

def main():
    pg.init()

    # Setting up game window
    width, height = 800, 600
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Not TBOI Clone")
    
    # set game window as the Rect to use for bounds
    BoundAwareSprite.SCREEN_RECT = screen.get_rect()

    # create clock
    clock = pg.time.Clock()

    # init sprite groups
    all_sprites = pg.sprite.RenderPlain()
    enemies = pg.sprite.Group()
    bullets = pg.sprite.Group()

    # init player
    player = Player((width // 2, height // 2), all_sprites)
    
    # loop that runs the game
    running = True
    while running:
        # update the clock (60 fps) and set current time
        clock.tick(60)
        current_time = pg.time.get_ticks()

        # check all events and stop the game loop if the window is closed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # get the state of all keys
        keys = pg.key.get_pressed()
        # move player based on WASD
        player.move(keys)
        player.update()

        # update all enemies (does nothing if enemies is empty)
        enemies.update(player.pos)

        if len(enemies) < 4:
            spawn_point = Enemy.get_valid_spawn(player.pos, 50, width, height)
            enemy = Enemy(spawn_point, all_sprites, enemies)

        # init a bullet instance if arrow key is pressed, otherwise return None
        bullet = player.shoot(keys, current_time)
        # if a bullet was initd, add it to the list of bullets on screen
        if bullet:
            bullet.add(all_sprites, bullets)

        # update the position of each bullet on the screen
        bullets.update()

        # collision detection between bullets and enemies
        # enemies can only lose health from bullet collision so killing logic is here, but may not in the future
        enemy_bullet_collisions = pg.sprite.groupcollide(enemies, bullets, False, True, collided=pg.sprite.collide_circle)
        for enemy, hits in enemy_bullet_collisions.items():
            enemy.health -= len(hits)
            if enemy.health <= 0:
                enemy.kill()

        # player collision with enemies
        player_enemies_collisions = pg.sprite.spritecollide(player, enemies, False, pg.sprite.collide_circle)
        player.health -= len(player_enemies_collisions)
        if player.health <= 0:
            running = False

        # fill Surface with a solid color then draw a rectangle the same size on top of it
        screen.fill((0, 0, 0))
        pg.draw.rect(screen, (50, 50, 50), (0, 0, width, height))
        
        # draw all sprites
        all_sprites.draw(screen)
        
        # update the full display Surface to the screen
        pg.display.flip()

    # cleanup pg
    pg.quit()
    # exit script
    sys.exit()
