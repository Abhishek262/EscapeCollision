import pygame
import time,random,os,math
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
#declaring variables
fuel_left = 100
fuel_time1 = time.time()

display_width = 860
display_height = 650

pause =  True
options = True
clicked = False
speed_up =False
Help_ = False
controls = False

f= 0.05887
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
reddish  = (200,0,0)
yellow= (247,217,9)
yellowish= (209,137,5)
green = (0,255,0)
greenish = (0,200,0)
block_color = (79,0,0)
blue = (0,0,255)
bluish = (0,0,120)
fuel_color = (1,1,101)
fuel_stats_color = (0,0,0)
grey = (195,195,195)
lightgreen = (139,230,57)
plightgreen =(70,130,17)
fuelbar_color = green
distance = 0
car_width = 92
speed = 0

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
#images
carImg = pygame.image.load('car_2.jpg') 
background = pygame.image.load('background.jpg')
Opt = pygame.image.load('Options.jpg')
Intro = pygame.image.load('intro.png')



def game_intro():

    intro = True

    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                game_sp()

       
        gameDisplay.fill(white)
        
        smallText = pygame.font.Font('freesansbold.ttf',20)
                
        TextSurf2  ,TextRect2  = text_objects_black('(Press any button to play)' , smallText)
        TextRect2.center  = ((display_width/2),(display_height *0.6))
        #gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(Intro ,(170,170))


        button("Play ", 150,450,100,50,green,greenish,game_sp)
        button("Quit" , 600,450,100,50,red,reddish,quitgame)
        button("Options" ,375 ,500 ,100,50,blue,bluish,Options)

        pygame.display.update()
        clock.tick(15)
        
def modes():
    mode = True
    while mode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


       
        gameDisplay.fill(white)
        
        smallText = pygame.font.Font('freesansbold.ttf',40)
                
        TextSurf2  ,TextRect2  = text_objects_black('Select Mode' , smallText)
        TextRect2.center  = ((display_width/2),(display_height *0.1))
        gameDisplay.blit(TextSurf2, TextRect2)

        button("Singleplayer ", 350,250,150,50,green,greenish,game_sp)
        button("Multiplayer" , 350,450,150,50,red,reddish,game_mp)


        pygame.display.update()
        clock.tick(15)        

def Options():
    
    global options
    options = True
    largeText = pygame.font.SysFont("Arial",60)
    smallText = pygame.font.SysFont(None, 10)
    
    TextSurf, TextRect = text_objects("Options", largeText)

    TextRect.center = ((display_width/2),(display_height*0.1))
    
    while options:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type  == pygame.KEYDOWN:
                if event.key ==pygame.K_ESCAPE:

                    options  = False
                    
        gameDisplay.fill(white)

        gameDisplay.blit(TextSurf, TextRect)


        gameDisplay.blit(Opt ,(170,130))        

        button("Select Car",350,150,150,50,green,greenish,carSelect)
        button("Help ",350,250,150,50,yellow,yellowish,Help)
        button("Controls",350,350,150,50,blue,bluish,Controls)

        button("Back",350,450,150,50,red,reddish,game_intro)


        pygame.display.update()
        clock.tick(15)

def Controls():
    global controls
    controls = True
    largeText = pygame.font.SysFont("Arial",60)
    smallText = pygame.font.SysFont(None, 30)
    TextSurf, TextRect = text_objects("Controls", largeText)
    TextSurf2, TextRect2 = text_objects_black("Movement keys :                    W , A , S , D", smallText)
    TextSurf3, TextRect3 = text_objects_black("Movement keys (Arrows) :                    Up , Down , Left , Right        ", smallText)
    TextSurf4, TextRect4 = text_objects_black("Pause :                    Spacebar or Escape", smallText)
    TextSurf5, TextRect5 = text_objects_black("Speed UP :                    F key", smallText)
    TextSurf6, TextRect6 = text_objects_black("Speed Down:                    G key", smallText)



    TextRect.center = ((display_width* 0.5),(display_height*0.1))
    TextRect2.center = ((display_width * 0.4),(display_height*0.3))
    TextRect3.center = ((display_width* 0.55),(display_height*0.4))
    TextRect4.center = ((display_width *0.395),(display_height*0.5))
    TextRect5.center = ((display_width* 0.33),(display_height*0.6))
    TextRect6.center = ((display_width *0.35),(display_height*0.7))




    
    while Help:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type  == pygame.KEYDOWN:
                if event.key ==pygame.K_ESCAPE:

                    options  = False
                    
        gameDisplay.fill(white)

        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(TextSurf3, TextRect3)
        gameDisplay.blit(TextSurf4, TextRect4)
        gameDisplay.blit(TextSurf5, TextRect5)
        gameDisplay.blit(TextSurf6, TextRect6)


        button("Back",350,display_width/2 + 100 ,150,50,red,reddish,Options)
        


        pygame.display.update()
        clock.tick(15)
    
    
    

def carSelect(c =930):

    select =True
    largeText = pygame.font.SysFont("Arial",80)
    TextSurf, TextRect = text_objects("Select Car", largeText)
    TextRect.center = ((display_width/2),(display_height/10))
    while select:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:

                    select  = False
                    
                
        gameDisplay.fill(white)
        
        gameDisplay.blit(TextSurf, TextRect)

        button("X",175,450,50,50,grey,black,car_1)
        button("X",375,450,50,50,grey,black,car_2)
        button("X",575,450,50,50,grey,black,car_3)
        button("Back" ,250 ,550,100,50,red,reddish,Options)
        button("Play", 450,550,100,50,green,greenish,game_sp)

        carImg1 = pygame.image.load('car_1.jpg')
        carImg2 = pygame.image.load('car_2.jpg')
        carImg3 = pygame.image.load('car_3.jpg')
        
        gameDisplay.blit(carImg1, (150,250))
        gameDisplay.blit(carImg2, (350,250))
        gameDisplay.blit(carImg3, (550,250))

        gsp=  pygame.image.load('gsp.jpg')
        gameDisplay.blit(gsp,(c,230))


        pygame.display.update()
        clock.tick(15)
    
def car_1():
    global carImg

    carImg = pygame.image.load('car_1.jpg')
    carSelect(130)

    
def car_2():
    global carImg

    carImg = pygame.image.load('car_2.jpg')
    carSelect(330)

def car_3():
    global carImg

    carImg = pygame.image.load('car_3.jpg')
    carSelect(530)

def Help():
    global Help_
    Help_ = True
    largeText = pygame.font.SysFont("Arial",60)
    smallText = pygame.font.SysFont(None, 30)
    TextSurf, TextRect = text_objects("Help", largeText)
    TextSurf2, TextRect2 = text_objects_black("The goal of this game is to acheive as much score as possible.", smallText)
    TextSurf3, TextRect3 = text_objects_black("Steer your car through incoming blocks and dodge them ASAP.", smallText)
    TextSurf4, TextRect4 = text_objects_black("Also , watch out for that fuel tank as it has a tendency", smallText)
    TextSurf5, TextRect5 = text_objects_black("to become empty at the time when it is most needed.", smallText)
    TextSurf6, TextRect6 = text_objects_black("Fuel can be collected by colliding with the blue blocks.", smallText)
    TextSurf7, TextRect7 = text_objects_black("As you dodge blocks your score increases. With the increment", smallText)
    TextSurf8, TextRect8 = text_objects_black("in score, the speed of the blocks , fuel distance increases and", smallText)
    TextSurf9, TextRect9 = text_objects_black("the game becomes harder in general. ", smallText)


    TextRect.center = ((display_width/2),(display_height*0.1))
    TextRect2.center = ((display_width/2),(display_height*0.25))
    TextRect3.center = ((display_width/2),(display_height*0.32))
    TextRect4.center = ((display_width/2),(display_height*0.39))
    TextRect5.center = ((display_width/2),(display_height*0.46))
    TextRect6.center = ((display_width/2),(display_height*0.53))
    TextRect7.center = ((display_width/2),(display_height*0.60))
    TextRect8.center = ((display_width/2),(display_height*0.67))
    TextRect9.center = ((display_width/2),(display_height*0.74))



    
    while Help:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type  == pygame.KEYDOWN:
                if event.key ==pygame.K_ESCAPE:

                    options  = False
                    
        gameDisplay.fill(white)

        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(TextSurf3, TextRect3)
        gameDisplay.blit(TextSurf4, TextRect4)
        gameDisplay.blit(TextSurf5, TextRect5)
        gameDisplay.blit(TextSurf6, TextRect6)
        gameDisplay.blit(TextSurf7, TextRect7)
        gameDisplay.blit(TextSurf8, TextRect8)
        gameDisplay.blit(TextSurf9, TextRect9)

        button("Back",350,display_width/2 + 100 ,150,50,red,reddish,Options)
        


        pygame.display.update()
        clock.tick(15)
    


def paused():
    global pause
    largeText = pygame.font.SysFont("Arial",80)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type  == pygame.KEYDOWN:
                if event.key ==pygame.K_SPACE or event.key == pygame.K_ESCAPE:

                    pause  = False
                    
                
        gameDisplay.fill(white)
        gameDisplay.blit(background,(0,0))
        gameDisplay.blit(TextSurf, TextRect)

        button("Restart",150,450,100,50,green,greenish,restart)
        button("Continue",350,450,100,50,blue,bluish,unpause)
        button("Quit",550,450,100,50,red,reddish,game_intro)

        pygame.display.update()
        clock.tick(15)

def pause_true():
    global pause
    pause = True

def restart() :
    game_sp()

def unpause():
    global pause
    pause = False

def button(msg,x,y,w,h,ic,ac,action = None,action2 = None):
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
    textSurf, textRect = text_objects_black(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def button2(msg,x,y,w,h,color,pcolor,action= None,action2 =None):
    global clicked
    global speed_up
    mouse = pygame.mouse.get_pos()
    
    click = pygame.mouse.get_pressed()

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects_black(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )

    if x+w >mouse[0] > x and y+h >mouse[1] > y:

        
        if click[0] == 1 and action != None and clicked == False:
            clicked = True
            action()


        elif click[0] == 1 and action != None and clicked == True:
          clicked = False
          speed_up = False
          if action2 != None:
              action2()
          
  
    if clicked == False:
        pygame.draw.rect(gameDisplay, color,(x,y,w,h))
        gameDisplay.blit(textSurf, textRect)

    if clicked == True:
        pygame.draw.rect(gameDisplay, pcolor, (x,y,w,h))
        gameDisplay.blit(textSurf, textRect)

def blocks_dodged(count):

    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(count), True, black)
    
    gameDisplay.blit(text,(30,2))


def fuel_stats(count):
    font  = pygame.font.SysFont(None , 25)
    
    text = font.render("Fuel:", True , fuel_stats_color)

    gameDisplay.blit(text ,(display_width - 720, 2))

    



def blocks(blockx, blocky, blockw, blockh, color):
    
    pygame.draw.rect(gameDisplay, color, [blockx, blocky, blockw, blockh])

def fuel(fuelx , fuely , fuelw  , fuelh , color):
    pygame.draw.rect(gameDisplay , color , [fuelx ,fuely , fuelw ,fuelh])\




def fuelbar(fbx,fby,fbw,fbh,color):
    pygame.draw.rect(gameDisplay , color , [fbx ,fby , fbw ,fbh])
    pygame.draw.aaline(gameDisplay , black , (690- 500,2),(810-500,2),20)
    pygame.draw.aaline(gameDisplay , black , (690-500,22),(810-500,22),20)
    pygame.draw.aaline(gameDisplay , black , (690-500,2),(690-500,22),20)
    pygame.draw.aaline(gameDisplay , black , (810-500,2),(810-500,23),20)

def speedup():
    global speed_up
    speed_up= True
    gameDisplay.fill(white)

    time.sleep(0.2)

def speeddown():

    global speed_up
    speed_up = False
    gameDisplay.fill(white)

    time.sleep(0.2)
    
def fuel_consume():
    global fuel_color
    fuel_color = grey

    global fuel_left
    fuel_left = 100.0

def fuel_color_change():
    global fuel_color
    fuel_color = (1,1,101)

def fuel_over():
    largeText = pygame.font.SysFont("Arial",75)
    TextSurf, TextRect = text_objects_black("Fuel Over", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)



    

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        button("Play Again",150,450,150,50,green,greenish,game_sp)
        button("Quit",550,450,150,50,red,reddish,quitgame)
        global fuel_left
        fuel_left  = 102

        pygame.display.update()
        clock.tick(15)     
    

def car(x,y):


    gameDisplay.blit(carImg,(x,y))

def blit_background(a,b):
    gameDisplay.blit(background, (a,b))



def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def text_objects_black(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()



    

def crash(count):
    
    largeText = pygame.font.SysFont("Arial",75)
    TextSurf, TextRect = text_objects_black("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    mediumText  = pygame.font.SysFont("Calibri(body)",35)
    TextSurf2 , TextRect2 = text_objects_black("Your Score : "  + str(count),  mediumText)
    TextRect2.center = ((display_width/2),(display_height* 0.6))
    gameDisplay.blit(TextSurf2, TextRect2)





    

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type  == pygame.KEYDOWN:
                game_sp()
                
        #gameDisplay.fill(white)
        

        button("Play Again",150,450,150,50,green,greenish,game_sp)
        button("Quit",550,450,150,50,red,reddish,quitgame)
        global fuel_left
        fuel_left  = 102

        pygame.display.update()
        clock.tick(15)



def quitgame():
    pygame.quit()
    quit()
    gameExit = True



    
def game_sp():
    #main game loop
    global fuel_left
    global fuel_time1
    global fuelbar_color
    global green
    global greenish
    global red
    global distance
    global carImg
    global pause
    global clicked
    global speed_up,clicked,coincolor1,coincolor2,f
    
    speed_up = False
    clicked = False
    block_incr = 0.25
    speed = 0
    


    x = (display_width * 0.45)
    y = (display_height * 0.72)

    x_change = 0

    block_startx = random.randrange(0, display_width - 100)


    block_starty = -600
    block_speed = 4
    block_width = 100
    block_height = 100
    
    blockCount = 1

    dodged = 0

    #fuel(block)
    fuel_startx = random.randrange(50 , display_width - 100)
    fuel_starty = -2000
    fuel_speed = 4
    fuel_width = 40
    fuel_height = 40

    fuelCount = 1
    global fuel_stats_color
    fuel_stats_color = (0,0,0)

    #fuelbar 
    fbx = display_width - 670
    fby = 2
    fbw = 120 
    fbh = 20


    
    gameExit = False
    

    while not gameExit:


        fuel_time2 = time.time()
        if (fuel_time2 - fuel_time1) >= 2.0:
            fuel_left -= 0.05
            fuel_time2 = fuel_time1
            fbw  = fbw - f


            
        if fbw <= 1 :
            fuel_left = 0
            fuel_over()
            
        if dodged > 50:
            block_incr += 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -8-dodged * 0.1 -speed
                if event.key == pygame.K_RIGHT:
                    x_change = 8+dodged * 0.1+ speed
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
                    x_change = -8- dodged*0.1- speed
                if event.key == pygame.K_d:
                    x_change = 8+ dodged*0.1 +speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

            if event.type== pygame.KEYDOWN:
                if event.key == pygame.K_f and speed_up == False:
                    speedup()
                    clicked = True

                if event.key == pygame.K_g and speed_up == True:
                    speeddown()
                    
                    clicked =False

                    

        x += x_change
        gameDisplay.fill(white)
        blit_background(0,0)



        fuel(fuel_startx , fuel_starty , fuel_width  , fuel_height , fuel_color)

        blocks(block_startx , block_starty, block_width, block_height, block_color)



        fuel_starty +=fuel_speed



        fuelbar(fbx,fby,fbw,fbh, fuelbar_color)
        button(' || ' ,display_width - 130, 2 ,35, 35,lightgreen,plightgreen,paused,pause_true )
        button2('>>',display_width - 180 ,2,35,35,lightgreen,plightgreen,speedup,speeddown)
        button('X',display_width - 80 ,2,35,35,lightgreen,plightgreen,game_intro)

        block_starty += block_speed

        car(x,y)
        blocks_dodged(dodged)
        fuel_stats(fuel_left)

        if x > display_width - (car_width+20) or x < 10:
            x_change = 0
        if block_starty > display_height:
            block_starty = 0 - block_height
            
            block_startx = random.randrange(0,display_width-100)

            dodged += 1
##            block_speed += block_incr
            
        if fuel_starty > display_height:
            fuel_lag = dodged * 50
            fuel_starty = -2000 - fuel_lag
            fuel_startx = random.randrange(50,display_width - 50)
            fuel_color_change()
            


        if y < block_starty+block_height:
            None

            if x > block_startx and x < block_startx + block_width or x+car_width > block_startx and x + car_width < block_startx+block_width:
                crash(dodged)
    
        if y < fuel_starty+fuel_height:
            

            if x > fuel_startx and x < fuel_startx + fuel_width or x+car_width > fuel_startx and x + car_width < fuel_startx+fuel_width:
                fuel_consume()
                fbw = 120
            if fuel_startx  in range(int(x) ,int(x)+car_width):
                fuel_consume()
                fbw = 120
    

            
        if fbw>75:
            fuelbar_color = green        
        if fbw <75:
            fuelbar_color = greenish
        if fbw<40:
            fuelbar_color = (255,128,0)
            speed_up = False
            clicked =False
            
        if fbw< 25 :
            fuelbar_color = red
        
        #special events(mostly wont occour)
            
        if dodged > 100:
            block_width = 120
        if dodged > 200:
            block_width =140
        if dodged >300:
            block_width = 160
        if dodged > 400:
            block_width = 180
        if dodged >500:
            block_width =200


        if speed_up == True:

            block_speed = 10 + block_incr *dodged
            speed = 1
            f = 0.072
        if speed_up == False:
            
            block_speed= 4  + block_incr *dodged
            speed= 0
            f = 0.0588
        if x< -20:
            crash(dodged)
        if x + car_width>display_width+10 :
            crash(dodged)


        pygame.display.update()
        clock.tick(60)


def game_mp():
    import mul.py
    



game_intro()
pygame.quit()
quit()

