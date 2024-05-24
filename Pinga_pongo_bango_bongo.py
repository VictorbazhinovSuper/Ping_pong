from pygame import *
from random import *
from time import time as timer

cet_okna = 250,40,80

window = display.set_mode((700,500))
window.fill(cet_okna)
display.set_caption('Шутер')


font.init()
font = font.SysFont('Arial', 70)

#font2 = font.SysFont('Arial',20)

ower1 = font.render(
    'Player 1 lose', True, (255,215,0)
)

ower2 = font.render(
    'Player 2 lose', True, (255,215,0)
)


lost = 0
chet = 0


class Labamba_a(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_w,player_h,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w,player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Labamba_a):
    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
        


fafa_right = Player('Tenis_rocket.png',600,450,50,50,5)
fifi_left = Player('Tenis_rocket.png',50,450,50,50,5)
Much_ball_navernoe = Labamba_a('Much_ball.png',300,235,50,50,5)


speed_x = 5
speed_y = 5

finish = False

FPS = 60
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            pass


    if finish != True:

        window.fill(cet_okna)
        
        fafa_right.update_right()
        

        fifi_left.update_left()
        

        Much_ball_navernoe.rect.x += speed_x
        Much_ball_navernoe.rect.y += speed_y
        if Much_ball_navernoe.rect.y >= 450 or Much_ball_navernoe.rect.y <= 0:
            speed_y *= -1
        if sprite.collide_rect(fafa_right,Much_ball_navernoe) or sprite.collide_rect(fifi_left,Much_ball_navernoe):
            speed_x *= -1

        if Much_ball_navernoe.rect.x > 700:
            finish = True
            window.blit(ower2,(200,200))
        if Much_ball_navernoe.rect.x < 0:
            finish = True
            window.blit(ower1,(200,200))

        Much_ball_navernoe.reset()
        fafa_right.reset()
        fifi_left.reset()

    clock.tick(FPS)
    display.update()
