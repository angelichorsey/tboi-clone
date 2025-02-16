import pygame as pg

class BoundAwareSprite(pg.sprite.Sprite):
    """
    Mixing for any sprite class that needs to be aware of the screen boundary.
    """
    SCREEN_RECT = None

    def check_bounds(self):
        if BoundAwareSprite.SCREEN_RECT is None:
            raise RuntimeError("SCREEN_RECT is not set!")
        if not BoundAwareSprite.SCREEN_RECT.contains(self.rect):
            self.handle_out_of_bounds()

    def handle_out_of_bounds(self):
        """Default action when out-of-bounds. Subclasses should override."""
        pass
