
import random
import pygame
import math
from pygame import mixer

pygame.init()
mixer.init()

# create the screen
screen=pygame.display.set_mode((800,600))
#icon and title
pygame.display.set_caption("pokecapture")
icon=pygame.image.load("C:\\users\\khuhan rawat\\Desktop\\pokemon\\pokeball.png")
pygame.display.set_icon(icon)

#background
bg=pygame.image.load("C:\\users\\khuhan rawat\\Desktop\\pokemon\\bg1.png")

# player
pokeball=pygame.image.load("C:\\users\\khuhan rawat\\Desktop\\pokemon\\pokeball.png")
playerImg=pokeball
playerX=374
playerY=536
playerX_change=0
def player(x,y):
    screen.blit(playerImg,(x,y))
#sound
mixer.music.load("C:\\users\\khuhan rawat\\Desktop\\pokemon\\bgsound.wav")
mixer.music.play(-1)
 #score
score=0
font=pygame.font.SysFont('inkfree.ttf',40)
textX=10
textY=10

def show_score():
    score1=font.render('SCORE:'+str(score),True, (0,0,0))
    screen.blit(score1,(30,30))
#pokemons
bullbasaur=pygame.image.load("C:\\users\\khuhan rawat\\Desktop\\pokemon\\bullbasaur.png")
charmander=pygame.image.load("C:\\users\\khuhan rawat\\Desktop\\pokemon\\charmander.png")
dratini=pygame.image.load("C:\\users\\khuhan rawat\\Desktop\\pokemon\\dratini.png")
eevee=pygame.image.load("C:\\users\\khuhan rawat\\Desktop\\pokemon\\eevee.png")
jigglypuff=pygame.image.load("C:\\users\\khuhan rawat\\Desktop\\pokemon\\jigglypuff.png")
meowth=pygame.image.load("C:\\users\\khuhan rawat\\Desktop\\pokemon\\meowth (2).png")
pikachu=pygame.image.load("C:\\users\\khuhan rawat\\Desktop\\pokemon\\pikachu.png")
psyduck=pygame.image.load("C:\\users\\khuhan rawat\\Desktop\\pokemon\\psyduck.png")
snorlax=pygame.image.load("C:\\users\\khuhan rawat\\Desktop\\pokemon\\snorlax.png")
squirtle=pygame.image.load("C:\\users\\khuhan rawat\\Desktop\\pokemon\\squirtle.png")
poke=[bullbasaur,charmander,dratini,eevee,jigglypuff,meowth,pikachu,psyduck,snorlax,squirtle]

pokeImg=[meowth,pikachu]
pokeX=[]
pokeY=[]
pokeY_change=[1,1]
for i in range(8):
    n=random.randint(0,9)
    poke1=poke[n]
    pokeImg.append(poke1)
    pokeX.append(random.randint(0,768))
    pokeY.append(random.randint(-80,400))
    
    pokeY_change.append(1)
for i in range (2):
    pokeX.append(random.randint(0,768))
    pokeY.append(random.randint(-80,400))
def pokemon(x,y,i,l):
    screen.blit(l[i],(x,y))
#collision
def collision(x,y,playerX,playerY):
    dist=math.sqrt((math.pow(x-playerX,2))+(math.pow(y-playerY,2)))
    if dist<=27:
        return True

#game over
over_font=pygame.font.SysFont('inkfree.ttf',60)
def gameover():
    overtext=over_font.render("GAME OVER",True,(0,0,0))
    screen.blit(overtext,(190,300))
    screen.blit(pokeball,(130,400))
#game loop

running=True
while running:
    
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    for event in pygame.event.get():        
        if event.type==pygame.QUIT:
            running=False
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
            playerX_change=-3
        if event.key==pygame.K_RIGHT:
            playerX_change=3
    if event.type==pygame.KEYUP:
        playerX_change=0
        
    playerX+=playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    player(playerX,playerY)
#show score
    
    for i in range(10):
        pokeY[i]+=pokeY_change[i]
        
        pokemon(pokeX[i],pokeY[i],i,pokeImg)
        col=collision(pokeX[i],pokeY[i],playerX,playerY)

        if pokeY[i]>=600:
            pokeY[i]=random.randint(-20,40)
            pokeX[i]=random.randint(0,768)
        if col:
            char=pokeImg[i]
            if char==pikachu:
                np=random.randint(0,9)
                pokeX[i]=random.randint(0,736)
                pokeY[i]=random.randint(0,40)
                pokemon(pokeX[i],pokeY[i],np,poke)
                cap=mixer.Sound("C:\\users\\khuhan rawat\\Desktop\\pokemon\\capture.wav")
                cap.play()
                score+=5
            elif char==meowth:
                for i in range(10):
                    screen.fill((34,34,34))
                    gameover()
                
                running=False
            else:
                np=random.randint(0,9)
                pokeX[i]=random.randint(0,736)
                pokeY[i]=random.randint(0,40)
                pokemon(pokeX[i],pokeY[i],np,poke)
                cap=mixer.Sound("C:\\users\\khuhan rawat\\Desktop\\pokemon\\capture.wav")
                cap.play()
                
            score+=5
            np=random.randint(0,9)
            pokeX[i]=random.randint(0,736)
            pokeY[i]=random.randint(0,40)
            pokemon(pokeX[i],pokeY[i],np,poke)
            cap=mixer.Sound("C:\\users\\khuhan rawat\\Desktop\\pokemon\\capture.wav")
            cap.play()
            
    show_score()


#Run=True

    

    pygame.display.update()
