from pygame import *

window = display.set_mode((700, 500))
clock = time.Clock()
display.set_caption('Ping Pong')

class Platform(sprite.Sprite):
    def __init__(self, color1, color2, color3, x, y, width, heigth, Player, speed):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = width
        self.heigth = heigth
        self.image = Surface((self.width, self.heigth))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.player = Player
        self.speed = speed
    def draw_platform(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        keys_pressed = key.get_pressed()
        if self.player == 'a':
            if keys_pressed[K_UP] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys_pressed[K_DOWN] and self.rect.y < 400:
                self.rect.y += self.speed
        else:
            if keys_pressed[K_w] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys_pressed[K_s] and self.rect.y < 400:
                self.rect.y += self.speed
    
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_x))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def colliderect(self, rect):
        return self.rect.colliderect(rect)


Player1 = Platform(255, 255, 255, 650, 150, 10, 100, 'a', 6)
Player2 = Platform(255, 255, 255, 50, 150, 10, 100, 'b', 6)
Ball = GameSprite('ball.png', 350, 250, 70, 70, 5)


game = True
while game:
    window.fill((0, 0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    Player1.draw_platform()
    Player1.update()
    Player2.draw_platform()
    Player2.update()
    Ball.draw()


    clock.tick(60)
    display.update()