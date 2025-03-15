import pygame

pygame.init()
clock = pygame.time.Clock()
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball")
radius = 25
running = True
x, y = 250, 250
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]: y = max(radius, y - 20)
    if pressed[pygame.K_DOWN]: y = min(height - radius, y + 20)
    if pressed[pygame.K_LEFT]: x = max(radius, x - 20)
    if pressed[pygame.K_RIGHT]: x = min(width - radius, x + 20)

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    clock.tick(60)
    pygame.display.flip()