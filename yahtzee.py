import random
import pygame
from Scoring import *


pygame.init()
##Initializes screen, sets size, caption, timer, font, and colors. 
##Also creates variables for white and black.
WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Yahtzee")
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 18)
background = (128, 128, 128)
white = (255, 255, 255)
black = (0, 0, 0)
numbers_list = [0, 0, 0, 0, 0,]
roll = False
rolls_left = 3
selected_choice = [True, False, False, False, False, False, False, False, False, False, False, False, False, False]
possible = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
done = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

#Draws scorecard outline + buttons
def draw_stuff():
    roll_text = font.render("Click To Roll", True, white)
    screen.blit(roll_text, (100, 167))
    accept_text = font.render("Accept Turn", True, white)
    screen.blit(accept_text, (400, 167))
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
        
#Score class is to draw score of PlayerScoreCard results
class Score:
    def __init__(self, x_pos, y_pos, text):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = text

    def draw(self):
        my_text = font.render(self.text, True, black)
        
def check_possibilities(possible_list, numbers_list):
    ##How does it handle running out of possibliities?
    ##Checks to see if there are any dice that can be kept for each choice
    for i in range(0, 5):
        if numbers_list[i] == 1:
            possible_list[0] = True
        if numbers_list[i] == 2:
            possible_list[1] = True
        if numbers_list[i] == 3:
            possible_list[2] = True
        if numbers_list[i] == 4:
            possible_list[3] = True
        if numbers_list[i] == 5:
            possible_list[4] = True
        if numbers_list[i] == 6:
            possible_list[5] = True
    max_count = 0
    
    for index in range(1, 7):
        if numbers_list.count(index) > max_count:
            max_count = numbers_list.count(index)
    return possible_list
    
Player = PlayerScoreCard
Player.InitiateScores(Player)
        

##Main Loop
running = True
while running:
    timer.tick(fps)
    screen.fill(background)
    
    ##Draws 5 Die at top of screen
    die1 = Dice(10, 50, numbers_list[0], 0)
    die2 = Dice(130, 50, numbers_list[1], 1)
    die3 = Dice(250, 50, numbers_list[2], 2)
    die4 = Dice(370, 50, numbers_list[3], 3)
    die5 = Dice(490, 50, numbers_list[4], 4)
    
    
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
    
    roll_button = pygame.draw.rect(screen, black, [10, 160, 280, 30])
    accept_button = pygame.draw.rect(screen, black, [310, 160, 280, 30])
    
    draw_stuff()

    die1.draw()
    die2.draw()
    die3.draw()
    die4.draw()
    die5.draw()
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
    
    
    
    
    ##Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        ##Button rolls dice if clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            if roll_button.collidepoint(event.pos) and rolls_left > 0:
                roll = True
                rolls_left -= 1
            if accept_button.collidepoint(event.pos):
                ChooseScoringOption(Player, numbers_list)

    ##Resets roll to false
    if roll: 
        for number in range(len(numbers_list)):
            numbers_list[number] = random.randint(1, 6)
        roll = False      
    
           
    pygame.display.flip()
pygame.quit()