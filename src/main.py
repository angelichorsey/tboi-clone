import pygame as pg
import sys
from player import Player
from enemy import Enemy
import random
# while this is no different than leaving all code outside of the function
# and running the file, putting it in a function now will be more extensible
# for future development
def main():
    # initialize all imported pg modules
    pg.init()
    # screen dimensions
    width, height = 800, 600
    # initialize a window or screen for display
    screen = pg.display.set_mode((width, height))
    # window title
    pg.display.set_caption("TBOI Clone")

    clock = pg.time.Clock()

    # initialize player and enemy
    player = Player((width // 2, height // 2))
    enemies = []
    spawns = [
        (100, -100), (50, 50), (75, -25)
    ]
    # initialize bullets as empty list
    bullets = []
    allsprites = pg.sprite.RenderPlain((player))

    running = True
    # game loop
    while running:
        # update the clock; 60 fps
        clock.tick(60)
        # check all events and stop the game loop if the window is closed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # get the state of all keys
        keys = pg.key.get_pressed()
        # move player based on WASD
        player.move(keys)
        # keep player in bounds
        player.update((width, height))

        # check if enemy still exists and update it's position based on player position
        if enemies:
            for enemy in enemies:
                enemy.update(player.pos)
        if len(enemies) <= 4:
            playerx = int(player.pos[0])
            playery = int(player.pos[1])
            xrange = list(range(0, playerx - 50)) + list(range(playerx + 50, width))
            yrange = list(range(0, playery - 50)) + list(range(playery + 50, height))
            enemy = Enemy((random.choice(xrange), random.choice(yrange)))
            enemies.append(enemy)

    
        # get current time
        current_time = pg.time.get_ticks()

        # initialize a bullet instance if arrow key is pressed, otherwise return None
        bullet = player.shoot(keys, current_time)
        # if a bullet was initialized, add it to the list of bullets on screen
        if bullet:
            bullets.append(bullet)

        # update the position of each bullet on the screen
        for bullet in bullets:
            bullet.update()
        # remove any bullets that reach the edge of the screen
        bullets = [b for b in bullets if 0 <= b.pos[0] <= width and 0 <= b.pos[1] <= height]

        # collision detection between bullets and enemy
        if enemies:
            for enemy in enemies: 
                dx = player.pos[0] - enemy.pos[0]
                dy = player.pos[1] - enemy.pos[1]
                distance = (dx**2 + dy**2) ** 0.5
                # if the distance is small enough
                if distance < player.radius + enemy.size / 2:
                    player.hp -= 1
        

            # go through each bullet in a copy of the bullets list (bullets[:] instead of just bullets)
            for bullet in bullets[:]:
                hit = False
                for enemy in enemies:
                    # and calculate the distance between the bullet and the enemy
                    dx = bullet.pos[0] - enemy.pos[0]
                    dy = bullet.pos[1] - enemy.pos[1]
                    distance = (dx**2 + dy**2) ** 0.5
                    # if the distance is small enough
                    if distance < bullet.radius + enemy.size / 2:
                        # reduce enemy health and remove the bullet
                        enemy.health -= bullet.damage
                        hit = True
                        # when health reaches 0, remove the enemy
                        if enemy.health <= 0:
                            player.fire_rate -= 10
                            enemies.remove(enemy)
                            break
                if hit: 
                    bullets.remove(bullet)

        # fill Surface with a solid color
        screen.fill((0, 0, 0))
        # draws a rectangle of the room
        pg.draw.rect(screen, (50, 50, 50), (0, 0, width, height))
        # draws the player
        # player.draw(screen)
        allsprites.draw(screen)
        # if the enemy exists, draw it
        if enemies:
            for enemy in enemies:
                enemy.draw(screen)
        # draw each bullet in bullets
        for bullet in bullets:
            bullet.draw(screen)
        # update the full display Surface to the screen
        pg.display.flip()

        if player.hp == 0:
            running = False
    # cleanup pg
    pg.quit()
    # exit script
    sys.exit()
