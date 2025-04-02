import pygame
import datetime

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bg_image = pygame.image.load("clock.png")
min_hand_img = pygame.image.load("min_hand.png")
sec_hand_img = pygame.image.load("sec_hand.png")

center_pos = (WIDTH // 2, HEIGHT // 2)

def draw_clock():
    current_time = datetime.datetime.now()
    
    min_angle = - (current_time.minute * 6)
    sec_angle = - (current_time.second * 6)
    
    rotated_min_hand = pygame.transform.rotate(min_hand_img, min_angle)
    rotated_sec_hand = pygame.transform.rotate(sec_hand_img, sec_angle)
    
    min_hand_rect = rotated_min_hand.get_rect(center=center_pos)
    sec_hand_rect = rotated_sec_hand.get_rect(center=center_pos)
    
    screen.blit(bg_image, (0, 0))
    screen.blit(rotated_min_hand, min_hand_rect.topleft)
    screen.blit(rotated_sec_hand, sec_hand_rect.topleft)
    
    pygame.display.flip()

running = True
while running:
    screen.fill((255, 255, 255))
    draw_clock()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(1)

pygame.quit()
