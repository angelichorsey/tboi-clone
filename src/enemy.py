import pygame

class Enemy:
    def __init__(self, pos, speed=2, color=(0, 255, 0), size=20, health=3):
        """
        Initialize a new Enemy instance.

        Parameters:
            pos (tuple): The initial (x, y) position of the enemy.
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

    def draw(self, surface):
        """
        Draw the enemy as an upwards-pointing triangle on the provided surface.

        Parameters:
            surface (pygame.Surface): The surface to draw the enemy on.
        """

        x, y = self.pos
        half_size = self.size / 2
        points = [(x, y - self.size), (x - half_size, y + half_size), (x + half_size, y + half_size)]
        pygame.draw.polygon(surface, self.color, points)
