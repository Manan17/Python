import random
import pygame
import sys
from pygame.locals import *

#Global Variables as constant

FPS = 32
SCREEN_WIDTH = 289
SCREEN_HEIGHT = 511
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
GROUNDY = SCREEN_HEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/bird.png'
BACKGROUND = 'gallery/sprites/background.png'
PIPE = 'gallery/sprites/pipe.png'

def welcomeScreen():

    playerx = int(SCREEN_WIDTH/5)
    playery = int((SCREEN_HEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREEN_WIDTH-GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREEN_HEIGHT*0.13)
    basex = 0
    
    while True:
        for event in pygame.event.get():
            key = pygame.key.get_pressed()        
            if event.type == QUIT or key[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

            elif key[pygame.K_SPACE] or key[pygame.K_UP]:
                return

            else:
                SCREEN.blit(GAME_SPRITES['background'],(0,0))
                SCREEN.blit(GAME_SPRITES['message'],(messagex,messagey))
                SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))
                SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)
        pygame.event.pump()

    pass



def mainGame():
    score = 0
    playerx = int(SCREEN_WIDTH/5)
    playery = int(SCREEN_WIDTH/2)
    basex = 0

    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    #Upper Pipes
    upperPipes = [
        {'x' : SCREEN_WIDTH+200 , 'y' : newPipe1[0]['y']},
        {'x' : SCREEN_WIDTH+200 + (SCREEN_WIDTH/2) , 'y' : newPipe2[0]['y']}
    ]

    #Lower Pipes
    lowerPipes = [
        {'x' : SCREEN_WIDTH+200 , 'y' : newPipe1[1]['y']},
        {'x' : SCREEN_WIDTH+200 + (SCREEN_WIDTH/2) , 'y' : newPipe2[1]['y']}
    ]


    pipeVelX = -4
    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1
    playerFlappV = -8
    playerFlapped = False

    while True:

        for event in pygame.event.get():
            key = pygame.key.get_pressed()        
            if event.type == QUIT or key[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

            elif key[pygame.K_SPACE] or key[pygame.K_UP]:
                if playery > 0:
                    playerVelY = playerFlappV
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()
            pygame.event.pump()
        crashTest = isCollide(playerx,playery,upperPipes,lowerPipes)

        if crashTest:
            return



        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score +=1
                print("Your score is ",score)
                GAME_SOUNDS['point'].play()

        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False

        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery + min(playerVelY, GROUNDY - playerHeight - playery)
        
        for upperPipe , lowerPipe in zip(upperPipes,lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX


        if 0<upperPipes[0]['x']<5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])


        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)



        SCREEN.blit(GAME_SPRITES['background'],(0,0))
        for upperPipe , lowerPipe in zip(upperPipes,lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'],upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'],lowerPipe['y']))
            
        SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))

        myDigits = [int(x) for x in list(str(score))]
        width = 0 
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset  = (SCREEN_WIDTH - width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit],(Xoffset,SCREEN_HEIGHT*0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)



def getRandomPipe():
    pipeheight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREEN_HEIGHT/6
    y2 = offset + random.randrange(0, int(SCREEN_HEIGHT - GAME_SPRITES['base'].get_height() - 1.2* offset))
    pipex = SCREEN_WIDTH+10
    y1 = pipeheight - y2 + offset
    pipe = [
        {
            'x' : pipex , 
            'y' : -y1
        },
        {
            'x' : pipex , 
            'y' : y2
        }
    ]
    return pipe

def isCollide(playerx,playery,upperPipes,lowerPipes):
    if playery < 0 or playery > GROUNDY - 25:
        GAME_SOUNDS['hit'].play()
        return True

    for pipe in upperPipes:
        pipeheight = GAME_SPRITES['pipe'][0].get_height()
        if playery < pipeheight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUNDS['hit'].play()
            return True

    for pipe in lowerPipes:
        if playery + GAME_SPRITES['player'].get_height() > pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUNDS['hit'].play()
            return True
    return False

if __name__ == "__main__":
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird By Manan')
    GAME_SPRITES['numbers']=(
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )


    GAME_SPRITES['message']= pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['base']= pygame.image.load('gallery/sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe']=(
     pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
     pygame.image.load(PIPE).convert_alpha()
    )

    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen()
        mainGame()
