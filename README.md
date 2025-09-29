# Asteroids (Python)

A simple 2D asteroid-shooting game written in Python. Your goal is to shoot as many asteroids as possible without colliding with any. Larger asteroids break into smaller ones when hit.

---

## Gameplay & Rules

- Control a player avatar (ship) in 2D space.  
- Move and shoot projectiles to destroy asteroids.  
- Asteroids come in different sizes; hitting a large one causes it to split into smaller pieces.  
- If your ship touches any asteroid, the game ends (you lose).  
- Score increases for every asteroid (or fragment) you destroy.

---

## Repository Structure
. </br>
├── asteroid.py # Asteroid / asteroid logic module </br>
├── asteroidfield.py # Management of multiple asteroids, spawning, movement </br>
├── circleshape.py # Shape / collision logic for circular objects </br>
├── constants.py # Game constants (e.g. screen size, speeds) </br>
├── main.py # Entry point / game loop </br>
├── player.py # Player / ship movement & shooting logic </br>
├── shot.py # Projectile / bullet logic </br>
├── requirements.txt # Python dependencies </br>
└── .gitignore </br>

---

## Requirements & Setup

- Python 3.7+ (or whatever minimum version you’ve tested)
- A library for graphics / game loop (e.g. `pygame`) — check `requirements.txt`

To set up: </br>
  git clone https://github.com/eraldvelcani/asteroids.git </br>
  cd asteroids </br>
  pip install -r requirements.txt </br>

---

## How to Play

Run the game: </br>
python main.py </br>

Controls (example — adapt if different in your implementation): </br>
  Arrow keys or WASD for moving / rotating; </br>
  Spacebar to shoot </br>
  Try to survive as long as possible, avoid collisions, and rack up a high score by destroying asteroids. </br>
