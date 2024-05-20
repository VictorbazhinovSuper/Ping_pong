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

win = font.render(
    'YOU WIN', True, (255,215,0)
)

ower = font.render(
    'GAME OWER', True, (255,215,0)
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
        fafa_right.reset()

        fifi_left.update_left()
        fifi_left.reset()


    clock.tick(FPS)
    display.update()