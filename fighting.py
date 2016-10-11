from PPlay.sprite import *
from random import randint, random
from cfg import *
import cfg

#Drawing the sprite--------------------------------------------------------------------------------------------
def drawing(spr):
    spr['spr'].set_position(spr['posx'],spr['posy'])
    spr['spr'].draw()

#Limiting sprite's movement------------------------------------------------------------------------------------
def heroPos(spr):
    if spr['posx'] < 0:
        spr['posx'] = 0
    elif spr['posx'] > width-spr['spr'].width:
        spr['posx'] = width-spr['spr'].width
    if spr['posy'] < 0:
        spr['posy'] = 0
    elif spr['posy'] > height-spr['spr'].height:
        spr['posy'] = height-spr['spr'].height

#Updating sprite's animation----------------------------------------------------------------------------------
def updating(spr):
    if spr['nAnim'] in [1,2,3,4,5,6,7,8]:
        spr['spr'].set_total_duration(spr['duration'])
        spr['spr'].update()

#Only moving the sprite through the screen--------------------------------------------------------------------
def onlyMoving(hero,kb,screen):
    if not hero['paralyzed']:
        if kb.key_pressed('w'):
            hero['posy'] -= hero['agility'] * screen.delta_time()
        if kb.key_pressed('a'):
            hero['posx'] -= hero['agility'] * screen.delta_time()
        if kb.key_pressed('s'):
            hero['posy'] += hero['agility'] * screen.delta_time()
        if kb.key_pressed('d'):
            hero['posx'] += hero['agility'] * screen.delta_time()

#Moving Sprite in battle and changing animation-------------------------------------------------------------
def movingBattle():
    sideways = False
    onlyMoving(hero,kb,screen)
    if kb.key_pressed('w') or kb.key_pressed('s'):
        if (kb.key_pressed('d') or kb.key_pressed('a')):
            sideways = True
    if kb.key_pressed('w'):
        hero['nDir'] = 1
        if hero['nAnim']!= 1 and not sideways:
            hero['nAnim'] = 1
            hero['spr'] = Sprite(hero['anims'][0],3)
    elif kb.key_pressed('a'):
        hero['nDir'] = 2
        if hero['nAnim'] != 2:
            hero['nAnim'] = 2
            hero['spr'] = Sprite(hero['anims'][2],3)
    elif kb.key_pressed('s'):
        hero['nDir'] = 3
        if hero['nAnim'] != 3 and not sideways:
            hero['nAnim'] = 3
            hero['spr'] = Sprite(hero['anims'][3],3)
    elif kb.key_pressed('d'):
        hero['nDir'] = 4
        if hero['nAnim'] != 4:
            hero['nAnim'] = 4
            hero['spr'] = Sprite(hero['anims'][1],3)
    else:
        if hero['nDir']==1:
            hero['nAnim'] = 10
            hero['spr'] = Sprite(hero['imgs'][1],1)
        elif hero['nDir']==2:
            hero['nAnim'] = 20
            hero['spr'] = Sprite(hero['imgs'][2],1)
        elif hero['nDir']==3:
            hero['nAnim'] = 30
            hero['spr'] = Sprite(hero['imgs'][0],1)
        elif hero['nDir']==4:
            hero['nAnim'] = 40
            hero['spr'] = Sprite(hero['imgs'][3],1)

    return hero['nAnim'],hero['nDir']

#Shooting spells------------------------------------------------------------------------------------------------
def shooting(hero,tm,attack):
    shot = 0
    if hero['mana']>=attack['manaSpent'] and screen.time_elapsed()-tm>=1000:
        if hero['nDir']==1 and kb.key_pressed(attack['key']):
            shot = Sprite(attack['up'])
            shot.set_position(hero['posx'],hero['posy'])
            hero['mana']-=attack['manaSpent']
            tm = screen.time_elapsed()
        elif hero['nDir']==2 and kb.key_pressed(attack['key']):
            shot = Sprite(attack['left'])
            shot.set_position(hero['posx'],hero['posy'])
            hero['mana']-=attack['manaSpent']
            tm = screen.time_elapsed()
        elif hero['nDir']==3 and kb.key_pressed(attack['key']):
            shot = Sprite(attack['down'])
            shot.set_position(hero['posx'],hero['posy']+hero['spr'].height/2)
            hero['mana']-=attack['manaSpent']
            tm = screen.time_elapsed()
        elif hero['nDir']==4 and kb.key_pressed(attack['key']):
            shot = Sprite(attack['right'])
            shot.set_position(hero['posx']+hero['spr'].width/2,hero['posy'])
            hero['mana']-=attack['manaSpent']
            tm = screen.time_elapsed()
    if shot!=0:
        tir = ['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v']
        for i in tir:
            if hero['shot'].get(i)==None:
                hero['shot'][i] = shot
                hero['shot'][i].dir = hero['nDir']
                hero['shot'][i].damage = attack['damage']*hero['strength']
                hero['shot'][i].speed = attack['speed']
                hero['shot'][i].count = 0
                return hero['shot'], tm



    return hero['shot'], tm

#Moving spells--------------------------------------------------------------------------------------------------
def movingShots(spr):
    for i in spr['shot']:
        if spr['shot'][i].y > -spr['shot'][i].height and spr['shot'][i].y < height and \
                            spr['shot'][i].x > -spr['shot'][i].width and spr['shot'][i].x < width:

            if spr['shot'][i].dir == 1:
                spr['shot'][i].y -= spr['shot'][i].speed * screen.delta_time()
            elif spr['shot'][i].dir == 2:
                spr['shot'][i].x -= spr['shot'][i].speed * screen.delta_time()
            elif spr['shot'][i].dir == 3:
                spr['shot'][i].y += spr['shot'][i].speed * screen.delta_time()
            elif spr['shot'][i].dir == 4:
                spr['shot'][i].x += spr['shot'][i].speed * screen.delta_time()

#Drawing shots-------------------------------------------------------------------------------------------------
def drawingShots(spr):
    for i in spr['shot']:
        spr['shot'][i].draw()

#Recovering mana ---------------------------------------------------------------------------------------------
def recoveringMana(spr,tm,screen):
    if screen.time_elapsed()-tm>=spr['recMana'] and spr['mana']<spr['manaLimit']:
        tm = screen.time_elapsed()
        spr['mana'] += 1

    return spr['mana'], tm

#Updating stats of the sprite-----------------------------------------------------------------------------------
def updateStats(spr):
    if spr['burnt']:
        spr['health'] -= 1 * screen.delta_time()

    if spr['frozen'] and screen.time_elapsed() - spr['statsTimer']['freeze'] >= 5000:
        spr['frozen'] = False
        spr['agility'] *= 2

    if spr['burnt'] and screen.time_elapsed() - spr['statsTimer']['burn'] >= 8000:
        spr['burnt'] = False

    if spr['paralyzed'] and screen.time_elapsed() - spr['statsTimer']['paralyze'] >= 1000:
        spr['paralyzed'] = False

#drawing mana and health stats---------------------------------------------------------------------------------
def status(spr,screen):
    screen.draw_text('Mana: %d'%spr['mana'], spr['posx']+10, spr['posy']+spr['spr'].height-5, size=11, color=(0,0,0), font_name='Arial', bold=False, italic=False)
    screen.draw_text('Health: %d'%spr['health'], spr['posx']+10, spr['posy']+spr['spr'].height+6, size=11, color=(0,0,0), font_name='Arial', bold=False, italic=False)

#Checking collision between spells and sprites------------------------------------------------------------------
def checkCollision(spr,sprB):
    vet = []
    for b in sprB['shot']:
        if spr['spr'].collided_perfect(sprB['shot'][b]) and sprB['shot'][b].count == 0:
            spr['health'] -= sprB['shot'][b].damage
            sprB['shot'][b].hide()
            sprB['shot'][b].count = 1

            if not spr['burnt'] and sprB['shot'][b].speed == attacks['fire']['speed'] and randint(0, 10) > 5:
                spr['burnt'] = True
                spr['statsTimer']['burn'] = screen.time_elapsed()

            if not spr['frozen'] and sprB['shot'][b].speed == attacks['ice']['speed'] and randint(0, 10) > 4:
                spr['frozen'] = True
                spr['statsTimer']['freeze'] = screen.time_elapsed()
                spr['agility'] /= 2

            if not spr['paralyzed'] and sprB['shot'][b].speed == attacks['bolt']['speed'] and randint(0, 10) > 6:
                spr['paralyzed'] = True
                spr['statsTimer']['paralyze'] = screen.time_elapsed()

            if sprB['shot'][b].dir == 1:
                spr['posy'] -= 15
            elif sprB['shot'][b].dir == 2:
                spr['posx'] -= 15
            elif sprB['shot'][b].dir == 3:
                spr['posy'] += 15
            elif sprB['shot'][b].dir == 4:
                spr['posx'] += 15

        if sprB['shot'][b].count > 0:
            vet.append(b)

    for i in vet:
        del sprB['shot'][i]

#Checking collision between sprites(not implemented yet)---------------------------------------------------------
def checkSprCollision(spr,sprB):
    if spr['posx']>sprB['posx']-spr['spr'].width and spr['posx']<sprB['posx']+spr['spr'].width :
        if spr['posy']>sprB['posy']-spr['spr'].height and spr['posy']<sprB['posy']+spr['spr'].height :
            if spr['nDir']==1:
                spr['posy'] = sprB['posy']+spr['spr'].height
            elif spr['nDir']==2:
                spr['posx'] = sprB['posx']+spr['spr'].width
            elif spr['nDir']==3:
                spr['posy'] = sprB['posy']-spr['spr'].height
            elif spr['nDir']==4:
                spr['posx'] = sprB['posx']-spr['spr'].width

#Checking victory or loss--------------------------------------------------------------------------------------
def checkWinOrLose(spr):
    if spr['health']<=0 and (spr['name']=='Lilith' or spr['name']=='Deimos'):
        player['gameIsEnding'] = True
        player['isInBattle'] = False

    elif spr['health']<=0:
        player['isDeciding'] = True #Winning Battles
        player['isInBattle'] = False
        hero['paralyzed'] = False
        hero['frozen'] = False
        currentCity['id'] += 1
        currentCity['name'] = citiesOrder[currentCity['id']]

    elif hero['health']<1:
        player['isInBattle'] = False
        player['gameIsOver'] = True
        #Losing Battles


#moving enemy's shots------------------------------------------------------------------------------------------
def enemyShot(spr,attack,dicShot):
    shot = 0
    if spr['mana']>=attack['manaSpent']:
        if spr['nDir']==1:
            shot = Sprite(attack['up'])
            shot.set_position(spr['posx'],spr['posy'])
            spr['mana']-=attack['manaSpent']
            spr['shootingTime'] = screen.time_elapsed()
        if spr['nDir']==2:
            shot = Sprite(attack['left'])
            shot.set_position(spr['posx'],spr['posy'])
            spr['mana']-=attack['manaSpent']
            spr['shootingTime'] = screen.time_elapsed()
        if spr['nDir']==3:
            shot = Sprite(attack['down'])
            shot.set_position(spr['posx'],spr['posy']+spr['spr'].height/2)
            spr['mana']-=attack['manaSpent']
            spr['shootingTime'] = screen.time_elapsed()
        if spr['nDir']==4:
            shot = Sprite(attack['right'])
            shot.set_position(spr['posx']+spr['spr'].width/2,spr['posy'])
            spr['mana']-=attack['manaSpent']
            spr['shootingTime'] = screen.time_elapsed()
    if shot!=0:
        tir = ['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v']
        for i in tir:
            if dicShot.get(i)==None:
                dicShot[i] = shot
                dicShot[i].dir = spr['nDir']
                dicShot[i].damage = attack['damage']*spr['strength']
                dicShot[i].speed = attack['speed']
                dicShot[i].count = 0
                return dicShot,spr['verAtt']
    spr['verAtt'] = True
    return dicShot, spr['verAtt']

#Enemy's walk to start shooting----------------------------------------------------------------------------------
def walkingIniMagic(spr):
    if not spr['paralyzed']:

        objX = hero['posx']
        ver = False
        if (spr['posx'] < objX-5 or spr['posx'] > objX+5) and (spr['posy'] < spr['objY']-5
                                                           or spr['posy'] > spr['objY']+5):
            ver = True

        if spr['posx'] > objX-5 and spr['posx'] < objX+5:
            if spr['posy']>hero['posy']:
                spr['nDir'] = 1
                spr['nAnim'] = 10
            elif spr['posy']<hero['posy']:
                spr['nDir'] = 3
                spr['nAnim'] = 30

            if spr['posy']>spr['objY']-5 and spr['posy']<spr['objY']+5:
                if spr['nDir']==1:
                    spr['nAnim'] = 10
                    spr['spr'] = Sprite(spr['imgs'][1],1)
                elif spr['nDir']==2:
                    spr['nAnim'] = 20
                    spr['spr'] = Sprite(spr['imgs'][2],1)
                elif spr['nDir']==3:
                    spr['nAnim'] = 30
                    spr['spr'] = Sprite(spr['imgs'][0],1)
                elif spr['nDir']==4:
                    spr['nAnim'] = 40
                    spr['spr'] = Sprite(spr['imgs'][3],1)
            if screen.time_elapsed() - spr['shootingTime'] >= 1000:
                spr['shootingTime'] = screen.time_elapsed()
                spell = cfg.currentEnemy['attacks'][randint(0, len(cfg.currentEnemy['attacks']) - 1)]

                spr['shot'], spr['verAtt'] = enemyShot(spr, attacks[spell], spr['shot'])

        else:
            if spr['posx']<objX-5 :
                spr['posx']+=spr['agility']*screen.delta_time()
                if spr['nAnim']!=4 and not ver:
                    spr['nAnim'] = 4
                    spr['spr'] = Sprite(spr['anims'][1],spr['frames'])
                spr['nDir'] = 4

            if spr['posx']>objX+5:
                spr['posx']-=spr['agility']*screen.delta_time()
                spr['nDir'] = 2
                if spr['nAnim']!= 2 and not ver:
                    spr['nAnim'] = 2
                    spr['spr'] = Sprite(spr['anims'][2],spr['frames'])

            if spr['posy']<spr['objY']-5:
                spr['posy']+=spr['agility']*screen.delta_time()
                if spr['nAnim']!=3:
                    spr['nAnim'] = 3
                    spr['spr'] = Sprite(spr['anims'][3],spr['framesMax'])
                spr['nDir'] = 3

            if spr['posy']>spr['objY']+5:
                spr['posy']-=spr['agility']*screen.delta_time()
                spr['nDir'] = 1
                if spr['nAnim']!= 1:
                    spr['nAnim'] = 1
                    spr['spr'] = Sprite(spr['anims'][0],spr['framesMax'])

        if screen.time_elapsed()-spr['walkingTime']>4000:
            spr['objY'] = randint(0,height-spr['spr'].height)
            spr['walkingTime'] = screen.time_elapsed()

    return None

#Checking if sword collided with sprite(not implemented yet)------------------------------------------------------
def checkSwordCollision(sprB,):
    '''if sword.collided_perfect(sprB['spr'])and screen.time_elapsed()-attack['colTime']>=500:
        sprB['health']-=attack['damage']*spr['strength']
        attack['colTime'] = screen.time_elapsed()
        sword.x = 1900
        sword.hide()
        if attack['nGif']==1:
            sprB['posy']-=20
        if attack['nGif']==2:
            sprB['posx']-=20
        if attack['nGif']==3:
            sprB['posy']+=20
        if attack['nGif']==4:
            sprB['posx']+=20
        return True
    else:
        return False'''

#CAttacking with sword(not implemented yet)-------------------------------------------------------------------------
def swordAttack(spr):

    #att = randint(0,len(spr['swAtt']))

    '''if (kb.key_pressed(attack['key']) and spr['playable']) or not spr['playable']:
        attack['drawTime'] = screen.time_elapsed()
        if spr['nDir']==1:
            if attack['nGif']!=1:
                attack['nGif'] = 1
                attack['spr'] = attack['up']
                attack['spr'].set_total_duration(400)
            attack['spr'].x = spr['posx']-30
            attack['spr'].y = spr['posy']-40
        elif spr['nDir']==2:
            if attack['nGif']!=2:
                attack['nGif'] = 2
                attack['spr'] = attack['left']
                attack['spr'].set_total_duration(400)
            attack['spr'].x = spr['posx']
            attack['spr'].y = spr['posy']+spr['spr'].height
        elif spr['nDir']==3:
            if attack['nGif']!=3:
                attack['nGif'] = 3
                attack['spr'] =attack['down']
                attack['spr'].set_total_duration(400)
            attack['spr'].x = spr['posx']+spr['spr'].width
            attack['spr'].y = spr['posy']+spr['spr'].height
        elif spr['nDir']==4:
            if attack['nGif']!=4:
                attack['nGif'] = 4
                attack['spr'] =attack['right']
                attack['spr'].set_total_duration(400)
            attack['spr'].x = spr['posx']+spr['spr'].width
            attack['spr'].y = spr['posy']
        attack['spr'].update()
        attack['spr'].draw()
        return checkSwordCollision(attack['spr'],sprB,attack,screen,spr)

    if attack['spr']!=0:
        if screen.time_elapsed()-attack['drawTime']>=250:

            attack['drawTime'] = screen.time_elapsed()
            attack['spr'].x = 1900
            attack['spr']=0
            attack['nGif'] = 0
            return True
        else:
            attack['spr'].x = spr['posx']+spr['spr'].width
            attack['spr'].y = spr['posy']
            attack['spr'].update()
            attack['spr'].draw()
            return checkSwordCollision(attack['spr'],sprB,attack,screen,spr)
    '''
    return True

#Walking to hero's position to attack him---------------------------------------------------------------------------
def walkingIniSword(spr):
    objX = hero['posx']+hero['spr'].width/2
    spr['objY'] = hero['posy']

    ver = False
    if not spr['paralyzed']:
        if (spr['posx']<objX-5 or spr['posx']>objX+5) and (spr['posy']<spr['objY']-5 or spr['posy']>spr['objY']+5):
            ver = True

        if spr['posx']<objX-20:
            spr['posx']+=spr['agility']*screen.delta_time()
            if spr['nAnim']!=4 and not ver:
                spr['nAnim'] = 4
                spr['spr'] = Sprite(spr['anims'][1],spr['frames'])
            spr['nDir'] = 4

        if spr['posx']>objX+20:
            spr['posx']-=spr['agility']*screen.delta_time()
            spr['nDir'] = 2
            if spr['nAnim']!= 2 and not ver:
                spr['nAnim'] = 2
                spr['spr'] = Sprite(spr['anims'][2],spr['frames'])

        if spr['posy']<spr['objY']-20:
            spr['posy']+=spr['agility']*screen.delta_time()
            if spr['nAnim']!=3:
                spr['nAnim'] = 3
                spr['spr'] = Sprite(spr['anims'][3],spr['framesMax'])
            spr['nDir'] = 3

        if spr['posy']>spr['objY']+20:
            spr['posy']-=spr['agility']*screen.delta_time()
            spr['nDir'] = 1
            if spr['nAnim']!= 1:
                spr['nAnim'] = 1
                spr['spr'] = Sprite(spr['anims'][0],spr['framesMax'])

        elif spr['posx']>objX-20 and spr['posx']<objX+20 and spr['posy']>spr['objY']-20 and spr['posy']<spr['objY']+20:
            spr['verAtt'] = swordAttack(spr)
    return spr['verAtt']

#Randomize enemy's attack--------------------------------------------------------------------------------
def random_attack(spr):
    if screen.time_elapsed()-spr['randTime'] >= 3000 or spr['verAtt']:
        spr['verAtt'] = False
        spr['randTime'] = screen.time_elapsed()
        spr['curAttack'] = randint(0, len(spr['vetAtt']) - 1)
    if spr['vetAtt'][spr['curAttack']]==0:
        return walkingIniMagic(spr)
    elif spr['vetAtt'][spr['curAttack']]==1:
        return walkingIniSword(spr)

#Checking if user wants to go to menu----------------------------------------------------------------------------
def checkingMenu():
    if kb.key_pressed('esc'):
        player['hasPaused'] = True

#Entire battle code---------------------------------------------------------------------------------------------
def battle():

    #Spells________________________________________________________________
    hero['shot'],cfg.attackTime = shooting(hero, cfg.attackTime, attacks['fire'])
    hero['shot'],cfg.attackTime = shooting(hero, cfg.attackTime, attacks['ice'])
    hero['shot'],cfg.attackTime = shooting(hero, cfg.attackTime, attacks['bolt'])
    movingShots(hero)
    movingShots(cfg.currentEnemy)

    #Checking spells collision_____________________________________________________
    checkCollision(cfg.currentEnemy, hero)
    checkCollision(hero, cfg.currentEnemy)

    #checkSprCollision(hero,currentEnemy)(not implemented yet)

    #Recovering Mana_________________________________________________________
    cfg.hero['mana'], cfg.startTime = recoveringMana(hero, cfg.startTime, screen)
    cfg.currentEnemy['mana'], cfg.startTimeEnemy = recoveringMana(cfg.currentEnemy, cfg.startTimeEnemy, screen)
    updateStats(hero)
    updateStats(cfg.currentEnemy)

    #hero moving______________________________________________________
    movingBattle()
    heroPos(hero)
    heroPos(cfg.currentEnemy)

    #Checking Pause menu________________________________________________________
    checkingMenu()

    #Checking end of battle_________________________________________________________________
    checkWinOrLose(cfg.currentEnemy)

    #Drawing and updating__________________________________________________________
    updating(cfg.currentEnemy)
    drawing(cfg.currentEnemy)
    drawingShots(hero)
    drawingShots(cfg.currentEnemy)
    status(cfg.currentEnemy,screen)
    updating(hero)
    drawing(hero)
    #Enemy's walk_________________________________________________________________________
    random_attack(cfg.currentEnemy)
    #swordAttack(hero,swAttack,kb,currentEnemy,screen)(not implemented yet)
    status(hero,screen)
