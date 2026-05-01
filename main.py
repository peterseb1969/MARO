import pygame
import sys

# --- Setup ---
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MaRo Gaming - v0.2 Spielfigur")

clock = pygame.time.Clock()
FPS = 60

# Farben (R, G, B)
BG_COLOR     = (30, 30, 40)
PLAYER_COLOR = (220, 60, 60)

# --- Spielfigur ---
PLAYER_WIDTH  = 40
PLAYER_HEIGHT = 60
PLAYER_SPEED  = 5   # Pixel pro Frame

# Startposition: mittig am unteren Rand
player = pygame.Rect(
    (WIDTH - PLAYER_WIDTH) // 2,        # x
    HEIGHT - PLAYER_HEIGHT - 20,        # y (20 px Abstand vom unteren Rand)
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
)

# --- Hauptschleife ---
running = True
while running:

    # 1. Events abarbeiten
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Tastatur-Status abfragen (für gedrückt-gehaltene Tasten)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED

    # 3. Figur am Fensterrand stoppen
    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH

    # 4. Zeichnen
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, PLAYER_COLOR, player)

    # 5. Frame anzeigen und FPS begrenzen
    pygame.display.flip()
    clock.tick(FPS)

# --- Aufräumen ---
pygame.quit()
sys.exit()