import pygame
import sys

# --- Setup ---
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MaRo Gaming - Keyboard Test")

# A font for drawing text. None = default system font, 72 = size in pixels.
font = pygame.font.Font(None, 72)

# Clock to limit the frame rate
clock = pygame.time.Clock()

# Background color (R, G, B) and text color
BG_COLOR = (30, 30, 40)
TEXT_COLOR = (255, 255, 255)

# This will hold the name of the last key pressed
last_key = "Press any key..."

# --- Main loop ---
running = True
while running:

    # 1. Handle events (input, window close, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # pygame.key.name() turns a key code into a readable string
            last_key = pygame.key.name(event.key)
            print(f"Key pressed: {last_key}")

    # 2. Draw everything
    screen.fill(BG_COLOR)                         # clear screen
    text_surface = font.render(last_key, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)          # paste text onto screen

    # 3. Show the new frame
    pygame.display.flip()

    # 4. Limit to 60 frames per second
    clock.tick(60)

# --- Cleanup ---
pygame.quit()
sys.exit()