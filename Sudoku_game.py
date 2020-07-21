# import Libraries

import pygame
import pygame.key
from Main import game_main
from NewBoard import NewBoard
display = [True,False]

#Initialise The game
pygame.init()
game = game_main()
newboard = NewBoard()
screen = pygame.display.set_mode((940,1000))
#Load Images and sound and shape
import time
font = pygame.font.Font(None, 50)

def solve(i = 0,j = 0):
    if i == 9 and j == 0 :
        return 1

    if shed[i,j] == 0:
        for k in range (1,10):
            if (
                    k not in Board[:,j] and
                    k not in Board[i,:] and
                    k not in Board[i//3 *3 :i//3 * 3 +3,j//3 * 3:j//3 * 3 +3]
            ):
                Board[i,j] = k
                screen.fill((255,255,255))
                display_Board()
                pygame.display.flip()
                if j < 8 :
                   c =  solve(i,j+1)
                   if c == 1:
                       return 1
                   else:
                       Board[i,j] = 0
                else :
                   c = solve(i+1,0)
                   if c == 1:
                       return 1
                   else:
                       Board[i,j] = 0


    else:
        if j < 8:
            c = solve(i, j + 1)
            if c == 1:
                return 1
        else :
            c = solve(i + 1, 0)
            if c == 1:
                return 1

    if Board[i,j] == 0 :
        return 0

    return 0

def solve_Check():
    for i in range(0,9) :
        for j in range(0,9):
            k = board[i][j]
            if k != 0 :
                board[i,j] = 0
                if (
                        k not in board[:,j] and
                        k not in board[i,:] and
                        k not in board[i//3 *3 :i//3 * 3 +3,j//3 * 3:j//3 * 3 +3]
                ):
                    board[i][j] = k
                    continue
                else:
                    board[i][j] = k
                    return  0
    return 1

class button :
    def __init__(self , text = "" ,position = (0,0), width = 0  , height = 0,color = (0,0,0)):
        self.text = text
        self.position = position
        self.width = width
        self.height = height
        self.color = color
        rect = pygame.draw.rect(screen ,color,(self.position[0],self.position[1],self.width,self.height),5)
        screen.fill(color,rect)
        self.display()
    def display(self):
        if len(self.text):
            font = pygame.font.Font(None, 48)
            survivedtext = font.render(str(self.text), True, (255,255,255))
            textRect = survivedtext.get_rect()
            x,y = self.position
            textRect.center = [int(x + self.width/2),int(y + self.height/2)]
            screen.blit(survivedtext, textRect)

    def click(self,pos):
                x,y = pos
                if (
                    x > self.position[0] and x < (self.position[0] + self.width) and
                    y > self.position[1] and y < (self.position[1] + self.height)
                ):
                    return  True
                else:
                    return False

def CurrentStatus():
    global Green
    font = pygame.font.Font(None, 48)
    if input :
        if solve_Check() == 1:
            survivedtext = font.render("KEEP GOING", True, (0, 255, 0))
            Green = True
        else:
            survivedtext = font.render("THIS SUDUKO IS INVALID", True, (0, 0, 0))
            Green = False
    else:
        if Green :
            survivedtext = font.render("KEEP GOING", True, (0, 255, 0))
        else :
            survivedtext = font.render("THIS SUDUKO IS INVALID", True, (255, 0, 0))
    textRect = survivedtext.get_rect()
    textRect.center = [475, 25]
    screen.blit(survivedtext, textRect)

def display_Board():
    space_i = 0
    for i in range(9):
        if i % 3 == 0:
            space_i += 1
        space_j = 0
        for j in range (9) :
            if j % 3 == 0 :
                space_j += 1
            pos = (i*100 + space_i * 10, j*100 + space_j * 10 + 30 ,100,100)
            pygame.draw.rect(screen,(0,0,0),pos,5)
            if Board[j][i] != 0 :
                if shed[j][i] == 0 :
                    survivedtext = font.render(str(Board[j][i]),True, (150,150,150))
                else:
                    survivedtext = font.render(str(Board[j][i]),True, (0, 0, 0))
                textRect = survivedtext.get_rect()
                textRect.center = [i*100 + space_i * 10 + 50, j*100 + space_j * 10 + 80]
                # pos = (i * 100 + space_i * 10 + 10 , j * 100 + space_j * 10 + 10  , 80, 80)
                # pygame.draw.rect(screen, (0, 0, 0), pos, 5)
                screen.blit(survivedtext, textRect)



#Kepp looping
clicked = False
cords = (0,0,0,0)
p,q = 0 ,0
number = 0
number_pass = False
Enter = False
wrong = True
push = True
input = True
create = False
Green = True
replay = 0
while 1 :
    screen.fill((255,255,255))

    if display[0] :
        Button1 = button("PLAY",(400,300),200,100)
        Button2 = button("Create",(400,500),200,100)
    elif display[1] :
        Button3 = button("<-", (0, 0), 60, 30)
        display_Board()
    if create :
        board[:,:] = Board[:,:]
        CurrentStatus()
        input = False

    if clicked :
        pygame.draw.rect(screen, 255, cords, 5)
    if Enter :
        if wrong :
            survivedtext = font.render("Not the correct matrix", True, (255, 0, 0))

        elif not wrong:
            survivedtext = font.render("Congratulation", True, (0, 255, 0))

        textRect = survivedtext.get_rect()
        textRect.center = [475, 470]
        screen.fill(0)
        screen.blit(survivedtext, textRect)
        pygame.display.flip()
        pygame.time.delay(2000)
        Enter = False


    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            if display[0]:
                if Button1.click(pygame.mouse.get_pos()):
                    survivedtext = font.render("PLEASE WAIT . WE ARE LOADNG YOUR GAME", True, (0, 0, 255))
                    textRect = survivedtext.get_rect()
                    textRect.center = [475, 470]
                    screen.fill(0)
                    screen.blit(survivedtext, textRect)
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    [board,Board,shed] = game.gen()
                    screen.fill((255,255,255))
                    display[0] = False
                    display[1] = True

                if Button2.click(pygame.mouse.get_pos()):

                    [newBoard, Board, shed, board] =newboard.plain_board()
                    screen.fill((255,255,255))
                    create = True
                    display[0] = False
                    display[1] = True
            elif display[1] :
                if Button3.click(pygame.mouse.get_pos()):
                    display[0] = True
                    display[1] = False
                    clicked = False
                    continue
                clicked = True
                Enter = False
                x,y = pygame.mouse.get_pos()
                x,y = x - x//300 * 10 , y - y//300 * 10
                cords = (x//100 * 100 + x//300 * 10  + 10, y//100 *100 + y//300 * 10 + 40 , 100 ,100)
                p = x//100
                q = y//100


        if clicked :
            if event.type == pygame.KEYUP:
                input = True
                if event.key == pygame.K_BACKSPACE:
                    if shed[q][p] == 0 or create:
                        Board[q][p] = 0
                elif event.key == pygame.K_1:
                    if shed[q][p] == 0 or create:
                        Board[q][p] = 1
                elif event.key == pygame.K_2:
                    if shed[q][p] == 0 or create:
                        Board[q][p] = 2
                elif event.key == pygame.K_3:
                    if shed[q][p] == 0 or create:
                        Board[q][p] = 3
                elif event.key == pygame.K_4:
                    if shed[q][p] == 0 or create:
                        Board[q][p] = 4
                elif event.key == pygame.K_5:
                    if shed[q][p] == 0 or create:
                        Board[q][p] = 5
                elif event.key == pygame.K_6:
                    if shed[q][p] == 0 or create:
                        Board[q][p] = 6
                elif event.key == pygame.K_7:
                    if shed[q][p] == 0 or create:
                        Board[q][p] = 7
                elif event.key == pygame.K_8:
                    if shed[q][p] == 0 or create:
                        Board[q][p] = 8
                elif event.key == pygame.K_9:
                    if shed[q][p] == 0 or create:
                        Board[q][p] = 9
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN :
                if Board.all() == board.all() :
                    Enter = True
                    wrong = False
                else :
                    Enter = True
                    wrong = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_END :
                if 0 in Board[:,:]:
                    survivedtext = font.render("IF YOU WANNA LEAVE  , YOU CAN LEAVE  ", True, (255,0, 0))
                else :
                    survivedtext = font.render("NICE PLAYING WITH YOU", True, (0,255, 0))
                textRect = survivedtext.get_rect()
                textRect.center = [475, 470]
                screen.fill(0)
                screen.blit(survivedtext, textRect)
                pygame.display.flip()
                pygame.time.delay(3000)
                pygame.quit()
                exit(0)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if not create:
                    survivedtext = font.render("We Are showing you the solution", True, (0, 255, 0))
                    textRect = survivedtext.get_rect()
                    textRect.center = [475, 470]
                    screen.fill(0)
                    screen.blit(survivedtext, textRect)
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    solve()

                else:
                    if solve_Check() == 1:
                        shed[:,:] = Board[:,:]
                        survivedtext = font.render("We Are showing you the solution", True, (0, 255, 0))
                        textRect = survivedtext.get_rect()
                        textRect.center = [475, 470]
                        screen.fill(0)
                        screen.blit(survivedtext, textRect)
                        pygame.display.flip()
                        pygame.time.delay(1000)
                        solve()
                    else:
                        survivedtext = font.render("DO NOT PLAY SMART", True, (255,0, 0))
                        textRect = survivedtext.get_rect()
                        textRect.center = [475, 470]
                        screen.fill(0)
                        screen.blit(survivedtext, textRect)
                        pygame.display.flip()
                        pygame.time.delay(2000)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    pygame.display.flip()

