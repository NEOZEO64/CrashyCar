# -*- coding: utf-8 -*-
'''
Name:   CrashyCar
Date:   11.04.19

Changes 31.5.22: Improved configuration
'''

from config import *

################################################################################
class playerSprite(object): #player1-Object
    def __init__(self,line,y,player1Size): #function when initializing the class
        self.line = line
        self.width = roadLineWidth * player1Size
        self.height = self.width * player1Height
        self.pic = pg.image.load(path+carPicName)
        self.pic = pg.transform.scale(self.pic, (int(self.width), int(self.height)))
        self.rotatedpic = self.pic
        self.y = y
        self.x = roadBorder + roadLineWidth * (self.line-1) + (roadLineWidth-self.width) / 2
        self.mkeyd = 0
        self.mkeya = 0

    def go(self):   #Control & Run function

        event = pg.event.poll()
        keys = pg.key.get_pressed() #list all the pressed keys
        if event.type == pg.MOUSEBUTTONDOWN or keys[pg.K_d] or keys[pg.K_a]:
            if event.type == pg.MOUSEBUTTONDOWN:
                x,y = pg.mouse.get_pos()
                if x > screenWidth/2 and self.mkeyd == 0 and self.line != streetLineQuantity:
                    self.mkeyd = 1 #memoryvariable = 1
                    self.line += 1 #switch to the right variable
                elif x < screenWidth/2 and self.mkeya == 0 and self.line != 1:
                    self.mkeya = 1 #memoryvariable = 1
                    self.line -= 1 #switch to the right variable

            if keys[pg.K_d] and self.mkeyd == 0 and self.line != streetLineQuantity: #to switch only one line by clicking, here is a flipflop-switch
                self.mkeyd = 1 #memoryvariable = 1
                self.line += 1 #switch to the right variable
            elif keys[pg.K_d] == False and event.type == pg.MOUSEBUTTONUP:
                self.mkeyd = 0 #memoryvariable = 0
            if keys[pg.K_a] and self.mkeya == 0 and self.line != 1: #to switch only one line by clicking, here is a flipflop-switch
                self.mkeya = 1 #memoryvariable to 1
                self.line -= 1 #switch to left line
            elif keys[pg.K_a] == False and event.type == pg.MOUSEBUTTONUP:
                self.mkeya = 0 #memoryvariable to 0
        else:
            self.mkeya = 0; self.mkeyd = 0

        if self.x + self.width/2 < (roadBorder + roadLineWidth * (self.line-1) + roadLineWidth - self.width / 2):
            self.zielabstand = (roadBorder + roadLineWidth * (self.line-1) + (roadLineWidth-self.width) / 2) - self.x
            self.x += self.zielabstand/8
            self.rotatedpic = pg.transform.rotate(self.pic,-self.zielabstand/4)

        elif self.x+self.width/2 > (roadBorder + roadLineWidth * (self.line-1) + roadLineWidth - self.width / 2):
            self.rotatedpic = pg.transform.rotate(self.pic,self.zielabstand/4)
            self.zielabstand = self.x - (roadBorder + roadLineWidth * (self.line-1) + (roadLineWidth-self.width)/2)
            self.x -= self.zielabstand/8

    def show(self): #show-function
        if self.zielabstand > 4:
            screen.blit(self.rotatedpic, (self.x, self.y)) #show the picture
        else:
            screen.blit(self.pic, (self.x, self.y)) #show the picture


class Warningobstacle(object): #Obstacle-Object
    def __init__(self,line, speed, size): #function when initializing the class
        self.line = line    #position on the road
        self.width = roadLineWidth * obstacleSize  #width of the obstacle
        self.height = self.width * obstacleHeight #height of the obstacle
        self.x = roadBorder + roadLineWidth * (self.line-1) + (roadLineWidth-self.width) / 2
        self.y = -self.height   #start y-position
        self.speed = speed
        self.pic = pg.image.load(path+warningPicName)
        self.pic = pg.transform.scale(self.pic, (int(self.width), int(self.height))) #resize the picture
    def show(self): #show the obstacle
        screen.blit(self.pic, (self.x, self.y))
    def move(self):
        self.y += self.speed #move down


class Flower(object): #Obstacle-Object
    def __init__(self,speed,pic,size,x): #function when initializing the class
        self.width = roadLineWidth * flowerSize  #width of the obstacle
        self.height = self.width * flowerHeight #height of the obstacle
        self.x = x
        self.y = -self.height   #start y-position
        self.speed = speed
        self.pic = pg.image.load(path+pic)
        self.pic = pg.transform.scale(self.pic, (int(self.width), int(self.height))) #resize the picture
    def move(self):
        self.y += self.speed #move down
    def show(self): #show the obstacle
        screen.blit(self.pic, (self.x, self.y))


class GrasPixel(object):
    def __init__(self,x,y,color):
        global speed, graspixelWidth,graspixelHeight
        self.x = x
        self.y = y
        self.width = graspixelWidth
        self.height = graspixelHeight
        self.color = color
        self.speed = speed
    def move(self):
        self.y+= self.speed
    def show(self):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0) #left yellow stripe


class Score(object):
    def __init__(self,start,addition):
        self.amount = start #the score-int
        self.amountAddition = addition #the difference between every new speed-level
        self.label = font.render(str(self.amount), 10, Fontcolor)
        w,h = font.size(("12345678"))
        self.signx = scoreLabelx-labelBackgroundBorder
        self.signy = scoreLabely-labelBackgroundBorder
        self.signwidth = int(w+2*labelBackgroundBorder)
        self.signheight = int(h+2*labelBackgroundBorder)
        self.signpic = pg.image.load(path+signPicName)
        self.signpic = pg.transform.scale(self.signpic, (self.signwidth, self.signheight)) #resize the picture
        self.y = scoreLabelx#y-position of the label
    def run(self):
        self.amount += self.amountAddition
    def show(self):
        w,h = font.size((str(self.amount)))
        self.label = font.render((str(self.amount)), 10, Fontcolor)
        screen.blit(self.signpic, (self.signx, self.signy))
        #pg.draw.rect(screen, LabelBackgroundColor, (moneyLabelx-labelBackgroundBorder, moneyLabely-labelBackgroundBorder, int(w+2*labelBackgroundBorder), int(h+2*labelBackgroundBorder), 0) #x,y,width,height
        screen.blit(self.label, (self.signx+self.signwidth-w-labelBackgroundBorder,self.y))


class Coin(object): #Coin-Object
    def __init__(self,line,speed,size,amount):
        self.line = line
        self.amount = amount
        self.width = roadLineWidth * size #coinSize
        self.height = self.width #height of the coin
        self.x = roadBorder + roadLineWidth * (self.line-1) + (roadLineWidth-self.width) / 2
        self.y = -self.height-10   #start y-position
        self.speed = speed
        self.pic = pg.image.load(path+"Coin{}.png".format(str(amount)))
        self.pic = pg.transform.scale(self.pic, (int(self.width), int(self.height))) #resize the picture
    def move(self):
        self.y += self.speed
    def show(self):
        screen.blit(self.pic, (self.x, self.y))


class Money(object):
    def __init__(self,start):
        self.amount = start #the score-int
        w,h = font.size(("123456"))
        self.signwidth = int(w+2*labelBackgroundBorder)
        self.signheight = int(h+2*labelBackgroundBorder)
        self.signx = screenWidth-self.signwidth-labelBackgroundBorder
        self.signy = moneyLabely-labelBackgroundBorder
        self.signpic = pg.image.load(path+signPicName)
        self.signpic = pg.transform.scale(self.signpic, (self.signwidth, self.signheight)) #resize the picture

        self.y = self.signy+ labelBackgroundBorder#y-position of the label

    def add(self,amount):
        self.amount += amount
    def show(self):
        global moneyLabelx, moneyLabely, labelBackgroundBorder
        w,h = font.size((str(self.amount)+"C"))
        scorel = font.render((str(self.amount)+"C"), 10, Fontcolor)
        screen.blit(self.signpic, (self.signx, self.signy))
        #pg.draw.rect(screen, LabelBackgroundColor, (moneyLabelx-labelBackgroundBorder, moneyLabely-labelBackgroundBorder, int(w+2*labelBackgroundBorder), int(h+2*labelBackgroundBorder), 0) #x,y,width,height
        screen.blit(scorel, (self.signx+self.signwidth-w-labelBackgroundBorder,self.y))


class FPSlabel(object):
    def __init__(self,fpsx,fpsy):
        global font
        w,h = font.size(("123456"))
        self.clock = pg.time.Clock()
        self.amount = self.clock.get_fps()
        self.x = fpsx
        self.y = fpsy
    def show(self):
        global labelBackgroundBorder
        self.amount = int(self.clock.get_fps())
        scorel = font.render(("FPS:"+str(self.amount)), 10, Fontcolor)
        screen.blit(scorel, (self.x,self.y))


class Button(object):
    def __init__(self,x,y,label):
        self.over = 10
        self.width = 400
        self.height = 60
        self.x = x - self.width/2
        self.y = y - self.height/2
        self.string = label
        self.lineColor = (100,100,255)
        self.pressColor = (0,0,120)
        self.maybePressColor = (0,0,150)
        self.noInterestColor = (0,0,200)
        self.lineThickness = 2
        self.rect = pg.Rect(self.x, self.y,self.width, self.height)
        self.rectOut = pg.Rect(self.x-self.lineThickness, self.y-self.lineThickness,self.width+2*self.lineThickness, self.height+2*self.lineThickness)
        self.font = pg.font.Font('freesansbold.ttf', 80)
        self.label = font.render(self.string, True, Fontcolor)
        self.labelwidth = self.label.get_width()
        self.labelheight = self.label.get_height()


    def checkMouseOverButton(self):
        x, y = pg.mouse.get_pos()
        if self.x < x < self.x+self.width and self.y < y < self.y+self.height:
            return True
        else:
            return False
    def show(self):
        x, y = pg.mouse.get_pos()
        leftPressed,rightPressed,middelPressed = pg.mouse.get_pressed()
        pg.draw.rect(screen, self.lineColor, self.rectOut)
        if self.x < x < self.x+self.width and self.y < y < self.y+self.height:
            if leftPressed:
                pg.draw.rect(screen, self.pressColor, self.rect)
            else:
                pg.draw.rect(screen, self.maybePressColor, self.rect)
        else:
            pg.draw.rect(screen, self.noInterestColor, self.rect)
        screen.blit(self.label,(self.x+self.width/2-self.labelwidth/2,self.y+self.height/2-self.labelheight/2))


################################################################################

def show():
    global stripes,stripeHeight,stripePositionxlst,obstacles,flowers,coins,player,scoreVisible,score

    screen.fill(borderColor) #draw background
    pg.draw.rect(screen, roadColor, (roadBorder-roadOverstand, 0, screenWidth-2*roadBorder+2*roadOverstand, screenHeight), 0) #road
    pg.draw.rect(screen, yellowStripeColor, (roadBorder-(stripeWidth/2), 0, stripeWidth, screenHeight), 0) #left yellow stripe
    pg.draw.rect(screen, yellowStripeColor, (screenWidth-roadBorder-stripeWidth/2, 0, stripeWidth, screenHeight), 0) #right yellow stripe
    if graspixels:
        for pixel in graspixellst:
            pixel.show()
    if stripes:
        for x in stripePositionxlst: #show every stripe on the road
            for y in range(0,screenHeight+stripeHeight,stripeHeight*2):
                pg.draw.rect(screen, whiteStripeColor, (x-(stripeWidth/2), y + stripePosition, stripeWidth, stripeHeight), 0) #x,y,width,height
    if obstacles:
        for obstacle in warningObstacleList: #show every obstacle
            obstacle.show()
    if flowers:
        for flower in flowerlst:
            flower.show()
    if coins:
        for coin in coinlst:
            coin.show()
        money.show()
    if player:
        player1.show()
    if scoreVisible:
        score.show()
    if fpsLabelOn:
        fpsLabel.show()
    pg.display.flip()

def gameOver():
    global run
    print("Score: {}".format(score.amount))
    print("Game Over")
    run = False

def escapeMenu():
    global run,mLeftClick
    print("Escape")
    exit = 0
    pg.mouse.set_visible(True)
    continueButton = Button(screenWidth/2,screenHeight/2,"Continue")
    backButton = Button(screenWidth/2,screenHeight/2+continueButton.height+buttonGap,"Back to Menu")


    titleFont = pg.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render("Stop", True, Fontcolor)
    infofont = pg.font.Font('freesansbold.ttf', 10)
    infolabel = font.render(info, True, Fontcolor)

    x = screenWidth/2-titleSurf1.get_width()/2
    y = (screenHeight/2-titleSurf1.get_height()/2)-4*Overstand

    true = True

    while true:
        for event in pg.event.get():
            if event.type == QUIT:      #event is quit
                work = 0
                true = False
                break #Press on the red button

        leftClick,middleClick,rightClick = pg.mouse.get_pressed()
        if leftClick:
            if mLeftClick:
                if continueButton.checkMouseOverButton():
                    print("continueButton pressed")
                    true = False
                if backButton.checkMouseOverButton():
                    print("backButton pressed")
                    run = 0
                    true = False
            mLeftClick = False
        else:
            mLeftClick = True

        screen.fill(roadColor)
        screen.blit(titleSurf1,(x,y))
        screen.blit(infolabel,(10,screenHeight-30))
        continueButton.show()
        backButton.show()
        pg.display.update()
        fpsLabel.clock.tick(FPS)
    pg.mouse.set_visible(mousevisibility)


def start():
    global work, run, mLeftClick
    pg.mouse.set_visible(True)
    playButton = Button(screenWidth/2,screenHeight/2,"Play")
    quitButton = Button(screenWidth/2,screenHeight/2+playButton.height+buttonGap,"Quit")

    #titleFont = pg.font.Font('freesansbold.ttf', 100)
    #titleSurf1 = titleFont.render(screenCaption, True, Fontcolor)
    infofont = pg.font.Font('freesansbold.ttf', 10)
    infolabel = font.render(info, True, Fontcolor)

    headerpic = pg.image.load(path+headerPicName)
    #self.pic = pg.transform.scale(self.pic, (int(self.width), int(self.height)))

    rectW1 = headerpic.get_width()
    rectH1 = headerpic.get_height()
    x = screenWidth/2-rectW1/2
    y = (screenHeight/2-rectH1/2)-4*Overstand
    startrun = True
    while startrun:
        screen.fill(roadColor)
        pg.draw.ellipse(screen, (random.randrange(100),random.randrange(100),random.randrange(100)), (x-Overstand, y, rectW1+2*Overstand,rectH1), 0)
        screen.blit(headerpic,(x,y))
        #screen.blit(titleSurf1,(x,y))
        screen.blit(infolabel,(10,screenHeight-30))

        playButton.show()
        quitButton.show()
        for event in pg.event.get():
            if event.type == QUIT:      #event is quit
                work = 0
                run = 0

        leftClick,middleClick,rightClick = pg.mouse.get_pressed()
        if leftClick:
            if mLeftClick:
                if playButton.checkMouseOverButton():
                    print("Playbutton pressed")
                    run = True
                    startrun = False
                if quitButton.checkMouseOverButton():
                    print("Quitbutton pressed")
                    work = 0
                    run = 0
                    startrun = False
            mLeftClick = False
        else:
            mLeftClick = True

        pg.display.update()
        fpsLabel.clock.tick(FPS)
    pg.mouse.set_visible(mousevisibility)
################################################################################

#import packages
import pygame as pg #game graphics
from pygame.locals import * #game graphics
import random,time,os
pg.init() #initialize pygame-package

infoObject = pg.display.Info()
screenWidth = 800 #infoObject.current_w #800
screenHeight = 480#infoObject.current_h #480
if fullScreen:
    screen = pg.display.set_mode((screenWidth,screenHeight),pg.FULLSCREEN) #build the screen as fullScreen
else:
    screen = pg.display.set_mode((screenWidth,screenHeight)) #build the screen fullscreen or as window #set the cursor to visible or unvisible

font = pg.font.Font('freesansbold.ttf', int(screenHeight/24))

labelBackgroundBorder = int((screenHeight/24)*1/4) #how much bigger is the rect behind the label?
Overstand = 40
pg.display.set_caption(screenCaption) #set the screenCaption
speed = screenHeight/120
roadBorder = int((screenWidth / 4) / 2)
roadLineWidth = (screenWidth - 2* roadBorder) / streetLineQuantity
stripeWidth = int(6 / streetLineQuantity * 5)
graspixelWidth = int(screenWidth/100)
graspixelHeight = int(graspixelWidth)
work = True
work = True
mkeyesc = False
mLeftClick = True


if stripes:
    stripePositionxlst = []
    stripeHeight = int(40 / streetLineQuantity * 5) #roadStripe settings
    for x in range(streetLineQuantity-1):
        stripePositionxlst.append(roadLineWidth*(x+1)+roadBorder-stripeWidth/2)

if player:
    startLine = int(streetLineQuantity/2)   #first line-position of the car
    yPosition = screenHeight-screenHeight*1/4 #the height of the car on teh screen

if fpsLabelOn:
    fpsLabel = FPSlabel(fpsx,fpsy)

while work:
    start()
    if work != True:
        break
    score = Score(startScore,scoreAddition)
    if coins:
        coinlst = []
        money = Money(startMoney)
    if obstacles:
        warningObstacleList = []
        obstacleProtection = 0 #start the game
        obstacleProbabilitylst = []
        probabilitylst = []
        for x in range(streetLineQuantity):
            probabilitylst.append(999-(streetLineQuantity-x)*5)
        for x in probabilitylst:
            if len(obstacleProbabilitylst) < streetLineQuantity - 1:
                obstacleProbabilitylst.append(x)
    if flowers:
        leftProtection = 0
        rightProtection = 0
        decorationProtection = 50
        flowerlst = []
    if stripes:
        stripePosition = 0
    if graspixels:
        pixelProtection = 10
        graspixellst = []
        for y in range(0,screenHeight,graspixelHeight):
            for x in range(0,roadBorder-roadOverstand,graspixelWidth): #left side
                color = (random.randrange(0,10),random.randrange(150,180),random.randrange(20,30))
                graspixellst.append(GrasPixel(x,y,color))
            for x in range(screenWidth-roadBorder+roadOverstand,screenWidth,graspixelWidth): #right side
                color = (random.randrange(0,10),random.randrange(150,180),random.randrange(20,30))
                graspixellst.append(GrasPixel(x,y,color))
    if player:
        player1 = playerSprite(startLine,yPosition,player1Size) #initializing player1-object
    print("Setup abgeschlossen") #debug information
    if run:
        print("runrunrun")
    while run: #game-loop
        if player:
            player1.go() #control the player1-Object (Car)
        score.run()

        if fasterandfaster:
            if score.amount > scorespeed: #make the game faster
                speed += screenHeight/240
                if obstacles:
                    for x in warningObstacleList:
                        x.speed = speed
                if flowers:
                    for x in flowerlst:
                        x.speed = speed
                if graspixels:
                    for x in graspixellst:
                        x.speed = speed
                if coins:
                    for x in coinlst:
                        x.speed = speed
                scorespeed += (scorespeed*1.2)

        if obstacles:
            for obstacle in warningObstacleList: #every warningObstacle moves
                if obstacle.y < screenHeight:
                    obstacle.move()
                    if player:
                        if player1.line == obstacle.line and player1.height+player1.y >= obstacle.y+obstacle.height >= player1.y:
                            gameOver()
                else: #delete all obstacles under the screen
                    del warningObstacleList[warningObstacleList.index(obstacle)]


            nopi = random.randrange(1000) #new-obstacle-probability-int
            if nopi > obstacleProbabilitylst[0] and obstacleProtection > obstacleDencity: #new obstacle-generation
                olst = [] #obstaclelist to add warningObstacleList

                for prob in obstacleProbabilitylst:
                    if nopi > prob:
                        line = random.randrange(1,streetLineQuantity+1) #line-position information
                        for x in olst:
                            while line == x:
                                line = random.randrange(1,streetLineQuantity+1) #line-position information
                        olst.append(line)
                        warningObstacleList.append(Warningobstacle(line,speed,obstacleSize))
                    else:
                        if coins:
                            for x in range(streetLineQuantity-len(olst)):
                                cn = random.randrange(0,1000)
                                if coin20Probability > cn:
                                    line = random.randrange(1,streetLineQuantity+1) #line-position information
                                    for x in olst:
                                        while line == x:
                                            line = random.randrange(1,streetLineQuantity+1) #line-position information
                                    olst.append(line)
                                    coinlst.append(Coin(line,speed,coinSize,20)) #last attribut: the amount of the money
                                elif coin5Probability > cn:
                                    line = random.randrange(1,streetLineQuantity+1) #line-position information
                                    for x in olst:
                                        while line == x:
                                            line = random.randrange(1,streetLineQuantity+1) #line-position information
                                    olst.append(line)
                                    coinlst.append(Coin(line,speed,coinSize,5)) #last attribut: the amount of the money
                                elif coin1Probability > cn:
                                    line = random.randrange(1,streetLineQuantity+1) #line-position information
                                    for x in olst:
                                        while line == x:
                                            line = random.randrange(1,streetLineQuantity+1) #line-position information
                                    olst.append(line)
                                    coinlst.append(Coin(line,speed,coinSize,1)) #last attribut: the amount of the money
                obstacleProtection = 0
            obstacleProtection += speed #give the player1 a chance to survive - every obstacle has to have a distance to the other

        if coins:
            for coin in coinlst:
                if coin.y < screenHeight:
                    coin.move()
                    if player:
                        if player1.line == coin.line and player1.y+player1.height >= coin.y+coin.height >= player1.y+player1.width*0.6:
                            money.amount += coin.amount
                            del coinlst[coinlst.index(coin)]
                else: #delete all obstacles under the screen
                    del coinlst[coinlst.index(coin)]

        if stripes:
            if stripePosition >= stripeHeight:  #"generate" new stripe on the road
                stripePosition = -stripeHeight
            stripePosition += speed #move the road

        if flowers:
            for flower in flowerlst: #move every flower
                if flower.y < screenHeight:
                    flower.y += flower.speed #move down
                else: #delete all obstacles under the screen
                    del flowerlst[flowerlst.index(flower)]

            nf = random.randrange(1000) #new-flower on the left side?
            if nf > flowerProbability and leftProtection > flowerDencity:
                picNumber = random.randrange(len(flowerPicNamelst))
                FlowerSelection = flowerPicNamelst[picNumber]
                xPos = random.randrange(int(roadBorder-roadLineWidth * flowerSize)) #line-position information
                flowerlst.append(Flower(speed,FlowerSelection,flowerSize,xPos))
                leftProtection = 0
            nf = random.randrange(1000) #new-flower on the right side?
            if nf > flowerProbability and rightProtection > flowerDencity:
                picNumber = random.randrange(len(flowerPicNamelst))
                FlowerSelection = flowerPicNamelst[picNumber]
                xPos = random.randrange(int(screenWidth-roadBorder),int(screenWidth-roadLineWidth * flowerSize)) #line-position information
                flowerlst.append(Flower(speed,FlowerSelection,flowerSize,xPos))
                rightProtection = 0
            leftProtection += 1
            rightProtection += 1

        if graspixels:
            for pixel in graspixellst: #every pixel moves
                if pixel.y < screenHeight:
                    pixel.move()
                else: #delete all pixels under the screen
                    del graspixellst[graspixellst.index(pixel)]
            if 20 > score.amount > 10:
                color = (random.randrange(0,10),random.randrange(150,180),random.randrange(20,30))
                graspixellst.append(GrasPixel(-10,-graspixelHeight-1,color))
            if pixelProtection>=graspixelHeight:
                for x in range(0,roadBorder-roadOverstand,graspixelWidth): #left
                    color = (random.randrange(0,10),random.randrange(150,180),random.randrange(20,30))
                    graspixellst.append(GrasPixel(x,-graspixelHeight-1,color))
                for x in range(screenWidth-roadBorder+roadOverstand,screenWidth,graspixelWidth): #right
                    color = (random.randrange(0,10),random.randrange(150,180),random.randrange(20,30))
                    graspixellst.append(GrasPixel(x,-graspixelHeight-1,color))
                pixelProtection = 0
            pixelProtection+=speed
        show()
        fpsLabel.clock.tick(FPS)

        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
            escapeMenu()

pg.quit()
print("Program ended without fails.")
