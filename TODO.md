# Features to Implement
My experience and any bias make judging programming difficulty...difficult. For now I'll categorize into Easy, Medium, and Hard. That may change.

Features I haven't organized and detailed yet:
* obstacles and collision detection between them and player, enemy
* enemy pathing around obstacles


## Difficulty - Easy
### Alternating Tears
When any character with two eyes fires tears, they alternate their starting position to left and right eyes.
* modules: `bullet`, `player`

### Tear Momentum
Tears don't always fire in a straight line with same velocity. If moving perpendicular to the firing direction, they curve. If moving into or away, they will start with more or less speed.
* modules: `bullet`, `main`, maybe `player`

### Tear Knockback
Getting hit by a tear should push the enemy back in some way, either reducing or resetting its movement.
* modules: `bullet`, `enemy`

### Multiple Enemies
On the harder end of easy. Making more enemies is easy enough as you can just add another Enemy object to the `main` module. Implementing spawn points, a list of enemies on the screen, and likely other changes are what makes it more difficult.
* modules: `main` and likely `enemy`

## Difficulty - Medium
### Player Collision
Easy enough to copy the collision logic for bullets+enemies in some way. I expect there to be edge cases to debug though, and that's why I am putting it in medium.

With enough new collision logic, we may want to dedicate a module to it.

* modules: `player`, `main`

### Range Stat
Currently the bullets travel to the bounds of the game and then disappear. Implementing this will need to add an attribute to bullets to keep track of their distance or the time they have been traveling. Both correlate to range.
* modules: `player`, `bullet`, `main`

### Enemy Projectiles
This is almost an easy difficulty, but it will need separate collision logic to detect the player being hit. It can mostly be copied from current collision logic for hitting an enemy. The firing direction can mostly be copied from logic for moving towards the player.
* modules: `enemy`, `bullet`

## Difficulty - Hard
### UI/HUD
Display information like health, room, stats. The difficulty of this feature is mostly because it depends on sprites being implemented. Otherwise it just pulls information from other resources.
* modules: `ui`

### Music and Sound Effects
Involving extra files for sound is a large feature. Loading them in should be easy enough, but it will be complex to work out the timing of when they play. It may even require developing our own event system.
* modules: `sound` and maybe `event`

### Sprites instead of Shapes
Actually creating the sprites isn't factored into this. Plus we can steal the ones from Issac, and therefore focus on the programming.

Implementing this feature is going to involve a lot of testing from tweaking the various timing of animations for the sprites.
* modules: all modules will need some modification
