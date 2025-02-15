import pygame as pg

class Bullet:
    def __init__(self, pos, direction, speed=10, radius=5, color=(255, 0, 0), damage=1):
        """
        Initialize a new Bullet instance.

        Parameters:
            pos (tuple): The starting (x, y) position of the bullet.
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

    def update(self):
        """
        Update the bullets position.
        """

        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

    def draw(self, surface):
        """
        Draw the bullet as a circle on the provided surface.

        Parameters:
            surface (pygame.Surface): The surface to draw the bullet on.
        """
        
        pg.draw.circle(surface, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius)
        