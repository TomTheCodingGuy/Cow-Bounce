import pygame
from pygame.locals import *
import sys
import random
import time
 
pygame.init()
vec = pygame.math.Vector2 
 
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.09
FPS = 60
 
FramePerSec = pygame.time.Clock()

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
    
def game():
    background = pygame.image.load("./Images/background.jpg")
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Cow Bounce!!")
    
    pygame.mixer.init()
    bounce = pygame.mixer.Sound("bounce.mp3")
    
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__() 
            self.image = pygame.image.load("./Images/cow.png")
            self.surf = pygame.transform.scale(self.image,(30,30))
            self.rect = self.surf.get_rect()
       
            self.pos = vec((10, 360))
            self.vel = vec(0,0)
            self.acc = vec(0,0)#
            self.jumping = False
            self.score = 0 
     
        def move(self):
            self.acc = vec(0,0.5)
            pressed_keys = pygame.key.get_pressed()
                    
            if pressed_keys[K_LEFT]:
                self.acc.x = -ACC
            if pressed_keys[K_RIGHT]:
                self.acc.x = ACC
                     
            self.acc.x += self.vel.x * FRIC
            self.vel += self.acc
            self.pos += self.vel + 0.5 * self.acc
             
            if self.pos.x > WIDTH-13:
                self.pos.x = WIDTH-13
            if self.pos.x < 13:
                self.pos.x = 13         
            self.rect.midbottom = self.pos
     
        def jump(self):
            hits = pygame.sprite.spritecollide(self, platforms, False)
            if hits and not self.jumping:
               self.jumping = True
               self.vel.y = -15
        
        def cancel_jump(self):
            if self.jumping:
                if self.vel.y < -3:
                    self.vel.y = -3
     
        def update(self):
            hits = pygame.sprite.spritecollide(self ,platforms, False)
            if self.vel.y > 0:        
                if hits:
                    if self.pos.y < hits[0].rect.bottom:
                        if hits[0].point == True:
                            pygame.mixer.Sound.play(bounce)
                            hits[0].point = False
                            self.score += 1          
                        self.pos.y = hits[0].rect.top +1
                        self.vel.y = 0
                        self.jumping = False

    class Coin(pygame.sprite.Sprite):
        def __init__(self, pos):
            super().__init__()

            self.image = pygame.image.load("Coin.png")
            self.rect = self.image.get_rect()

            self.rect.topleft = pos

        def update(self):
            if self.rect.colliderect(P1.rect):
                P1.score += 5
                self.kill()
                
    class platform(pygame.sprite.Sprite):
        def __init__(self, width = 0, height = 18):
            super().__init__()
     
            if width == 0:
                width = random.randint(50, 120)
     
            self.image = pygame.image.load("./Images/platform.png")
            self.surf = pygame.transform.scale(self.image, (width, height))
            self.rect = self.surf.get_rect(center = (random.randint(0,WIDTH-10),
                                                     random.randint(0, HEIGHT-30)))
            
            self.point = True   
            self.moving = True
            self.speed = random.randint(-1, 1)

            if (self.speed == 0):
                self.moving == False
     
        def move(self):
            hits = self.rect.colliderect(P1.rect)
            if self.moving == True:  
                self.rect.move_ip(self.speed,0)
                if hits:
                    P1.pos += (self.speed, 0)
                if self.speed > 0 and self.rect.left > WIDTH:
                    self.rect.right = 0
                if self.speed < 0 and self.rect.right < 0:
                    self.rect.left = WIDTH
        
        def generateCoin(self):
            if (self.speed == 0):
                coins.add(Coin((self.rect.centerx, self.rect.centery - 50)))

    def check(platform, groupies):
        if pygame.sprite.spritecollideany(platform,groupies):
            return True
        else:
            for entity in groupies:
                if entity == platform:
                    continue
                if (abs(platform.rect.top - entity.rect.bottom) < 40) and (abs(platform.rect.bottom - entity.rect.top) < 40):
                    return True
            C = False
            
    def plat_gen():
        while len(platforms) < 6:
            width = random.randrange(50,100)
            p  = None      
            C = True
             
            while C:
                 p = platform()
                 p.rect.center = (random.randrange(0, WIDTH - width),
                                  random.randrange(-50, 0))
                 C = check(p, platforms)

            p.generateCoin()
            platforms.add(p)
            all_sprites.add(p)
     
    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    coins = pygame.sprite.Group()
            
    PT1 = platform(450, 80) 
    PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 13))
    PT1.moving = False
    PT1.point = False 
     
    P1 = Player()

    all_sprites.add(PT1)
    all_sprites.add(P1)
    platforms.add(PT1)
     
    for x in range(random.randint(4, 5)):
        C = True
        pl = platform()
        while C:
            pl = platform()
            C = check(pl, platforms)
        pl.generateCoin()
        platforms.add(pl)
        all_sprites.add(pl)
     
    while True:
        P1.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_SPACE:
                    P1.jump()
            if event.type == pygame.KEYUP:    
                if event.key == pygame.K_SPACE:
                    P1.cancel_jump()

        if P1.rect.top > HEIGHT:
            for entity in all_sprites:
                entity.kill()
                time.sleep(1)
                displaysurface.fill((0,0,0))
                f = pygame.font.SysFont("Verdana", 30)     
                g = f.render("Game Over Dude", True, (255,0,0,))
                s = f.render("Score: "+str(P1.score), True, (255,0,0))
                displaysurface.blit(g, (80, HEIGHT/2))
                displaysurface.blit(s, (120, HEIGHT/2+30)) 
                pygame.display.update()
                time.sleep(1)
                game()
     
        if P1.rect.top <= HEIGHT / 3:
            P1.pos.y += abs(P1.vel.y)
            for plat in platforms:
                plat.rect.y += abs(P1.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()

            for coin in coins:
                coin.rect.y += abs(P1.vel.y)
                if coin.rect.top >= HEIGHT:
                    coin.kill()
                    
     
        plat_gen()
        displaysurface.blit(background, (0, 0))
        f = pygame.font.SysFont("Verdana", 20)     
        g  = f.render(str(P1.score), True, (123,255,0))   
        displaysurface.blit(g, (WIDTH/2, 10))   
         
        for entity in all_sprites:
            displaysurface.blit(entity.surf, entity.rect)
            entity.move()

        for coin in coins:
            displaysurface.blit(coin.image, coin.rect)
            coin.update()
     
        pygame.display.update()
        FramePerSec.tick(FPS)

game()
