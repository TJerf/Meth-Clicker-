<<<<<<< HEAD
import pygame,random
pygame.init()
screenX = 800
screenY = 600 
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption('Meth Clicker')
upgradeBoxSize = 50

#font
fontBig = pygame.font.Font('freesansbold.ttf', 36)
fontMedium = pygame.font.Font('freesansbold.ttf', 24)
fontSmall = pygame.font.Font('freesansbold.ttf', 16)
fontVerySmall = pygame.font.Font('freesansbold.ttf', 12)
fontTiny = pygame.font.Font('freesansbold.ttf', 9)


methWidth = screenY // 3
methWidthTemp = methWidth
methHeight = screenY // 3
methHeightTemp = methHeight
methDisplayY = screenY//3
methDisplayX = screenX//8



mousePos = (0,0)
methPerSecound = 0
methPerSecoundString = "  Meth Per Secound " + str(methPerSecound)+"  "
methCooked = 0
methCookedString = "  Meth Cooked" + str(methCooked) + "  "
methPerClick = 5
methCookedAllTime = 0
selfImprovementCondition = False



walterBlackPrice = 500
walterBlackPriceString = "walterBlackPrice" + str(walterBlackPrice)
basewalterBlackMethPerSecound = 30#temp
walterBlackOwned = 0
walterBlackOwnedString = "walterBlack owned " + str(walterBlackOwned)
walterBlackWidth = 20
walterBlackHeight = 20


jessePrice = 50
jessePriceString = "jessePrice" + str(jessePrice)
baseJesseMethPerSecound = -64
jesseMPS = 0
jesseOwned = 0
jesseOwnedString = "jesse owned " + str(jesseOwned)
jesseWidth = 20
jesseHeight = 20
jesseUpgradesCondition1 = False
jesseUpgradesCost1 = 100000
jesseUpgradesCondition2=False
jesseUpgradesCost1 = 2500000


walterWhitePrice = 5000
walterWhitePriceString = "WalterWhitePrice" + str(walterWhitePrice)
basewalterWhiteMethPerSecound = 200
walterWhiteOwned = 0
walterWhiteOwnedString = "WalterWhite owned " + str(walterWhiteOwned)
walterWhiteWidth = 20
walterWhiteHeight = 20


#gus buffs and gus itself(soon)
GusSize = random.randint(30,50)
GusX = random.randint(200,600)
GusY = random.randint(100,500)
gusLifeSpan = random.randint(30,50)
gusIsAlive = False
gusLifeSpan = 0
gusSpawnCoolDown = 5#random.randint(150,200)
gusMultiplier = [3,7,10,-10]
gusMultiplierRandom = 0
gusMultiplierLifeSpan = 0
gusMultiplierIsActive = False



#gus text
gusFrenzyString = "Happy Gus"
gusFrenzyText = fontMedium.render(gusFrenzyString, True, (255,255,255), (0,0,0))
gusFrenzyRect = (0,0,0,0)
gusFrenzyMultiplierString = "Meth Multiplier " 
gusFrenzyMultiplierText  = fontSmall.render(gusFrenzyMultiplierString, True, (255,255,255), (0,0,0))
gusFrenzyMultiplierRect = (0,0,0,0)
gusStringLifeSpan = 0


#img loading part
backGround = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\\huyandere-Anime-фэндомы-crossover-7614771.jpeg")
meth = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\\meth.jpg")
meth = pygame.transform.scale(meth,(methWidth,methHeight))
jesseAddict = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\\jesse_addicted.jpg")
jesseAddict = pygame.transform.scale(jesseAddict,(jesseWidth*3,jesseHeight*3))
jesseClean = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\\jesse_clean.jpg")
jesseClean = pygame.transform.scale(jesseClean,(jesseWidth*3,jesseHeight*3))
walterBlack = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\\walter_black.jpg")
walterBlack = pygame.transform.scale(walterBlack,(walterBlackWidth*3,walterBlackHeight*3))
redWalter = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\\red_walter.jpg")
redWalter = pygame.transform.scale(redWalter,(walterWhiteWidth*3,walterWhiteHeight*3))
walterWhite = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\\walter_white.png")
walterWhite = pygame.transform.scale(walterWhite,(walterWhiteWidth*3,walterWhiteHeight*3))
gus = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\\gus.jpg")
gameOver = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\\game_over.jpg")
drugAddictionCamp = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\drug_addiction_camp.jpg")
drugAddictionCamp = pygame.transform.scale(drugAddictionCamp,(upgradeBoxSize ,upgradeBoxSize ))
howToCook =  pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\how_to_cook.jpg")
howToCook = pygame.transform.scale(howToCook,(upgradeBoxSize ,upgradeBoxSize ))



#jesse info
jesseMPSString = "each jesse cook " + str(baseJesseMethPerSecound)
jesseMPSText = fontVerySmall.render(jesseMPSString, True, (0,0,0), (153,153,51))
jesseState = "Addicted"
jesseStateText = fontVerySmall.render(jesseState, True, (0,0,0), (153,153,51))
JesseFirstState = "He is not useful at all and he uses"
JesseFirstStateText = fontVerySmall.render(JesseFirstState, True, (0,0,0), (153,153,51))
JesseFirstStatePartTwo = "your meth but he might get better"
JesseFirstStateTextPartTwo = fontVerySmall.render(JesseFirstStatePartTwo, True, (0,0,0), (153,153,51))
jesseDispription = "Jesse current state is :" + jesseState 
jesseDispriptionText = fontVerySmall.render(jesseDispription, True, (0,0,0), (153,153,51))
jesseUpgradeLevetCosts = [50000,100000,200000,500000,1000000,0]
jesseUpgradesCondition1Max = False
jesseUpgradeLevetCounter = 0
toggleIsActivated = False






#selfimprovment
selfImprovmentPrice=[100000,150000,250000,1000000,2000000]



characterUpgrade = [50,50]
upgradeBox = (220,60,10)
clock = pygame.time.Clock()
timer = 30
timerReset = 0
hoverCheck = False
hoverPos = (0,0)
gameRun = True
gameTimer = 0
while gameRun:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRun = False
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
        hoverPos = pygame.mouse.get_pos()
    #screen.blit(backGround,(0,0))
    #MPS part
    screen.blit(meth, (methDisplayX, methDisplayY))
    jesseMPS = baseJesseMethPerSecound*jesseOwned
    methCookedString = "  Meth Cooked" + str(methCooked) + "  "
    if gusMultiplierIsActive :
        methPerSecoundString = "  Meth Per Secound " + str((methPerSecound+jesseMPS)*gusMultiplier[gusMultiplierRandom])+"  "
    else :
        methPerSecoundString = "  Meth Per Secound " + str(methPerSecound+jesseMPS)+"  "
    methCookedText = fontBig.render(methCookedString , True, (255,255,255), (0,0,0))
    methPerSecoundText = fontSmall.render(methPerSecoundString, True, (255,255,255), (0,0,0))
    methPerSecoundRect = methPerSecoundText.get_rect()
    methPerSecoundRect.center = (screenX//4 , screenY//8+50)
    methCookedRect = methCookedText.get_rect()
    methCookedRect.center = (screenX//4 , screenY//8)
    screen.blit(methCookedText, methCookedRect)
    screen.blit(methPerSecoundText, methPerSecoundRect)
    if mousePos[1] in range (methDisplayY,methDisplayY+methHeight) and mousePos[0] in range (methDisplayX , methDisplayX + methWidth) :
        if gusMultiplierIsActive :
            methCooked+=methPerClick*gusMultiplier[gusMultiplierRandom]
            methCookedAllTime+=methPerClick*gusMultiplier[gusMultiplierRandom]
        else :
            methCooked+=methPerClick
            methCookedAllTime+=methPerClick
        mousePos = (0,0)



    #Jesse part
    
    pygame.draw.rect(screen,(255,255,0),(screenX-upgradeBox[0],screenY//3,upgradeBox[0],upgradeBox[1]))
    jessePriceText = fontVerySmall.render(jessePriceString, True, (0,0,0), (255,255,0))
    jessePriceRect = jessePriceText.get_rect()
    jessePriceRect.center = (screenX-screenX//6,screenY//3+10)
    jesseOwnedText = fontVerySmall.render(jesseOwnedString, True, (0,0,0), (255,255,0))
    jesseOwnedRect = jesseOwnedText.get_rect()
    jesseOwnedRect.center = (screenX-screenX//6,screenY//3+30)
    jesseOwnedString = "Jesse owned " + str(jesseOwned)
    jesseOwnedString = "Jesse owned " + str(jesseOwned)
    jessePriceString = "JessePrice" + str(jessePrice)
    screen.blit (jessePriceText,jessePriceRect)
    screen.blit(jesseOwnedText,jesseOwnedRect)
    #screen.blit(jesseAddict,(screenX-60,screenY//3))
    if mousePos [0] in range (screenX-upgradeBox[0],screenX) and mousePos [1] in range (screenY//3,screenY//3+upgradeBox[1])  :
        if methCooked >= jessePrice :
            if jesseOwned>=24:
                jesseUpgradesCondition1 = True
            if jesseOwned>=99 :
                jesseUpgradesCondition2 = True
            
            jesseOwned+=1
            methCooked-=jessePrice
            jessePrice+=round(jessePrice/15)
        mousePos = (0,0)

    #Jesse hovering part

        
    if hoverPos [0] in range (screenX-upgradeBox[0],screenX) and hoverPos [1] in range (screenY//3,screenY//3+upgradeBox[1]) :
        pygame.draw.rect(screen,(153,153,51),(screenX-upgradeBox[0]*2,screenY//3,upgradeBox[0],upgradeBox[1]))
        if jesseState == "Addicted":
            jesseMPSString = "each jesse cook " + str(baseJesseMethPerSecound)
            jesseMPSText = fontVerySmall.render(jesseMPSString, True, (0,0,0), (153,153,51))
            jesseMPSRect = jesseMPSText.get_rect()
            jesseMPSRect.center = (screenX-upgradeBox[0]*2+60,screenY//3+7) 
            jesseDispription = "Jesse current state is :" + jesseState
            jesseMPSText = fontVerySmall.render(jesseMPSString, True, (0,0,0), (153,153,51))
            jesseDispriptionText = fontVerySmall.render(jesseDispription, True, (0,0,0), (153,153,51))
            jesseDispriptionRect = jesseDispriptionText.get_rect()
            jesseDispriptionRect.center = (screenX-upgradeBox[0]*2+95,screenY//3+20)
            JesseFirstStateRect = JesseFirstStateText.get_rect()
            JesseFirstStateRect.center = (screenX-upgradeBox[0]*2+100,screenY//3+35)
            JesseFirstStateRectPartTwo = JesseFirstStateTextPartTwo.get_rect()
            JesseFirstStateRectPartTwo.center = (screenX-upgradeBox[0]*2+98,screenY//3+50)
            screen.blit(JesseFirstStateTextPartTwo,JesseFirstStateRectPartTwo)
            screen.blit(jesseMPSText,jesseMPSRect)
            screen.blit(JesseFirstStateText,JesseFirstStateRect)
            screen.blit(jesseDispriptionText,jesseDispriptionRect)
        elif jesseState == "Improving" :
            jesseMPSString = "each jesse cook " + str(baseJesseMethPerSecound)
            jesseMPSText = fontVerySmall.render(jesseMPSString, True, (0,0,0), (153,153,51))
            jesseMPSRect = jesseMPSText.get_rect()
            jesseMPSRect.center = (screenX-upgradeBox[0]*2+60,screenY//3+7) 
            jesseDispription = "Jesse current state is :" + jesseState 
            jesseDispriptionText = fontVerySmall.render(jesseDispription, True, (0,0,0), (153,153,51))
            JesseSecondStateState = "He is getting better and not"
            JesseSecondStateStatePartTwo = "doing drugs as much keep pushing"
            JesseSecondStateText = fontVerySmall.render(JesseSecondStateState, True, (0,0,0), (153,153,51))
            JesseSecondStateTextPartTwo = fontVerySmall.render(JesseSecondStateStatePartTwo, True, (0,0,0), (153,153,51))
            jesseMPSRect = jesseMPSText.get_rect()
            jesseMPSRect.center = (screenX-upgradeBox[0]*2+60,screenY//3+7)
            jesseDispriptionRect = jesseDispriptionText.get_rect()
            jesseDispriptionRect.center = (screenX-upgradeBox[0]*2+100,screenY//3+20)
            JesseSecondStateRect = JesseSecondStateText.get_rect()
            JesseSecondStateRect.center = (screenX-upgradeBox[0]*2+85,screenY//3+35)
            JesseSecondStateRectPartTwo = JesseSecondStateTextPartTwo.get_rect()
            JesseSecondStateRectPartTwo.center = (screenX-upgradeBox[0]*2+105,screenY//3+50)
            screen.blit(JesseSecondStateTextPartTwo,JesseSecondStateRectPartTwo)
            screen.blit(jesseMPSText,jesseMPSRect)
            screen.blit(JesseSecondStateText,JesseSecondStateRect)
            screen.blit(jesseDispriptionText,jesseDispriptionRect)
        elif jesseState == "Improved" :
            jesseMPSString = "each jesse cook " + str(baseJesseMethPerSecound)
            jesseMPSText = fontVerySmall.render(jesseMPSString, True, (0,0,0), (153,153,51))
            jesseMPSRect = jesseMPSText.get_rect()
            jesseMPSRect.center = (screenX-upgradeBox[0]*2+60,screenY//3+7) 
            jesseDispription = "Jesse current state is :" + jesseState 
            jesseDispriptionText = fontVerySmall.render(jesseDispription, True, (0,0,0), (153,153,51))
            JesseThirdStateState = "He is not doing drugs anymore"
            JesseThirdStateStatePartTwo = "But he do noy know how to cook"
            JesseThirdStateText = fontVerySmall.render(JesseThirdStateState, True, (0,0,0), (153,153,51))
            JesseThirdStateTextPartTwo = fontVerySmall.render(JesseThirdStateStatePartTwo, True, (0,0,0), (153,153,51))
            jesseMPSRect = jesseMPSText.get_rect()
            jesseMPSRect.center = (screenX-upgradeBox[0]*2+60,screenY//3+7)
            jesseDispriptionRect = jesseDispriptionText.get_rect()
            jesseDispriptionRect.center = (screenX-upgradeBox[0]*2+100,screenY//3+20)
            JesseThirdStateRect = JesseThirdStateText.get_rect()
            JesseThirdStateRect.center = (screenX-upgradeBox[0]*2+95,screenY//3+35)
            JesseThirdStateRectPartTwo = JesseThirdStateTextPartTwo.get_rect()
            JesseThirdStateRectPartTwo.center = (screenX-upgradeBox[0]*2+95,screenY//3+50)
            screen.blit(JesseThirdStateTextPartTwo,JesseThirdStateRectPartTwo)
            screen.blit(jesseMPSText,jesseMPSRect)
            screen.blit(JesseThirdStateText,JesseThirdStateRect)
            screen.blit(jesseDispriptionText,jesseDispriptionRect)
            screen.blit(jesseClean,(screenX-60,screenY//3))
        
        

    if methCookedAllTime >= 50000 :
        selfImprovementCondition = True
    

    
    

    #WalterBlack part    
    pygame.draw.rect(screen,(255,255,0),(screenX-upgradeBox[0],screenY//3+upgradeBox[1]+upgradeBox[2],upgradeBox[0],upgradeBox[1]))
    walterBlackPriceText = fontVerySmall.render(walterBlackPriceString, True, (0,0,0), (255,255,0))
    walterBlackPriceRect = walterBlackPriceText.get_rect()
    walterBlackPriceRect.center = (screenX-screenX//6,screenY//3+10+upgradeBox[1]+upgradeBox[2])
    walterBlackOwnedText = fontVerySmall.render(walterBlackOwnedString, True, (0,0,0), (255,255,0))
    walterBlackOwnedRect = walterBlackOwnedText.get_rect()
    walterBlackOwnedRect.center = (screenX-screenX//6,screenY//3+30+upgradeBox[1]+upgradeBox[2])
    walterBlackOwnedString = "WalterBlack owned " + str(walterBlackOwned)
    walterBlackOwnedString = "WalterBlack owned " + str(walterBlackOwned)
    walterBlackPriceString = "WalterBlackPrice" + str(walterBlackPrice)
    screen.blit (walterBlackPriceText,walterBlackPriceRect)
    screen.blit(walterBlackOwnedText,walterBlackOwnedRect)
    screen.blit(walterBlack,(screenX-60,screenY//3+upgradeBox[1]+upgradeBox[2]))
    if mousePos [0] in range (screenX-upgradeBox[0],screenX) and mousePos [1] in range ((screenY//3)+(upgradeBox[1])+(upgradeBox[2]),screenY//3+(upgradeBox[1]*2)+upgradeBox[2]):
        if methCooked >= walterBlackPrice :
            walterBlackOwned+=1
            methCooked-=walterBlackPrice
            methPerSecound += basewalterBlackMethPerSecound
            walterBlackPrice+=walterBlackPrice//15
        mousePos = (0,0)
        
        
    #WalterWhite part
    pygame.draw.rect(screen,(255,255,0),(screenX-upgradeBox[0],screenY//3+((upgradeBox[1]+upgradeBox[2])*2),upgradeBox[0],upgradeBox[1]))
    walterWhitePriceText = fontVerySmall.render(walterWhitePriceString, True, (0,0,0), (255,255,0))
    walterWhitePriceRect = walterWhitePriceText.get_rect()
    walterWhitePriceRect.center = (screenX-screenX//6,screenY//3+10+((upgradeBox[1]+upgradeBox[2])*2))
    walterWhiteOwnedText = fontVerySmall.render(walterWhiteOwnedString, True, (0,0,0), (255,255,0))
    walterWhiteOwnedRect = walterWhiteOwnedText.get_rect()
    walterWhiteOwnedRect.center = (screenX-screenX//6,screenY//3+30+((upgradeBox[1]+upgradeBox[2])*2))
    walterWhiteOwnedString = "WalterWhite owned " + str(walterWhiteOwned)
    walterWhiteOwnedString = "WalterWhite owned " + str(walterWhiteOwned)
    walterWhitePriceString = "WalterWhite Price" + str(walterWhitePrice)
    screen.blit (walterWhitePriceText,walterWhitePriceRect)
    screen.blit (walterWhiteOwnedText,walterWhiteOwnedRect)
    if walterWhiteOwned >100 :
        screen.blit(redWalter,(screenX-60,screenY//3+((upgradeBox[1]+upgradeBox[2])*2)))
    else :
        screen.blit(walterWhite,(screenX-60,screenY//3+((upgradeBox[1]+upgradeBox[2])*2)))
    if mousePos [0] in range (screenX-upgradeBox[0],screenX) and mousePos [1] in range ((screenY//3)+(upgradeBox[1]*2)+(upgradeBox[2]*2),screenY//3+(upgradeBox[1]*3)+(upgradeBox[2])*2):
        if methCooked >= walterWhitePrice :
            walterWhiteOwned+=1
            methCooked-=walterWhitePrice
            methPerSecound += basewalterWhiteMethPerSecound
            walterWhitePrice+=walterWhitePrice//15
        mousePos = (0,0)
        
    #Gus buff
    if gusSpawnCoolDown <= 0 :
        gusIsAlive = True
        gusMultiplierRandom = random.randint(0,3)
        gusSize = random.randint(30,50)
        gusX = random.randint(200,600)
        gusY = random.randint(100,500)
        gusSpawnCoolDown = random.randint(150,200)
        gusLifeSpan = random.randint(10,20)
        gusMultiplierRandom = random.randint(0,3)
        gusFrenzyMultiplierString = "Meth Multiplier " + str(gusMultiplier[gusMultiplierRandom]) + "  "
        gusFrenzyMultiplierText  = fontSmall.render(gusFrenzyMultiplierString, True, (255,255,255), (0,0,0))
        gusFrenzyRect = gusFrenzyText.get_rect()
        gusFrenzyRect.center = (gusX,gusY-30)
        gusFrenzyMultiplierRect = gusFrenzyMultiplierText.get_rect()
        gusFrenzyMultiplierRect.center = (gusX,gusY-10)
        
    if gusIsAlive  :
        gus = pygame.transform.scale(gus,(gusSize,gusSize))
        screen.blit(gus,(gusX,gusY))
        if mousePos [0] in range (gusX,gusX+gusSize) and mousePos [1] in range (gusY,gusY+(gusSize)):
            gusIsAlive = False
            gusMultiplierLifeSpan = random.randint(60,120)
            gusMultiplierIsActive = True
            gusStringLifeSpan = 3
            print(gusMultiplier[gusMultiplierRandom],gusMultiplierLifeSpan)
    if gusMultiplierIsActive :
        methCooked += ((methPerSecound+jesseMPS)*gusMultiplier[gusMultiplierRandom])//timer
        methCooked += (methPerClick*gusMultiplier[gusMultiplierRandom])//timer
        methCookedAllTime += ((methPerSecound+jesseMPS)*gusMultiplier[gusMultiplierRandom])//timer
    else:
        methCooked += (methPerSecound+ jesseMPS)//timer
        methCookedAllTime += methPerSecound//timer

    
    #upgrades
    if selfImprovementCondition :
        screen.blit(howToCook,(screenX-upgradeBox[0],0))
        if hoverPos[0]in range(screenX-upgradeBox[0],screenX-upgradeBox[0]+upgradeBoxSize) and hoverPos[1] in range (0,0+upgradeBoxSize):
            pygame.draw.rect(screen,(153,153,51),(screenX-upgradeBox[0]*2 , 0 ,upgradeBox[0],upgradeBoxSize))
            if not jesseUpgradesCondition1Max and not jesseUpgradeLevetCounter>=5:
                #text
                jesseLevelText = fontVerySmall.render("Jesse De-addiction level is " +str(jesseUpgradeLevetCounter)+" out of "+str(len(jesseUpgradeLevetCosts)-2), True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-113,6)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("Next Upgrade Price Would be "+str(jesseUpgradeLevetCosts[jesseUpgradeLevetCounter]), True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-110,25)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontTiny.render("Jesse's are 2 time's cheaper steal twice less ", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-110,40)
                screen.blit(jesseLevelText,jesseLevelRect) 
                #end text
            if jesseUpgradesCondition1Max and toggleIsActivated:
                #text
                jesseLevelText = fontVerySmall.render("jesse would be addicted again ", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-130,10)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("and steal your meth |click to toggle", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-115,25)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("price is : "+ str(methCooked//10), True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-110,40)
                screen.blit(jesseLevelText,jesseLevelRect) 
                #end text
            elif not toggleIsActivated and jesseUpgradesCondition1Max :
                #text
                jesseLevelText = fontVerySmall.render("Jesse will no longer will be a addict", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-115,10)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("and will continue to cook |click to toggle", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-115,25)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("price is : "+ str(methCooked//10), True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-110,40)
                screen.blit(jesseLevelText,jesseLevelRect) 
                #end text


        #if mousePos[0]in range(screenX-upgradeBox[0],screenX-upgradeBox[0]+upgradeBoxSize) and mousePos[1] in range (0,0+upgradeBoxSize)  :
    if jesseUpgradesCondition1 :
        screen.blit(drugAddictionCamp,(screenX-upgradeBox[0]+upgradeBoxSize+10,0))
        if mousePos[0]in range((screenX-upgradeBox[0])+10+upgradeBoxSize,screenX-upgradeBox[0]+upgradeBoxSize*2+10) and mousePos[1] in range (0,0+upgradeBoxSize)  :
            if jesseUpgradesCondition1Max and toggleIsActivated :
                methCooked-=(methCooked//10)
                baseJesseMethPerSecound = -64
                jesseState = "Addicted"
                toggleIsActivated = False
            elif not toggleIsActivated and jesseUpgradesCondition1Max:
                methCooked-=(methCooked//10)
                baseJesseMethPerSecound = 1
                jesseState = "Improved"
                toggleIsActivated = True
            if not jesseUpgradesCondition1Max and not jesseUpgradeLevetCounter>5 and methCooked >= jesseUpgradeLevetCosts[jesseUpgradeLevetCounter]:
                methCooked -=jesseUpgradeLevetCosts[jesseUpgradeLevetCounter]
                jesseUpgradeLevetCounter+=1
                baseJesseMethPerSecound=baseJesseMethPerSecound//2
                jessePrice=jessePrice//2
                jesseState = "Improving"
                print(jessePrice,baseJesseMethPerSecound)
                print(jesseUpgradesCondition1Max,jesseState)
                if jesseUpgradeLevetCounter>=5:
                    jesseUpgradesCondition1Max = True
                    toggleIsActivated = True
            mousePos=(0,0)
        if hoverPos[0]in range((screenX-upgradeBox[0])+10+upgradeBoxSize,screenX-upgradeBox[0]+upgradeBoxSize*2+10) and hoverPos[1] in range (0,0+upgradeBoxSize):
            pygame.draw.rect(screen,(153,153,51),(screenX-upgradeBox[0]*2 , 0 ,upgradeBox[0],upgradeBoxSize))
            if not jesseUpgradesCondition1Max and not jesseUpgradeLevetCounter>=5:
                #text
                jesseLevelText = fontVerySmall.render("Jesse De-addiction level is " +str(jesseUpgradeLevetCounter+1)+" out of "+str(len(jesseUpgradeLevetCosts)-1), True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-113,6)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("Next Upgrade Price Would be "+str(jesseUpgradeLevetCosts[jesseUpgradeLevetCounter]), True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-110,25)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontTiny.render("Jesse's are 2 time's cheaper steal twice less ", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-110,40)
                screen.blit(jesseLevelText,jesseLevelRect) 
                #end text
            if jesseUpgradesCondition1Max and toggleIsActivated:
                #text
                jesseLevelText = fontVerySmall.render("jesse would be addicted again ", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-130,10)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("and steal your meth |click to toggle", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-115,25)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("price is : "+ str(methCooked//10), True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-110,40)
                screen.blit(jesseLevelText,jesseLevelRect) 
                #end text
            elif not toggleIsActivated and jesseUpgradesCondition1Max :
                #text
                jesseLevelText = fontVerySmall.render("Jesse will no longer will be a addict", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-115,10)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("and will continue to cook |click to toggle", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-115,25)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("price is : "+ str(methCooked//10), True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-110,40)
                screen.blit(jesseLevelText,jesseLevelRect) 
                #end text



    if toggleIsActivated:
        jesseState = "Improved"
    elif not toggleIsActivated and jesseUpgradesCondition1Max:
        jesseState = "Addicted"
    if jesseState == "Addicted" or jesseState == "Improving":
        screen.blit(jesseAddict,(screenX-60,screenY//3))
    elif jesseState == "Improved" :
        screen.blit(jesseClean,(screenX-60,screenY//3))
    if gusStringLifeSpan >0 :
        screen.blit(gusFrenzyMultiplierText,gusFrenzyMultiplierRect)
        screen.blit(gusFrenzyText,gusFrenzyRect)  
    timerReset+=1
    if methCooked >= 1000000000000 :
        screen.blit(gameOver,(0,0))
        gameRun = False
    if timerReset >= timer :
        timerReset = 0
        gameTimer +=1
        gusSpawnCoolDown-=1
        gusLifeSpan-=1
        gusMultiplierLifeSpan-=1
        gusStringLifeSpan-=1
        if gusMultiplierLifeSpan <0:
            gusMultiplierIsActive = False
        if gusLifeSpan <= 0 :
            gusIsAlive = False
    clock.tick(timer)
    pygame.display.flip()
pygame.quit()
 



=======
import pygame,random
pygame.init()
screenX = 800
screenY = 600 
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption('Meth Clicker')
upgradeBoxSize = 50

#font
fontBig = pygame.font.Font('freesansbold.ttf', 36)
fontMedium = pygame.font.Font('freesansbold.ttf', 24)
fontSmall = pygame.font.Font('freesansbold.ttf', 16)
fontVerySmall = pygame.font.Font('freesansbold.ttf', 12)
fontTiny = pygame.font.Font('freesansbold.ttf', 9)


methWidth = screenY // 3
methWidthTemp = methWidth
methHeight = screenY // 3
methHeightTemp = methHeight
methDisplayY = screenY//3
methDisplayX = screenX//8



mousePos = (0,0)
methPerSecound = 0
methPerSecoundString = "  Meth Per Secound " + str(methPerSecound)+"  "
methCooked = 0
methCookedString = "  Meth Cooked" + str(methCooked) + "  "
methPerClick = 5
methCookedAllTime = 0
selfImprovementCondition = False



walterBlackPrice = 500
walterBlackPriceString = "walterBlackPrice" + str(walterBlackPrice)
basewalterBlackMethPerSecound = 30#temp
walterBlackOwned = 0
walterBlackOwnedString = "walterBlack owned " + str(walterBlackOwned)
walterBlackWidth = 20
walterBlackHeight = 20


jessePrice = 50
jessePriceString = "jessePrice" + str(jessePrice)
baseJesseMethPerSecound = -64
jesseMPS = 0
jesseOwned = 0
jesseOwnedString = "jesse owned " + str(jesseOwned)
jesseWidth = 20
jesseHeight = 20
jesseUpgradesCondition1 = False
jesseUpgradesCost1 = 100000
jesseUpgradesCondition2=False
jesseUpgradesCost1 = 2500000


walterWhitePrice = 5000
walterWhitePriceString = "WalterWhitePrice" + str(walterWhitePrice)
basewalterWhiteMethPerSecound = 200
walterWhiteOwned = 0
walterWhiteOwnedString = "WalterWhite owned " + str(walterWhiteOwned)
walterWhiteWidth = 20
walterWhiteHeight = 20


#gus buffs and gus itself(soon)
GusSize = random.randint(30,50)
GusX = random.randint(200,600)
GusY = random.randint(100,500)
gusLifeSpan = random.randint(30,50)
gusIsAlive = False
gusLifeSpan = 0
gusSpawnCoolDown = 5#random.randint(150,200)
gusMultiplier = [3,7,10,-10]
gusMultiplierRandom = 0
gusMultiplierLifeSpan = 0
gusMultiplierIsActive = False



#gus text
gusFrenzyString = "Happy Gus"
gusFrenzyText = fontMedium.render(gusFrenzyString, True, (255,255,255), (0,0,0))
gusFrenzyRect = (0,0,0,0)
gusFrenzyMultiplierString = "Meth Multiplier " 
gusFrenzyMultiplierText  = fontSmall.render(gusFrenzyMultiplierString, True, (255,255,255), (0,0,0))
gusFrenzyMultiplierRect = (0,0,0,0)
gusStringLifeSpan = 0


#img loading part
backGround = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\\huyandere-Anime-фэндомы-crossover-7614771.jpeg")
meth = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\\meth.jpg")
meth = pygame.transform.scale(meth,(methWidth,methHeight))
jesseAddict = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\\jesse_addicted.jpg")
jesseAddict = pygame.transform.scale(jesseAddict,(jesseWidth*3,jesseHeight*3))
jesseClean = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\\jesse_clean.jpg")
jesseClean = pygame.transform.scale(jesseClean,(jesseWidth*3,jesseHeight*3))
walterBlack = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\\walter_black.jpg")
walterBlack = pygame.transform.scale(walterBlack,(walterBlackWidth*3,walterBlackHeight*3))
redWalter = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\\red_walter.jpg")
redWalter = pygame.transform.scale(redWalter,(walterWhiteWidth*3,walterWhiteHeight*3))
walterWhite = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\\walter_white.png")
walterWhite = pygame.transform.scale(walterWhite,(walterWhiteWidth*3,walterWhiteHeight*3))
gus = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\\gus.jpg")
gameOver = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\\game_over.jpg")
drugAddictionCamp = pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\drug_addiction_camp.jpg")
drugAddictionCamp = pygame.transform.scale(drugAddictionCamp,(upgradeBoxSize ,upgradeBoxSize ))
howToCook =  pygame.image.load("C:\\Users\\pc\\Desktop\\Meth src\how_to_cook.jpg")
howToCook = pygame.transform.scale(howToCook,(upgradeBoxSize ,upgradeBoxSize ))



#jesse info
jesseMPSString = "each jesse cook " + str(baseJesseMethPerSecound)
jesseMPSText = fontVerySmall.render(jesseMPSString, True, (0,0,0), (153,153,51))
jesseState = "Addicted"
jesseStateText = fontVerySmall.render(jesseState, True, (0,0,0), (153,153,51))
JesseFirstState = "He is not useful at all and he uses"
JesseFirstStateText = fontVerySmall.render(JesseFirstState, True, (0,0,0), (153,153,51))
JesseFirstStatePartTwo = "your meth but he might get better"
JesseFirstStateTextPartTwo = fontVerySmall.render(JesseFirstStatePartTwo, True, (0,0,0), (153,153,51))
jesseDispription = "Jesse current state is :" + jesseState 
jesseDispriptionText = fontVerySmall.render(jesseDispription, True, (0,0,0), (153,153,51))
jesseUpgradeLevetCosts = [50000,100000,200000,500000,1000000,0]
jesseUpgradesCondition1Max = False
jesseUpgradeLevetCounter = 0
toggleIsActivated = False






#selfimprovment
selfImprovmentPrice=[100000,150000,250000,1000000,2000000]



characterUpgrade = [50,50]
upgradeBox = (220,60,10)
clock = pygame.time.Clock()
timer = 30
timerReset = 0
hoverCheck = False
hoverPos = (0,0)
gameRun = True
gameTimer = 0
while gameRun:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRun = False
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
        hoverPos = pygame.mouse.get_pos()
    #screen.blit(backGround,(0,0))
    #MPS part
    screen.blit(meth, (methDisplayX, methDisplayY))
    jesseMPS = baseJesseMethPerSecound*jesseOwned
    methCookedString = "  Meth Cooked" + str(methCooked) + "  "
    if gusMultiplierIsActive :
        methPerSecoundString = "  Meth Per Secound " + str((methPerSecound+jesseMPS)*gusMultiplier[gusMultiplierRandom])+"  "
    else :
        methPerSecoundString = "  Meth Per Secound " + str(methPerSecound+jesseMPS)+"  "
    methCookedText = fontBig.render(methCookedString , True, (255,255,255), (0,0,0))
    methPerSecoundText = fontSmall.render(methPerSecoundString, True, (255,255,255), (0,0,0))
    methPerSecoundRect = methPerSecoundText.get_rect()
    methPerSecoundRect.center = (screenX//4 , screenY//8+50)
    methCookedRect = methCookedText.get_rect()
    methCookedRect.center = (screenX//4 , screenY//8)
    screen.blit(methCookedText, methCookedRect)
    screen.blit(methPerSecoundText, methPerSecoundRect)
    if mousePos[1] in range (methDisplayY,methDisplayY+methHeight) and mousePos[0] in range (methDisplayX , methDisplayX + methWidth) :
        if gusMultiplierIsActive :
            methCooked+=methPerClick*gusMultiplier[gusMultiplierRandom]
            methCookedAllTime+=methPerClick*gusMultiplier[gusMultiplierRandom]
        else :
            methCooked+=methPerClick
            methCookedAllTime+=methPerClick
        mousePos = (0,0)



    #Jesse part
    
    pygame.draw.rect(screen,(255,255,0),(screenX-upgradeBox[0],screenY//3,upgradeBox[0],upgradeBox[1]))
    jessePriceText = fontVerySmall.render(jessePriceString, True, (0,0,0), (255,255,0))
    jessePriceRect = jessePriceText.get_rect()
    jessePriceRect.center = (screenX-screenX//6,screenY//3+10)
    jesseOwnedText = fontVerySmall.render(jesseOwnedString, True, (0,0,0), (255,255,0))
    jesseOwnedRect = jesseOwnedText.get_rect()
    jesseOwnedRect.center = (screenX-screenX//6,screenY//3+30)
    jesseOwnedString = "Jesse owned " + str(jesseOwned)
    jesseOwnedString = "Jesse owned " + str(jesseOwned)
    jessePriceString = "JessePrice" + str(jessePrice)
    screen.blit (jessePriceText,jessePriceRect)
    screen.blit(jesseOwnedText,jesseOwnedRect)
    #screen.blit(jesseAddict,(screenX-60,screenY//3))
    if mousePos [0] in range (screenX-upgradeBox[0],screenX) and mousePos [1] in range (screenY//3,screenY//3+upgradeBox[1])  :
        if methCooked >= jessePrice :
            if jesseOwned>=24:
                jesseUpgradesCondition1 = True
            if jesseOwned>=99 :
                jesseUpgradesCondition2 = True
            
            jesseOwned+=1
            methCooked-=jessePrice
            jessePrice+=round(jessePrice/15)
        mousePos = (0,0)

    #Jesse hovering part

        
    if hoverPos [0] in range (screenX-upgradeBox[0],screenX) and hoverPos [1] in range (screenY//3,screenY//3+upgradeBox[1]) :
        pygame.draw.rect(screen,(153,153,51),(screenX-upgradeBox[0]*2,screenY//3,upgradeBox[0],upgradeBox[1]))
        if jesseState == "Addicted":
            jesseMPSString = "each jesse cook " + str(baseJesseMethPerSecound)
            jesseMPSText = fontVerySmall.render(jesseMPSString, True, (0,0,0), (153,153,51))
            jesseMPSRect = jesseMPSText.get_rect()
            jesseMPSRect.center = (screenX-upgradeBox[0]*2+60,screenY//3+7) 
            jesseDispription = "Jesse current state is :" + jesseState
            jesseMPSText = fontVerySmall.render(jesseMPSString, True, (0,0,0), (153,153,51))
            jesseDispriptionText = fontVerySmall.render(jesseDispription, True, (0,0,0), (153,153,51))
            jesseDispriptionRect = jesseDispriptionText.get_rect()
            jesseDispriptionRect.center = (screenX-upgradeBox[0]*2+95,screenY//3+20)
            JesseFirstStateRect = JesseFirstStateText.get_rect()
            JesseFirstStateRect.center = (screenX-upgradeBox[0]*2+100,screenY//3+35)
            JesseFirstStateRectPartTwo = JesseFirstStateTextPartTwo.get_rect()
            JesseFirstStateRectPartTwo.center = (screenX-upgradeBox[0]*2+98,screenY//3+50)
            screen.blit(JesseFirstStateTextPartTwo,JesseFirstStateRectPartTwo)
            screen.blit(jesseMPSText,jesseMPSRect)
            screen.blit(JesseFirstStateText,JesseFirstStateRect)
            screen.blit(jesseDispriptionText,jesseDispriptionRect)
        elif jesseState == "Improving" :
            jesseMPSString = "each jesse cook " + str(baseJesseMethPerSecound)
            jesseMPSText = fontVerySmall.render(jesseMPSString, True, (0,0,0), (153,153,51))
            jesseMPSRect = jesseMPSText.get_rect()
            jesseMPSRect.center = (screenX-upgradeBox[0]*2+60,screenY//3+7) 
            jesseDispription = "Jesse current state is :" + jesseState 
            jesseDispriptionText = fontVerySmall.render(jesseDispription, True, (0,0,0), (153,153,51))
            JesseSecondStateState = "He is getting better and not"
            JesseSecondStateStatePartTwo = "doing drugs as much keep pushing"
            JesseSecondStateText = fontVerySmall.render(JesseSecondStateState, True, (0,0,0), (153,153,51))
            JesseSecondStateTextPartTwo = fontVerySmall.render(JesseSecondStateStatePartTwo, True, (0,0,0), (153,153,51))
            jesseMPSRect = jesseMPSText.get_rect()
            jesseMPSRect.center = (screenX-upgradeBox[0]*2+60,screenY//3+7)
            jesseDispriptionRect = jesseDispriptionText.get_rect()
            jesseDispriptionRect.center = (screenX-upgradeBox[0]*2+100,screenY//3+20)
            JesseSecondStateRect = JesseSecondStateText.get_rect()
            JesseSecondStateRect.center = (screenX-upgradeBox[0]*2+85,screenY//3+35)
            JesseSecondStateRectPartTwo = JesseSecondStateTextPartTwo.get_rect()
            JesseSecondStateRectPartTwo.center = (screenX-upgradeBox[0]*2+105,screenY//3+50)
            screen.blit(JesseSecondStateTextPartTwo,JesseSecondStateRectPartTwo)
            screen.blit(jesseMPSText,jesseMPSRect)
            screen.blit(JesseSecondStateText,JesseSecondStateRect)
            screen.blit(jesseDispriptionText,jesseDispriptionRect)
        elif jesseState == "Improved" :
            jesseMPSString = "each jesse cook " + str(baseJesseMethPerSecound)
            jesseMPSText = fontVerySmall.render(jesseMPSString, True, (0,0,0), (153,153,51))
            jesseMPSRect = jesseMPSText.get_rect()
            jesseMPSRect.center = (screenX-upgradeBox[0]*2+60,screenY//3+7) 
            jesseDispription = "Jesse current state is :" + jesseState 
            jesseDispriptionText = fontVerySmall.render(jesseDispription, True, (0,0,0), (153,153,51))
            JesseThirdStateState = "He is not doing drugs anymore"
            JesseThirdStateStatePartTwo = "But he do noy know how to cook"
            JesseThirdStateText = fontVerySmall.render(JesseThirdStateState, True, (0,0,0), (153,153,51))
            JesseThirdStateTextPartTwo = fontVerySmall.render(JesseThirdStateStatePartTwo, True, (0,0,0), (153,153,51))
            jesseMPSRect = jesseMPSText.get_rect()
            jesseMPSRect.center = (screenX-upgradeBox[0]*2+60,screenY//3+7)
            jesseDispriptionRect = jesseDispriptionText.get_rect()
            jesseDispriptionRect.center = (screenX-upgradeBox[0]*2+100,screenY//3+20)
            JesseThirdStateRect = JesseThirdStateText.get_rect()
            JesseThirdStateRect.center = (screenX-upgradeBox[0]*2+95,screenY//3+35)
            JesseThirdStateRectPartTwo = JesseThirdStateTextPartTwo.get_rect()
            JesseThirdStateRectPartTwo.center = (screenX-upgradeBox[0]*2+95,screenY//3+50)
            screen.blit(JesseThirdStateTextPartTwo,JesseThirdStateRectPartTwo)
            screen.blit(jesseMPSText,jesseMPSRect)
            screen.blit(JesseThirdStateText,JesseThirdStateRect)
            screen.blit(jesseDispriptionText,jesseDispriptionRect)
            screen.blit(jesseClean,(screenX-60,screenY//3))
        
        

    if methCookedAllTime >= 50000 :
        selfImprovementCondition = True
    

    
    

    #WalterBlack part    
    pygame.draw.rect(screen,(255,255,0),(screenX-upgradeBox[0],screenY//3+upgradeBox[1]+upgradeBox[2],upgradeBox[0],upgradeBox[1]))
    walterBlackPriceText = fontVerySmall.render(walterBlackPriceString, True, (0,0,0), (255,255,0))
    walterBlackPriceRect = walterBlackPriceText.get_rect()
    walterBlackPriceRect.center = (screenX-screenX//6,screenY//3+10+upgradeBox[1]+upgradeBox[2])
    walterBlackOwnedText = fontVerySmall.render(walterBlackOwnedString, True, (0,0,0), (255,255,0))
    walterBlackOwnedRect = walterBlackOwnedText.get_rect()
    walterBlackOwnedRect.center = (screenX-screenX//6,screenY//3+30+upgradeBox[1]+upgradeBox[2])
    walterBlackOwnedString = "WalterBlack owned " + str(walterBlackOwned)
    walterBlackOwnedString = "WalterBlack owned " + str(walterBlackOwned)
    walterBlackPriceString = "WalterBlackPrice" + str(walterBlackPrice)
    screen.blit (walterBlackPriceText,walterBlackPriceRect)
    screen.blit(walterBlackOwnedText,walterBlackOwnedRect)
    screen.blit(walterBlack,(screenX-60,screenY//3+upgradeBox[1]+upgradeBox[2]))
    if mousePos [0] in range (screenX-upgradeBox[0],screenX) and mousePos [1] in range ((screenY//3)+(upgradeBox[1])+(upgradeBox[2]),screenY//3+(upgradeBox[1]*2)+upgradeBox[2]):
        if methCooked >= walterBlackPrice :
            walterBlackOwned+=1
            methCooked-=walterBlackPrice
            methPerSecound += basewalterBlackMethPerSecound
            walterBlackPrice+=walterBlackPrice//15
        mousePos = (0,0)
        
        
    #WalterWhite part
    pygame.draw.rect(screen,(255,255,0),(screenX-upgradeBox[0],screenY//3+((upgradeBox[1]+upgradeBox[2])*2),upgradeBox[0],upgradeBox[1]))
    walterWhitePriceText = fontVerySmall.render(walterWhitePriceString, True, (0,0,0), (255,255,0))
    walterWhitePriceRect = walterWhitePriceText.get_rect()
    walterWhitePriceRect.center = (screenX-screenX//6,screenY//3+10+((upgradeBox[1]+upgradeBox[2])*2))
    walterWhiteOwnedText = fontVerySmall.render(walterWhiteOwnedString, True, (0,0,0), (255,255,0))
    walterWhiteOwnedRect = walterWhiteOwnedText.get_rect()
    walterWhiteOwnedRect.center = (screenX-screenX//6,screenY//3+30+((upgradeBox[1]+upgradeBox[2])*2))
    walterWhiteOwnedString = "WalterWhite owned " + str(walterWhiteOwned)
    walterWhiteOwnedString = "WalterWhite owned " + str(walterWhiteOwned)
    walterWhitePriceString = "WalterWhite Price" + str(walterWhitePrice)
    screen.blit (walterWhitePriceText,walterWhitePriceRect)
    screen.blit (walterWhiteOwnedText,walterWhiteOwnedRect)
    if walterWhiteOwned >100 :
        screen.blit(redWalter,(screenX-60,screenY//3+((upgradeBox[1]+upgradeBox[2])*2)))
    else :
        screen.blit(walterWhite,(screenX-60,screenY//3+((upgradeBox[1]+upgradeBox[2])*2)))
    if mousePos [0] in range (screenX-upgradeBox[0],screenX) and mousePos [1] in range ((screenY//3)+(upgradeBox[1]*2)+(upgradeBox[2]*2),screenY//3+(upgradeBox[1]*3)+(upgradeBox[2])*2):
        if methCooked >= walterWhitePrice :
            walterWhiteOwned+=1
            methCooked-=walterWhitePrice
            methPerSecound += basewalterWhiteMethPerSecound
            walterWhitePrice+=walterWhitePrice//15
        mousePos = (0,0)
        
    #Gus buff
    if gusSpawnCoolDown <= 0 :
        gusIsAlive = True
        gusMultiplierRandom = random.randint(0,3)
        gusSize = random.randint(30,50)
        gusX = random.randint(200,600)
        gusY = random.randint(100,500)
        gusSpawnCoolDown = random.randint(150,200)
        gusLifeSpan = random.randint(10,20)
        gusMultiplierRandom = random.randint(0,3)
        gusFrenzyMultiplierString = "Meth Multiplier " + str(gusMultiplier[gusMultiplierRandom]) + "  "
        gusFrenzyMultiplierText  = fontSmall.render(gusFrenzyMultiplierString, True, (255,255,255), (0,0,0))
        gusFrenzyRect = gusFrenzyText.get_rect()
        gusFrenzyRect.center = (gusX,gusY-30)
        gusFrenzyMultiplierRect = gusFrenzyMultiplierText.get_rect()
        gusFrenzyMultiplierRect.center = (gusX,gusY-10)
        
    if gusIsAlive  :
        gus = pygame.transform.scale(gus,(gusSize,gusSize))
        screen.blit(gus,(gusX,gusY))
        if mousePos [0] in range (gusX,gusX+gusSize) and mousePos [1] in range (gusY,gusY+(gusSize)):
            gusIsAlive = False
            gusMultiplierLifeSpan = random.randint(60,120)
            gusMultiplierIsActive = True
            gusStringLifeSpan = 3
            print(gusMultiplier[gusMultiplierRandom],gusMultiplierLifeSpan)
    if gusMultiplierIsActive :
        methCooked += ((methPerSecound+jesseMPS)*gusMultiplier[gusMultiplierRandom])//timer
        methCooked += (methPerClick*gusMultiplier[gusMultiplierRandom])//timer
        methCookedAllTime += ((methPerSecound+jesseMPS)*gusMultiplier[gusMultiplierRandom])//timer
    else:
        methCooked += (methPerSecound+ jesseMPS)//timer
        methCookedAllTime += methPerSecound//timer

    
    #upgrades
    if selfImprovementCondition :
        screen.blit(howToCook,(screenX-upgradeBox[0],0))
        if hoverPos[0]in range(screenX-upgradeBox[0],screenX-upgradeBox[0]+upgradeBoxSize) and hoverPos[1] in range (0,0+upgradeBoxSize):
            pygame.draw.rect(screen,(153,153,51),(screenX-upgradeBox[0]*2 , 0 ,upgradeBox[0],upgradeBoxSize))
            if not jesseUpgradesCondition1Max and not jesseUpgradeLevetCounter>=5:
                #text
                jesseLevelText = fontVerySmall.render("Jesse De-addiction level is " +str(jesseUpgradeLevetCounter)+" out of "+str(len(jesseUpgradeLevetCosts)-2), True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-113,6)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("Next Upgrade Price Would be "+str(jesseUpgradeLevetCosts[jesseUpgradeLevetCounter]), True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-110,25)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontTiny.render("Jesse's are 2 time's cheaper steal twice less ", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-110,40)
                screen.blit(jesseLevelText,jesseLevelRect) 
                #end text
            if jesseUpgradesCondition1Max and toggleIsActivated:
                #text
                jesseLevelText = fontVerySmall.render("jesse would be addicted again ", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-130,10)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("and steal your meth |click to toggle", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-115,25)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("price is : "+ str(methCooked//10), True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-110,40)
                screen.blit(jesseLevelText,jesseLevelRect) 
                #end text
            elif not toggleIsActivated and jesseUpgradesCondition1Max :
                #text
                jesseLevelText = fontVerySmall.render("Jesse will no longer will be a addict", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-115,10)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("and will continue to cook |click to toggle", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-115,25)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("price is : "+ str(methCooked//10), True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-110,40)
                screen.blit(jesseLevelText,jesseLevelRect) 
                #end text


        #if mousePos[0]in range(screenX-upgradeBox[0],screenX-upgradeBox[0]+upgradeBoxSize) and mousePos[1] in range (0,0+upgradeBoxSize)  :
    if jesseUpgradesCondition1 :
        screen.blit(drugAddictionCamp,(screenX-upgradeBox[0]+upgradeBoxSize+10,0))
        if mousePos[0]in range((screenX-upgradeBox[0])+10+upgradeBoxSize,screenX-upgradeBox[0]+upgradeBoxSize*2+10) and mousePos[1] in range (0,0+upgradeBoxSize)  :
            if jesseUpgradesCondition1Max and toggleIsActivated :
                methCooked-=(methCooked//10)
                baseJesseMethPerSecound = -64
                jesseState = "Addicted"
                toggleIsActivated = False
            elif not toggleIsActivated and jesseUpgradesCondition1Max:
                methCooked-=(methCooked//10)
                baseJesseMethPerSecound = 1
                jesseState = "Improved"
                toggleIsActivated = True
            if not jesseUpgradesCondition1Max and not jesseUpgradeLevetCounter>5 and methCooked >= jesseUpgradeLevetCosts[jesseUpgradeLevetCounter]:
                methCooked -=jesseUpgradeLevetCosts[jesseUpgradeLevetCounter]
                jesseUpgradeLevetCounter+=1
                baseJesseMethPerSecound=baseJesseMethPerSecound//2
                jessePrice=jessePrice//2
                jesseState = "Improving"
                print(jessePrice,baseJesseMethPerSecound)
                print(jesseUpgradesCondition1Max,jesseState)
                if jesseUpgradeLevetCounter>=5:
                    jesseUpgradesCondition1Max = True
                    toggleIsActivated = True
            mousePos=(0,0)
        if hoverPos[0]in range((screenX-upgradeBox[0])+10+upgradeBoxSize,screenX-upgradeBox[0]+upgradeBoxSize*2+10) and hoverPos[1] in range (0,0+upgradeBoxSize):
            pygame.draw.rect(screen,(153,153,51),(screenX-upgradeBox[0]*2 , 0 ,upgradeBox[0],upgradeBoxSize))
            if not jesseUpgradesCondition1Max and not jesseUpgradeLevetCounter>=5:
                #text
                jesseLevelText = fontVerySmall.render("Jesse De-addiction level is " +str(jesseUpgradeLevetCounter+1)+" out of "+str(len(jesseUpgradeLevetCosts)-1), True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-113,6)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("Next Upgrade Price Would be "+str(jesseUpgradeLevetCosts[jesseUpgradeLevetCounter]), True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-110,25)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontTiny.render("Jesse's are 2 time's cheaper steal twice less ", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-110,40)
                screen.blit(jesseLevelText,jesseLevelRect) 
                #end text
            if jesseUpgradesCondition1Max and toggleIsActivated:
                #text
                jesseLevelText = fontVerySmall.render("jesse would be addicted again ", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-130,10)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("and steal your meth |click to toggle", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-115,25)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("price is : "+ str(methCooked//10), True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-110,40)
                screen.blit(jesseLevelText,jesseLevelRect) 
                #end text
            elif not toggleIsActivated and jesseUpgradesCondition1Max :
                #text
                jesseLevelText = fontVerySmall.render("Jesse will no longer will be a addict", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-115,10)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("and will continue to cook |click to toggle", True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-115,25)
                screen.blit(jesseLevelText,jesseLevelRect)
                jesseLevelText = fontVerySmall.render("price is : "+ str(methCooked//10), True, (0,0,0), (153,153,51))
                jesseLevelRect = jesseLevelText.get_rect()
                jesseLevelRect.center = (screenX-upgradeBox[0]-110,40)
                screen.blit(jesseLevelText,jesseLevelRect) 
                #end text



    if toggleIsActivated:
        jesseState = "Improved"
    elif not toggleIsActivated and jesseUpgradesCondition1Max:
        jesseState = "Addicted"
    if jesseState == "Addicted" or jesseState == "Improving":
        screen.blit(jesseAddict,(screenX-60,screenY//3))
    elif jesseState == "Improved" :
        screen.blit(jesseClean,(screenX-60,screenY//3))
    if gusStringLifeSpan >0 :
        screen.blit(gusFrenzyMultiplierText,gusFrenzyMultiplierRect)
        screen.blit(gusFrenzyText,gusFrenzyRect)  
    timerReset+=1
    if methCooked >= 1000000000000 :
        screen.blit(gameOver,(0,0))
        gameRun = False
    if timerReset >= timer :
        timerReset = 0
        gameTimer +=1
        gusSpawnCoolDown-=1
        gusLifeSpan-=1
        gusMultiplierLifeSpan-=1
        gusStringLifeSpan-=1
        if gusMultiplierLifeSpan <0:
            gusMultiplierIsActive = False
        if gusLifeSpan <= 0 :
            gusIsAlive = False
    clock.tick(timer)
    pygame.display.flip()
pygame.quit()
 



>>>>>>> 3527660f6e171efd820d9ecf1650615a078f99b7
