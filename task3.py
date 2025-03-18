import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Red Ball Movement")

ball_radius = 25
ball_color = (255, 0, 0)
bg_color = (255, 255, 255)
speed = 20

x, y = width // 2, height // 2

running = True
while running:
    screen.fill(bg_color)
    pygame.draw.circle(screen, ball_color, (x, y), ball_radius)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT and x - ball_radius - speed >= 0:
                x -= speed
            elif event.key == pygame.K_RIGHT and x + ball_radius + speed <= width:
                x += speed
            elif event.key == pygame.K_UP and y - ball_radius - speed >= 0:
                y -= speed
            elif event.key == pygame.K_DOWN and y + ball_radius + speed <= height:
                y += speed

pygame.quit()
