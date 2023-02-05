import pygame
import time
import random

pygame.init()
##Initializes screen, sets size, caption, timer, font, and colors.
##Also creates variables for white and black.
WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Yahtzee")
timer = pygame.time.Clock()
fps = 60

##Font size
font = pygame.font.Font('freesansbold.ttf', 18)
smallText = pygame.font.Font("freesansbold.ttf",20)
midText = pygame.font.Font('freesansbold.ttf', 50)
largeText = pygame.font.Font('freesansbold.ttf',115)

##Colors
background = (128, 128, 128)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 200, 0)
red = (200, 0, 0)

numbers = [0, 0, 0, 0, 0,]
roll = False

##Left/Right alignment
centered = WIDTH/2 - 50
left = 100
right = 400

##Up/Down alignment
topMenuButton = 300
middleMenuButton = 450
bottomMenuButton = 600
bottomRulesButton = 650

##Button size
menuButtonWidth = 100
menuButtonHeight = 50

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            if action == "Play":
               game_loop()
            elif action == "Rules":
               rules_page()
            elif action == "Back":
               game_intro()
            elif action == "How to play":
               htp_page()
            elif action == "Example Turn":
               example_page()
            elif action == "Ending a Game":
               end_page()
            elif action == "Scoring":
                scoring_page()
            elif action == "Upper Deck Scoring":
                upperdeckpage()
            elif action == "Lower Deck Scoring":
                lowerdeckpage()
            elif action == "Back to rules":
                rules_page()
            elif action == "Back to menu":
                game_intro()
            elif action == "Quit":
               pygame.quit()
               quit()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def rules_page():
    screen.fill(background)

    TextSurf, TextRect = text_objects("The Rules of", midText)
    TextRect.center = ((WIDTH/2), (HEIGHT/8))
    screen.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_objects("YAHTZEE", largeText)
    TextRect.center = ((WIDTH/2),(HEIGHT/4))
    screen.blit(TextSurf, TextRect)
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()

        Back = button("Back", left, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, green, "Back")
        Quit = button("Exit", right, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")
        Scoring = button('Scoring' , centered, 400, menuButtonWidth , menuButtonHeight, black, green, 'Scoring')
        Howtoplay = button('How to Play' , 225 , 250 , 150 , menuButtonHeight, black , green , 'How to play')
        ExampleTurn = button('Example Turn' , 225 , 325 , 150 , menuButtonHeight , black , green , 'Example Turn')
        Ending = button('Ending a Game', 220, 475 , 160, menuButtonHeight , black , green , 'Ending a Game')

        pygame.display.update()
        timer.tick(15)

def game_loop():
    print("Hello")

def htp_page():
    screen.fill(background)
    TextSurf, TextRect = text_objects("HOW TO PLAY" , midText)
    TextRect.center = ((WIDTH/2) , (HEIGHT/4))
    screen.blit(TextSurf, TextRect)
    oghtpimg = pygame.image.load('htp.png')
    htpimg= pygame.transform.scale(oghtpimg , (600 , 200))
    screen.blit(htpimg , (0 , 250))
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()

        Backtor = button("Back to Rules", centered , bottomRulesButton, 135 , menuButtonHeight, black, green, "Back to rules")
        Quit = button("Exit", right, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")
        mBack = button("Back to menu", left, bottomRulesButton, 135, menuButtonHeight, black, green, "Back to menu")

        pygame.display.update()
        timer.tick(15)

def example_page():
    screen.fill(background)
    TextSurf, TextRect = text_objects("EXAMPLE TURN" , midText)
    TextRect.center = ((WIDTH/2) , (HEIGHT/4))
    screen.blit(TextSurf, TextRect)
    ogexampleimg = pygame.image.load('example.png')
    examplepimg= pygame.transform.scale(ogexampleimg , (600 , 400))
    screen.blit(examplepimg , (0 , 225))
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()

        Backtor = button("Back to Rules", centered , bottomRulesButton, 135 , menuButtonHeight, black, green, "Back to rules")
        Quit = button("Exit", right, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")
        mBack = button("Back to menu", left, bottomRulesButton, 135, menuButtonHeight, black, green, "Back to menu")

        pygame.display.update()
        timer.tick(15)

def scoring_page():
    screen.fill(background)
    TextSurf, TextRect = text_objects("SCORING", largeText)
    TextRect.center = ((WIDTH/2),(HEIGHT/4))
    screen.blit(TextSurf, TextRect)
    ogrulesimg = pygame.image.load('Scoring.png')
    rulesimg = pygame.transform.scale(ogrulesimg , (600 , 150))
    screen.blit(rulesimg , (0 , 250))
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()

        upperdeck = button('Upper Deck Scoring' , (WIDTH/2 - 100), 475, 200 , menuButtonHeight, black, green, 'Upper Deck Scoring')
        lowerdeck = button('Lower Deck Scoring' , (WIDTH/2 - 100) , 550 , 200, menuButtonHeight , black , green , 'Lower Deck Scoring')
        Backtor = button("Back to Rules", centered , bottomRulesButton, 135 , menuButtonHeight, black, green, "Back to rules")
        Quit = button("Exit", right, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")
        mBack = button("Back to menu", left, bottomRulesButton, 135, menuButtonHeight, black, green, "Back to menu")

        pygame.display.update()
        timer.tick(15)

def end_page():
    screen.fill(background)
    TextSurf, TextRect = text_objects("ENDING A GAME" , midText)
    TextRect.center = ((WIDTH/2) , (HEIGHT/4))
    screen.blit(TextSurf, TextRect)
    ogendingimg = pygame.image.load('end.png')
    endingimg = pygame.transform.scale(ogendingimg , (600 , 400))
    screen.blit(endingimg , (0 , 225))
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()

        Backtor = button("Back to Rules", centered , bottomRulesButton, 135 , menuButtonHeight, black, green, "Back to rules")
        Quit = button("Exit", right, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")
        mBack = button("Back to menu", left, bottomRulesButton, 135, menuButtonHeight, black, green, "Back to menu")

        pygame.display.update()
        timer.tick(15)

def upperdeckpage():
    screen.fill(background)
    TextSurf, TextRect = text_objects("UPPER DECK" , midText)
    TextRect.center = ((WIDTH/2) , (HEIGHT/4))
    screen.blit(TextSurf, TextRect)
    ogupperimg = pygame.image.load('upper.png')
    upperimg = pygame.transform.scale(ogupperimg , (600 , 150))
    screen.blit(upperimg , (0 , 250))

def lowerdeckpage():
    screen.fill(background)
    TextSurf, TextRect = text_objects("LOWER DECK" , midText)
    TextRect.center = ((WIDTH/2) , 30)
    screen.blit(TextSurf, TextRect)
    oglowerimg = pygame.image.load('lower.png')
    lowerimg = pygame.transform.scale(oglowerimg , (600 , 400))
    screen.blit(lowerimg , (0 , 50))


def game_intro():
    intro = True
    screen.fill(background)

    TextSurf, TextRect = text_objects("YAHTZEE", largeText)
    TextRect.center = ((WIDTH/2),(HEIGHT/4))
    screen.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_objects("Welcome to", midText)
    TextRect.center = ((WIDTH/2), (HEIGHT/8))
    screen.blit(TextSurf, TextRect)

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()

        Rules = button("Rules", centered, topMenuButton, menuButtonWidth, menuButtonHeight, black, green, "Rules")
        Play = button("Play", centered, middleMenuButton, menuButtonWidth, menuButtonHeight, black, green, "Play")
        Quit = button("Exit", centered, bottomMenuButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")

        pygame.display.update()
        timer.tick(15)

game_intro()
pygame.quit()
quit()
