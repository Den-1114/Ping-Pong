from pygame import *

window = display.set_mode((1520, 780))
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
            if keys_pressed[K_DOWN] and self.rect.y < 680:
                self.rect.y += self.speed
        else:
            if keys_pressed[K_w] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys_pressed[K_s] and self.rect.y < 680:
                self.rect.y += self.speed
    
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def colliderect(self, rect):
        return self.rect.colliderect(rect)


Player1 = Platform(0, 255, 0, 1470, 760/2, 10, 100, 'a', 6)
Player2 = Platform(255, 0, 0, 50, 760/2, 10, 100, 'b', 6)
Ball = GameSprite('ball.png', 350, 250, 70, 70, 5)

speed_x = 3
speed_y = 3

points_A = 0
points_B = 0
timer = 0
FPS_timer = 60
timer = 120
finish = False
font.init()
font1 = font.Font(None, 30)
A = False
B = False
b = False

A_Winner = font1.render(
    'Player A is winner!!!', True, (0, 255, 0)
)

B_Winner = font1.render(
    'Player B is winner!!!', True, (0, 255, 0)
)

Both_Winner = font1.render(
    'Both players are winners!!!', True, (0, 255, 0)
)

game = True
while game:
    window.fill((0, 0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False

    if A:
        window.blit(A_Winner, (220, 325))

    if B:
        window.blit(B_Winner, (220, 325))

    if b:
        window.blit(Both_Winner, (220, 325))

    if not finish:

        FPS_timer -= 1
        if FPS_timer == 0:
            FPS_timer = 60
        if FPS_timer == 60:
            timer -= 1

        if timer == 0:
            if points_A > points_B:
                A_Winner = font1.render(
                    'Player A is winner!!!', True, (0, 255, 0)
                )
                window.blit(A_Winner, (220, 325))
                A = True
                finish = True
                
            elif points_B > points_A:
                B_Winner = font1.render(
                    'Player B is winner!!!', True, (0, 255, 0)
                )
                window.blit(B_Winner, (220, 325))
                B = True
                finish = True

            else:
                Both_Winner = font1.render(
                    'Both players are winners!!!', True, (0, 205, 0)
                )
                window.blit(Both_Winner, (220, 325))
                b = True
                finish = True

        timer_lb = font1.render(
            str(timer) + 'seconds left', True, (255, 255, 255)
        )

        window.blit(timer_lb, (660, 10))
        score_A = font1.render(
            'Player A Points: ' + str(points_A), True, (255, 255, 255)
        )

        score_B = font1.render(
            'Player B Points: ' + str(points_B), True, (255, 255, 255)
        )

        window.blit(score_A, (1330, 10))
        window.blit(score_B, (25, 10))

        Ball.rect.x += speed_x
        Ball.rect.y += speed_y

        if Ball.colliderect(Player1.rect):
            speed_x *= -1

        if Ball.colliderect(Player2.rect):
            speed_x *= -1

        if Ball.rect.y < 0:
            speed_y *= -1
    
        if Ball.rect.y > 730:
            speed_y *= -1

        if Ball.rect.x > 1470:
            speed_x *= -1
            points_B += 1

        if Ball.rect.x < 0:
            speed_x *= -1
            points_A += 1
    
        Player1.draw_platform()
        Player1.update()
        Player2.draw_platform()
        Player2.update()
        Ball.draw()


    clock.tick(60)
    display.update()