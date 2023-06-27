import pygame
import math

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

def shoot_bullet():
    bullet = pygame.image.load("bullet.png")
    bullet_rect = bullet.get_rect()
    bullet_rect.center = (400, 370)
    bullet_speed = 5

    return bullet, bullet_rect, bullet_speed

bullet, bullet_rect, bullet_speed = shoot_bullet()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dx = mouse_x - bullet_rect.x
            dy = mouse_y - bullet_rect.y
            distance = math.hypot(dx, dy)
            velocity_x = (dx / distance) * bullet_speed
            velocity_y = (dy / distance) * bullet_speed

            # Move the bullet towards the mouse position
            while distance > 0:
                bullet_rect.x += velocity_x
                bullet_rect.y += velocity_y
                distance -= bullet_speed

                # Clear the screen
                screen.fill((0, 0, 0))

                # Draw the bullet
                screen.blit(bullet, bullet_rect)

                # Update the display
                pygame.display.flip()

                # Limit the frame rate
                clock.tick(60)

pygame.quit()

