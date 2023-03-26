#This is the config of the program "CrashyCar"
#please use no " to mark strings.
#please use "-" in Strings instead of " "

#general settings (1 = True, 0 = False)
player = True  #(1 = True, 0 = False)
flowers = True
stripes = True
graspixels = True
obstacles = True
scoreVisible = True
coins = True
fasterandfaster = False

#must be between 3 and 80
streetLineQuantity = 5
fullScreen = 0
mousevisibility = False
FPS = 60

screenCaption = "CrashyCar"

path = "./Resource/"
info = "Made by Carl R. Becker 2019"

roadOverstand = 16

borderColor = (5,200,5)
#borderColor = (5,190,40) #120
roadColor = (50,50,50)
yellowStripeColor = (255,190,47)
whiteStripeColor = (210,210,210)
Fontcolor = (255,255,255)
BackFontcolor = (0,0,100)
FontColor3 = (0,50,0)
LabelBackgroundColor = (150,150,150)


#Carsettings / player1settings
carPicName = "Car.png"
player1Size = 0.4 #(width) proportion of the roadLine-width
player1Height = 1.5 #(height) proportion to the width


#Warningsettings
warningPicName = "Warning.png"
obstacleDencity = 300 #the size of the space between every obstacle
obstacleSize = 0.6 #(width) proportion of road-line
obstacleHeight = 0.666 #(height) proportion to the width


#Flowers
flowerProbability = 980 #probability to spawn a flower
flowerSize = 0.4 #(width) proportion of road-line
flowerHeight = 1.5 #(height) proportion to the width
flowerDencity = 20 #the size of the space between every obstacle

flowerPicNamelst = ["Flower2.png","Flower3.png","Flower4.png","Flower5.png","Flower6.png"]#Flower1 not included
flower1PicName = "Flower1.png"

startScore = 0
scoreAddition = 1
scorespeed = 1200
scoreLabelx = 20
scoreLabely = 20
scoreLabelHeight = 30

startMoney = 0
moneyLabely = 20
moneyLabelHeight = 30

fpsLabelOn = True
fpsx = 10
fpsy = 80

buttonGap = 20 #gap between every button of the startScreen


#coins
coinSize = 0.25 #proportion of road-line
coin1Probability = 500 #/1000
coin5Probability = 60 #/1000
coin20Probability = 8 #/1000
coin1PicName = "Coin1.png"
coin5PicName = "Coin5.png"
coin20PicName = "Coin20.png"

signPicName = "Sign.png"

headerPicName = "Header.png"
