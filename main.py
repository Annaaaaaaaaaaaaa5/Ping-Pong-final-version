from pygame import*
font.init()
#створюємо вікно і додаємо фон
window = display.set_mode((700, 500))
display.set_caption("Пінг-понг")
background = transform.scale(image.load("back.jpg"), (700, 500))

#створюємо клас батько
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#створюємо клас для граців
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__(player_image, player_x, player_y, player_speed, w, h)
    def update_r(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y>1:
            self.rect.y-=self.speed
        if keys_pressed[K_DOWN] and self.rect.y<210:
            self.rect.y+=self.speed
    def update_l(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_s] and self.rect.y<300:
            self.rect.y+=self.speed
        if keys_pressed[K_w] and self.rect.y>1:
            self.rect.y-=self.speed

#створюємо клас для м'яча
class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__(player_image, player_x, player_y, player_speed, w, h)
    def update(self):
        pass

#змінні
x1=640
x2=15
y=200
finish=False
clock = time.Clock()
FPS = 60
game=True
speed_x=3
speed_y=3

#створюємо спрайти
ball=Ball('ball.png', 310, 250, 3, 65, 65)
racketka_r=Player('racketka.png', x1, y, 3, 65, 380)
racketka_l=Player('racketka.png', x2, y, 3, 65, 380)

#додаємо текст
font1=font.Font(None,40)
f_text1=font1.render('Вітаємо 1 гравця! 2 гавець не засмучуйся:)', True, (255, 255, 0))
f_text2=font1.render('Вітаємо 2 гравця! 1 гавець не засмучуйся:)', True, (255, 255, 0))

#ігровий цикл
while game:
    if finish ==False:
        window.blit(background, (0, 0))
        ball.reset()
        racketka_r.update_r()
        racketka_l.update_l()
        racketka_l.reset()
        racketka_r.reset()
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y
        if sprite.collide_rect(racketka_l, ball) or sprite.collide_rect(racketka_r, ball):
            speed_x*=-1
        if ball.rect.y<1 or ball.rect.y>480:
            speed_y*=-1
    if ball.rect.x<0:
        finish=True
        window.blit(f_text1, (90, 200))
    if ball.rect.x>700:
        finish=True
        window.blit(f_text2, (90, 200))
    for e in event.get():
        if e.type == QUIT:
            game=False
    display.update()
    clock.tick(FPS)