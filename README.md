# tboi-clone
Minimal copy of The Binding of Isaac. Copying something is a great way to learn.

Developed and tested using Python 3.10.2.

Pygame documentation: https://www.pygame.org/docs/

## How to run
```shell
git clone https://github.com/angelichorsey/tboi-clone.git
cd tboi-clone/
python -m venv venv
./venv/bin/Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

## Improvements
In no specific order of difficulty

* alternating bullet starting position (like tears alternating from Isaac's eyes)
* UI and HUD
* music and sound effects
* sprites instead of shapes
* bullet range / travel distance
* curving bullets
* knockback from bullets
* enemies that can fire bullets
* multiple enemies
* collision detection between player and enemy, reducing player health
* obstacles and collision detection between them and player, enemy
* enemy pathing around obstacles