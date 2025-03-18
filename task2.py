import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

pygame.init()
pygame.mixer.init()

screen_width, screen_height = 600, 350
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("🎵 IOWA Music Player")

font_title = pygame.font.SysFont("Arial", 28, bold=True)
font_info = pygame.font.SysFont("Arial", 20)
font_keys = pygame.font.SysFont("Arial", 16)

music_dir = "music"
required_tracks = [
    "IOWA - Одно и То Же.mp3",
    "IOWA - Маршрутка.mp3",
    "IOWA - Улыбайся.mp3"
]

if not os.path.exists(music_dir):
    os.makedirs(music_dir)

tracks = [track for track in required_tracks if os.path.exists(os.path.join(music_dir, track))]
track_index = 0
status = "Играет"

def draw_interface():
    screen.fill((25, 25, 25))

    if tracks:
        title_text = font_title.render(tracks[track_index], True, (255, 255, 255))
        status_text = font_info.render(f"Статус: {status}", True, (200, 200, 200))
    else:
        title_text = font_title.render("Нет треков", True, (255, 100, 100))
        status_text = font_info.render("", True, (0, 0, 0))

    # Название трека и статус
    screen.blit(title_text, ((screen_width - title_text.get_width()) // 2, 90))
    screen.blit(status_text, ((screen_width - status_text.get_width()) // 2, 140))

    # Подсказки по клавишам
    keys = [
        "P — Play / Продолжить",
        "SPACE — Пауза",
        "S — Стоп",
        "N — Следующий трек",
        "B — Предыдущий трек",
        "ESC — Выход"
    ]

    for i, text in enumerate(keys):
        key_text = font_keys.render(text, True, (180, 180, 180))
        screen.blit(key_text, (20, 200 + i * 22))

    pygame.display.flip()

def play_track(index):
    path = os.path.join(music_dir, tracks[index])
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

if len(tracks) != len(required_tracks):
    print("⛔ Не все треки найдены в папке 'music'.")
    print("➡ Убедись, что в папке 'music' лежат файлы с такими названиями:")
    for name in required_tracks:
        print(f"  - {name}")
    exit()

play_track(track_index)

running = True

while running:
    draw_interface()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play()
                    status = "Играет"
                else:
                    pygame.mixer.music.unpause()
                    status = "Играет"
            elif event.key == pygame.K_SPACE:
                pygame.mixer.music.pause()
                status = "Пауза"
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                status = "Стоп"
            elif event.key == pygame.K_n:
                track_index = (track_index + 1) % len(tracks)
                play_track(track_index)
                status = "Играет"
            elif event.key == pygame.K_b:
                track_index = (track_index - 1) % len(tracks)
                play_track(track_index)
                status = "Играет"
            elif event.key == pygame.K_ESCAPE:
                running = False

pygame.quit()
