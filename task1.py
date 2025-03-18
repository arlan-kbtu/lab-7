import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MickeyClock")

clock_face = pygame.image.load("mickeyclock.jpeg")
right_hand = pygame.image.load("hand2.png")
left_hand = pygame.image.load("hand2.png")

clock_face = pygame.transform.scale(clock_face, (WIDTH, HEIGHT))
right_hand = pygame.transform.scale(right_hand, (95, 30))
left_hand = pygame.transform.scale(left_hand, (120, 30))

center_x, center_y = WIDTH // 2, HEIGHT // 2

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_face, (0, 0))
    
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    
    sec_angle = -seconds * 6
    min_angle = -minutes * 6
    
    rotated_left_hand = pygame.transform.rotate(left_hand, sec_angle)
    rotated_right_hand = pygame.transform.rotate(right_hand, min_angle)
    
    left_hand_rect = rotated_left_hand.get_rect(center=(center_x, center_y))
    right_hand_rect = rotated_right_hand.get_rect(center=(center_x, center_y))
    
    screen.blit(rotated_left_hand, left_hand_rect.topleft)
    screen.blit(rotated_right_hand, right_hand_rect.topleft)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    time.sleep(1)

pygame.quit()