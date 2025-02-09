import pygame
import sys
from player import Player
from enemy import Enemy

# initialize all imported pygame modules
pygame.init()
# screen dimensions
width, height = 800, 600
# initialize a window or screen for display
screen = pygame.display.set_mode((width, height))
# window title
pygame.display.set_caption("TBOI Clone")

clock = pygame.time.Clock()

# initialize player and enemy
player = Player((width // 2, height // 2))
enemy = Enemy((100, 100))
# initialize bullets as empty list
bullets = []

running = True
# game loop
while running:
    # update the clock; 60 fps
    clock.tick(60)
    # check all events and stop the game loop if the window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # get the state of all keys
    keys = pygame.key.get_pressed()
    # move player based on WASD
    player.move(keys)
    # keep player in bounds
    player.update((width, height))

    # check if enemy still exists and update it's position based on player position
    if enemy:
        enemy.update(player.pos)

    # get current time
    current_time = pygame.time.get_ticks()

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
    if enemy:
        # go through each bullet in a copy of the bullets list (bullets[:] instead of just bullets)
        for bullet in bullets[:]:
            # and calculate the distance between the bullet and the enemy
            dx = bullet.pos[0] - enemy.pos[0]
            dy = bullet.pos[1] - enemy.pos[1]
            distance = (dx**2 + dy**2) ** 0.5
            # if the distance is small enough
            if distance < bullet.radius + enemy.size / 2:
                # reduce enemy health and remove the bullet
                enemy.health -= bullet.damage
                bullets.remove(bullet)
                # when health reaches 0, remove the enemy
                if enemy.health <= 0:
                    enemy = None
                    break

    # fill Surface with a solid color
    screen.fill((0, 0, 0))
    # draws a rectangle of the room
    pygame.draw.rect(screen, (50, 50, 50), (0, 0, width, height))
    # draws the player
    player.draw(screen)
    # if the enemy exists, draw it
    if enemy:
        enemy.draw(screen)
    # draw each bullet in bullets
    for bullet in bullets:
        bullet.draw(screen)
    # update the full display Surface to the screen
    pygame.display.flip()

# cleanup pygame
pygame.quit()
# exit script
sys.exit()
