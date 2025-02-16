import random
import pygame as pg

class Enemy(pg.sprite.Sprite):
    def __init__(self, pos, *groups, speed=2, color=(0, 255, 0), size=20, health=3):
        super().__init__(*groups)
        """
        Initialize a new Enemy instance.

        Parameters:
            pos (tuple): The initial (x, y) position of the enemy.
            groups (pg.sprite.Group): any sprite groups this should be added to.
            speed (int): The movement speed of the enemy.
            color (tuple): The RGB color of the enemy.
            size (int): The size of the enemy's triangle.
            health (int): The hit points of the enemy.
        """

        self.pos = list(pos)
        self.speed = speed
        self.color = color
        self.size = size
        self.health = health

        self.radius = size // 2

        self.image = pg.Surface((self.size, self.size), pg.SRCALPHA)
        # vertices of downward-facing triangle
        points = [
            (0, 0), # top left
            (self.size, 0), # top right
            (self.size // 2, self.size) # bottom mid
            ]
        pg.draw.polygon(self.image, self.color, points)
        self.rect = self.image.get_rect(center=pos)

    def update(self, target_pos):
        """
        Update the enemy's position to move towards the target.

        Parameters:
            target_pos (tuple): The (x, y) position of the target (e.g., the player).
        """

        dx = target_pos[0] - self.pos[0]
        dy = target_pos[1] - self.pos[1]
        distance = (dx**2 + dy**2) ** 0.5
        if distance:
            dx, dy = dx / distance, dy / distance
            self.pos[0] += dx * self.speed
            self.pos[1] += dy * self.speed
        
        self.rect.center = self.pos

    @staticmethod
    def get_valid_spawn(target_pos, safe_radius, width, height):
        while True:
            x = random.randint(0, width)
            y = random.randint(0, height)
            dx = x - target_pos[0]
            dy = y - target_pos[1]
            if dx * dx + dy * dy >= safe_radius * safe_radius:
                return (x, y)
