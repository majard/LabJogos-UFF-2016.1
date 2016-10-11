from PPlay.gameimage import *
from PPlay.sprite import *
from random import randint
from cfg import screen, kb, hero,width,height, hists, dialog, player, cities, currentCity, currentEnemy
import cfg
from fighting import movingBattle, drawing, updating, heroPos

def setDialogPosition(spr):
    spr.set_position(screen.width /2 - spr.width/2, screen.height - spr.height)

def correctPosition(x, y):
    if hero['nDir'] == 1:
        hero['posy'] = y + hero['spr'].height
        hero['posx'] = x
    if hero['nDir'] == 2:
        hero['posx'] = x + hero['spr'].width
        hero['posy'] = y
    if hero['nDir'] == 3:
        hero['posy'] = y - hero['spr'].height
        hero['posx'] = x
    if hero['nDir'] == 4:
        hero['posx'] = x - hero['spr'].width
        hero['posy'] = y

def checkBattle(enemy, hero):
    if hero['spr'].collided_perfect(enemy):
        hero['posx'] = randint(0, width/2)
        hero['posy'] = randint(0, height)
        player['isInTown'] = False
        player['isInBattle'] = True
        path = cities[currentCity['name']]['path']
        image = 'Resources/' + path + 'bg.png'
        cfg.bg = GameImage(image)


def checkingMenu():
    if kb.key_pressed('esc'):
        player['hasPaused'] = True


def collisionTreatment(spr, x, y, house1, house2, npc1, npc2, path):
    #there was a bug with collided perfect with house1, this was a workaround
    if house1.x <= spr.x  and spr.x <= house1.x + house1.width \
            and house1.y <= spr.y + spr.height and spr.y + 10 <= house1.y + house1.height:
        correctPosition(x, y)

    if spr.collided_perfect(npc1):

        dialog['spr'] = Sprite('dialogs/' + path + 'npc1_1.png')
        dialog['n'] = 1

        setDialogPosition(dialog['spr'])
        correctPosition(x, y)

    if spr.collided_perfect(npc2):
        dialog['spr'] = Sprite('dialogs/' + path + 'npc2_1.png')
        dialog['n'] = 2

        setDialogPosition(dialog['spr'])
        correctPosition(x, y)

    if spr.collided_perfect(house2):
        correctPosition(x, y)



def town():

    path = cities[currentCity['name']]['path']
    house = 'Resources/' + path + 'house.png'
    image = 'Resources/'+ path + 'bg.png'
    if currentCity['name'] != 'kingsia':
        char1 = 'characters/NPCS/' + cities[currentCity['name']]['char1']
        char2 = 'characters/NPCS/' + cities[currentCity['name']]['char2']
        npc1 = Sprite(char1)
        npc2 = Sprite(char2)

    else:
        if 'jinnyx' not in hero['isDead']:
            npc1 = Sprite(cfg.enemies['jinnyx']['imgs'][0], 1)
        else:
            npc1 = Sprite('characters/NPCS/old man.gif')
        if 'pennae' not in hero['isDead']:
            npc2 = Sprite(cfg.enemies['pennae']['imgs'][0], 1)
        else:
            npc2 = Sprite('characters/NPCS/old woman.gif')

    cfg.bg = GameImage(image)

    house1 = Sprite(house)
    house2 = Sprite(house)
    enemy = Sprite(cfg.currentEnemy['imgs'][0], 1)

    agility = hero['agility']
    hero['agility'] = 3000  #updates agility to move faster

    house1.set_position(20, 20)
    house2.set_position(screen.width - house1.width - 20 , 20)
    npc1.set_position(house1.x, house1.y + house1.height + npc1.height )
    npc2.set_position(house2.x + house2.width - npc2.width, house2.y + house2.height + npc2.height)
    enemy.set_position(300, 100)

    lastX = hero['posx']
    lastY = hero['posy']

    house1.draw()
    house2.draw()
    npc1.draw()
    npc2.draw()
    enemy.draw()

    drawing(hero)
    checkBattle(enemy, hero)
    movingBattle()
    heroPos(hero)
    updating(hero)
    collisionTreatment(hero['spr'], lastX, lastY, house1, house2, npc1, npc2, path)

    if dialog['n'] != 0:
        dialog['spr'].draw()

    if kb.key_pressed('enter'):
        if dialog['n'] == 1 and currentCity['name'] != 'kingsia':
            dialog['n'] = 2
            dialog['spr'] = Sprite('dialogs/' + path + 'npc1_2.png')
            setDialogPosition(dialog['spr'])
        else:
            dialog['n'] = 0

    checkingMenu()
    screen.update()


    hero['agility'] = agility
    hero['health'] = hero['maxHealth']



