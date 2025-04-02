import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2 
ball_speed = 20

running = True
while running:
    screen.fill(WHITE)  
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius) 
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
        elif event.type == pygame.KEYDOWN: 
            move_map = {
                pygame.K_UP: (0, -ball_speed),
                pygame.K_DOWN: (0, ball_speed),
                pygame.K_LEFT: (-ball_speed, 0),
                pygame.K_RIGHT: (ball_speed, 0)
            }
            if event.key in move_map:
                dx, dy = move_map[event.key]
                if 0 <= ball_x + dx - ball_radius <= WIDTH and 0 <= ball_y + dy - ball_radius <= HEIGHT:
                    ball_x += dx
                    ball_y += dy

pygame.quit()