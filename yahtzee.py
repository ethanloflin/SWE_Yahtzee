import random
import pygame

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
rolls_left = 50
selected = [False, False, False, False, False]
selected_choice = [True, False, False, False, False, False, False, False, False, False, False, False, False, False]
possible = [False, False, False, False, False, False, False, False, False, False, False, False, False]
done = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
totals = [0, 0, 0, 0, 0, 0, 0]
clicked = -1
current_score = 0


def check_scores(selected_choice, numbers_list, possible, current_score):
    active = 0
    for index in range(len(selected_choice)):
        if selected_choice[index]:
            active = index
    if active == 0:
        current_score = numbers_list.count(1)
    elif active == 1:
        current_score = numbers_list.count(2)
    elif active == 2:
        current_score = numbers_list.count(3)
    elif active == 3:
        current_score = numbers_list.count(4)
    elif active == 4:
        current_score = numbers_list.count(5)
    elif active == 5:
        current_score = numbers_list.count(6)
    elif active == 6 or active == 7:
        if possible[active]:
                current_score = sum(numbers_list)
        else:
                current_score = 0
    elif active == 8:
        if possible[active]:
            current_score = 25
        else:
            current_score = 0
    elif active == 9:
        if possible[active]:
            current_score = 30
        else:
            current_score = 0
    elif active == 10:
        if possible[active]:
            current_score = 40
        else:
            current_score = 0
    elif active == 11:
        if possible[active]:
            current_score = 50
        else:
            current_score = 0
    elif active == 12:
        current_score = sum(numbers_list)
    return current_score

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
    def __init__(self, x_pos, y_pos, num, key):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.number = num
        global selected
        self.key = key
        self.active = selected[self.key]
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
        if self.active:
            pygame.draw.rect(screen, (255, 0, 0), [self.x_pos, self.y_pos, 100, 100], 4, 5)
            
    #Checks if die is clicked & adds to the dice_selected list     
    def check_click(self, coordinates):
        if self.die.collidepoint(coordinates):
            if selected[self.key]:
                selected[self.key] = False
            elif not selected[self.key]:
                selected[self.key] = True
##Class for choice, draws table for choices and text for each choice.
class Choice:
    def __init__(self, x_pos, y_pos, text, select, possible, done, score):
        global selected_choice
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.select = select
        self.text = text
        self.done = done
        self.possible = possible
        self.score = score
        
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
        if self.select:
            pygame.draw.rect(screen, (20, 35, 30), [self.x_pos, self.y_pos, 155, 30])
        screen.blit(my_text, (self.x_pos + 10, self.y_pos + 5))
        score_text = font.render(str(self.score), True, (0, 0, 255))
        screen.blit(score_text, (self.x_pos + 165, self.y_pos + 10))
        
    def check_click(self, coordinates):
        if self.die.collidepoint(coordinates):
            if selected[self.key]:
                selected[self.key] = False
        elif not selected[self.key]:
            selected[self.key] = True
        
        
def check_possibilities(possible_list, numbers_list):
    ##How does it handle running out of possibliities?
    ##Checks to see if there are any dice that can be kept for each choice
    possible_list[0] = True
    possible_list[1] = True
    possible_list[2] = True
    possible_list[3] = True
    possible_list[4] = True
    possible_list[5] = True
    possible_list[6] = True
    possible_list[7] = True
    possible_list[8] = True
    possible_list[9] = True
    possible_list[10] = True
    possible_list[11] = True
    possible_list[12] = True
    max_count = 0
    ##Max_count is a variable to check for 3, 4, or 5 of a kind.
    for index in range(1, 7):
        if numbers_list.count(index) > max_count:
            max_count = numbers_list.count(index)
    ##Lines 125-148 check for 3, 4, or 5 of a kind
    if max_count >=3:
        possible_list[6] = True
        if max_count >=4:
            possible_list[7] = True
            if max_count >= 5:
                possible_list[11] = True
    
    if max_count < 3:
        possible_list[6] = False
        possible_list[7] = False
        possible_list[8] = False
        possible_list[11] = False
    elif max_count == 3:
        possible_list[7] = False
        possible_list[11] = False
        checker = False
        for index in range(len(numbers_list)):
            if numbers_list.count(numbers_list[index]) == 2:
                possible_list[8] = True
                checker = True
        if not checker:
            possible_list[8] = False
    elif max_count == 4:
        possible_list[11] = False
        
    lowest = 10
    highest = 0
    for index in range(len(numbers_list)):
        if numbers_list[index] < lowest:
            lowest = numbers_list[index]
        if numbers_list[index] > highest:
            highest = numbers_list[index]
    
    if (lowest + 1 in numbers_list) and (lowest + 2 in numbers_list) and (lowest+3 in numbers_list) and (lowest+4 in numbers_list):
        possible_list[10] = True
    else:
        possible_list[10] = False
        
    if ((lowest + 1 in numbers_list) and (lowest + 2 in numbers_list) and (lowest+3 in numbers_list)) or ((highest - 1 in numbers_list) and (highest - 2 in numbers_list) and (highest-3 in numbers_list)):
        possible_list[9] = True
    else:
        possible_list[9] = False    
        
    return possible_list
        
def make_choice(clicked_num, selected, done_list):
    for index in range(len(selected)):
        selected[index] = False
    if not done_list[clicked_num]:
        selected[clicked_num] = True
    return selected
      
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
    
    
    ones = Choice(0, 200, "Ones", selected_choice[0], possible[0], done[0], score[0])
    twos = Choice(0, 230, "Twos", selected_choice[1], possible[1], done[1], score[1])
    threes = Choice(0, 260, "Threes", selected_choice[2], possible[2], done[2], score[2])
    fours = Choice(0, 290, "Fours", selected_choice[3], possible[3], done[3], score[3])
    fives = Choice(0, 320, "Fives", selected_choice[4], possible[4], done[4], score[4])
    sixes = Choice(0, 350, "Sixes", selected_choice[5], possible[5], done[5], score[5])
    upper_total1 = Choice(0, 380, "Total Score", False, False, True, totals[0])
    upper_bonus = Choice(0, 410, "Bonus if >= 63", False, False, True, totals[1])
    upper_total2 = Choice(0, 440, "Upper Total", False, False, True, totals[2])
    three_kind = Choice(0, 470, "Three of a Kind",selected_choice[6], possible[6], done[6], score[6])
    four_kind = Choice(0, 500, "Four of a Kind", selected_choice[7], possible[7], done[7],  score[7])
    full_house = Choice(0, 530, "Full House", selected_choice[8], possible[8], done[8], score[8])
    small_straight = Choice(0, 560, "Small Straight",selected_choice[9], possible[9], done[9], score[9])
    large_straight = Choice(0, 590, "Large Straight", selected_choice[10], possible[10], done[10], score[10])
    yahtzee = Choice(0, 620, "Yahtzee",selected_choice[11], possible[11], done[11], score[11])
    chance = Choice(0, 650, "Chance", selected_choice[12], possible[12], done[12], score[12])
    yahtzee_bonus = Choice(0, 680, "Yahtzee Bonus", False, False, True, totals[3])
    lower_total = Choice(0, 710, "Lower Total", False, False, True, totals[4])
    lower_total2 = Choice(0, 740, "Upper Total", False, False, True, totals[5])
    grand_total = Choice(0, 770, "Grand Total", False, False, True, totals[6])
    possible = check_possibilities(possible, numbers_list)
    current_score = check_scores(selected_choice, numbers_list, possible, score)
    
    
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            die1.check_click(event.pos)
            die2.check_click(event.pos)
            die3.check_click(event.pos)
            die4.check_click(event.pos)
            die5.check_click(event.pos)
            if 0 <= event.pos[0] <= 155:
                if 200 <= event.pos[1] <= 380  or 470 <= event.pos[1] <= 680:
                    if 200 < event.pos[1] < 230:
                        clicked = 0
                    if 230 < event.pos[1] < 260:
                        clicked = 1
                    if 260 < event.pos[1] < 290:
                        clicked = 2
                    if 290 < event.pos[1] < 320:
                        clicked = 3
                    if 320 < event.pos[1] < 350:
                        clicked = 4
                    if 350 < event.pos[1] < 380:
                        clicked = 5
                    if 470 < event.pos[1] < 500:
                        clicked = 6
                    if 500 < event.pos[1] < 530:
                        clicked = 7
                    if 530 < event.pos[1] < 560:
                        clicked = 8
                    if 560 < event.pos[1] < 590:
                        clicked = 9
                    if 590 < event.pos[1] < 620:
                        clicked = 10
                    if 620 < event.pos[1] < 650:
                        clicked = 11
                    if 650 < event.pos[1] < 680:
                        clicked = 12
                    selected_choice = make_choice(clicked, selected_choice, done)

        ##Button rolls dice if clicked
            if roll_button.collidepoint(event.pos) and rolls_left > 0:
                roll = True
                rolls_left -= 1
                
    ##Resets roll to false
    if roll:
        for number in range(len(numbers_list)):
            if not selected[number]:
                numbers_list[number] = random.randint(1, 6)
        roll = False




    if False not in done:
        game_over = True        
        
           
    pygame.display.flip()
pygame.quit()