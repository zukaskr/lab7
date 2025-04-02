import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

playlist = ["song1.mp3", "song2.mp3", "song3.mp3"]
current_track = 0  

def play_music():
    pygame.mixer.music.load(playlist[current_track]) 
    pygame.mixer.music.play()  
    print(f"Playing: {playlist[current_track]}")

def stop_music():
    pygame.mixer.music.stop()
    print("Music Stopped")

def change_track(step):
    global current_track
    current_track = (current_track + step) % len(playlist)  
    play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.KEYDOWN:
            actions = {
                pygame.K_p: lambda: (print("P Key Pressed - Play Music"), play_music()),
                pygame.K_s: lambda: (print("S Key Pressed - Stop Music"), stop_music()),
                pygame.K_n: lambda: (print("N Key Pressed - Next Track"), change_track(1)),
                pygame.K_b: lambda: (print("B Key Pressed - Previous Track"), change_track(-1))
            }
            if event.key in actions:
                actions[event.key]()  
    
    pygame.display.update()

pygame.quit()  
