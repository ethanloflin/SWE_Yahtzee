import random
import pygame
import time

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

##Dice
numbers_list = [0, 0, 0, 0, 0,]
selected_choice = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
possible = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
done = [False, False, False, False, False, False, False, False, False, False, False, False, False]
score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
rolled = False

dice_choice = [True, True, True, True, True]

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def wordsOnScreen(msg,txtSize,h,y):
    TextSurf, TextRect = text_objects(msg , txtSize)
    TextRect.center = ((WIDTH/2) , (HEIGHT/h + y))
    screen.blit(TextSurf, TextRect)

#Buttons
def diceButton(x, y, w, h, ic, ac, choice,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "One":
                choice[0] = True
                return choice
            elif action == "Two":
                choice[1] = True
                return choice
            elif action == "Three":
                choice[2] = True
                return choice
            elif action == "Four":
                choice[3] = True
                return choice
            elif action == "Five":
                choice[4] = True
                return choice

def rollButton(msg,x,y,w,h,ic,ac,dice,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "FirstRoll":
                roll_dice(dice)
                return True
            elif action == "Reroll":
                roll_dice(dice)
                return True
            elif action == "Not selected":
                print("No dice selected")
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def menuButton(msg,x,y,w,h,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            if action == "Play":
               game_loop(3)
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
            elif action =="Accepted":
                accepted()
            elif action == "Nothing":
                print("No more rolls")
            elif action == "Quit":
               pygame.quit()
               quit()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def scoreButton(x,y,w,h,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "Aces":
                ScoreAces(numbers_list, possible)
            elif action == "Twos":
                ScoreTwos(numbers_list, possible)
            elif action == "Threes":
                ScoreThrees(numbers_list, possible)
            elif action == "Fours":
                ScoreFours(numbers_list, possible)
            elif action == "Fives":
                ScoreFives(numbers_list, possible)
            elif action == "Sixes":
                ScoreSixes(numbers_list, possible)
            elif action == "3ofAKind":
                ScoreThreeOfAKind(numbers_list, possible)
            elif action == "4ofAKind":
                ScoreFourOfAKind(numbers_list, possible)
            elif action == "FullHouse":
                ScoreFullHouse(numbers_list, possible)
            elif action == "SmStraight":
                ScoreSmStraight(numbers_list, possible)
            elif action == "LgStraight":
                ScoreLgStraight(numbers_list, possible)
            elif action == "YAHTZEE":
                ScoreYahtzee(numbers_list, possible)
            elif action == "Chance":
                ScoreChance(numbers_list, possible)
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

#Rules
def rules_page():
    topText = "The Rules of"
    bottomText = "YAHTZEE"

    screen.fill(background)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        wordsOnScreen(topText, midText, 8, -50)
        wordsOnScreen(bottomText, largeText, 4, -50)

        mouse = pygame.mouse.get_pos()

        Back = menuButton("Back", left, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, green, "Back")
        Quit = menuButton("Exit", right, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")
        Howtoplay = menuButton('How to Play' , 225 , 250 , 150 , menuButtonHeight, black , green , 'How to play')
        Scoring = menuButton('Scoring' , centered, 350, menuButtonWidth , menuButtonHeight, black, green, 'Scoring')
        Ending = menuButton('Ending a Game', 220, 450 , 160, menuButtonHeight , black , green , 'Ending a Game')
        ExampleTurn = menuButton('Example Turn' , 225 , 550 , 150 , menuButtonHeight , black , green , 'Example Turn')

        pygame.display.update()
        timer.tick(15)

def htp_page():
    htpTitle = "HOW TO PLAY"
    one = "Each player takes one score card."
    two ="On your turn, you may roll dice up to 3 times."
    three = "Although you may stop and score after your 1st or 2nd roll."
    four = "After the 1st or 2nd roll, you can decide"
    five = "to keep any number of dice and reroll the rest."
    six = "After 3 rolls, or you are happy with your dice"
    seven = "you can now score on the score sheet."

    screen.fill(background)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        wordsOnScreen(htpTitle, midText, 4, 0)
        wordsOnScreen(one, smallText, 3, 0)
        wordsOnScreen(two, smallText, 3, 40)
        wordsOnScreen(three, smallText, 3, 60)
        wordsOnScreen(four, smallText, 3, 100)
        wordsOnScreen(five, smallText, 3, 120)
        wordsOnScreen(six, smallText, 3, 160)
        wordsOnScreen(seven, smallText, 3, 180)

        mouse = pygame.mouse.get_pos()

        Backtor = menuButton("Back to Rules", centered , bottomRulesButton, 135 , menuButtonHeight, black, green, "Back to rules")
        Quit = menuButton("Exit", right, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")
        mBack = menuButton("Back to menu", left, bottomRulesButton, 135, menuButtonHeight, black, green, "Back to menu")

        pygame.display.update()
        timer.tick(15)

def example_page():
    exampleTitle = "EXAMPLE TURN"
    one = "First Roll: 2, 3, 4, 4, 5"
    two ="You could reroll for a 3 of a Kind,"
    three ="a 4 of a Kind, or a Large Straight."
    four = "You already have a Small Straight, so you could reroll a 4"
    five = "in the hopes of getting a 1 or 6. So you reroll a 4."
    six = "Second Roll: 2, 2, 3, 4, 5"
    seven = "You now could reroll a 2 and go for a Large Straight,"
    eight = "or set the Twos aside and roll for Twos or 3 of a Kind."
    nine = "You decide to keep the Twos, and reroll the rest"
    ten = "Third Roll: 2, 2, 2, 3, 3" 
    eleven = "You now have to score, and here are your options:"
    twelve = "6 for Twos"
    thirteen = "6 for Threes"
    fourteen = "12 for Three of a Kind"
    fifteen = "25 for Full House"
    sixteen = "You choose the Full House, so you score 25 points."

    screen.fill(background)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        wordsOnScreen(exampleTitle, midText, 6, 0)
        wordsOnScreen(one, smallText, 4, 0)
        wordsOnScreen(two, smallText, 4, 20)
        wordsOnScreen(three, smallText, 4, 40)
        wordsOnScreen(four, smallText, 4, 80)
        wordsOnScreen(five, smallText, 4, 100)
        wordsOnScreen(six, smallText, 4, 140)
        wordsOnScreen(seven, smallText, 4, 160)
        wordsOnScreen(eight, smallText, 4, 180)
        wordsOnScreen(nine, smallText, 4, 200)
        wordsOnScreen(ten, smallText, 4, 240)
        wordsOnScreen(eleven, smallText, 4, 260)
        wordsOnScreen(twelve, smallText, 4, 280)
        wordsOnScreen(thirteen, smallText, 4, 300)
        wordsOnScreen(fourteen, smallText, 4, 320)
        wordsOnScreen(fifteen, smallText, 4, 340)
        wordsOnScreen(sixteen, smallText, 4, 380)

        mouse = pygame.mouse.get_pos()

        Backtor = menuButton("Back to Rules", centered , bottomRulesButton, 135 , menuButtonHeight, black, green, "Back to rules")
        Quit = menuButton("Exit", right, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")
        mBack = menuButton("Back to menu", left, bottomRulesButton, 135, menuButtonHeight, black, green, "Back to menu")

        pygame.display.update()
        timer.tick(15)

def scoring_page():
    scoreTitle = "SCORING"
    first = "When you have finished rolling,"
    second = "decide which box you would like to fill in."
    third = "For each game there are 13 boxes."
    fourth = "You must fill in a box each turn."
    fifth = "If you are not able to fill in a box (or don't want to)"
    sixth = "you must enter a zero in any box."
    seventh = "You can only fill in a box once, so choose carefully."

    screen.fill(background)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        wordsOnScreen(scoreTitle, midText, 6, 0)
        wordsOnScreen(first, smallText, 4, 20)
        wordsOnScreen(second, smallText, 4, 40)
        wordsOnScreen(third, smallText, 4, 80)
        wordsOnScreen(fourth, smallText, 4, 100)
        wordsOnScreen(fifth, smallText, 4, 140)
        wordsOnScreen(sixth, smallText, 4, 160)
        wordsOnScreen(seventh, smallText, 4, 200)

        mouse = pygame.mouse.get_pos()

        upperdeck = menuButton('Upper Section' , (WIDTH/2 - 250), 500, 150 , menuButtonHeight, black, green, 'Upper Deck Scoring')
        Backtor = menuButton("Back to Rules", centered , bottomRulesButton, 135 , menuButtonHeight, black, green, "Back to rules")
        Quit = menuButton("Exit", right, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")
        mBack = menuButton("Back to menu", left, bottomRulesButton, 135, menuButtonHeight, black, green, "Back to menu")

        pygame.display.update()
        timer.tick(15)

def end_page():
    endTitle = "ENDING A GAME"
    first = "Once each player has filled in all 13 boxes, the game ends."
    second = "Each player then adds up their scores as follows:"
    third = "Add all of the Upper section together."
    fourth = "If you get at least 63 points in the Upper section"
    fifth = "you get 35 bonus points."
    sixth = "Add all of the Lower section together."
    seventh = "If you have any bonus YAHTZEEs add them now."
    eighth = "Add total of Upper and Lower sections."
    ninth = "If you have the highest score, you win!"

    screen.fill(background)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        wordsOnScreen(endTitle, midText, 6, 0)
        wordsOnScreen(first, smallText, 4, 0)
        wordsOnScreen(second, smallText, 4, 40)
        wordsOnScreen(third, smallText, 4, 80)
        wordsOnScreen(fourth, smallText, 4, 100)
        wordsOnScreen(fifth, smallText, 4, 120)
        wordsOnScreen(sixth, smallText, 4, 160)
        wordsOnScreen(seventh, smallText, 4, 180)
        wordsOnScreen(eighth, smallText, 4, 220)
        wordsOnScreen(ninth, smallText, 4, 260)

        mouse = pygame.mouse.get_pos()

        Backtor = menuButton("Back to Rules", centered , bottomRulesButton, 135 , menuButtonHeight, black, green, "Back to rules")
        Quit = menuButton("Exit", right, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")
        mBack = menuButton("Back to menu", left, bottomRulesButton, 135, menuButtonHeight, black, green, "Back to menu")

        pygame.display.update()
        timer.tick(15)

def upperdeckpage():
    udTitle = "UPPER DECK"
    first = "To score in the Upper Section, add only"
    second = "the dice with the same number you are wanting to enter"
    third = "For Example. You roll: 3, 3, 3, 2, 4 "
    fourth = "You could enter one of the following"
    fifth = "9 in the Threes segment"
    sixth ="2 in the Twos segment"
    seventh = "4 in the Fours segment"
    eighth = "If you are able to score 63 points in the Upper section"
    ninth ="you earn 35 bonus points"

    screen.fill(background)
   
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        wordsOnScreen(udTitle, midText, 6, 0)
        wordsOnScreen(first, smallText, 4, 0)
        wordsOnScreen(second, smallText, 4, 20)
        wordsOnScreen(third, smallText, 4, 60)
        wordsOnScreen(fourth, smallText, 4, 80)
        wordsOnScreen(fifth, smallText, 4, 120)
        wordsOnScreen(sixth, smallText, 4, 140)
        wordsOnScreen(seventh, smallText, 4, 160)
        wordsOnScreen(eighth, smallText, 4, 200)
        wordsOnScreen(ninth, smallText, 4, 220)

        mouse = pygame.mouse.get_pos()
        
        lowerdeck = menuButton('Lower Section' , (WIDTH/2 + 100) , 500 , 150, menuButtonHeight , black , green , 'Lower Deck Scoring')
        Backtor = menuButton("Back to Rules", centered , bottomRulesButton, 135 , menuButtonHeight, black, green, "Back to rules")
        Quit = menuButton("Exit", right, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")
        mBack = menuButton("Back to menu", left, bottomRulesButton, 135, menuButtonHeight, black, green, "Back to menu")

        pygame.display.update()
        timer.tick(15)

def lowerdeckpage():
    ldTitle = "LOWER DECK"
    first = "To score in the Lower Section"
    second = "the dice have to match the requirements."
    threeofaKind = "3 of a Kind: 3 of any one number."
    tallyTotal = "Tally the total of all your dice."
    fourofaKind = "4 of a Kind: 4 of any one number."
    fullHouse = "Full House: 3 of a Kind and 2 of a Kind."
    twentyFivePoints = "Worth 25 points regardless of dice numbers."
    smStraight = "Small Straight: Any sequence of 4 numbers in order."
    thirtyPoints = "Worth 30 points."
    lgStraight = "Large Straight: Any sequence of 5 numbers in order."
    fortyPoints = "Worth 40 points."
    yahtzee = "YAHTZEE: 5 of any one number."
    fifty = "Worth 50 points"
    bonusYahtzee = "Any additional YAHTZEEs are 100 bonus points each."
    chance = "Chance: All the dice in your hand."
    allDice = "Add the value of all the dice in your hand."

    screen.fill(background)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        wordsOnScreen(ldTitle, midText, 8, -10)
        wordsOnScreen(first, smallText, 6, 0)
        wordsOnScreen(second, smallText, 6, 20)
        wordsOnScreen(threeofaKind, smallText, 6, 60)
        wordsOnScreen(tallyTotal, smallText, 6, 80)
        wordsOnScreen(fourofaKind, smallText, 6, 120)
        wordsOnScreen(tallyTotal, smallText, 6, 140)
        wordsOnScreen(fullHouse, smallText, 6, 180)
        wordsOnScreen(twentyFivePoints, smallText, 6, 200)
        wordsOnScreen(smStraight, smallText, 6, 240)
        wordsOnScreen(thirtyPoints, smallText, 6, 260)
        wordsOnScreen(lgStraight, smallText, 6, 300)
        wordsOnScreen(fortyPoints, smallText, 6, 320)
        wordsOnScreen(yahtzee, smallText, 6, 360)
        wordsOnScreen(fifty, smallText, 6, 380)
        wordsOnScreen(bonusYahtzee, smallText, 6, 400)
        wordsOnScreen(chance, smallText, 6, 440)
        wordsOnScreen(allDice, smallText, 6, 460)

        mouse = pygame.mouse.get_pos()

        Backtor = menuButton("Back to Rules", centered , bottomRulesButton, 135 , menuButtonHeight, black, green, "Back to rules")
        Quit = menuButton("Exit", right, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")
        mBack = menuButton("Back to menu", left, bottomRulesButton, 135, menuButtonHeight, black, green, "Back to menu")

        pygame.display.update()
        timer.tick(15)

#Scoring
def ScoreAces(numbers_list, possible):
    temp = 0
    if possible[0] == False:
        temp = 0
    else:
        for x in numbers_list:
            if x == 1:
                temp += 1
    score[0] = temp
    done[0] = True
    rolled = False
    game_loop(3)

def ScoreTwos(numbers_list, possible):
    temp = 0
    if possible[1] == False:
        temp = 0
    else:
        for x in numbers_list:
            if x == 2:
                temp += 2
    score[1] = temp
    done[1] = True
    rolled = False
    game_loop(3) 

def ScoreThrees(numbers_list, possible):
    temp = 0
    if possible[2] == False:
        temp = 0
    else:
        for x in numbers_list:
            if x == 3:
                temp += 3
    score[2] = temp
    done[2] = True
    rolled = False
    game_loop(3)   

def ScoreFours(numbers_list, possible):
    temp = 0
    if possible[3] == False:
        temp = 0
    else:
        for x in numbers_list:
            if x == 4:
                temp += 4
    score[3] = temp
    done[3] = True
    rolled = False
    game_loop(3)   

def ScoreFives(numbers_list, possible):
    temp = 0
    if possible[4] == False:
        temp = 0
    else:
        for x in numbers_list:
            if x == 5:
                temp += 5
    score[4] = temp
    done[4] = True
    rolled = False
    game_loop(3)   

def ScoreSixes(numbers_list, possible):
    temp = 0
    if possible[5] == False:
        temp = 0
    else:
        for x in numbers_list:
            if x == 6:
                temp += 6
    score[5] = temp
    done[5] = True
    rolled = False
    game_loop(3)   

    temp = 0
    for x in numbers_list:
        if x == 1:
            temp += 1
    score[0] = temp
    done[0] = True
    rolled = False
    game_loop(3)

def ScoreThreeOfAKind(numbers_list, possible):
    temp = 0
    if possible[6] == False:
        temp = 0
    else:
        for x in numbers_list:
            temp += x
    score[6] = temp
    done[6] = True
    rolled = False
    game_loop(3)   

def ScoreFourOfAKind(numbers_list, possible):
    temp = 0
    if possible[7] == False:
        temp = 0
    else:
        for x in numbers_list:
            temp += x
    score[7] = temp
    done[7] = True
    rolled = False
    game_loop(3)   

def ScoreFullHouse(numbers_list, possible):
    temp = 0
    if possible[8] == False:
        temp = 0
    else:
        temp = 25
    score[8] = temp
    done[8] = True
    rolled = False
    game_loop(3)   

def ScoreSmStraight(numbers_list, possible):
    temp = 0
    if possible[9] == False:
        temp = 0
    else:
        temp = 30
    score[9] = temp
    done[9] = True
    rolled = False
    game_loop(3)   

def ScoreLgStraight(numbers_list, possible):
    temp = 0
    if possible[10] == False:
        temp = 0
    else:
        temp = 40
    score[10] = temp
    done[10] = True
    rolled = False
    game_loop(3)   

def ScoreYahtzee(numbers_list, possible):
    temp = 0
    if possible[11] == False:
        temp = 0
    else:
        temp = 50
    score[11] = temp
    done[11] = True
    rolled = False
    game_loop(3)   

def ScoreChance(numbers_list, possible):
    temp = 0
    if possible[12] == False:
        temp = 0
    else:
        for x in numbers_list:
            temp += x
    score[12] = temp
    done[12] = True
    rolled = False
    game_loop(3)   

def accepted():
    while True:
        mouse = pygame.mouse.get_pos()

        possible_real = possible
        done_real = done

        timer.tick(fps)
        screen.fill(background)
        
        draw_stuff(0)
        draw_dice(numbers_list)   
        draw_scoreCard(selected_choice, possible_real, done_real)   
        if done[0] != True:
            aces = scoreButton(157, 203, 68, 25, white, green, "Aces")
        if done[1] != True:
            twos = scoreButton(157, 233, 68, 25, white, green, "Twos")
        if done[2] != True:
            threes = scoreButton(157, 263, 68, 25, white, green, "Threes")
        if done[3] != True:
            fours = scoreButton(157, 293, 68, 25, white, green, "Fours")
        if done[4] != True:
            fives = scoreButton(157, 323, 68, 25, white, green, "Fives")
        if done[5] != True:
            sixes = scoreButton(157, 353, 68, 25, white, green, "Sixes")
        if done[6] != True:
            threeOfAKind = scoreButton(157, 473, 68, 25, white, green, "3ofAKind")
        if done[7] != True:
            fourOfAKind = scoreButton(157, 503, 68, 25, white, green, "4ofAKind")
        if done[8] != True:
            fullHouse = scoreButton(157, 533, 68, 25, white, green, "FullHouse")
        if done[9] != True:
            smStraight = scoreButton(157, 563, 68, 25, white, green, "SmStraight")
        if done[10] != True:
            lgStraight = scoreButton(157, 593, 68, 25, white, green, "LgStraight")
        if done[11] != True:
            yahtzee = scoreButton(157, 623, 68, 25, white, green, "YAHTZEE")
        if done[12] != True:
            chance = scoreButton(157, 653, 68, 25, white, green, "Chance")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.flip()

#Draws scorecard outline + buttons
def draw_stuff(rolls_left):
    rolls_text = font.render("Rolls Left: " + str(rolls_left), True, white)
    screen.blit(rolls_text, (15, 15))
    pygame.draw.rect(screen, white, [0, 200, 225, HEIGHT - 200])
    pygame.draw.line(screen, black, (0, 40), (WIDTH, 40), 3)
    pygame.draw.line(screen, black, (0, 200), (WIDTH, 200), 5)
    pygame.draw.line(screen, black, (155, 200), (155, HEIGHT), 3)
    pygame.draw.line(screen, black, (225, 200), (225, HEIGHT), 3)
    
##Class for die, includes draw function used to draw each die 1-6.
class Dice:
    def __init__(self, x_pos, y_pos, number, key):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.number = number
        self.key = key
        self.die = ''
    ##Draw function that draws each die.    
    def draw(self):
        self.die = pygame.draw.rect(screen, white, [self.x_pos, self.y_pos, 100, 100], 0, 5)
        if self.number == 1:
            pygame.draw.circle(screen, black, (self.x_pos + 50, self.y_pos + 50), 10)
        if self.number == 2:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 3:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 4:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 20), 10)
        if self.number == 5:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 20), 10)    
        if self.number == 6:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 20), 10)

##Class for choice, draws table for choices and text for each choice.
class Choice:
    def __init__(self, x_pos, y_pos, text, select, possible, done):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.select = select
        self.text = text
        self.done = done
        self.possible = possible
        
    def draw(self):
        pygame.draw.line(screen, black, (self.x_pos, self.y_pos), (self.x_pos + 225, self.y_pos), 5)
        pygame.draw.line(screen, black, (self.x_pos, self.y_pos + 30), (self.x_pos + 225, self.y_pos + 30), 5)
        ##If statement that determines whether die rolled is available to keep
        if not self.done:
            if self.possible:
                my_text = font.render(self.text, True, (34, 140, 34))
            elif not self.possible:
                my_text = font.render(self.text, True, (255, 0, 0))
        else:
            my_text = font.render(self.text, True, black)
        screen.blit(my_text, (self.x_pos + 10, self.y_pos + 5))      
        
def check_possibilities(possible_list, numbers_list):
    ##How does it handle running out of possibliities?
    ##Checks to see if there are any dice that can be kept for each choice
    size = len(numbers_list)
    tempList = numbers_list
    tempList.sort()

    for i in range(0, 5):
        if 1 in numbers_list:
            possible_list[0] = True
        elif 1 not in numbers_list:
            possible_list[0] = False

        if 2 in numbers_list:
            possible_list[1] = True
        elif 2 not in numbers_list:
            possible_list[1] = False

        if 3 in numbers_list:
            possible_list[2] = True
        elif 3 not in numbers_list:
            possible_list[2] = False

        if 4 in numbers_list:
            possible_list[3] = True
        elif 4 not in numbers_list:
            possible_list[3] = False

        if 5 in numbers_list:
            possible_list[4] = True
        elif 5 not in numbers_list:
            possible_list[4] = False

        if 6 in numbers_list:
            possible_list[5] = True
        elif 6 not in numbers_list:
            possible_list[5] = False

        #Three of a Kind
        for i in range(1):
            if (tempList[i] == tempList[i + 2]) or (tempList[i + 1] == tempList[i + 3]) or (tempList[i + 2] == tempList[i + 4]):
                possible_list[6] = True
            else:
                possible_list[6] = False

        #Four of a Kind
        for i in range(1):
            if (tempList[i] == tempList[i + 3] )or (tempList[i + 1] == tempList[i + 4]):
                possible_list[7] = True
            else:
                possible_list[7] = False

        #Full House
        for i in range(1):
            if(tempList[i] == tempList[i + 2] and tempList[i + 3] == tempList[i + 4]) or (tempList[i] == tempList[i + 1] and tempList[i + 2] == tempList[i + 4]):
                possible_list[8] = True
            else:
                possible_list[8] = False

        #Small Straight
        for i in range(1):
            if(tempList[i + 1] == (tempList[i] + 1) and tempList[i + 2] == (tempList[i + 1] + 1) and tempList[i + 3] == (tempList[i + 2] + 1)):
                possible_list[9] = True
            elif(tempList[i + 1] == (tempList[i] + 1) and tempList[i + 2] == (tempList[i + 1] + 1) and tempList[i + 4] == (tempList[i + 2] + 1)):
                possible_list[9] = True
            elif(tempList[i + 1] == (tempList[i] + 1) and tempList[i + 3] == (tempList[i + 1] + 1) and tempList[i + 4] == (tempList[i + 3] + 1)):
                possible_list[9] = True
            elif(tempList[i + 2] == (tempList[i + 1] + 1) and tempList[i + 3] == (tempList[i + 2] + 1) and tempList[i + 4] == (tempList[i + 3] + 1)):
                possible_list[9] = True
            else: 
                possible_list[9] = False

        #Large Straight
        for i in range(1):
            if(tempList[i + 1] == (tempList[i] + 1) and tempList[i + 2] == (tempList[i + 1] + 1) and tempList[i + 3] == (tempList[i + 2] + 1) and tempList[i + 4] == (tempList[ i + 3] + 1)):
                possible_list[10] = True
            else:
                possible_list[10] = False

        #YAHTZEE
        for i in range(1):
            if (tempList[i] == tempList[i + 4] ):
                possible_list[11] = True
            else:
                possible_list[11] = False
        
        #Chance
        if done[12] == False:
            possible_list[12] = True
        else:
            possible_list[12] = False
        
    max_count = 0

    for index in range(1, 7):
        if numbers_list.count(index) > max_count:
            max_count = numbers_list.count(index)
    return possible_list      

def draw_dice(numbers_list):
        die1 = Dice(10, 50, numbers_list[0], 0)
        die2 = Dice(130, 50, numbers_list[1], 1)
        die3 = Dice(250, 50, numbers_list[2], 2)
        die4 = Dice(370, 50, numbers_list[3], 3)
        die5 = Dice(490, 50, numbers_list[4], 4)

        die1.draw()
        die2.draw()
        die3.draw()
        die4.draw()
        die5.draw()

def draw_scoreCard(selected_chioce, possible, done):
    ones = Choice(0, 200, "Ones", selected_choice[0], possible[0], done[0])
    twos = Choice(0, 230, "Twos", selected_choice[1], possible[1], done[1])
    threes = Choice(0, 260, "Threes", selected_choice[2], possible[2], done[2])
    fours = Choice(0, 290, "Fours", selected_choice[3], possible[3], done[3])
    fives = Choice(0, 320, "Fives", selected_choice[4], possible[4], done[4])
    sixes = Choice(0, 350, "Sixes", selected_choice[5], possible[5], done[5])
    upper_total1 = Choice(0, 380, "Total Score", False, False, True)
    upper_bonus = Choice(0, 410, "Bonus if >= 63", False, False, True)
    upper_total2 = Choice(0, 440, "Upper Total", False, False, True)
    three_kind = Choice(0, 470, "Three of a Kind",selected_choice[6], possible[6], done[6])
    four_kind = Choice(0, 500, "Four of a Kind", selected_choice[7], possible[7], done[7])
    full_house = Choice(0, 530, "Full House", selected_choice[8], possible[8], done[8])
    small_straight = Choice(0, 560, "Small Straight",selected_choice[9], possible[9], done[9])
    large_straight = Choice(0, 590, "Large Straight", selected_choice[10], possible[10], done[10])
    yahtzee = Choice(0, 620, "Yahtzee",selected_choice[11], possible[11], done[11])
    chance = Choice(0, 650, "Chance", selected_choice[12], possible[12], done[12])
    yahtzee_bonus = Choice(0, 680, "Yahtzee Bonus", False, False, True)
    lower_total = Choice(0, 710, "Lower Total", False, False, True)
    lower_total2 = Choice(0, 740, "Upper Total", False, False, True)
    grand_total = Choice(0, 770, "Grand Total", False, False, True)
    possible = check_possibilities(possible, numbers_list)

    ones.draw()
    twos.draw()
    threes.draw()
    fours.draw()
    fives.draw()
    sixes.draw()
    upper_total1.draw()
    upper_bonus.draw()
    upper_total2.draw()
    three_kind.draw()
    four_kind.draw()
    full_house.draw()
    small_straight.draw()
    large_straight.draw()
    yahtzee.draw()
    chance.draw()
    yahtzee_bonus.draw()
    lower_total.draw()
    lower_total2.draw()
    grand_total.draw()

def roll_dice(choice):
    for x in range (0, 5):
        if choice[x] == True:
            numbers_list[x] = random.randint(1, 6)
    rolled = True

def choose_dice(x):
    dice_choice[x] = True

def endScore():
    finalScore = 23
    topText = "Final Score"
    bottomText = str(finalScore)

    screen.fill(background)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        wordsOnScreen(topText, midText, 8, 0)
        wordsOnScreen(bottomText, largeText, 4, 0)

        pygame.display.update()
        timer.tick(15)    


##Main Loop
def game_loop(roll):
    rolls_left = roll
    running = True
    dice_choice_real = dice_choice
    while running:
        mouse = pygame.mouse.get_pos()

        numbers_list_real = numbers_list

        selected_choice_real = selected_choice
        possible_real = possible
        done_real = done

        timer.tick(fps)
        screen.fill(background)
        
        draw_stuff(rolls_left)
        draw_dice(numbers_list_real)   
        draw_scoreCard(selected_choice_real, possible_real, done_real)   

        dice_one = diceButton(10, 50, 100, 100, white, green,dice_choice_real,"One")  
        dice_two = diceButton(130, 50, 100, 100, white, green,dice_choice_real,"Two")
        dice_three = diceButton(250, 50, 100, 100, white, green,dice_choice_real,"Three")
        dice_four = diceButton(370, 50, 100, 100, white, green,dice_choice_real,"Four")
        dice_five = diceButton(490, 50, 100, 100, white, green,dice_choice_real,"Five")

        if(rolls_left == 3):
            first_roll = rollButton("Click to Roll", 10, 160, 280, 30, black, green, dice_choice_real, "FirstRoll")
            if first_roll == True:
                rolls_left -= 1 
                dice_choice_real = [False, False, False, False, False]    
        elif(rolls_left < 3 and rolls_left >= 1):
            if True not in dice_choice_real:
                not_selected = rollButton("Choose Dice to Reroll", 10, 160, 280, 30, black, red, dice_choice_real, "Not Selected")
            if True in dice_choice_real:
                roll_again = rollButton("Re-roll Selected Dice", 10, 160, 280, 30, black, green, dice_choice_real, "Reroll")
                if roll_again == True:
                    dice_choice_real = [False,False,False,False,False]
                    rolls_left -= 1
        else:
            no_rolls = menuButton("No Rolls Left", 10, 160, 280, 30, black, red, "Nothing")
        
        if rolls_left == 3:
            accept_button = menuButton("Roll Some Dice", 310, 160, 280, 30, black, red, "Not Selected")
        else:
            accept_button = menuButton("Accept Turn", 310, 160, 280, 30, black, green, "Accepted")

        if False not in done:
            endScore()

        ##Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()  
                        
        pygame.display.flip()

def game_intro():
    topText = "Welcome to"
    bottomText = "YAHTZEE"

    screen.fill(background)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        wordsOnScreen(topText, midText, 8, 0)
        wordsOnScreen(bottomText, largeText, 4, 0)

        mouse = pygame.mouse.get_pos()

        Rules = menuButton("Rules", centered, topMenuButton, menuButtonWidth, menuButtonHeight, black, green, "Rules")
        Play = menuButton("Play", centered, middleMenuButton, menuButtonWidth, menuButtonHeight, black, green, "Play")
        Quit = menuButton("Exit", centered, bottomMenuButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")

        pygame.display.update()
        timer.tick(15)        

game_intro()
pygame.quit()
