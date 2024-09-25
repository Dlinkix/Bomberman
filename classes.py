import pygame


class Player(pygame.sprite.Sprite):
    death = [pygame.image.load('Images/death1.png'), pygame.image.load('Images/death2.png'),
             pygame.image.load('Images/death3.png'),
             pygame.image.load('Images/death4.png'), pygame.image.load('Images/death5.png'),
             pygame.image.load('Images/death6.png'),
             pygame.image.load('Images/death7.png'), pygame.image.load('Images/death8.png'),
             pygame.image.load('Images/death9.png'),
             pygame.image.load('Images/death10.png'), pygame.image.load('Images/death11.png'),
             pygame.image.load('Images/death12.png'),
             pygame.image.load('Images/death13.png'), pygame.image.load('Images/death14.png'),
             pygame.image.load('Images/death15.png'),
             pygame.image.load('Images/death16.png'), pygame.image.load('Images/death17.png'),
             pygame.image.load('Images/death18.png'),pygame.image.load('Images/death19.png'),
             pygame.image.load('Images/death20.png')]
    p1walkLeft = [pygame.image.load('Images/p1left.png'), pygame.image.load('Images/p1left1.png'),
             pygame.image.load('Images/p1left2.png'),
             pygame.image.load('Images/p1left3.png'), pygame.image.load('Images/p1left2.png'),
             pygame.image.load('Images/p1left1.png'), pygame.image.load('Images/p1left.png')]
    p1walkLeftshield = [pygame.image.load('Images/p1leftshield.png'), pygame.image.load('Images/p1left1shield.png'),
                  pygame.image.load('Images/p1left2shield.png'),
                  pygame.image.load('Images/p1left3shield.png'), pygame.image.load('Images/p1left2shield.png'),
                  pygame.image.load('Images/p1left1shield.png'), pygame.image.load('Images/p1leftshield.png')]
    p1walkRight = [pygame.image.load('Images/p1right.png'), pygame.image.load('Images/p1right1.png'),
                  pygame.image.load('Images/p1right2.png'),
                  pygame.image.load('Images/p1right3.png'), pygame.image.load('Images/p1right2.png'),
                  pygame.image.load('Images/p1right1.png'), pygame.image.load('Images/p1right.png')]
    p1walkRightshield = [pygame.image.load('Images/p1rightshield.png'), pygame.image.load('Images/p1right1shield.png'),
                   pygame.image.load('Images/p1right2shield.png'),
                   pygame.image.load('Images/p1right3shield.png'), pygame.image.load('Images/p1right2shield.png'),
                   pygame.image.load('Images/p1right1shield.png'), pygame.image.load('Images/p1rightshield.png')]
    p1walkFront = [pygame.image.load('Images/p1front.png'), pygame.image.load('Images/p1front1.png'),
                   pygame.image.load('Images/p1front2.png'),
                   pygame.image.load('Images/p1front3.png'), pygame.image.load('Images/p1front2.png'),
                   pygame.image.load('Images/p1front1.png'), pygame.image.load('Images/p1front.png')]
    p1walkFrontshield = [pygame.image.load('Images/p1frontshield.png'), pygame.image.load('Images/p1front1shield.png'),
                   pygame.image.load('Images/p1front2shield.png'),
                   pygame.image.load('Images/p1front3shield.png'), pygame.image.load('Images/p1front2shield.png'),
                   pygame.image.load('Images/p1front1shield.png'), pygame.image.load('Images/p1frontshield.png')]
    p1walkBack = [pygame.image.load('Images/p1back.png'), pygame.image.load('Images/p1back1.png'),
                   pygame.image.load('Images/p1back2.png'),
                   pygame.image.load('Images/p1back3.png'), pygame.image.load('Images/p1back2.png'),
                   pygame.image.load('Images/p1back1.png'), pygame.image.load('Images/p1back.png')]
    p1walkBackshield = [pygame.image.load('Images/p1backshield.png'), pygame.image.load('Images/p1back1shield.png'),
                  pygame.image.load('Images/p1back2shield.png'),
                  pygame.image.load('Images/p1back3shield.png'), pygame.image.load('Images/p1back2shield.png'),
                  pygame.image.load('Images/p1back1shield.png'), pygame.image.load('Images/p1backshield.png')]
    p2walkLeft = [pygame.image.load('Images/p2left.png'), pygame.image.load('Images/p2left1.png'),
                  pygame.image.load('Images/p2left2.png'),
                  pygame.image.load('Images/p2left3.png'), pygame.image.load('Images/p2left2.png'),
                  pygame.image.load('Images/p2left1.png'), pygame.image.load('Images/p2left.png')]
    p2walkRight = [pygame.image.load('Images/p2right.png'), pygame.image.load('Images/p2right1.png'),
                   pygame.image.load('Images/p2right2.png'),
                   pygame.image.load('Images/p2right3.png'), pygame.image.load('Images/p2right2.png'),
                   pygame.image.load('Images/p2right1.png'), pygame.image.load('Images/p2right.png')]
    p2walkFront = [pygame.image.load('Images/p2front.png'), pygame.image.load('Images/p2front1.png'),
                   pygame.image.load('Images/p2front2.png'),
                   pygame.image.load('Images/p2front3.png'), pygame.image.load('Images/p2front2.png'),
                   pygame.image.load('Images/p2front1.png'), pygame.image.load('Images/p2front.png')]
    p2walkBack = [pygame.image.load('Images/p2back.png'), pygame.image.load('Images/p2back1.png'),
                  pygame.image.load('Images/p2back2.png'),
                  pygame.image.load('Images/p2back3.png'), pygame.image.load('Images/p2back2.png'),
                  pygame.image.load('Images/p2back1.png'), pygame.image.load('Images/p2back.png')]
    p2walkLeftshield = [pygame.image.load('Images/p2leftshield.png'), pygame.image.load('Images/p2left1shield.png'),
                  pygame.image.load('Images/p2left2shield.png'),
                  pygame.image.load('Images/p2left3shield.png'), pygame.image.load('Images/p2left2shield.png'),
                  pygame.image.load('Images/p2left1shield.png'), pygame.image.load('Images/p2leftshield.png')]
    p2walkRightshield = [pygame.image.load('Images/p2rightshield.png'), pygame.image.load('Images/p2right1shield.png'),
                   pygame.image.load('Images/p2right2shield.png'),
                   pygame.image.load('Images/p2right3shield.png'), pygame.image.load('Images/p2right2shield.png'),
                   pygame.image.load('Images/p2right1shield.png'), pygame.image.load('Images/p2rightshield.png')]
    p2walkFrontshield = [pygame.image.load('Images/p2frontshield.png'), pygame.image.load('Images/p2front1shield.png'),
                   pygame.image.load('Images/p2front2shield.png'),
                   pygame.image.load('Images/p2front3shield.png'), pygame.image.load('Images/p2front2shield.png'),
                   pygame.image.load('Images/p2front1shield.png'), pygame.image.load('Images/p2frontshield.png')]
    p2walkBackshield = [pygame.image.load('Images/p2backshield.png'), pygame.image.load('Images/p2back1shield.png'),
                  pygame.image.load('Images/p2back2shield.png'),
                  pygame.image.load('Images/p2back3shield.png'), pygame.image.load('Images/p2back2shield.png'),
                  pygame.image.load('Images/p2back1shield.png'), pygame.image.load('Images/p2backshield.png')]
    # Constructor function
    def __init__(self, x, y, number):
        super().__init__()
        self.image = pygame.Surface([24, 28])
        self.image.fill((0,0,0))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.front = True
        self.back = False
        self.left = False
        self.right = False
        self.number = number

        self.change_x = 0
        self.change_y = 0
        self.walkCount = 0
        self.walls = None

        self.alive = True
        self.canmove = True
        self.deathCount = 0
        self.gotomenu=False

        self.speed=3
        self.superspeed=False
        self.superspeedcount=0

        self.shield=False
        self.shieldcount=0

        self.megabombs=False
        self.megabombcount = 0

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
        if self.superspeed and self.change_x==0 and self.change_y==0:
            self.speed=6
            if self.superspeedcount>=150:
                self.superspeed = False
                self.speed=3
                self.superspeedcount=0

    def update(self):
        if self.canmove:
            self.rect.x += self.change_x
            if self.change_x <0:
                self.left=True
                self.right=False
                self.front=False
                self.back=False
            elif self.change_x >0:
                self.left=False
                self.right=True
                self.front=False
                self.back=False
            block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            for block in block_hit_list:
                if self.change_x > 0:
                    self.rect.right = block.rect.left
                else:
                    self.rect.left = block.rect.right
            self.rect.y += self.change_y
            if self.change_y <0:
                self.left=False
                self.right=False
                self.front=False
                self.back=True
            elif self.change_y >0:
                self.left=False
                self.right=False
                self.front=True
                self.back=False
            block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            for block in block_hit_list:
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                else:
                    self.rect.top = block.rect.bottom

    def draw(self, screen):
        if self.number == 1:
            screen.blit(pygame.image.load('Images2/'+str(self.megabombcount)+'megabombs.png'), (2, 0))
            if self.alive:
                if self.front:
                    if self.shield:
                        if self.change_y == 0:
                            screen.blit(pygame.image.load('Images/p1frontshield.png'),
                                        (self.rect.x, self.rect.y))
                        else:
                            if self.walkCount + 1 >= 21:
                                self.walkCount = 0
                            screen.blit(self.p1walkFrontshield[self.walkCount // 3], (self.rect.x, self.rect.y))
                            self.walkCount += 1
                    else:
                        if self.change_y == 0:
                            screen.blit(pygame.image.load('Images/p1front.png'),
                                        (self.rect.x, self.rect.y))
                        else:
                            if self.walkCount + 1 >= 21:
                                self.walkCount = 0
                            screen.blit(self.p1walkFront[self.walkCount // 3], (self.rect.x, self.rect.y))
                            self.walkCount += 1
                elif self.back:
                    if self.shield:
                        if self.change_y == 0:
                            screen.blit(pygame.image.load('Images/p1backshield.png'),
                                        (self.rect.x, self.rect.y))
                        else:
                            if self.walkCount + 1 >= 21:
                                self.walkCount = 0
                            screen.blit(self.p1walkBackshield[self.walkCount // 3], (self.rect.x, self.rect.y))
                            self.walkCount += 1
                    else:
                        if self.change_y == 0:
                            screen.blit(pygame.image.load('Images/p1back.png'),
                                        (self.rect.x, self.rect.y))
                        else:
                            if self.walkCount + 1 >= 21:
                                self.walkCount = 0
                            screen.blit(self.p1walkBack[self.walkCount // 3], (self.rect.x, self.rect.y))
                            self.walkCount += 1
                elif self.left:
                    if self.shield:
                        if self.change_x == 0:
                            screen.blit(pygame.image.load('Images/p1leftshield.png'),
                                        (self.rect.x, self.rect.y))
                        else:
                            if self.walkCount + 1 >= 21:
                                self.walkCount = 0
                            screen.blit(self.p1walkLeftshield[self.walkCount // 3], (self.rect.x, self.rect.y))
                            self.walkCount += 1
                    else:
                        if self.change_x == 0:
                            screen.blit(pygame.image.load('Images/p1left.png'),
                                        (self.rect.x, self.rect.y))
                        else:
                            if self.walkCount + 1 >= 21:
                                self.walkCount = 0
                            screen.blit(self.p1walkLeft[self.walkCount // 3], (self.rect.x, self.rect.y))
                            self.walkCount += 1
                elif self.right:
                    if self.shield:
                        if self.change_x == 0:
                            screen.blit(pygame.image.load('Images/p1rightshield.png'),
                                        (self.rect.x, self.rect.y))
                        else:
                            if self.walkCount + 1 >= 21:
                                self.walkCount = 0
                            screen.blit(self.p1walkRightshield[self.walkCount // 3], (self.rect.x, self.rect.y))
                            self.walkCount += 1
                    else:
                        if self.change_x == 0:
                            screen.blit(pygame.image.load('Images/p1right.png'),
                                        (self.rect.x, self.rect.y))
                        else:
                            if self.walkCount + 1 >= 21:
                                self.walkCount = 0
                            screen.blit(self.p1walkRight[self.walkCount // 3], (self.rect.x, self.rect.y))
                            self.walkCount += 1
        elif self.number == 2:
            screen.blit(pygame.image.load('Images2/'+str(self.megabombcount)+'megabombs.png'), (415, 0))
            if self.alive:
                if self.front:
                    if self.shield:
                        if self.change_y == 0:
                            screen.blit(pygame.image.load('Images/p2frontshield.png'),
                                        (self.rect.x, self.rect.y))
                        else:
                            if self.walkCount + 1 >= 21:
                                self.walkCount = 0
                            screen.blit(self.p2walkFrontshield[self.walkCount // 3], (self.rect.x, self.rect.y))
                            self.walkCount += 1
                    else:
                        if self.change_y == 0:
                            screen.blit(pygame.image.load('Images/p2front.png'),
                                        (self.rect.x, self.rect.y))
                        else:
                            if self.walkCount + 1 >= 21:
                                self.walkCount = 0
                            screen.blit(self.p2walkFront[self.walkCount // 3], (self.rect.x, self.rect.y))
                            self.walkCount += 1
                elif self.back:
                    if self.shield:
                        if self.change_y == 0:
                            screen.blit(pygame.image.load('Images/p2backshield.png'),
                                        (self.rect.x, self.rect.y))
                        else:
                            if self.walkCount + 1 >= 21:
                                self.walkCount = 0
                            screen.blit(self.p2walkBackshield[self.walkCount // 3], (self.rect.x, self.rect.y))
                            self.walkCount += 1
                    else:
                        if self.change_y == 0:
                            screen.blit(pygame.image.load('Images/p2back.png'),
                                        (self.rect.x, self.rect.y))
                        else:
                            if self.walkCount + 1 >= 21:
                                self.walkCount = 0
                            screen.blit(self.p2walkBack[self.walkCount // 3], (self.rect.x, self.rect.y))
                            self.walkCount += 1
                elif self.left:
                    if self.shield:
                        if self.change_x == 0:
                            screen.blit(pygame.image.load('Images/p2leftshield.png'),
                                        (self.rect.x, self.rect.y))
                        else:
                            if self.walkCount + 1 >= 21:
                                self.walkCount = 0
                            screen.blit(self.p2walkLeftshield[self.walkCount // 3], (self.rect.x, self.rect.y))
                            self.walkCount += 1
                    else:
                        if self.change_x == 0:
                            screen.blit(pygame.image.load('Images/p2left.png'),
                                        (self.rect.x, self.rect.y))
                        else:
                            if self.walkCount + 1 >= 21:
                                self.walkCount = 0
                            screen.blit(self.p2walkLeft[self.walkCount // 3], (self.rect.x, self.rect.y))
                            self.walkCount += 1
                elif self.right:
                    if self.shield:
                        if self.change_x == 0:
                            screen.blit(pygame.image.load('Images/p2rightshield.png'),
                                        (self.rect.x, self.rect.y))
                        else:
                            if self.walkCount + 1 >= 21:
                                self.walkCount = 0
                            screen.blit(self.p2walkRightshield[self.walkCount // 3], (self.rect.x, self.rect.y))
                            self.walkCount += 1
                    else:
                        if self.change_x == 0:
                            screen.blit(pygame.image.load('Images/p2right.png'),
                                        (self.rect.x, self.rect.y))
                        else:
                            if self.walkCount + 1 >= 21:
                                self.walkCount = 0
                            screen.blit(self.p2walkRight[self.walkCount // 3], (self.rect.x, self.rect.y))
                            self.walkCount += 1
        if self.alive == False and self.deathCount < 200:
            screen.blit(self.death[self.deathCount // 10], (self.rect.x, self.rect.y))
            self.deathCount += 1
        if self.deathCount >= 200:
            self.rect.x = 1000
            self.gotomenu=True
    def reset(self,x,y):
        self.gotomenu = False
        self.alive = True
        self.deathCount = 0
        self.rect.x = x
        self.rect.y = y
        self.canmove = True
        self.front = True
        self.change_x=0
        self.change_y=0
        self.superspeed=False
        self.speed=3
        self.shield=False
        self.megabombs=False
        self.megabombcount=0
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width,height], pygame.SRCALPHA, 32)
        image = self.image.convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
class powerup(pygame.sprite.Sprite):
    superspeedanimation=[pygame.image.load('Images/superspeed1.png'), pygame.image.load('Images/superspeed2.png'),
             pygame.image.load('Images/superspeed3.png'), pygame.image.load('Images/superspeed3.png'),
             pygame.image.load('Images/superspeed2.png'), pygame.image.load('Images/superspeed1.png')]
    shieldanimation = [pygame.image.load('Images/shield1.png'), pygame.image.load('Images/shield2.png'),
                           pygame.image.load('Images/shield3.png'), pygame.image.load('Images/shield3.png'),
                           pygame.image.load('Images/shield2.png'), pygame.image.load('Images/shield1.png')]
    megabombanimation = [pygame.image.load('Images2/megabombicon1.png'), pygame.image.load('Images2/megabombicon2.png'),
                       pygame.image.load('Images2/megabombicon3.png'), pygame.image.load('Images2/megabombicon3.png'),
                       pygame.image.load('Images2/megabombicon2.png'), pygame.image.load('Images2/megabombicon1.png')]
    def __init__(self, x, y, number):
        super().__init__()
        self.image = pygame.Surface([22, 28], pygame.SRCALPHA, 32)
        image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.number = number
        self.spawntimer=0
        self.respawntimer=0
        self.exists=True
        self.animationcount=0
    def draw(self, screen):
        if self.number==1:
            if self.exists and self.spawntimer>50:
                if self.animationcount + 1 >= 30:
                    self.animationcount = 0
                screen.blit(self.superspeedanimation[self.animationcount // 5], (self.rect.x, self.rect.y))
                self.animationcount += 1
        elif self.number==2:
            if self.exists and self.spawntimer > 50:
                if self.animationcount + 1 >= 30:
                    self.animationcount = 0
                screen.blit(self.shieldanimation[self.animationcount // 5], (self.rect.x, self.rect.y))
                self.animationcount += 1
        else:
            if self.exists and self.spawntimer > 50:
                if self.animationcount + 1 >= 30:
                    self.animationcount = 0
                screen.blit(self.megabombanimation[self.animationcount // 5], (self.rect.x, self.rect.y))
                self.animationcount += 1
    def reset(self):
        self.spawntimer=0
        self.respawntimer=0
        self.exists=True
class bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, bomb_count, bomb_type):
        super().__init__()
        self.image = pygame.Surface([22, 28], pygame.SRCALPHA, 32)
        image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.width = width
        self.height = height
        self.bomb_count = bomb_count
        self.bomb_type = bomb_type

        self.walls = None
        self.leftcheck = self.rect.x - 32
        self.rightcheck = self.rect.x + self.width
        self.upcheck = self.rect.y - 32
        self.downcheck = self.rect.y + self.height
        self.expleft = True
        self.doubleexpleft = True
        self.expright = True
        self.doubleexpright = True
        self.expup = True
        self.doubleexpup = True
        self.expdown = True
        self.doubleexpdown = True
        self.expboxlist = []

    def draw(self, screen):
        if self.bomb_count < 30:
            if self.bomb_type==0:
                screen.blit(pygame.image.load('Images/bomb3.png'), (self.rect.x, self.rect.y))
            else:
                screen.blit(pygame.image.load('Images2/megabomb3.png'), (self.rect.x, self.rect.y))
        elif self.bomb_count < 60:
            if self.bomb_type == 0:
                screen.blit(pygame.image.load('Images/bomb2.png'), (self.rect.x, self.rect.y))
            else:
                screen.blit(pygame.image.load('Images2/megabomb2.png'), (self.rect.x, self.rect.y))
        elif self.bomb_count < 90:
            if self.bomb_type == 0:
                screen.blit(pygame.image.load('Images/bomb1.png'), (self.rect.x, self.rect.y))
            else:
                screen.blit(pygame.image.load('Images2/megabomb1.png'), (self.rect.x, self.rect.y))
        elif self.bomb_count < 120:
            if self.bomb_type==0:
                for i in self.walls:
                    if i.rect.collidepoint(self.leftcheck,self.rect.y):
                        self.expleft = False
                    if i.rect.collidepoint(self.rightcheck,self.rect.y):
                        self.expright = False
                    if i.rect.collidepoint(self.rect.x,self.upcheck):
                        self.expup = False
                    if i.rect.collidepoint(self.rect.x,self.downcheck):
                        self.expdown = False
                screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.rect.y))
                self.expboxlist.append(pygame.Rect(self.rect.x, self.rect.y, 32, 32))
                if self.expleft:
                    screen.blit(pygame.image.load('Images/explosion.png'), (self.leftcheck, self.rect.y))
                    self.expboxlist.append(pygame.Rect(self.leftcheck, self.rect.y, 32, 32))
                    screen.blit(pygame.image.load('Images/explosion.png'), (self.leftcheck+16, self.rect.y))
                    self.expboxlist.append(pygame.Rect(self.leftcheck+16, self.rect.y, 32, 32))
                if self.expright:
                    screen.blit(pygame.image.load('Images/explosion.png'), (self.rightcheck, self.rect.y))
                    self.expboxlist.append(pygame.Rect(self.rightcheck, self.rect.y, 32, 32))
                    screen.blit(pygame.image.load('Images/explosion.png'), (self.rightcheck-16, self.rect.y))
                    self.expboxlist.append(pygame.Rect(self.rightcheck-16, self.rect.y, 32, 32))
                if self.expup:
                    screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.upcheck))
                    self.expboxlist.append(pygame.Rect(self.rect.x, self.upcheck, 32, 32))
                    screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.upcheck+16))
                    self.expboxlist.append(pygame.Rect(self.rect.x, self.upcheck+16, 32, 32))
                if self.expdown:
                    screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.downcheck))
                    self.expboxlist.append(pygame.Rect(self.rect.x, self.downcheck, 32, 32))
                    screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.downcheck-16))
                    self.expboxlist.append(pygame.Rect(self.rect.x, self.downcheck-16, 32, 32))
            elif self.bomb_type==1:
                for i in self.walls:
                    if i.rect.collidepoint(self.leftcheck, self.rect.y):
                        self.expleft = False
                    if i.rect.collidepoint(self.leftcheck-32, self.rect.y):
                            self.doubleexpleft = False
                    if i.rect.collidepoint(self.rightcheck, self.rect.y):
                        self.expright = False
                    if i.rect.collidepoint(self.rightcheck+32, self.rect.y):
                            self.doubleexpright = False
                    if i.rect.collidepoint(self.rect.x, self.upcheck):
                        self.expup = False
                    if i.rect.collidepoint(self.rect.x, self.upcheck-32):
                            self.doubleexpup = False
                    if i.rect.collidepoint(self.rect.x, self.downcheck):
                        self.expdown = False
                    if i.rect.collidepoint(self.rect.x, self.downcheck+32):
                            self.doubleexpdown = False
                screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.rect.y))
                self.expboxlist.append(pygame.Rect(self.rect.x, self.rect.y, 32, 32))
                if self.expleft:
                    screen.blit(pygame.image.load('Images/explosion.png'), (self.leftcheck, self.rect.y))
                    self.expboxlist.append(pygame.Rect(self.leftcheck, self.rect.y, 32, 32))
                    screen.blit(pygame.image.load('Images/explosion.png'), (self.leftcheck + 16, self.rect.y))
                    self.expboxlist.append(pygame.Rect(self.leftcheck + 16, self.rect.y, 32, 32))
                    if self.doubleexpleft:
                        screen.blit(pygame.image.load('Images/explosion.png'), (self.leftcheck-32, self.rect.y))
                        self.expboxlist.append(pygame.Rect(self.leftcheck-32, self.rect.y, 32, 32))
                        screen.blit(pygame.image.load('Images/explosion.png'), (self.leftcheck-16, self.rect.y))
                        self.expboxlist.append(pygame.Rect(self.leftcheck-16, self.rect.y, 32, 32))
                if self.expright:
                    screen.blit(pygame.image.load('Images/explosion.png'), (self.rightcheck, self.rect.y))
                    self.expboxlist.append(pygame.Rect(self.rightcheck, self.rect.y, 32, 32))
                    screen.blit(pygame.image.load('Images/explosion.png'), (self.rightcheck - 16, self.rect.y))
                    self.expboxlist.append(pygame.Rect(self.rightcheck - 16, self.rect.y, 32, 32))
                    if self.doubleexpright:
                        screen.blit(pygame.image.load('Images/explosion.png'), (self.rightcheck+32, self.rect.y))
                        self.expboxlist.append(pygame.Rect(self.rightcheck+32, self.rect.y, 32, 32))
                        screen.blit(pygame.image.load('Images/explosion.png'), (self.rightcheck+16, self.rect.y))
                        self.expboxlist.append(pygame.Rect(self.rightcheck+16, self.rect.y, 32, 32))
                if self.expup:
                    screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.upcheck))
                    self.expboxlist.append(pygame.Rect(self.rect.x, self.upcheck, 32, 32))
                    screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.upcheck + 16))
                    self.expboxlist.append(pygame.Rect(self.rect.x, self.upcheck + 16, 32, 32))
                    if self.doubleexpup:
                        screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.upcheck-32))
                        self.expboxlist.append(pygame.Rect(self.rect.x, self.upcheck-32, 32, 32))
                        screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.upcheck-16))
                        self.expboxlist.append(pygame.Rect(self.rect.x, self.upcheck-16, 32, 32))
                if self.expdown:
                    screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.downcheck))
                    self.expboxlist.append(pygame.Rect(self.rect.x, self.downcheck, 32, 32))
                    screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.downcheck - 16))
                    self.expboxlist.append(pygame.Rect(self.rect.x, self.downcheck - 16, 32, 32))
                    if self.doubleexpdown:
                        screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.downcheck+32))
                        self.expboxlist.append(pygame.Rect(self.rect.x, self.downcheck+32, 32, 32))
                        screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.downcheck+16))
                        self.expboxlist.append(pygame.Rect(self.rect.x, self.downcheck+16, 32, 32))