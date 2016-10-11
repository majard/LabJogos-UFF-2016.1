from cfg import *
import cfg
count = 0
speed = 240

def drawing(dic):
    dic['img'].set_position(dic['posx'],dic['posy'])
    dic['img'].draw()
    return None

def drawingOver(dic):
    dic['img2'].set_position(dic['posx'],dic['posy'])
    dic['img2'].draw()
    return None

def histDraw():
    screen.draw_text('%s'%cfg.currentCity['name'].upper(), width/2 - 80, 30, size=40, color=(0,0,0), font_name='Arial', bold=True, italic=False)
    screen.draw_text('Press Enter', width/2 - 50, 450, size=16, color=(0,0,0), font_name='Arial', bold=True, italic=False)
    hist = GameImage(hists['imgs'][hists['cur']])
    hist.draw()

    if hists['cur'] > 0:
        cfg.currentEnemy = enemies[cities[currentCity['name']]['enemy']]
        enemy = Sprite(cfg.currentEnemy['imgs'][0],1)
        enemy.set_position(290,290)
        enemy.draw()

    if kb.key_pressed('enter') and screen.time_elapsed()-hists['time']>=250:
        player['isInStory'] = False
        player['isChoosingPoints'] = True


def decsDraw(dic):
    hero['spr'].draw()

    cfg.bg = GameImage('Bgs/menubg.png')
    decs = GameImage(dic['imgs'][dic['cur']])
    decs.draw()
    drawing(dic['kill'])
    drawing(dic['leave'])
    if ms.is_over_object(dic['kill']['img']):
        drawingOver(dic['kill'])
        if ms.is_button_pressed(1):
            hero['isDead'].append(cfg.currentEnemy['name'])
            hero['kills']+=1
            dic['cur'] += 1

            player['isDeciding'] = False
            player['isChoosingPoints'] = True


    if ms.is_over_object(dic['leave']['img']):
        drawingOver(dic['leave'])
        if ms.is_button_pressed(1):
            dic['cur'] += 1

            player['isDeciding'] = False
            player['isChoosingPoints'] = True


def choosingPoints(dic,count):

    cfg.bg = GameImage(dic['img'])

    screen.draw_text('Health: %d'%hero['health'], 410, 120, size=26, color=(0,0,0), font_name='Arial', bold=False, italic=False)
    screen.draw_text('Mana: %d'%hero['manaLimit'], 410, 170, size=26, color=(0,0,0), font_name='Arial', bold=False, italic=False)
    screen.draw_text('Strength: %d'%hero['strength'], 410, 220, size=26, color=(0,0,0), font_name='Arial', bold=False, italic=False)
    screen.draw_text('Agility: %d'%(hero['agility']//8), 410, 270, size=26, color=(0,0,0), font_name='Arial', bold=False, italic=False)

    if currentCity['id'] == 0:
        cfg.currentEnemy['spr'] = Sprite(cfg.currentEnemy['imgs'][0], 1)
        screen.draw_text('CHOOSE YOUR SKILLS', 120, 20, size=40, color=(0,0,0), font_name='Arial', bold=True, italic=False)

    screen.draw_text('%d Points'%dic['total'], 430, 380, size=32, color=(0,0,0), font_name='Arial', bold=False, italic=False)

    if dic['total']>0 and screen.time_elapsed()-dic['time']>100:
        if kb.key_pressed('h'):
            dic['time'] = screen.time_elapsed()
            hero['health']+=1
            dic['total']-=1
            return count
        if kb.key_pressed('m'):
            dic['time'] = screen.time_elapsed()
            hero['manaLimit']+=1
            dic['total']-=1
            return count
        if kb.key_pressed('s'):
            dic['time'] = screen.time_elapsed()
            hero['strength']+=1
            dic['total']-=1
            return count
        if kb.key_pressed('a'):
            dic['time'] = screen.time_elapsed()
            hero['agility']+=8
            dic['total']-=1
            return count

    if dic['total']>=0 and screen.time_elapsed()-dic['time']>100:
        if kb.key_pressed('q') and hero['agility']>0:
            dic['time'] = screen.time_elapsed()
            hero['agility']-=8
            dic['total']+=1
        elif kb.key_pressed('w') and hero['strength']>0:
            dic['time'] = screen.time_elapsed()
            hero['strength']-=1
            dic['total']+=1
        elif kb.key_pressed('j') and hero['manaLimit']>0:
            dic['time'] = screen.time_elapsed()
            hero['manaLimit']-=1
            dic['total']+=1
        elif kb.key_pressed('y') and hero['health']>0:
            dic['time'] = screen.time_elapsed()
            hero['health']-=1
            dic['total']+=1

    if count==0 or currentCity['id'] > 0:
        hero['spr'] = Sprite('characters/Hero/example.png')
        hero['spr'].set_position(40,100)
        count = 1

    hero['spr'].draw()

    if dic['total'] <= 0 and kb.key_pressed('enter'):
        player['isChoosingPoints'] = False
        player['isInTown'] = True
        hero['posx'] = screen.width - hero['spr'].width
        hero['posy'] = screen.height - hero['spr'].height
        hero['spr'] = Sprite('characters/Hero/bunekinDeFronte.png')
        hero['mana'] = hero['manaLimit']
        hero['maxHealth'] = hero['health']

    if currentCity['id'] > 0:
        if cfg.currentEnemy['name'] in hero['isDead']:
            if not cfg.currentEnemy['itemVer']:
                hero['strength'] += 2
                cfg.currentEnemy['itemVer'] = True
            screen.draw_text('Strength: %d (+1)'%hero['strength'], 410, 220, size=26, color=(0,0,0), font_name='Arial', bold=False, italic=False)
        else:
            if cfg.currentEnemy['item']=='a':
                if not cfg.currentEnemy['itemVer']:
                    hero['agility']+= 32
                    hero['health'] = hero['maxHealth']
                    cfg.currentEnemy['itemVer'] = True
                screen.draw_text('Agility: %d (+4)'%(hero['agility']//8), 410, 270, size=26, color=(0,0,0), font_name='Arial', bold=False, italic=False)
            if cfg.currentEnemy['item']=='h':
                if not cfg.currentEnemy['itemVer']:
                    hero['maxHealth'] += 20
                    hero['health'] = hero['maxHealth']
                    cfg.currentEnemy['itemVer'] = True
                screen.draw_text('Health: %d (+20)'%hero['maxHealth'], 410, 120, size=26, color=(0,0,0), font_name='Arial', bold=False, italic=False)
            if cfg.currentEnemy['item']=='s':
                if not cfg.currentEnemy['itemVer']:
                    hero['strength']+= 5
                    hero['health'] = hero['maxHealth']
                    cfg.currentEnemy['itemVer'] = True
                screen.draw_text('Strength: %d (+5)'%hero['strength'], 410, 220, size=26, color=(0,0,0), font_name='Arial', bold=False, italic=False)
            if cfg.currentEnemy['item']=='m':
                if not cfg.currentEnemy['itemVer']:
                    hero['manaLimit'] += 20
                    hero['health'] = hero['maxHealth']
                    cfg.currentEnemy['itemVer'] = True
                screen.draw_text('Mana: %d (+20)'%hero['manaLimit'], 410, 170, size=26, color=(0,0,0), font_name='Arial', bold=False, italic=False)


    if (currentCity['name'] == 'swaard' and hero['kills']>=3):
        cfg.currentEnemy = enemies['warmann']

    elif currentCity['name'] == 'swaard' and hero['kills'] < 3:
        cfg.currentEnemy = enemies['arius']

    elif currentCity['name'] == 'kingsia' and hero['kills'] < 3 and not 'pennae' in hero['isDead']:
        cfg.currentEnemy = enemies['deimos']

    elif currentCity['name'] == 'kingsia' and (hero['kills'] >= 3 or 'pennae' in hero['isDead']):
        cfg.currentEnemy = enemies['lilith']

    else:
        cfg.currentEnemy = enemies[cities[currentCity['name']]['enemy']]

    cfg.currentEnemy['spr'] = Sprite(cfg.currentEnemy['imgs'][0], 1)

    return count

