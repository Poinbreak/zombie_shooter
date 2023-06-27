import pygame
import math
import random

pygame.init()
pygame.font.init()
pygame.display.set_caption("Zombie mania!!")

enemy_speed=1
#Player Health
health=pygame.font.SysFont("freesanbold.ttf",50)
player_health=100
healthbar=health.render(str(player_health),True,(0,0,0))
healthbar_rect=healthbar.get_rect()
healthbar_rect.center=(400,360)

over=pygame.font.SysFont("freesanbold.ttf",100)
gameover=over.render("GAME OVER",True,(255,0,255))
gameover_rect=healthbar.get_rect()
gameover_rect.center=(225,300)

icon1=pygame.image.load("Settings.png")
icon1_R=icon1.get_rect()
icon1_Rect=icon1_R.center=(650,150)
icon2=pygame.image.load("shop.png")
icon2_rect=icon2.get_rect()
icon2_rect_rect=icon2_rect.center=(600,150)

pygame.mouse.set_visible(True)
pygame.mouse.set_pos(300,300)
plyaerx,playery= pygame.math.Vector2(400,400)
time=0

enemy_x,enemy_y=pygame.math.Vector2(0,0)
angle=0

window_height=800
window_width=800

waves=1
no_enem=3

screen=pygame.display.set_mode((window_width,window_height))
bg=pygame.image.load("bg.png")
player_original = pygame.image.load("player.png")
player_rect=player_original.get_rect(center=(plyaerx,playery))


playerprotect=pygame.image.load("playerprotecarea.png")
playerprotect_rect=playerprotect.get_rect()
angle=0


def Player():
    screen.blit(player,player_rect)

l1=[10,40,120,54]

#enemies contains all the enemy rects

def SpawnEnemy(n):
    enemies = []
    for _ in range(n):
        enemy_original = pygame.image.load("enemyzombie.png")
        enemy_rect = enemy_original.get_rect()
        a=random.randint(1,4)
        #left
        if a==1:
            enemy_rect.x=0
            enemy_rect.y=random.randrange(0,window_height,32)
        #right
        elif a==2:
            enemy_rect.x=window_width
            enemy_rect.y=random.randrange(0,window_height,32)
        #top
        elif a==3:
            enemy_rect.x=random.randrange(0,window_width,32)
            enemy_rect.y=0
        #bottom
        else:
            enemy_rect.x=random.randrange(0,window_width,32)
            enemy_rect.y=window_height

        enemies.append([enemy_original, enemy_rect])
    return enemies

def blit_enemies(enemies):
    for enemy in enemies:
        screen.blit(enemy[0], enemy[1])

def enemyAttack():
    global enemy_speed
    global no_enem
    global player_health
    global screen
    for i in enemies:
        dx=player_rect.x-i[1].x
        dy=player_rect.y-i[1].y
        d=math.hypot(dx,dy)
        if d > 0:
            enemy_speed=1
            if i[1].colliderect(player_rect):
                #enemy fallback
                enemy_speed=-random.randint(50,200)
                if player_health>=5:
                    player_health-=5
                else:
                    player_health=0
                    enemy_speed=0
                no_enem=0
            enemy_velocity = pygame.math.Vector2(dx / d, dy / d) * enemy_speed
            i[1].x += enemy_velocity.x
            i[1].y += enemy_velocity.y



'''def shoot_gun():
    if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is pressed
        bullet_image = pygame.image.load("bullet.png")
        bullet_rect = bullet_image.get_rect(center=(400, 370))
        bullet_list.append((bullet_image, bullet_rect))'''

# Update bullets logic
def update_bullets():
    for bullet in bullet_list:
        bullet[1].x -= bullet_speed * math.cos(angle)
        bullet[1].y -= bullet_speed * math.sin(angle)

# Draw bullets on the screen
def draw_bullets():
    for bullet in bullet_list:
        screen.blit(bullet[0], bullet[1])



enemies = SpawnEnemy(no_enem)
bullet_image = pygame.image.load("bullet.png")
bullet_list = []
bullet_speed = 5

running=True

while running==True:
    if player_health>0:
        a=pygame.time.get_ticks()
    mousx,mousey=pygame.mouse.get_pos()
    dx=mousx-300
    dy=mousey-300
    angle = math.degrees(math.atan2(-dy,dx))
    screen.blit(bg,(100,100))
    screen.blit(playerprotect,(0,0))
    screen.blit(healthbar,healthbar_rect)
    screen.blit(icon1,(650,150))
    screen.blit(icon2,(600,150))

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running=False
    
    #rotation
    if player_health!=0:
        player=pygame.transform.rotate(player_original,angle-90)
    
    Player()
    
    blit_enemies(enemies)

    enemyAttack()

    healthbar = health.render(str(player_health), True, (0, 0, 0))
    
    a_timer_font=pygame.font.SysFont("freesanbold.ttf",30)
    a_timer=a_timer_font.render("Time Survived = "+str(a/1000)+"s",True,(0,0,0))
    timer_rect=a_timer.get_rect()
    timer_rect.center=(250,150)
    screen.blit(a_timer,timer_rect)


    '''if icon2.get_rect().collidepoint(pygame.mouse.get_pos()):
        icon2=pygame.image.load("shop_on_click.png")
        if pygame.MOUSEBUTTONDOWN:
            screen.blit(icon2,(600,150))'''

    if player_health<=0:
        screen.blit(gameover,gameover_rect)
        k=a/1000
        a_timer=a_timer_font.render("Time Survived = "+str(k)+"s",True,(0,0,0))
        screen.blit(a_timer,timer_rect)

    '''else:
        shoot_gun()
        update_bullets()
        draw_bullets()'''

    if no_enem==0:
        waves+=1
        no_enem=3*waves
            
    pygame.display.update()
