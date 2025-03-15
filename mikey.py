import pygame
import datetime

pygame.init()

WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clock")

clock_img = pygame.image.load("mainclock.png")
rgh_hand_img = pygame.image.load("rightarm.png")
lft_hand_img = pygame.image.load("leftarm.png")
clock_img = pygame.transform.scale(clock_img, (900, 675))
lft_hand_img = pygame.transform.scale(lft_hand_img, (42, 700))
rgh_hand_img = pygame.transform.scale(rgh_hand_img, (933, 700))

CENTER = (WIDTH // 2, HEIGHT // 2)

def rotate_hand(surf, image, pos, angle):
    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=pos)
    surf.blit(rotated_image, new_rect.topleft)



running = True
while running:
    screen.fill((255, 255, 255))

    clock_rect = clock_img.get_rect(center=CENTER)
    screen.blit(clock_img, clock_rect.topleft)

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    minute_angle = minutes * 6 + 48
    second_angle = seconds * 6 + 4

    rotate_hand(screen, rgh_hand_img, CENTER, minute_angle)
    rotate_hand(screen, lft_hand_img, CENTER, second_angle)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False