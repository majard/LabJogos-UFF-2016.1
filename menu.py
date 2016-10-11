from cfg import *
import cfg

def drawing(dic):
    dic['img'].set_position(dic['posx'],dic['posy'])
    dic['img'].draw()

def controlsDraw(dic):
    if (ms.is_button_pressed(1) and ms.is_over_object(dic['back']['img'])) or kb.key_pressed('esc'):
        player['isInControlsScreen'] = False
        player['isInMenu'] = True
        cfg.bg = GameImage('Bgs/menu.png')

    drawing(dic['back'])

def loading(decs,chooseP):
    bd = open('forgKingSave.txt','r')
    linha = bd.readline()
    itens = linha.strip().split('#')
    hero['posx'] = int(itens[0])
    hero['posy'] = int(itens[1])
    linha = bd.readline()
    itens = linha.strip().split('#')
    hero['health'] = int(itens[0])
    hero['mana'] = int(itens[1])
    hero['agility'] = int(itens[2])
    hero['strength'] = int(itens[3])
    hero['manaLimit'] = int(itens[4])
    hero['kills'] = int(itens[5])
    hero['maxHealth'] = int(itens[6])
    linha = bd.readline()
    itens = linha.strip().split('#')
    hero['nAnim'] = int(itens[0])
    hero['nDir'] = int(itens[1])
    linha = bd.readline()
    itens = linha.strip().split('#')
    cfg.currentCity['id'] = int(itens[0])
    cfg.currentCity['name'] = itens[1]
    linha = bd.readline()
    linha = linha.strip()
    cfg.currentEnemy = enemies[cities[cfg.currentCity['name']]['enemy']]
    cfg.currentEnemy['name'] = linha
    linha = bd.readline()
    itens = linha.strip().split('#')
    cfg.currentEnemy['posx'] = int(itens[0])
    cfg.currentEnemy['posy'] = int(itens[1])
    linha = bd.readline()
    itens = linha.strip().split('#')
    cfg.currentEnemy['health'] = int(itens[0])
    cfg.currentEnemy['mana'] = int(itens[1])
    linha = bd.readline()
    itens = linha.strip().split('#')
    cfg.currentEnemy['nAnim'] = int(itens[0])
    cfg.currentEnemy['nDir'] = int(itens[1])
    linha = bd.readline()
    itens = linha.strip().split('#')
    decs['cur'] = int(itens[0])
    chooseP['total'] = int(itens[1])
    linha = bd.readline()
    itens = linha.strip().split('#')
    for i in itens:
        hero['isDead'].append(i)
    linha = bd.readline()
    itens = linha.strip().split('#')

    if itens[0] == 'False':
        player['isInBattle'] = False
    else:
        player['isInBattle'] = True

    if itens[1] == 'False':
        player['isInTown'] = False
    else:
        player['isInTown'] = True
    player['isInMenu'] = False
    player['hasPaused'] = True
    cfg.currentEnemy['spr'] = Sprite(cfg.currentEnemy['imgs'][0], 1)

    path = cities[currentCity['name']]['path']
    image = 'Resources/'+ path + 'bg.png'
    cfg.bg = GameImage(image)

    bd.close()

def menuDraw(decs, chooseP):
    if (ms.is_button_pressed(1) and ms.is_over_object(menu['play']['img'])) or kb.key_pressed('enter'):
        player['isInMenu'] = False
        player['isInStory'] = True
        cfg.bg = GameImage('Bgs/images.png')

    elif (ms.is_button_pressed(1) and ms.is_over_object(menu['controls']['img'])) or kb.key_pressed('space'):
        player['isInMenu'] = False
        player['isInControlsScreen'] = True
        cfg.bg = GameImage('Bgs/controls.png')

    elif (ms.is_button_pressed(1) and ms.is_over_object(menu['quit']['img'])) or kb.key_pressed('esc'):
        screen.close()

    elif (ms.is_button_pressed(1) and ms.is_over_object(menu['cont']['img'])) or kb.key_pressed('c'):
        loading(decs,chooseP)

    drawing(menu['play'])
    drawing(menu['cont'])
    drawing(menu['controls'])
    drawing(menu['quit'])
