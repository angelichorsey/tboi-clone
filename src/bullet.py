import pygame as pg
from mixins import BoundAwareSprite

class Bullet(BoundAwareSprite):
    def __init__(self, pos, direction, *groups, speed=10, radius=5, color=(255, 0, 0), damage=1):
        super().__init__(*groups)
        """
        Initialize a new Bullet instance.

        Parameters:
            pos (tuple): The starting (x, y) position of the bullet.
            groups (pg.sprite.Group): any sprite groups this should be added to.
            direction (tuple): The normalized (x, y) direction vector for bullet travel.
            speed (int, optional): The speed of the bullet.
            radius (int, optional): The radius of the bullet.
            color (tuple, optional): The RGB color of the bullet.
            damage (int, optional): The damage inflicted by the bullet.
        """

        self.pos = list(pos)
        self.speed = speed
        self.radius = radius
        self.color = color
        self.damage = damage
        self.velocity = [direction[0] * speed, direction[1] * speed]

        self.image = pg.Surface((self.radius * 2, self.radius * 2), pg.SRCALPHA)
        pg.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        """
        Update the bullets position.
        """

        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

        self.rect.center = self.pos

        # inherited from BoundAwareSprite
        self.check_bounds()

    def handle_out_of_bounds(self):
        # remove from all sprite groups
        self.kill()
