import pygame as pg
from bullet import Bullet

class Player(pg.sprite.Sprite):
    def __init__(self, pos, radius=20, speed=8, color=(255, 12, 255), fire_rate=500, health=3):
        pg.sprite.Sprite.__init__(self)
        """
        Initialize a new Player instance.

        Parameters:
            pos (tuple): The initial (x, y) position of the player.
            radius (int): The radius of the player's circle.
            speed (int): The movement speed of the player.
            color (tuple): The RGB color of the player.
            fire_rate (int): How often a bullet is fired in milliseconds.
        """
        self.pos = list(pos)
        self.radius = radius
        self.speed = speed
        self.color = color
        self.fire_rate = fire_rate # milliseconds
        self.last_shot_time = 0
        self.hp = health
        self.image = pg.Surface([self.radius * 2, self.radius * 2])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, keys):
        """
        Update the player's position based on the current key states.

        Parameters:
            keys (dict): A dictionary of key states as returned by pg.key.get_pressed().

        Notes:
            The method normalizes diagonal movement to ensure uniform speed.
        """

        move_keys = {
            pg.K_w: (0, -1),
            pg.K_s: (0, 1),
            pg.K_a: (-1, 0),
            pg.K_d: (1, 0)
        }
        dx, dy = 0, 0
        for key, (mx, my) in move_keys.items():
            if keys[key]:
                dx += mx
                dy += my
        if dx or dy:
            mag = (dx**2 + dy**2) ** 0.5
            dx, dy = dx / mag, dy / mag
        self.pos[0] += dx * self.speed
        self.pos[1] += dy * self.speed

    def update(self, bounds):
        """
        Clamp the player's position within the specified bounds.

        Parameters:
            bounds (tuple): The (width, height) limits for the player's movement.
        """

        self.pos[0] = max(self.radius, min(bounds[0] - self.radius, self.pos[0]))
        self.pos[1] = max(self.radius, min(bounds[1] - self.radius, self.pos[1]))

        self.rect.center = self.pos

    def shoot(self, keys, current_time):
        """
        Handle continuous shooting based on arrow key input.

        Parameters:
            keys (dict): A dictionary of key states as returned by pg.key.get_pressed().
            current_time (int): The current time in milliseconds from pg.time.get_ticks().

        Returns:
            Bullet or None: A new Bullet instance if the firing interval has elapsed and a valid
            arrow key is pressed; otherwise, None.
        """

        if current_time - self.last_shot_time < self.fire_rate:
            return None
        
        direction = None
        if keys[pg.K_UP]:
            direction = (0, -1)
        elif keys[pg.K_DOWN]:
            direction = (0, 1)
        elif keys[pg.K_LEFT]:
            direction = (-1, 0)
        elif keys[pg.K_RIGHT]:
            direction = (1, 0)
        
        if direction:
            self.last_shot_time = current_time
            return Bullet(self.pos, direction)
        
        return None
