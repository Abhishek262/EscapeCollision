

#Multiplayer version of EscapeCollision
import pygame
import time,random,os,math
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

display_width=1240
display_height =650
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('game_mp')
clock =pygame.time.Clock()
pause =False
imgpath  = 'images\\'
exppath = 'Explosion\\'
dmgpath = 'Damages\\'
time1=time.time()
dead = False
setpos=  False

class Fuel:

    fuel_left = 100
    f= 0.05887
    fuel_time1 = time.time()

class Health:
    health = 100
    healthBar=  None
    hbw = None
    x1health =None
    x2health= None
    x1time =time.time()
    x2time = time.time()


class color:

    red =(255,0,0)
    white = (255,255,255)
    black= (0,0,0)
    grey = (195,195,195)
    black = (0,0,0)
    reddish  = (200,0,0)
    yellow= (247,217,9)
    yellowish= (209,137,5)
    green = (0,255,0)
    greenish = (0,200,0)
    block_color = (79,0,0)
    blue = (0,0,255)
    bluish = (0,0,120)
    fuel_color = (1,1,101)
    orange=  (250,165,5)
    fuel_stats_color = (0,0,0)
    lightgreen = (139,230,57)
    plightgreen =(70,130,17)
    fuelbar_color = green
    car_menu_color = (37,151,184)
    health_stats_color = (0,0,0)
    health_bar_color = green
    gear_stats_color = black

    
class Car_player:
    Car = None
    x = (display_width * 0.45)
    y = (display_height * 0.72)
    width = 92
    gear =1
    i = 0

    
class Cars:
    ID = None
    car1 = pygame.image.load(imgpath+ 'car_1.jpg')
    car2 = pygame.image.load(imgpath+'car_2.jpg')
    car3 = pygame.image.load(imgpath+'car_3.jpg')
    
    car1dmg1 = pygame.image.load(dmgpath+'car_1_burnt.png')
    car1dmg2 = pygame.image.load(dmgpath+'car_1_broke1.png')
    car1dmg3 = pygame.image.load(dmgpath+'car_1_broke2.png')
    car1dmg4 = pygame.image.load(dmgpath+'car_1_broke3.png')
    
    car2dmg1 = pygame.image.load(dmgpath+'car_2_burnt.png')
    car2dmg2 = pygame.image.load(dmgpath+'car_2_broke1.png')
    car2dmg3 = pygame.image.load(dmgpath+'car_2_broke2.png')
    car2dmg4 = pygame.image.load(dmgpath+'car_2_broke3.png')

    car3dmg1 = pygame.image.load(dmgpath+'car_3_burnt.png')
    car3dmg2 = pygame.image.load(dmgpath+'car_3_broke1.png')
    car3dmg3 = pygame.image.load(dmgpath+'car_3_broke2.png')
    car3dmg4 = pygame.image.load(dmgpath+'car_3_broke3.png')
    
class Car_AI:
    Car1= None
    Car2= None
    x1 =0
    x2=0
    x1_change=0
    x2_change=0
    LCarID = None
    RCarID = None

class AI:
    push =False

    
class Explosion:
    Exp1 = pygame.image.load(exppath + 'Exp1.gif')
    Exp2 = pygame.image.load(exppath + 'Exp2.gif')
    Exp3 = pygame.image.load(exppath + 'Exp3.gif')
    Exp4 = pygame.image.load(exppath + 'Exp4.gif')
    Exp5 = pygame.image.load(exppath + 'Exp5.gif')
    Exp6 = pygame.image.load(exppath + 'Exp6.gif')
    Exp7 = pygame.image.load(exppath + 'Exp7.gif')
    Exp8 = pygame.image.load(exppath + 'Exp8.gif')
    Exp9 = pygame.image.load(exppath + 'Exp9.gif')
    Exp10 = pygame.image.load(exppath + 'Exp10.gif')
    Exp11 = pygame.image.load(exppath + 'Exp11.gif')
    Exp12 = pygame.image.load(exppath + 'Exp12.gif')
    Exp13 = pygame.image.load(exppath + 'Exp13.gif')
    Exp14 = pygame.image.load(exppath + 'Exp14.gif')
    Exp15 = pygame.image.load(exppath + 'Exp15.gif')
    Exp16 = pygame.image.load(exppath + 'Exp16.gif')
    Exp17 = pygame.image.load(exppath + 'Exp17.gif')
    Cexp = 0
    Exploding = False
    e = 0
    f=0
    g=0
    
def blocks_dodged(count):

    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(count), True, color.black)

    gameDisplay.blit(text,(60,2))



def fuel_stats():
    font  = pygame.font.SysFont(None , 25)

    text = font.render("Fuel:", True , color.black)

    gameDisplay.blit(text ,(display_width - 1020, 2))

def health_stats():
    font  = pygame.font.SysFont(None , 25)

    text = font.render("Health:", True , color.health_stats_color)

    gameDisplay.blit(text ,(display_width - 770, 2))

def gear_stats():
    font  = pygame.font.SysFont(None , 25)
    text = font.render("Gear:" + str(int(Car_player.gear)), True , color.gear_stats_color)

    gameDisplay.blit(text ,(display_width - 500, 2))
    
def fuel(fuelx , fuely , fuelw  , fuelh , color):
    pygame.draw.rect(gameDisplay , color , [fuelx ,fuely , fuelw ,fuelh])

    
def fuelbar(fbx,fby,fbw,fbh,Color):
    pygame.draw.rect(gameDisplay , Color , [fbx ,fby , fbw ,fbh])
    pygame.draw.aaline(gameDisplay , color.black , (290,2),(410,2),20)
    pygame.draw.aaline(gameDisplay , color.black , (290,22),(410,22),20)
    pygame.draw.aaline(gameDisplay , color.black , (290,2),(290,22),20)
    pygame.draw.aaline(gameDisplay , color.black , (410,2),(410,23),20)

def healthbar(hbx,hby,hbw,hbh,Color):
    pygame.draw.rect(gameDisplay , Color , [hbx ,hby ,hbw ,hbh])
    pygame.draw.aaline(gameDisplay , color.black , (hbx,2),(hbx+150,2),200)
    pygame.draw.aaline(gameDisplay , color.black , (hbx,22),(hbx+150,22),20)
    pygame.draw.aaline(gameDisplay , color.black , (hbx,2),(hbx,22),20)
    pygame.draw.aaline(gameDisplay , color.black , (hbx+150,2),(hbx+150,23),20)

def Expblit(x,y):

    
    Explosion.Cexp+=1

    if Explosion.Cexp == 1:
        gameDisplay.blit(Explosion.Exp1,(x,y))
    if Explosion.Cexp == 2:
        gameDisplay.blit(Explosion.Exp2,(x,y))
    if Explosion.Cexp == 3:
        gameDisplay.blit(Explosion.Exp3,(x,y))
    if Explosion.Cexp == 4:
        gameDisplay.blit(Explosion.Exp4,(x,y))
    if Explosion.Cexp == 5:
        gameDisplay.blit(Explosion.Exp5,(x,y))
    if Explosion.Cexp == 6:
        gameDisplay.blit(Explosion.Exp6,(x,y))
    if Explosion.Cexp == 7:
        gameDisplay.blit(Explosion.Exp7,(x,y))
    if Explosion.Cexp == 8:
        gameDisplay.blit(Explosion.Exp8,(x,y))
    if Explosion.Cexp == 9:
        gameDisplay.blit(Explosion.Exp9,(x,y))
    if Explosion.Cexp == 10:
        gameDisplay.blit(Explosion.Exp10,(x,y))
    if Explosion.Cexp == 11:
        gameDisplay.blit(Explosion.Exp11,(x,y))
    if Explosion.Cexp == 12:
        gameDisplay.blit(Explosion.Exp12,(x,y))
    if Explosion.Cexp == 13:
        gameDisplay.blit(Explosion.Exp13,(x,y))
    if Explosion.Cexp == 14:
        gameDisplay.blit(Explosion.Exp14,(x,y))
    if Explosion.Cexp == 15:
        gameDisplay.blit(Explosion.Exp15,(x,y))
    if Explosion.Cexp == 16:
        gameDisplay.blit(Explosion.Exp16,(x,y))
    if Explosion.Cexp == 17:
        gameDisplay.blit(Explosion.Exp17,(x,y))

    if Explosion.Cexp >=18:
        Explosion.Cexp =-5

def ExplodeCar(x,y):
    Explosion.e +=1

    
    if Explosion.e in range(1,10):
        Expblit(x,y)
    if Explosion.e in range(11,20):
        Expblit(x+32 ,y+64)
    if Explosion.e in range(21,30):
        Expblit(x +64,y+88)
    if Explosion.e in range(31,40):
        Expblit(x , y +30)
    if Explosion.e in range(41,50):
        Expblit(x- 32 , y +30)
    if Explosion.e in range(51,60):
        Expblit(x , y +64)        

    if Explosion.e in range(61,70):
        Expblit(x,y)
    if Explosion.e in range(71,80):
        Expblit(x+32 , y+64)
    if Explosion.e in range(81,90):
        Expblit(x +64, y+88)
    if Explosion.e in range(91,100):
        Expblit(x , y +30)
    if Explosion.e in range(101,110):
        Expblit(x- 32 , y +30)
    if Explosion.e in range(111,120):
        Expblit(x , y +64)
        

    if Explosion.e in range(121,140):
        Expblit(x , y)
        Expblit(x+32 , y+32)
        Expblit(x-32 , y-32)
        Expblit(x+64 , y+64)
        Expblit(x , y+88)
        Expblit(x+32 , y+88)
        Expblit(x+64 , y+88)
        Expblit(x , y-32)
        Expblit(x , y+120)
        Expblit(x-32 , y +88)
        Expblit(x - 32 ,y+ 64)

def ExplodeCar2(x,y):
    Explosion.f +=1

    
    if Explosion.f in range(1,10):
        Expblit(x,y)
    if Explosion.f in range(11,20):
        Expblit(x+32 ,y+64)
    if Explosion.f in range(21,30):
        Expblit(x +64,y+88)
    if Explosion.f in range(31,40):
        Expblit(x , y +30)
    if Explosion.f in range(41,50):
        Expblit(x- 32 , y +30)
    if Explosion.f in range(51,60):
        Expblit(x , y +64)        

    if Explosion.f in range(61,70):
        Expblit(x,y)
    if Explosion.f in range(71,80):
        Expblit(x+32 , y+64)
    if Explosion.f in range(81,90):
        Expblit(x +64, y+88)
    if Explosion.f in range(91,100):
        Expblit(x , y +30)
    if Explosion.f in range(101,110):
        Expblit(x- 32 , y +30)
    if Explosion.f in range(111,120):
        Expblit(x , y +64)
        

    if Explosion.f in range(121,140):
        Expblit(x , y)
        Expblit(x+32 , y+32)
        Expblit(x-32 , y-32)
        Expblit(x+64 , y+64)
        Expblit(x , y+88)
        Expblit(x+32 , y+88)
        Expblit(x+64 , y+88)
        Expblit(x , y-32)
        Expblit(x , y+120)
        Expblit(x-32 , y +88)
        Expblit(x - 32 ,y+ 64)        
        
def ExplodeCar3(x,y):
    Explosion.g +=1

    
    if Explosion.g in range(1,10):
        Expblit(x,y)
    if Explosion.g in range(11,20):
        Expblit(x+32 ,y+64)
    if Explosion.g in range(21,30):
        Expblit(x +64,y+88)
    if Explosion.g in range(31,40):
        Expblit(x , y +30)
    if Explosion.g in range(41,50):
        Expblit(x- 32 , y +30)
    if Explosion.g in range(51,60):
        Expblit(x , y +64)        

    if Explosion.g in range(61,70):
        Expblit(x,y)
    if Explosion.g in range(71,80):
        Expblit(x+32 , y+64)
    if Explosion.g in range(81,90):
        Expblit(x +64, y+88)
    if Explosion.g in range(91,100):
        Expblit(x , y +30)
    if Explosion.g in range(101,110):
        Expblit(x- 32 , y +30)
    if Explosion.g in range(111,120):
        Expblit(x , y +64)
        

    if Explosion.g in range(121,140):
        Expblit(x , y)
        Expblit(x+32 , y+32)
        Expblit(x-32 , y-32)
        Expblit(x+64 , y+64)
        Expblit(x , y+88)
        Expblit(x+32 , y+88)
        Expblit(x+64 , y+88)
        Expblit(x , y-32)
        Expblit(x , y+120)
        Expblit(x-32 , y +88)
        Expblit(x - 32 ,y+ 64)    
        
def fuel_over():
    largeText = pygame.font.SysFont("Arial",75)
    TextSurf, TextRect = text_objects("Fuel Over", largeText,color.black)
    TextRect.center = ((display_width/2),(display_height*0.4))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)


        button("Play Again",450,450,150,50,color.green,color.greenish,game_mp)
        button("Quit",650,450,150,50,color.red,color.reddish,quitgame)

        pygame.display.update()
        clock.tick(60)
def Carselected_car1():
    Car_player.Car= Cars.car1
    Cars.ID = 1
    #ai id 1 = blue car 2 = red car 3 = white car
    Car_AI.LCarID =2
    Car_AI.RCarID = 3
    

    
def Carselected_car2():
    Car_player.Car= Cars.car2
    Cars.ID=2
    Car_AI.LCarID =1
    Car_AI.RCarID = 3
    
def Carselected_car3():
    Car_player.Car= Cars.car3
    Cars.ID=3
    Car_AI.LCarID =1
    Car_AI.RCarID = 2

def blocks(block_x,block_y,block_width,block_height,color):
    pygame.draw.rect(gameDisplay, color, [block_x, block_y, block_width, block_height])

def fuel_color_change():
    color.fuel_color = (1,1,101)


def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action = None,action2 = None, ):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()



    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            time.sleep(0.3)
            action()
            if action2 != None:
                action2()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText,color.black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)    

def selectCar():
    gsp = pygame.image.load(imgpath+'gsp.jpg')
    select =True
    largeText = pygame.font.SysFont("Arial",80)
    TextSurf, TextRect = text_objects("Select Car", largeText,color.red )
    TextRect.center = ((display_width/2),(display_height/10))
    while select:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:

                    select  = False
                if event.key == pygame.K_RETURN:
                    Carselected_car2()
                    game_mp()

        gameDisplay.fill(color.car_menu_color)
        gameDisplay.blit(TextSurf, TextRect)


        button("X",400,450,50,50,color.grey,color.black,Carselected_car1)
        button("X",600,450,50,50,color.grey,color.black,Carselected_car2)
        button("X",800,450,50,50,color.grey,color.black,Carselected_car3)
        button("Play", 500,550,100,50,color.green,color.greenish,game_mp)
        button("Back", 650,550,100,50,color.red,color.reddish,game_sp)

        if Car_player.Car == Cars.car1:
            gameDisplay.blit(gsp,(355,235))
        elif Car_player.Car == Cars.car2:

            gameDisplay.blit(gsp,(555,235))
        elif Car_player.Car == Cars.car3:
            gameDisplay.blit(gsp,(755,235))
        else:
            gameDisplay.blit(gsp, (2000,250))
        

        gameDisplay.blit(Cars.car1, (375,250))
        gameDisplay.blit(Cars.car2, (575,250))
        gameDisplay.blit(Cars.car3, (775,250))



        pygame.display.update()
        clock.tick(30)
    
        

def paused():
    global pause
    pause = True
    background = pygame.image.load(imgpath+'background_mul.jpg')
    largeText = pygame.font.SysFont("Arial",80)
    TextSurf, TextRect = text_objects("Paused", largeText ,color.red)
    TextRect.center = ((display_width/2),(display_height*0.35))
    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type  == pygame.KEYDOWN:
                if event.key ==pygame.K_SPACE or event.key == pygame.K_ESCAPE:

                    pause  = False


        gameDisplay.fill(color.white)
        gameDisplay.blit(background,(0,0))
        gameDisplay.blit(TextSurf, TextRect)

        button("Restart",370,450,100,50,color.green,color.greenish,game_mp)
        button("Continue",570,450,100,50,color.blue,color.bluish,unpause)
        button("Quit",770,450,100,50,color.red,color.reddish,selectCar)


        pygame.display.update()
        clock.tick(60)

def randomizespeed():
    xrl = random.randrange(1,4)
    if xrl== 1:
        Car_AI.x1_change= -8
    if xrl == 2:
        Car_AI.x1_change= +8
    if xrl == 3:
        Car_AI.x1_change = 0
def unpause():
    global pause
    pause =False
def destroy(count):
    pygame.display.update()
    largeText = pygame.font.SysFont("Arial",75)
    TextSurf, TextRect = text_objects("Wasted", largeText,color.black)
    TextRect.center = ((display_width/2),(display_height * 0.4))
    gameDisplay.blit(TextSurf, TextRect)

    mediumText  = pygame.font.SysFont("Calibri(body)",35)
    TextSurf2 , TextRect2 = text_objects("Your Score : "  + str(count),  mediumText ,color.black)
    TextRect2.center = ((display_width/2),(display_height* 0.5))
    gameDisplay.blit(TextSurf2, TextRect2)

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    game_mp()


        
        button("Play Again",400,450,150,50,color.green,color.greenish,game_mp)
        button("Back",700,450,150,50,color.red,color.reddish,selectCar)

        pygame.display.update()
        clock.tick(60)
   
def quitgame():
    pygame.quit()

    quit()
    gameExit =  True
def game_sp():
    from src.py import game_intro


def game_mp():

    test = False
    if Car_player.Car == None:
        selectCar()
    if Car_player.Car == Cars.car1:
        Car_AI.Car1 = Cars.car2
        Car_AI.Car2= Cars.car3
    if Car_player.Car == Cars.car2:
        Car_AI.Car1 = Cars.car1
        Car_AI.Car2= Cars.car3
    if Car_player.Car == Cars.car3:
        Car_AI.Car1 = Cars.car1
        Car_AI.Car2= Cars.car2

    Car_AI.x1=Car_AI.x2=y1=y2=0

    if Car_AI.Car1== Cars.car1:
        Car_AI.x1 =(display_width * 0.20)
        y1 =(display_height * 0.72)
    if Car_AI.Car1==Cars.car2:
        Car_AI.x1 =(display_width * 0.20)
        y1 =(display_height * 0.72)
    if Car_AI.Car1== Cars.car3:
        Car_AI.x1 =(display_width * 0.20)
        y1 =(display_height * 0.72)

    if Car_AI.Car2== Cars.car1:
        Car_AI.x2 =(display_width * 0.72)
        y2 =(display_height * 0.72)
    if Car_AI.Car2== Cars.car2:
        Car_AI.x2 =(display_width * 0.72)
        y2 =(display_height * 0.72)
    if Car_AI.Car2== Cars.car3:
        Car_AI.x2 =(display_width * 0.72)
        y2 =(display_height * 0.72)
    global pause,Screen,dead,setpos
    block_x = random.randrange(0,display_width-100)
    block_y=-600
    block_x2 = random.randrange(0,display_width-100)
    block_y2 = -600 - random.randrange(100,400)
    car_width = 99
    Car_player.x = (display_width * 0.45)
    Car_player.y = (display_height * 0.72)
    Car_AI.x1_change =0
    Car_AI.x2_change = 0
    block_width = 100
    block_height= 100
    block_speed = 8
    Explosion.Cexp= 0
    Explosion.e =0
    Explosion.f =0
    Explosion.g =0

    x1_change= Car_AI.x1_change
    x2_change= Car_AI.x2_change
    x1 = Car_AI.x1
    x2= Car_AI.x2
    Health.x1health= 150
    Health.x2health = 150
    dead =False
    randBlockIncr  = random.randrange(-200, 200, 100)
    if randBlockIncr == 0:
        randBlockIncr =random.randrange(-200,200,100)
    gameExit = False
    Screen = False
    ctrl_pressed = False
    setpos=  False
    background =pygame.image.load(imgpath+'background_mul.jpg')
    block_pic= pygame.image.load(imgpath + 'block.png')
    block_dmg_pic = pygame.image.load(imgpath + 'block_dmg.png')
    arrow1 = pygame.image.load(imgpath + 'arrow1.png')
    arrow2 = pygame.image.load(imgpath + 'arrow2.png')
    arrow3 = pygame.image.load(imgpath + 'arrow3.png')
    arrow4 = pygame.image.load(imgpath + 'arrow4.png')
    arrow5 = pygame.image.load(imgpath + 'arrow5.png')
    arrow6 = pygame.image.load(imgpath + 'arrow6.png')
    arrow7 = pygame.image.load(imgpath + 'arrow7.png')
    
    dodged = 0
    x_change = 0
    Car_player.gear =1
    car_speed= 8+dodged*0.1
    collision = 10
    color.gear_stats_color =color.black
    hit = 2
    #fuel(block)
    fuel_startx = random.randrange(50 , display_width - 100)
    fuel_starty = -2000
    fuel_width = 40
    fuel_height = 40
    fuelCount = 1
    color.fuel_stats_color = (0,0,0)

    #fuelbar
    fbx = display_width - 950
    fby = 2
    fbw = 120
    fbh = 20
    #Health
    Health.health = 100
    hbx = display_width - 700
    hby = 2
    
    Health.hbw = 150        
    hbh = 20
    bdmg1 = False
    bdmg2 = False
    gx = False
#ai

    xrl = random.randrange(1,3)
    if xrl== 1:
        Car_AI.x1_change= -8
    if xrl == 2:
        Car_AI.x1_change= +8

    xrl2 = random.randrange(1,3)
    if xrl2== 1:
        Car_AI.x2_change= -8
    if xrl2 == 2:
        Car_AI.x2_change= +8
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -8-Car_player.gear
                if event.key == pygame.K_RIGHT:
                    x_change = 8+Car_player.gear
                if event.key == pygame.K_SPACE :
                    paused()
                    pause = True
                if event.key == pygame.K_ESCAPE    :
                    paused()
                    pause = True


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -8- Car_player.gear
                if event.key == pygame.K_d:
                    x_change = 8+ Car_player.gear

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT :
                    AI.push =True


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT :
                    AI.push = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RSHIFT :
                    AI.push =True


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RSHIFT :
                    AI.push = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    Car_player.gear = Car_player.gear +0.5
                    color.gear_stats_color= color.orange
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    Car_player.gear = Car_player.gear -0.5
                    color.gear_stats_color= color.orange
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Car_player.gear = Car_player.gear +0.5
                    color.gear_stats_color= color.orange
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    
                    Car_player.gear = Car_player.gear -0.5
                    color.gear_stats_color= color.orange

            if event.type==  pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL :
                    ctrl_pressed = True                    
            if event.type==  pygame.KEYUP:
                if event.key == pygame.K_RCTRL :
                    ctrl_pressed = False
            if event.type==  pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL :
                    ctrl_pressed = True                    
            if event.type==  pygame.KEYUP:
                if event.key == pygame.K_LCTRL :
                    ctrl_pressed = False
                    
        fuel_time2 = time.time()
        if (fuel_time2 - Fuel.fuel_time1) >= 2.0:
            Fuel.fuel_left -= 0.05
            fuel_time2 = Fuel.fuel_time1
            fbw  = fbw - Fuel.f

        x1time2= time.time()
        if (x1time2 - Health.x1time) >= 2.0:
            x1time2 = Health.x1time
            if Explosion.f <=0:
                Health.x1health = Health.x1health + 0.01        

        x2time2= time.time()
        if (x2time2 - Health.x2time) >= 2.0:
            x2time2 = Health.x2time
            if Explosion.g<=0:
                Health.x2health = Health.x2health + 0.01       

            
        fuel_speed = block_speed-8
        
        
        block_y += block_speed
        block_y2 +=block_speed
        Car_AI.x1+=Car_AI.x1_change
        Car_AI.x2+=Car_AI.x2_change
        Car_player.x+=x_change
        gameDisplay.blit(background ,(0,0))
        gameDisplay.blit(Car_AI.Car1,(Car_AI.x1,y1))
        gameDisplay.blit(Car_AI.Car2 ,(Car_AI.x2,y2))


        blocks(block_x,block_y,block_width,block_height,color.block_color)
        blocks(block_x2,block_y2,block_width,block_height,color.block_color)
        gameDisplay.blit(block_pic, (block_x ,block_y))
        gameDisplay.blit(block_pic, (block_x2,block_y2))
        fuel_starty +=fuel_speed
        fuelbar(fbx,fby,fbw,fbh, color.fuelbar_color)
        healthbar(hbx,hby,Health.hbw,hbh,color.health_bar_color)
        fuel(fuel_startx , fuel_starty , fuel_width  , fuel_height , color.fuel_color)
        button("||",display_width -150,2,35,35,color.green,color.greenish,paused )
        button(" ",display_width -200,2,35,35,color.green,color.greenish,game_mp)
        Reload = pygame.image.load(imgpath+ 'reload.png')
        gameDisplay.blit(Reload, (display_width- 198,4))
        button("X",display_width -100,2,35,35,color.green,color.greenish,selectCar )
        blocks_dodged(dodged)
        fuel_stats()
        health_stats()
        gear_stats()
        

        gameDisplay.blit(Car_player.Car ,(Car_player.x, Car_player.y))


        
        #fuel recursion
        if fuel_starty > display_height:
            
             
            fuel_lag = dodged * 20
            if fuel_lag >10000:
                fuel_lag =10000
            fuel_starty = -2000 - fuel_lag
            fuel_startx = random.randrange(50,display_width - 50)
            fuel_color_change()
        #misc
            
        if Health.hbw>= 150:
            Health.hbw = 150

        if Health.x1health >150:
            Health.x1health = 150
        if Health.x2health >150:
            Health.x2health = 150

        if Health.x1health <=0:
            Health.x1health = 0
        if Health.x2health <=0:
            Health.x2health = 0
            
        if color.health_stats_color==  color.red :
            color.health_stats_color = color.black
        if color.health_stats_color==  color.blue :
            color.health_stats_color = color.black
            
        if color.gear_stats_color == color.orange and Car_player.gear in range(1,6,1):

            color.gear_stats_color= color.black
                

        if Car_player.gear == 1:
            Fuel.f = 0.0587
        if Car_player.gear == 2:
            Fuel.f = 0.065
        if Car_player.gear == 3:
            Fuel.f = 0.07
        if Car_player.gear == 4:
            Fuel.f = 0.075
        if Car_player.gear == 5:
            Fuel.f = 0.08

        if Explosion.e >140:
            destroy(dodged)
        if Explosion.e >1:
            x_change= 0
        if Explosion.e>139:
            Car_player.y = -345

        if Explosion.f >1:
            Car_AI.x1_change= 0
        if Explosion.f>139:
            y1 = 4345

        if Explosion.g >1:
            Car_AI.x2_change= 0
        if Explosion.g>139:
            y2 = 5345
            
       #block recursion
        if block_x2 <0:
            block_x2 = block_x2 + 200
        if block_x2 >display_width -100:
            block_x2 = block_x2 - 200
        if block_y> display_height:
            block_y = 0 - block_height
            
            block_x = random.randrange(0,display_width-150)
            dodged += 1
            bdmg1 = False
        if block_y2>display_height:
            Ric = random.randrange(1,2)
            if Ric == 1:
                ricr=  random.randrange(100,200)

            if Ric == 2:
                ricr = random.randrange(-100,-200)
            block_y2 = 0 -block_height-ricr
            bdmg2=  False
            block_x2 = random.randrange(0,display_width - block_width-50)
            dodged += 1
            
        #push car
        if int(Car_player.x) in range (int(Car_AI.x1) +car_width-30-int(Car_player.gear),int(Car_AI.x1)+ car_width) and AI.push == True  :
            Car_AI.x1 = Car_AI.x1 -1-Car_player.gear* 0.5
            Car_player.x = Car_player.x + collision + int(Car_player.gear)
            Health.hbw = Health.hbw-0.05
            if Car_AI.x1_change !=0:
                Car_AI.x1_change -=Car_player.gear* 0.25
            


        if int(Car_player.x +car_width) in range(int(Car_AI.x1),int(Car_AI.x1+30+int(Car_player.gear))) and AI.push == True:
            Car_AI.x1 = Car_AI.x1+1 + Car_player.gear* 0.5
            Car_player.x = Car_player.x - collision- int(Car_player.gear)
            Health.hbw = Health.hbw-0.05
            if Car_AI.x1_change !=0:
                Car_AI.x1_change +=Car_player.gear* 0.25

                
        if int(Car_player.x + car_width) in range(int(Car_AI.x2),int(Car_AI.x2+30+int(Car_player.gear))) and AI.push ==True:
            Car_AI.x2 = Car_AI.x2 +1+ Car_player.gear* 0.5
            Car_player.x  = Car_player.x - collision- int(Car_player.gear)
            Health.hbw = Health.hbw-0.05
            if Car_AI.x2_change !=0:
                Car_AI.x2_change +=Car_player.gear* 0.25

                
        if int(Car_player.x) in range(int(Car_AI.x2+car_width-30-int(Car_player.gear)),int(Car_AI.x2+car_width)) and AI.push == True:
            Car_AI.x2 = Car_AI.x2 -1- Car_player.gear* 0.5
            Car_player.x = Car_player.x + collision+ int(Car_player.gear)
            Health.hbw = Health.hbw-0.05
            if Car_AI.x2_change !=0:
                Car_AI.x2_change -=Car_player.gear* 0.25
                
         #boundaries
        if Car_player.x <0:
            Car_player.x = 0
        if Car_player.x +car_width >display_width:
            Car_player.x= display_width -car_width

            
        if Car_AI.x1 <=0:
            Car_AI.x1 = 0
            AI.push= False
            Car_AI.x1_change =8
        if Car_AI.x1 +car_width >=display_width:
            Car_AI.x1= display_width -car_width
            AI.push = False
            Car_AI.x1_change =-8
        if Car_AI.x2 <=0:
            Car_AI.x2 = 0
            AI.push =False
            Car_AI.x2_change =8
        if Car_AI.x2 +car_width >=display_width:
            Car_AI.x2= display_width -car_width
            AI.push =False
            Car_AI.x2_change= -8

        #########
        
        #crash mechanic


        if Car_player.y < block_y+block_height and test == False:
            None

            if Car_player.x > block_x and Car_player.x < block_x + block_width or Car_player.x+car_width > block_x and Car_player.x + car_width < block_x+block_width:

                Expblit(block_x,block_y)
                Health.hbw =Health.hbw- random.randrange(2,8) - block_speed * 0.2
                color.health_stats_color=  color.red
                if  Car_player.x + car_width >block_x and block_x +50 > Car_player.x + car_width:
                    Car_player.x = Car_player.x -2
                if  Car_player.x <block_x +100 and block_x+50<Car_player.x:
                    Car_player.x = Car_player.x +2
                bdmg1 = True

        
                    
        if Car_player.y < block_y2+block_height and test == False:
            None

            if Car_player.x > block_x2 and Car_player.x < block_x2 + block_width or Car_player.x+car_width > block_x2 and Car_player.x + car_width < block_x2+block_width:


                Expblit(block_x2,block_y2)
                Health.hbw =Health.hbw- random.randrange(2,8)-  block_speed * 0.2
                color.health_stats_color=  color.red
                if  Car_player.x + car_width >block_x2 and block_x2 +50 > Car_player.x + car_width:
                    Car_player.x = Car_player.x -2
                if  Car_player.x <block_x2 +100 and block_x2+50<Car_player.x:
                    Car_player.x = Car_player.x +2
                    bdmg2 = True
        #revive health
        if int(Car_player.y) in range(int(block_y) +80,int(block_y)+block_width)and Explosion.e == 0 and Health.hbw<150:
            if Car_player.x + car_width >block_x - 50 and Car_player.x < block_x :
                Health.hbw= Health.hbw  + int(Car_player.gear)
                color.health_stats_color= color.blue
            if Car_player.x <block_x+block_width + 50 and Car_player.x >block_x:
                Health.hbw= Health.hbw + int(Car_player.gear)
                color.health_stats_color= color.blue
        if int(Car_player.y) in range(int(block_y2) +80,int(block_y2)+block_width) and Explosion.e == 0 and Health.hbw <150:
            if Car_player.x + car_width >block_x2 - 50 and Car_player.x < block_x2 :
                Health.hbw= Health.hbw +  int(Car_player.gear)
                color.health_stats_color= color.blue
            if Car_player.x <block_x2+block_width+ 50 and Car_player.x >block_x2:
                Health.hbw= Health.hbw + int(Car_player.gear)
                color.health_stats_color= color.blue
                


        #collect fuel
        if Car_player.y < fuel_starty+fuel_height:


            if Car_player.x > fuel_startx and Car_player.x < fuel_startx + fuel_width or Car_player.x+car_width > fuel_startx and Car_player.x + car_width < fuel_startx+fuel_width:
                fuel_starty = fuel_starty + 150
                
                fbw = 120
            if fuel_startx  in range(int(Car_player.x) ,int(Car_player.x)+car_width):
                fuel_starty =  fuel_starty  + 150
                fbw = 120
        #gear
        if Car_player.gear == 1:
            block_speed = 8
            Car_player.gear = 1
        if Car_player.gear == 2:
            block_speed = 10
            Car_player.gear = 2
        if Car_player.gear== 3:
            block_speed = 12
            Car_player.gear = 3
        if Car_player.gear== 4:
            block_speed = 14
            Car_player.gear = 4
        if Car_player.gear== 5:
            block_speed = 16
            Car_player.gear = 5
        if Car_player.gear >=6:
            Car_player.gear =5
        if Car_player.gear<1:
            Car_player.gear=1

       #fuelbar color
        if fbw>85:
            color.fuelbar_color = color.green
        if fbw <85:
            color.fuelbar_color = color.greenish
        if fbw<60:
            color.fuelbar_color = (255,128,0)

        if fbw< 25 :
            color.fuelbar_color = color.red

        if fbw <=0 and test== False:
            fuel_over()
        #healthbar

        if Health.hbw>100 :
            color.health_bar_color = color.green
        if Health.hbw<100:
            color.health_bar_color = color.greenish
        if Health.hbw<50:
            color.health_bar_color = (255,128,0)
        if Health.hbw<25:
            color.health_bar_color = color.red
        if Health.hbw<=0:
            Health.hbw =0
            ExplodeCar(Car_player.x ,Car_player.y)

        #arrows blit
        if ctrl_pressed == True:    
            gameDisplay.blit(arrow1, (Car_player.x + 25 ,Car_player.y-30))
            if Health.hbw <=0:
                gameDisplay.blit(arrow7, (Car_player.x + 25 , Car_player.y - 30))
            
            if Health.x1health >= 120:
                gameDisplay.blit(arrow2, (Car_AI.x1 + 25 , y1 - 30))
            elif Health.x1health >=90 :
                gameDisplay.blit(arrow3, (Car_AI.x1 + 25 , y1 - 30))
            elif Health.x1health >= 60 :
                gameDisplay.blit(arrow4, (Car_AI.x1 + 25 , y1 - 30))
            elif Health.x1health >= 30 :
                gameDisplay.blit(arrow5, (Car_AI.x1 + 25 , y1 - 30))
            elif Health.x1health >0:
                gameDisplay.blit(arrow6 , (Car_AI.x1 + 25  , y1- 30))
            elif Health.x1health == 0 :
                gameDisplay.blit(arrow7 , (Car_AI.x1 + 25  , y1- 30))

            if Health.x2health >= 120:
                gameDisplay.blit(arrow2, (Car_AI.x2 + 25 , y2 - 30))
            elif Health.x2health >=90 :
                gameDisplay.blit(arrow3, (Car_AI.x2 + 25 , y2 - 30))
            elif Health.x2health >= 60 :
                gameDisplay.blit(arrow4, (Car_AI.x2 + 25 , y2 - 30))
            elif Health.x2health >= 30 :
                gameDisplay.blit(arrow5, (Car_AI.x2 + 25 , y2 - 30))
            elif Health.x2health >0 :
                gameDisplay.blit(arrow6 , (Car_AI.x2 + 25  , y2- 30))
            elif Health.x2health == 0 :
                gameDisplay.blit(arrow7 , (Car_AI.x2 + 25  , y2- 30))            

        #block damages blit

        if bdmg1== True:
            gameDisplay.blit(block_dmg_pic, (block_x,block_y))
        if bdmg2== True:
            gameDisplay.blit(block_dmg_pic, (block_x2,block_y2))                             
        #car damages blit

        if Cars.ID == 1:
            
            if Health.hbw>110:
                Car_player.Car =Cars.car1
            if Health.hbw<110:
                Car_player.Car =Cars.car1dmg1
            if Health.hbw<80:
                Car_player.Car = Cars.car1dmg2
            if Health.hbw<50:
                Car_player.Car =Cars.car1dmg3
            if Health.hbw<25:
                Car_player.Car =Cars.car1dmg4
        if Cars.ID == 2:
            
            if Health.hbw>110:
                Car_player.Car =Cars.car2
            if Health.hbw<110:
                Car_player.Car =Cars.car2dmg1
            if Health.hbw<80:
                Car_player.Car = Cars.car2dmg2
            if Health.hbw<50:
                Car_player.Car =Cars.car2dmg3
            if Health.hbw<25:
                Car_player.Car =Cars.car2dmg4
        if Cars.ID == 3:
            
            if Health.hbw>110:
                Car_player.Car =Cars.car3
            if Health.hbw<110:
                Car_player.Car =Cars.car3dmg1
            if Health.hbw<80:
                Car_player.Car = Cars.car3dmg2
            if Health.hbw<50:
                Car_player.Car =Cars.car3dmg3
            if Health.hbw<25:
                Car_player.Car =Cars.car3dmg4

        if Car_AI.LCarID == 1:
            if Health.x1health>110:
                Car_AI.Car1 =Cars.car1
            if Health.x1health<110:
                Car_AI.Car1 =Cars.car1dmg1
            if Health.x1health<80:
                Car_AI.Car1 = Cars.car1dmg2
            if Health.x1health<50:
                Car_AI.Car1 =Cars.car1dmg3
            if Health.x1health<25:
                Car_AI.Car1 =Cars.car1dmg4
            
        if Car_AI.LCarID == 2:
            if Health.x1health>110:
                Car_AI.Car1 =Cars.car2
            if Health.x1health<110:
                Car_AI.Car1 =Cars.car2dmg1
            if Health.x1health<80:
                Car_AI.Car1 = Cars.car2dmg2
            if Health.x1health<50:
                Car_AI.Car1 =Cars.car2dmg3
            if Health.x1health<25:
                Car_AI.Car1 =Cars.car2dmg4

        if Car_AI.LCarID == 3:
            if Health.x1health>110:
                Car_AI.Car1 =Cars.car3
            if Health.x1health<110:
                Car_AI.Car1 =Cars.car3dmg1
            if Health.x1health<80:
                Car_AI.Car1 = Cars.car3dmg2
            if Health.x1health<50:
                Car_AI.Car1 =Cars.car3dmg3
            if Health.x1health<25:
                Car_AI.Car1 =Cars.car3dmg4

                
        if Car_AI.RCarID == 1:
            if Health.x2health>110:
                Car_AI.Car2 =Cars.car1
            if Health.x2health<110:
                Car_AI.Car2 =Cars.car1dmg1
            if Health.x2health<80:
                Car_AI.Car2 = Cars.car1dmg2
            if Health.x2health<50:
                Car_AI.Car2 =Cars.car1dmg3
            if Health.x2health<25:
                Car_AI.Car2 =Cars.car1dmg4
            
        if Car_AI.RCarID == 2:
            if Health.x2health>110:
                Car_AI.Car2 =Cars.car2
            if Health.x2health<110:
                Car_AI.Car2 =Cars.car2dmg1
            if Health.x2health<80:
                Car_AI.Car2 = Cars.car2dmg2
            if Health.x2health<50:
                Car_AI.Car2 =Cars.car2dmg3
            if Health.x2health<25:
                Car_AI.Car2 =Cars.car2dmg4

        if Car_AI.RCarID == 3:
            if Health.x2health>110:
                Car_AI.Car2 =Cars.car3
            if Health.x2health<110:
                Car_AI.Car2 =Cars.car3dmg1
            if Health.x2health<80:
                Car_AI.Car2 = Cars.car3dmg2
            if Health.x2health<50:
                Car_AI.Car2 =Cars.car3dmg3
            if Health.x2health<25:
                Car_AI.Car2 =Cars.car3dmg4
                
        #text
        font = pygame.font.SysFont(None, 20)
        text = font.render(str(-(fuel_starty)+display_height-176)+'m', True, color.black)

        if (-(fuel_starty)+display_height-176) in range(0,1250):
            
            gameDisplay.blit(text,(display_width -930,5))

        # Crappy AI
        rad = False
        rad2 = True

        raad  = False
        raad2 = True
        


        if Car_AI.x2_change<1 and Car_AI.x2_change >0:
            randomizespeed()
        if Car_AI.x2_change >-1 and Car_AI.x2_change <0:
            randomizespeed()
        if Car_AI.x2_change== 0:
            randomizespeed()



        #max change in speed
        if Car_AI.x1_change>Car_player.gear+8:
            Car_AI.x1_change = Car_player.gear+8

        if Car_AI.x1_change<-Car_player.gear-8:
            Car_AI.x1_change= -Car_player.gear-8


        if Car_AI.x2_change>Car_player.gear+8:
            Car_AI.x2_change = Car_player.gear+8

        if Car_AI.x2_change<-Car_player.gear-8:
            Car_AI.x2_change= -Car_player.gear-8
            
        #avoiding blocks
        if block_y +350> y1 and rad2 == True:
            if int(Car_AI.x1) +int(car_width) in range(int(block_x),int(block_x) + 50):
                Car_AI.x1_change += -Car_player.gear-8
                rad = True
            if int(Car_AI.x1)  in range(int(block_x+50),int(block_x) + 100) :
                Car_AI.x1_change += Car_player.gear+8
                rad = True
            
        if block_y2+350 > y1 and rad2== True:
            if int(Car_AI.x1) +int(car_width) in range(int(block_x2),int(block_x2) + 50):
                Car_AI.x1_change += -Car_player.gear-8
                rad= True
            if int(Car_AI.x1)  in range(int(block_x2+50),int(block_x2) + 100):
                Car_AI.x1_change += Car_player.gear+8
                rad=True


        if block_y +350> y2 and raad2 == True:
            if int(Car_AI.x2) +int(car_width) in range(int(block_x),int(block_x) + 50):
                Car_AI.x2_change += -Car_player.gear-8
                raad = True
            if int(Car_AI.x2)  in range(int(block_x+50),int(block_x) + 100) :
                Car_AI.x2_change += Car_player.gear+8
                raad = True
            
        if block_y2+350 > y2 and raad2== True:
            if int(Car_AI.x2) +int(car_width) in range(int(block_x2),int(block_x2) + 50):
                Car_AI.x2_change += -Car_player.gear-8
                rad= True
            if int(Car_AI.x2)  in range(int(block_x2+50),int(block_x2) + 100):
                Car_AI.x2_change += Car_player.gear+8
                rad=True               
        #when block somehow comes in contact
        if y1 < block_y+block_height :
            
            if Car_AI.x1 > block_x and Car_AI.x1 < block_x + block_width or Car_AI.x1+car_width > block_x and Car_AI.x1 + car_width < block_x+block_width:

                Expblit(block_x,block_y)
                if  Car_AI.x1+ car_width >block_x and block_x +50 > Car_AI.x1 + car_width:
                    Car_AI.x1_change -= Car_player.gear-8
                    rad = True
                if  Car_AI.x1 <block_x +100 and block_x+50<Car_AI.x1:
                    Car_AI.x1_change += Car_player.gear+8
                    rad = True
                bdmg1 = True
            
                Health.x1health = Health.x1health- hit
                
        if y1 < block_y2+block_height :
            None

            if Car_AI.x1 > block_x2 and Car_AI.x1< block_x2 + block_width or Car_AI.x1+car_width > block_x2 and Car_AI.x1 + car_width < block_x2+block_width:


                Expblit(block_x2,block_y2)
                if Car_AI.x1 + car_width >block_x2 and block_x2 +50 > Car_AI.x1 + car_width:
                    Car_AI.x1_change -= Car_player.gear-8
                    rad = True
                if  Car_AI.x1 <block_x2 +100 and block_x2+50<Car_AI.x1:
                    Car_AI.x1_change += Car_player.gear+8
                    rad = True
                bdmg2 = True
                Health.x1health = Health.x1health- hit
           


        if y2 < block_y+block_height :
            
            if Car_AI.x2 > block_x and Car_AI.x2 < block_x + block_width or Car_AI.x2+car_width > block_x and Car_AI.x2 + car_width < block_x+block_width:

                Expblit(block_x,block_y)
                if  Car_AI.x2+ car_width >block_x and block_x +50 > Car_AI.x2 + car_width:
                    Car_AI.x2_change -= Car_player.gear-8
                    raad = True
                if  Car_AI.x2 <block_x +100 and block_x+50<Car_AI.x2:
                    Car_AI.x2_change += Car_player.gear+8
                    raad = True
                bdmg1 = True
                Health.x2health = Health.x2health- hit
        
                    
        if y2 < block_y2+block_height :
            None

            if Car_AI.x2 > block_x2 and Car_AI.x2< block_x2 + block_width or Car_AI.x2+car_width > block_x2 and Car_AI.x2 + car_width < block_x2+block_width:


                Expblit(block_x2,block_y2)
                if Car_AI.x2 + car_width >block_x2 and block_x2 +50 > Car_AI.x2 + car_width:
                    Car_AI.x2_change -= Car_player.gear-8
                    raad = True
                if  Car_AI.x2 <block_x2 +100 and block_x2+50<Car_AI.x2:
                    Car_AI.x2_change += Car_player.gear+8
                    raad = True
                bdmg2 = True
                Health.x2health = Health.x2health- hit


        ##
        if y1 < block_y + block_height:
            if Car_AI.x1 > block_x and Car_AI.x1 < block_x + block_width +50 or Car_AI.x1+car_width +50> block_x and Car_AI.x1 + car_width < block_x+block_width:
                if  Car_AI.x1+ car_width >block_x and block_x +50 > Car_AI.x1 + car_width:
                    Car_AI.x1_change -= Car_player.gear-8
                    rad = True
                if  Car_AI.x1 <block_x +100 and block_x+50<Car_AI.x1:
                    Car_AI.x1_change += Car_player.gear+8
                    rad = True

        if y1 < block_y2 + block_height:
            if Car_AI.x1 > block_x2 and Car_AI.x1 < block_x2 + block_width +50 or Car_AI.x1+car_width +50> block_x2 and Car_AI.x1 + car_width < block_x2+block_width:
                if  Car_AI.x1+ car_width >block_x2 and block_x2 +50 > Car_AI.x1 + car_width:
                    Car_AI.x1_change -= Car_player.gear-8
                    rad = True
                if  Car_AI.x1 <block_x2 +100 and block_x2+50<Car_AI.x1:
                    Car_AI.x1_change += Car_player.gear+8
                    rad = True
                    
                

        if y2 < block_y + block_height:
            if Car_AI.x2 > block_x and Car_AI.x2 < block_x + block_width +50 or Car_AI.x2+car_width +50> block_x and Car_AI.x2 + car_width < block_x+block_width:
                if  Car_AI.x2+ car_width >block_x and block_x +50 > Car_AI.x2 + car_width:
                    Car_AI.x2_change -= Car_player.gear-8
                    raad = True
                if  Car_AI.x2 <block_x +100 and block_x+50<Car_AI.x2:
                    Car_AI.x2_change += Car_player.gear+8
                    raad = True

        if y1 < block_y2 + block_height:
            if Car_AI.x1 > block_x2 and Car_AI.x1 < block_x2 + block_width +50 or Car_AI.x1+car_width +50> block_x2 and Car_AI.x1 + car_width < block_x2+block_width:
                if  Car_AI.x1+ car_width >block_x2 and block_x2 +50 > Car_AI.x1 + car_width:

                    Car_AI.x1_change -= Car_player.gear-8
                    rad = True
                if  Car_AI.x1 <block_x2 +100 and block_x2+50<Car_AI.x1:
                    Car_AI.x1_change += Car_player.gear+8
                    rad = True
        #sides AI
        if block_x + block_width >1100 and block_y +block_height +200>y1 and Car_AI.x1 + car_width > 1100:
            Car_AI.x1_change = -Car_player.gear-8
            rad = True
            rad2 = False

        if block_x2 + block_width >1100 and block_y2 +block_height +200>y1 and Car_AI.x1 + car_width > 1100:
            Car_AI.x1_change = -Car_player.gear-8
            rad=  True
            rad2 = False

        if block_x+block_width<140 and block_y + block_height + 200 >y1 and Car_AI.x1 <140:
            Car_AI.x1_change = +Car_player.gear+8
            rad  = True
            rad2 = False
            
        if block_x2+block_width<140 and block_y2 +  block_height + 200 > y1 and Car_AI.x1 < 140:
            Car_AI.x1_change = +Car_player.gear+8
            rad = True
            rad2 = False



        if block_x + block_width >1100 and block_y +block_height +200>y2 and Car_AI.x2 + car_width > 1100:
            Car_AI.x2_change = -Car_player.gear-8
            raad = True
            raad2 = False

        if block_x2 + block_width >1100 and block_y2 +block_height +200>y2 and Car_AI.x2 + car_width > 1100:
            Car_AI.x2_change = -Car_player.gear-8
            raad=  True
            raad2 = False

        if block_x+block_width<140 and block_y + block_height + 200 >y2 and Car_AI.x2 <140:
            Car_AI.x2_change = +Car_player.gear+8
            raad  = True
            raad2 = False
            
        if block_x2+block_width<140 and block_y2 +  block_height + 200 > y2 and Car_AI.x2 < 140:
            Car_AI.x2_change = +Car_player.gear+8
            raad = True
            raad2 = False
            
        #Health
        if Health.x1health <=0:
            ExplodeCar2(Car_AI.x1,y1)
        if Health.x2health <= 0:
            ExplodeCar3(Car_AI.x2, y2)
            
            
        pygame.display.update()
        clock.tick(60)

          
selectCar()
pygame.quit()
quit()
