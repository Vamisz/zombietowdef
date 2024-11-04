'''
Tower-defence game code
'''
import sys
import math
import pygame as pg
pg.init()

class Monster(pg.sprite.Sprite):
    '''
    This is the Monster sprite class
    it's purpose is to spawn monsters with specific values of:
    -two walking images
    -initial position
    -velocity
    -its hitpoints
    -its damage(towards the player)
    -its value in GOLD when killed
    '''
    PLAYER_HP = 200
    ZCOUNT = 0
    SCOUNT = 0
    GZCOUNT = 0
    MCOUNT = 0
    WAVE = 0
    def __init__(self, mimage, wimage, initialx, initialy, velocity, hp, dmg, value):
        super().__init__()
        self.origin = mimage
        self.image = pg.image.load(mimage)
        self.wimage = wimage
        self.rect = self.image.get_rect()
        self.velocity = (velocity, velocity)
        self.rect.x = initialx
        self.rect.y = initialy
        self.position = (initialx, initialy)
        self.hp = hp
        self.dmg = dmg
        self.walk = 1
        self.rec = pg.time.get_ticks()
        self.walkcool = 180
        self.value = value
    
    def draw(self, surface):
        '''
        class function including surface blit
        and changing the image to create
        illusion of walking
        '''
        now = pg.time.get_ticks()
        if now - self.rec >= self.walkcool:
            self.rec = now
            if self.walk == 1:
                self.image = pg.image.load(self.wimage)
                self.walk = 0
            else:
                self.image = pg.image.load(self.origin)
                self.walk = 1
        surface.blit(self.image, self.position)
        


    def update(self):
        '''
        the function for moving the sprite across
        the field with specific coordinates (at corners)
        When arriving to the middle the monster enters
        the castle and deals damage
        '''
        if self.position[0] <= 805 and self.position[1] <= 20:
            self.position = (self.position[0] + self.velocity[0], self.position[1])
            self.rect.x = self.position[0]
            self.rect.y = self.position[1]
        if self.position[0] >= 805 and self.position[1] <= 600:
            self.position = (self.position[0], self.position[1] + self.velocity[1])
            self.rect.x = self.position[0]
            self.rect.y = self.position[1]
        if self.position[0] >= 80 and self.position[1] >= 600:
            self.position = (self.position[0] - self.velocity[0], self.position[1])
            self.rect.x = self.position[0]
            self.rect.y = self.position[1]
        if self.position[0] >= 70 and self.position[0] <= 85 and self.position[1] >= 150:
            self.position = (self.position[0], self.position[1] - self.velocity[1])
            self.rect.x = self.position[0]
            self.rect.y = self.position[1]
        if self.position[0] >= 70 and self.position[0] <= 230 and self.position[1] >= 150 and self.position[1] <= 200:
            self.position = (self.position[0] + self.velocity[0], self.position[1])
            self.rect.x = self.position[0]
            self.rect.y = self.position[1]
        if self.position[0] >= 230 and self.position[0] <= 290 and self.position[1] <= 210 and self.position[1] >= 120:
            self.position = (self.position[0], self.position[1] - self.velocity[1])
            self.rect.x = self.position[0]
            self.rect.y = self.position[1]
        if self.position[0] >= 230 and self.position[0] <= 630 and self.position[1] <= 120 and self.position[1] >= 100:
            self.position = (self.position[0] + self.velocity[0], self.position[1])
            self.rect.x = self.position[0]
            self.rect.y = self.position[1]
        if self.position[0] >= 630 and self.position[0] <= 635 and self.position[1] <= 480 and self.position[1] >= 100:
            self.position = (self.position[0], self.position[1] + self.velocity[1])
            self.rect.x = self.position[0]
            self.rect.y = self.position[1]
        if self.position[0] >= 240 and self.position[0] <= 635 and self.position[1] <= 480 and self.position[1] >= 470:
            self.position = (self.position[0] - self.velocity[0], self.position[1])
            self.rect.x = self.position[0]
            self.rect.y = self.position[1]
        if self.position[0] >= 240 and self.position[0] <= 245 and self.position[1] <= 480 and self.position[1] >= 300:
            self.position = (self.position[0], self.position[1] - self.velocity[1])
            self.rect.x = self.position[0]
            self.rect.y = self.position[1]
        if self.position[0] >= 240 and self.position[0] <= 316 and self.position[1] >= 300 and self.position[1] <= 310:
            self.position = (self.position[0] + self.velocity[0], self.position[1])
            self.rect.x = self.position[0]
            self.rect.y = self.position[1]
        if self.position[0] >= 316 and self.position[0] <= 320 and self.position[1] >= 300 and self.position[1] <= 310:
            self.deal_dmg()
            self.kill()

    def take_dmg(self, amount):
        '''
        Function for when the monster is dealt damage from towers
        including killing the monster if hitpoints fall below 0
        '''
        self.hp = self.hp - amount
        if self.hp <= 0:
            Button.GOLD = Button.GOLD + self.value
            self.kill()

    def deal_dmg(self):
        '''
        Function for when the monster passess the doors of the palace
        The function makes the player lose hp
        if hp below 0, they die
        '''
        Monster.PLAYER_HP = Monster.PLAYER_HP - self.dmg
        if Monster.PLAYER_HP <= 0:
            myfont = pg.font.Font('freesansbold.ttf', 48)
            msg = myfont.render("You Lost!", True, (255, 0, 0))
            msg_box = msg.get_rect()
            msg_box.center = (450, 350)
            SCR.blit(msg, msg_box)
            pg.display.flip()
            pg.time.wait(2000)
            sys.exit()


class Button(pg.sprite.Sprite):
    '''
    Class for initial buttons spawning towers
    with a class variable GOLD
    ID is for speific class instances
    '''
    GOLD = 200

    def __init__(self, posx, posy, ID):
        super().__init__()
        self.org = pg.image.load("buttonorg1.png")
        self.hov = pg.image.load("buttonhov1.png")
        self.image = self.org
        self.position = (posx, posy)
        self.rect = self.image.get_rect(topleft = self.position)
        self.ID = ID

    def draw(self, surface):
        surface.blit(self.image, self.position)

    def update(self, events):
        '''
        Function for lighting up when hovered
        and for buying towers
        Button kills itself after tower is bought to prevent bugs
        '''
        POS = pg.mouse.get_pos()
        HIT = self.rect.collidepoint(POS)
        if HIT:
            self.image = self.hov
        else:
            self.image = self.org
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN and HIT:
                if self.ID == 1:
                    if Button.GOLD >= 150:
                        TOWER1 = Tower(self.position[0] + 46, self.position[1] + 46, "towerfire.png")
                        towers.add(TOWER1)
                        self.kill()
                        Button.GOLD = Button.GOLD - 150
                if self.ID == 2:
                    if Button.GOLD >= 150:
                        TOWER2 = Tower(self.position[0] + 46, self.position[1] + 46, "towerfire.png")
                        towers.add(TOWER2)
                        self.kill()
                        Button.GOLD = Button.GOLD - 150
                if self.ID == 3:
                    if Button.GOLD >= 150:
                        TOWER3 = Tower(self.position[0] + 46, self.position[1] + 46, "towerfire.png")
                        towers.add(TOWER3)
                        self.kill()
                        Button.GOLD = Button.GOLD - 150
                if self.ID == 4:
                    if Button.GOLD >= 150:
                        TOWER4 = Tower(self.position[0] + 46, self.position[1] + 46, "towerfire.png")
                        towers.add(TOWER4)
                        self.kill()
                        Button.GOLD = Button.GOLD - 150
                if self.ID == 5:
                    if Button.GOLD >= 150:
                        TOWER5 = Tower(self.position[0] + 46, self.position[1] + 46, "towerfire.png")
                        towers.add(TOWER5)
                        self.kill()
                        Button.GOLD = Button.GOLD - 150
                if self.ID == 6:
                    if Button.GOLD >= 150:
                        TOWER6 = Tower(self.position[0] + 46, self.position[1] + 46, "towerfire.png")
                        towers.add(TOWER6)
                        self.kill()
                        Button.GOLD = Button.GOLD - 150
                if self.ID == 7:
                    if Button.GOLD >= 150:
                        TOWER7 = Tower(self.position[0] + 46, self.position[1] + 46, "towerfire.png")
                        towers.add(TOWER7)
                        self.kill()
                        Button.GOLD = Button.GOLD - 150
                if self.ID == 8:
                    if Button.GOLD >= 150:
                        TOWER8 = Tower(self.position[0] + 46, self.position[1] + 46, "towerfire.png")
                        towers.add(TOWER8)
                        self.kill()
                        Button.GOLD = Button.GOLD - 150


class BigButton(Button):
    '''
    Class Button for buying a bigger powerful tower
    '''
    def __init__(self, posx, posy, ID):
        super().__init__(posx, posy, ID)
        self.org = pg.image.load("buttonorg1.png")
        self.org = pg.transform.scale(self.org, (120, 120))
        self.hov = pg.image.load("buttonhov1.png")
        self.hov = pg.transform.scale(self.hov, (120, 120))
        self.image = self.org
        self.position = (posx, posy)
        self.rect = self.image.get_rect(topleft = self.position)
        self.ID = ID

    def update(self, events):
        '''
        Function for lighting up when hovered
        and for buying towers
        Button kills itself after tower is bought to prevent bugs
        '''
        POS = pg.mouse.get_pos()
        HIT = self.rect.collidepoint(POS)
        if HIT:
            self.image = self.hov
        else:
            self.image = self.org
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN and HIT:
                if Button.GOLD >= 1000:
                    BIGTOWER = BigTower(self.position[0], self.position[1], "bigtowerfire.png")
                    towers.add(BIGTOWER)
                    self.kill()
                    Button.GOLD = Button.GOLD - 1000



class Tower(pg.sprite.Sprite):
    '''
    Class for Towers shooting at monsters
    timage - image of the tower
    '''
    def __init__(self, posx, posy, timage):
        super().__init__()
        self.position = (posx, posy)
        self.image = pg.image.load(timage)
        self.rect = self.image.get_rect(center = self.position)
        self.target = self.angle = 0
        self.originalimage = self.image
        self.fired = 1
        self.last = pg.time.get_ticks()
        self.cooldown = 2700
        self.load = 700
        self.towerempty = "towerempty.png"
        self.towerfire = "towerfire.png"
        self.upgraded = 0
        self.built = 0
        self.damage = 80
        self.range = 250

    def update(self, monsters):
        '''
        Function for aiming at monsters and shooting
        ie. spawning bullets
        '''
        if len(monsters) > 0:
            self.built = 1
            now = pg.time.get_ticks()
            near = min(monsters, key=lambda s: math.hypot(self.rect.centerx-s.rect.centerx, self.rect.centery - s.rect.centery))
            self.target = math.atan2(near.rect.centerx - self.rect.centerx, near.rect.centery - self.rect.centery)
            self.target = math.degrees(self.target)
            angle_diff = (self.target - self.angle + 180) % 360 - 180
            self.angle += angle_diff * 0.1
            if now - self.last >= self.load:
                self.image = pg.image.load(self.towerfire)
                self.originalimage = self.image
            self.image = pg.transform.rotate(self.originalimage, self.angle + 180)
            self.rotated_rect = self.image.get_rect(center = self.rect.center)
            self.rect.center = self.position
            if self.fired == 0:
                if math.hypot(self.rect.centerx-near.rect.centerx, self.rect.centery - near.rect.centery) < self.range:
                    self.image = pg.image.load(self.towerempty)
                    self.rotated_rect = self.image.get_rect(center = self.position)
                    BULLET = Bullets(self.position[0] - 48, self.position[1] - 48, "arrowbolt.png", self.damage)
                    bullets.add(BULLET)
                    BULLET.update(self.angle, near)
                    pg.mixer.Sound.play(shoot_sound)
                    self.fired = 1
                    self.originalimage = self.image
            else:
                if now - self.last >= self.cooldown:
                    self.last = now
                    self.fired = 0
                    self.image = pg.image.load(self.towerfire)
                    self.originalimage = self.image
        else:
            self.rotated_rect = self.rect

    def upgrade(self, events):
        '''
        Function for upgrading the towers
        '''
        POS = pg.mouse.get_pos()
        HIT = self.rect.collidepoint(POS)
        if self.built == 1 and self.upgraded == 0:
            for event in events:
                if event.type == pg.MOUSEBUTTONDOWN and HIT:
                    if Button.GOLD >= 100:
                        upgrading = True
                        while upgrading:
                            for event in pg.event.get():
                                quit_game(event)
                                if event.type == pg.KEYDOWN:
                                    if event.key == pg.K_SPACE:
                                        upgrading = False
                                    if event.key ==pg.K_1:
                                        Button.GOLD = Button.GOLD - 100
                                        self.towerfire = "goldentowerfire.png"
                                        self.towerempty = "goldentowerempty.png"
                                        self.image = pg.image.load("goldentowerfire.png")
                                        self.originalimage = self.image
                                        self.upgraded = 1
                                        self.cooldown = 1900
                                        self.load = 500
                                        upgrading = False
                                    if event.key == pg.K_2:
                                        Button.GOLD = Button.GOLD - 100
                                        self.towerfire = "glasstowerfire.png"
                                        self.towerempty = "glasstowerempty.png"
                                        self.image = pg.image.load("glasstowerfire.png")
                                        self.originalimage = self.image
                                        self.upgraded = 1
                                        self.cooldown = 2600
                                        self.load = 600
                                        self.damage = 150
                                        self.range = 350
                                        upgrading = False
        

    def draw(self, surface):
        surface.blit(self.image, self.rotated_rect.topleft)


class BigTower(Tower):
    def __init__(self, posx, posy, timage):
        super().__init__(posx, posy, timage)
        self.position = (posx, posy)
        self.image = pg.image.load(timage)
        self.image = pg.transform.scale(self.image, (160, 160))
        self.rect = self.image.get_rect(center = self.position)
        self.fired = 1
        self.last = pg.time.get_ticks()
        self.cooldown = 3500
        self.load = 2000

    def update(self, monsters):
        if len(monsters) > 0:
            now = pg.time.get_ticks()
            near = min(monsters, key=lambda s: math.hypot(450-s.rect.centerx, 350 - s.rect.centery))
            if now - self.last >= self.load:
                self.image = pg.image.load("bigtowerfire.png")
                self.image = pg.transform.scale(self.image, (160, 160))
            if self.fired == 0:
                self.image = pg.image.load("bigtowerempty.png")
                self.image = pg.transform.scale(self.image, (160, 160))
                BULLET = MagicBullet(self.position[0] - 48, self.position[1] - 48, "magicbolt.png", near, None)
                bullets.add(BULLET)
                pg.mixer.Sound.play(magic_sound)
                self.fired = 1
            else:
                if now - self.last >= self.cooldown:
                    self.last = now
                    self.fired = 0
                    self.image = pg.image.load("bigtowerfire.png")
                    self.image = pg.transform.scale(self.image, (160, 160))


    def draw(self, surface):
        surface.blit(self.image, (self.position[0]- 21, self.position[1] - 19))

class Bullets(pg.sprite.Sprite):
    '''
    Class for Bullets
    The bullets themself are only cosmetic, 
    they always hit the target
    '''
    def __init__(self, posx, posy, bimage, damage):
        super().__init__()
        self.startingpos = (posx, posy)
        self.position = pg.Vector2(posx, posy)
        self.originalimage = self.image = pg.image.load(bimage)
        self.rect = self.image.get_rect(center = self.startingpos)
        self.target = self.angle = 0
        self.speed = 20
        self.dietime = 130
        self.last = pg.time.get_ticks()
        self.damage = damage

    def update(self, angle, near):
        '''
        Function for rotating the arrow and damaging the monster
        near - instance of the nearest monster
        '''
        self.angle = angle + 180
        self.image = pg.transform.rotate(self.originalimage, self.angle)
        self.rotated_rect = self.image.get_rect(center = self.rect.center)
        near.take_dmg(self.damage)


    def zoom(self):
        '''
        Function for moving the arrow across the screen
        '''
        now = pg.time.get_ticks()
        if now - self.last >= self.dietime:
            self.kill()
            self.last = now
        dy = self.speed * math.cos(math.radians(self.angle))
        dx = self.speed * math.sin(math.radians(self.angle))
        self.position.x -= dx
        self.position.y -= dy
        self.rect.center = self.position
        self.rotated_rect[0] = self.position.x
        self.rotated_rect[1] = self.position.y
        self.draw(SCR)

        
    def draw(self, surface):
        surface.blit(self.image, self.rotated_rect.topleft)
        
class MagicBullet(Bullets):
    '''
    A special bullets class for the big tower
    '''
    def __init__(self, posx, posy, bimage, near, damage):
        super().__init__(posx, posy, bimage, damage)
        self.startingpos = (posx, posy)
        self.position = pg.Vector2(posx, posy)
        self.originalimage = self.image = pg.image.load(bimage)
        self.rect = self.image.get_rect(topleft = self.startingpos)
        self.speed = 15
        self.dietime = 500
        self.last = pg.time.get_ticks()
        self.choose = near
        self.target = math.atan2(self.choose.rect.centerx - self.rect.centerx, self.choose.rect.centery - self.rect.centery)
        self.target = math.degrees(self.target)
        self.angle = self.target + 180


    def zoom(self):
        '''
        Function for moving the arrow across the screen
        '''
        angle_diff = (self.target - self.angle) % 360 - 180
        self.angle += angle_diff * 0.1
        now = pg.time.get_ticks()
        if now - self.last >= self.dietime:
            self.kill()
            self.last = now
            self.choose.take_dmg(1000)
        dy = self.speed * math.cos(math.radians(self.angle))
        dx = self.speed * math.sin(math.radians(self.angle))
        self.position.x -= dx
        self.position.y -= dy
        self.rect.center = self.position
        self.draw(SCR)

    def draw(self, surface):
        surface.blit(self.image, (self.position[0]+46, self.position[1]+46))

def run(TICK):
    '''
    The main loop function
    '''
    while True:
        spawn_wave()
        events = pg.event.get()
        draw_screen()
        draw_gold()
        draw_hp()
        draw_time()
        draw_wave_number()
        for monster in monsters:
            monster.update()
            monster.draw(SCR)
        for button in buttons:
            button.draw(SCR)
            button.update(events)
        for tower in towers:
            tower.upgrade(events)
            tower.update(monsters)
            tower.draw(SCR)
        for bullet in bullets:
            bullet.zoom()
        add_gold()
        pg.display.flip()
        pause(events)
        for event in events:
            quit_game(event)
        FPS.tick(TICK)
        
        
def main_menu():
    '''
    Function for displaying the main menu and buttons
    '''
    waiting_for_input = True
    while waiting_for_input:
        SCR.blit(menu_image, (0, 0))
        draw_text("Main Menu", MENUFONT, (153, 51, 255), WIDTH // 2, HEIGHT // 4)
        mx, my = pg.mouse.get_pos()

        start_button = pg.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 30, 200, 50)
        pg.draw.rect(SCR, BLACK, start_button)
        draw_text("START", FONT, WHITE, WIDTH // 2, HEIGHT // 2)

        instructions_button = pg.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 40, 200, 50)
        pg.draw.rect(SCR, BLACK, instructions_button)
        draw_text("INSTRUCTIONS", FONT, WHITE, WIDTH // 2, HEIGHT // 2 + 70)

        quit_button = pg.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 110, 200, 50)
        pg.draw.rect(SCR, BLACK, quit_button)
        draw_text("QUIT", FONT, WHITE, WIDTH // 2, HEIGHT // 2 + 140)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if start_button.collidepoint(mx, my):
                    run(TICK)
                elif instructions_button.collidepoint(mx, my):
                    waiting_for_input = False
                    show_instructions()
                elif quit_button.collidepoint(mx, my):
                    sys.exit()

        pg.display.flip()


def show_instructions():
    '''
    Function for displaying the instructions
    '''
    backgroundrect = pg.Rect(30, 150, 840, 450)
    SCR.blit(menu_image, (0, 0))
    pg.draw.rect(SCR, GREENBACK, backgroundrect)
    draw_text("Instructions:", FONT, BLACK, WIDTH // 2, HEIGHT // 4)
    instructions = [
        "Welcome to Castle Defense!",
        "In this game you need to protect the palace from invaders",
        "The palace is located in the middle",
        "To build towers press on the Buttons highlighting",
        "You can upgrade your towers by pressing on them and clicking 1 or 2",
        "The big button in middle is for bigger tower",
        "You lose if your HP goes below zero",
        "Press Space to pause and unpause the game",
        "Have Fun!",
        "",
        "Press ESC to go back to menu, when in game press ESC to quit"
    ]
    for i, instruction in enumerate(instructions):
        draw_text(instruction, FONT, BLACK, WIDTH // 2, HEIGHT // 4 + (i + 1) * 36)
    
    pg.display.flip()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    main_menu()

def draw_screen():
    SCR.blit(bg_image, (0, 0))
    

def pause(events):
    '''
    Function for pausing and unpausing the game
    using Space
    '''
    for event in events:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                paused = True
                while paused:
                    draw_pause()
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            sys.exit()
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_ESCAPE:
                                sys.exit()
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_SPACE:
                                paused = False
                


def quit_game(event):  
    '''
    Quit game function for Quit and Escape
    ''' 
    if event.type == pg.QUIT:
        sys.exit()
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
            sys.exit()


def spawn_wave():
    '''
    Function for spawning a new specific wave of monsters in

    
    Z - Zombie
    S - Spider
    G - Greater Zombie count
    M - Miner

    number after the letter depends on the wave
    '''
    if Monster.WAVE == 0:
        spawn(Z1, 2, 2, 2)
    if Monster.WAVE == 1:
        spawn(Z2, 0, 0, 0)
    if Monster.WAVE == 2:
        spawn(Z3, S3, 0, 0)
    if Monster.WAVE == 3:
        spawn(Z4, 0, G4, 0)
    if Monster.WAVE == 4:
        spawn(0, S5, G5, 0)
    if Monster.WAVE == 5:
        spawn(Z6, 0, G6, M6)
    if Monster.WAVE == 6:
        spawn(0, S7, G7, M7)
    if Monster.WAVE > 6:
        spawn(0, 30, 30, 20)
        

def spawn(zombiecount, spidercount, greaterzombiecount, minercount):
    '''
    Function for specific monster's spawns
    The order of each function 
    means the order in which the monsters spawn in
    The counters define the number of monsters that should
    spawn of each type
    '''
    if Monster.GZCOUNT < greaterzombiecount:
        spawn_gzombies()
    elif Monster.SCOUNT < spidercount:
        spawn_spiders()
    elif Monster.ZCOUNT < zombiecount:
        spawn_zombies()
    elif Monster.MCOUNT < minercount:
        spawn_miners()
    else:
        if len(monsters) == 0:
            Monster.WAVE = Monster.WAVE + 1
            Monster.ZCOUNT = 0
            Monster.SCOUNT = 0
            Monster.GZCOUNT = 0
            Monster.MCOUNT = 0
            draw_next()
            pg.display.flip()
            pg.time.delay(1000)




def spawn_zombies():
    '''
    Function spawning zombies, creating an instance of a zombie
    '''
    global START
    NOW = pg.time.get_ticks()
    if NOW - START >= ZOMWAIT:
        pg.mixer.Sound.play(zombie_sound)
        ZOMBIE = Monster("zombieimage.png", "zombiewimage.png", INITIALX, INITIALY, ZOMBIEVELOCITY, ZOMBIEHP, ZOMBIEDMG, ZOMBIEVALUE)
        monsters.add(ZOMBIE)
        START = NOW
        Monster.ZCOUNT = Monster.ZCOUNT + 1


def spawn_gzombies():
    '''
    Function spawning greater zombies with more hp but slower
    creates an instance of Greater zombie
    '''
    global START
    NOW = pg.time.get_ticks()
    if NOW - START >= ZOMWAIT:
        pg.mixer.Sound.play(gzombie_sound)
        GZOMBIE = Monster("gzombieimage.png", "gzombiewimage.png", INITIALX, INITIALY, GZOMBIEVELOCITY, GZOMBIEHP, GZOMBIEDMG, GZOMBIEVALUE)
        monsters.add(GZOMBIE)
        START = NOW
        Monster.GZCOUNT = Monster.GZCOUNT + 1


def spawn_spiders():
    '''
    Function for spawning in spiders, faster but easier to kill
    creates an instance of Spider
    '''
    global START
    NOW = pg.time.get_ticks()
    if NOW - START >= SPIWAIT:
        pg.mixer.Sound.play(spider_sound)
        SPIDER = Monster("spiderimage.png", "spiderwimage.png", INITIALX, INITIALY, SPIDERVELOCITY, SPIDERHP, SPIDERDMG, SPIDERVALUE)
        monsters.add(SPIDER)
        START = NOW
        Monster.SCOUNT = Monster.SCOUNT + 1


def spawn_miners():
    '''
    Function for spawning in miners, same as zombies but further in the map
    creates an instance of Miner
    '''
    global START
    NOW = pg.time.get_ticks()
    if NOW - START >= ZOMWAIT:
        pg.mixer.Sound.play(miner_sound)
        MINER = Monster("minerimage.png", "minerwimage.png", MINITIALX, MINITIALY, ZOMBIEVELOCITY, ZOMBIEHP, ZOMBIEDMG, ZOMBIEVALUE)
        monsters.add(MINER)
        START = NOW
        Monster.MCOUNT = Monster.MCOUNT + 1


def add_gold():
    '''
    Function for debugging, testing and development
    if specific combination of keys ('w' and 's')
    are pressed the game adds gold
    '''
    keys = pg.key.get_pressed()
    if keys[pg.K_w] and keys[pg.K_s]:
        Button.GOLD = Button.GOLD + 10


def draw_gold():
    '''
    Function drawing the number of gold a player has
    '''
    myfont = pg.font.Font('freesansbold.ttf', 20)
    msg = myfont.render(f"GOLD: {Button.GOLD}", True, YELLOW)
    msg_box = msg.get_rect()
    msg_box.topright = (890, 0)
    SCR.blit(msg, msg_box)

def draw_wave_number():
    '''
    Function for drawing the wave number
    the + 1 inside the function is because the count 
    starts at 0, but 1 is more logical
    '''
    myfont = pg.font.Font('freesansbold.ttf', 20)
    msg = myfont.render(f"Wave: {Monster.WAVE + 1}", True, RED)
    msg_box = msg.get_rect()
    msg_box.topright = (450, 0)
    SCR.blit(msg, msg_box)

def draw_hp():
    '''
    Function for drawing the hp a player has
    '''
    myfont = pg.font.Font('freesansbold.ttf', 20)
    msg = myfont.render(f"HP: {Monster.PLAYER_HP}", True, RED)
    msg_box = msg.get_rect()
    msg_box.topleft = (10, 0)
    SCR.blit(msg, msg_box)


def draw_time():
    '''
    Function drawing seconds a game has been played for
    paused time included
    '''
    seconds = pg.time.get_ticks() // 1000
    myfont = pg.font.Font('freesansbold.ttf', 20)
    msg = myfont.render(f"Time: {seconds}", True, RED)
    msg_box = msg.get_rect()
    msg_box.topleft = (250, 0)
    SCR.blit(msg, msg_box)


def draw_next():
    '''
    Function for when the Wave has ended and a new one should spawn in
    '''
    myfont = pg.font.Font('freesansbold.ttf', 40)
    msg = myfont.render(f"NEXT WAVE", True, (76, 153, 0))
    msg_box = msg.get_rect()
    msg_box.center = (450, 350)
    SCR.blit(msg, msg_box)


def draw_pause():
    '''
    Function for pausing
    '''
    myfont = pg.font.Font('freesansbold.ttf', 60)
    msg = myfont.render(f"PAUSED", True, (76, 153, 0))
    msg_box = msg.get_rect()
    msg_box.center = (450, 350)
    SCR.blit(msg, msg_box)
    pg.display.flip()


def draw_text(text, font, color, x, y):
    '''
    Function for more repetitional drawing of text
    '''
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    SCR.blit(text_surface, text_rect)


if __name__ == "__main__":
    MENUFONT = pg.font.Font('freesansbold.ttf', 55)
    FONT = pg.font.Font(None, 36)
    Z1 = 7
    Z2 = 9
    S3 = 7
    Z3 = 10
    Z4 = 20
    G4 = 3
    G5 = 2
    S5 = 30
    G6 = 4
    Z6 = 10
    M6 = 6
    G7 = 5
    M7 = 20
    S7 = 20
    START = pg.time.get_ticks()
    ZOMWAIT = 1800
    SPIWAIT = 500
    TOW_NUM = 1
    INITIALX = 0
    MINITIALX = 80
    MINITIALY = 170
    INITIALY = 20
    ZOMBIEVELOCITY = 1.3
    GZOMBIEVELOCITY = 1.1
    SPIDERVELOCITY = 2.5
    ZOMBIEHP = 200
    ZOMBIEDMG = 30
    GZOMBIEHP = 500
    GZOMBIEDMG = 50
    SPIDERHP = 80
    SPIDERDMG = 30
    ZOMBIEVALUE = 15
    GZOMBIEVALUE = 25
    SPIDERVALUE = 5
    BUTTON1 = Button(120, 68, 1)
    BUTTON2 = Button(284, 188, 2)
    BUTTON3 = Button(692, 68, 3)
    BUTTON4 = Button(532, 188, 4)
    BUTTON5 = Button(284, 372, 5)
    BUTTON6 = Button(532, 372, 6)
    BUTTON7 = Button(120, 496, 7)
    BUTTON8 = Button(692, 496, 8)
    BIGBUTTON = BigButton(394, 264, 9)
    bullets = pg.sprite.Group()
    towers = pg.sprite.Group()
    buttons = pg.sprite.Group()
    buttons.add(BIGBUTTON, BUTTON1, BUTTON2, BUTTON3, BUTTON4, BUTTON5, BUTTON6, BUTTON7, BUTTON8)
    monsters = pg.sprite.Group()
    WINDOWSIZE = (900, 700)
    WIDTH = 900
    HEIGHT = 700
    SCR = pg.display.set_mode(WINDOWSIZE)
    bg_image = pg.image.load('backgroundtower.png')
    menu_image = pg.image.load('menubackground.png')
    WIN = SCR.get_rect()
    GREENBACK = (20, 100, 44)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    YELLOW = (207, 190, 6)
    zombie_sound = pg.mixer.Sound("zombiesound.wav")
    gzombie_sound = pg.mixer.Sound("gzombiesound.wav")
    miner_sound = pg.mixer.Sound("minersound.wav")
    spider_sound = pg.mixer.Sound("spidersound.wav")
    shoot_sound = pg.mixer.Sound("crossbowshot.wav")
    magic_sound = pg.mixer.Sound("magicsmite.wav")
    TICK = 60
    FPS = pg.time.Clock()
    pg.mixer.music.load('backgroundmusic.mp3')
    gzombie_sound.set_volume(0.3)
    spider_sound.set_volume(0.7)
    zombie_sound.set_volume(0.9)
    pg.mixer.music.set_volume(0.2)
    pg.mixer.music.play(-1)
    main_menu()
    run(TICK)