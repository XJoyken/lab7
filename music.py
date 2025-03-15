import pygame
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
sp_img = pygame.image.load("spotify.png")
pygame.display.set_caption("SPOTIFY")
pygame.display.set_icon(sp_img)


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
LIGHT_BLUE = (100, 100, 255)

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.SysFont("arialblack", 20)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=10)
        text_surf = self.font.render(self.text, True, WHITE)
        text_x = self.rect.x + (self.rect.width - text_surf.get_width()) // 2
        text_y = self.rect.y + (self.rect.height - text_surf.get_height()) // 2
        screen.blit(text_surf, (text_x, text_y))

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

previous_button = Button(WIDTH // 2 - 300, HEIGHT // 2 + 100, 150, 60, "PREVIOUS", BLUE, LIGHT_BLUE)
next_button = Button(WIDTH // 2 + 150, HEIGHT // 2 + 100, 150, 60, "NEXT", BLUE, LIGHT_BLUE)
play_button = Button(WIDTH // 2 - 30, HEIGHT // 2 + 60, 60, 60, "PLAY", BLUE, LIGHT_BLUE)
stop_button = Button(WIDTH // 2 - 30, HEIGHT // 2 + 130, 60, 60, "STOP", BLUE, LIGHT_BLUE)

font = pygame.font.SysFont("arialblack", 28)
font2 = pygame.font.SysFont("arialblack", 20)
font3 = pygame.font.SysFont("arialblack", 18)

music_folder = "music"
music_list = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
current_track = 0
is_playing = False
is_paused = False

def play_music():
    global is_playing, is_paused
    if is_paused:
        pygame.mixer.music.unpause()
        is_paused = False
    else:
        pygame.mixer.music.load(os.path.join(music_folder, music_list[current_track]))
        pygame.mixer.music.play()
        is_playing = True

def stop_music():
    global is_playing, is_paused
    pygame.mixer.music.pause()
    is_paused = True
    is_playing = False

def next_track():
    global current_track, is_paused
    current_track = (current_track + 1) % len(music_list)
    is_paused = False
    play_music()

def previous_track():
    global current_track, is_paused
    current_track = (current_track - 1) % len(music_list)
    is_paused = False
    play_music()

running = True
while running:
    screen.fill((160, 160, 160))

    previous_button.draw(screen)
    next_button.draw(screen)
    play_button.draw(screen)
    stop_button.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif previous_button.is_clicked(event):
            previous_track()
        elif next_button.is_clicked(event):
            next_track()
        elif play_button.is_clicked(event):
            play_music()
        elif stop_button.is_clicked(event):
            stop_music()

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(20, 40, 760, 280))
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(20, 40, 760, 280), 10)

    music_text = font.render("MUSIC PLAYER", True, (0, 0, 0))
    player_text = font2.render("NOW PLAYING:", True, (0, 0, 0))
    track_name = os.path.splitext(music_list[current_track])[0]
    track_text = font3.render(track_name, True, (0, 0, 0))

    screen.blit(music_text, (WIDTH // 2 - music_text.get_width() // 2, 5))
    screen.blit(player_text, (WIDTH // 2 - player_text.get_width() // 2, 50))
    screen.blit(track_text, (WIDTH // 2 - track_text.get_width() // 2, 120))

    pygame.display.flip()

pygame.quit()