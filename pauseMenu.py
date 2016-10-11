from PPlay.gameimage import *
from PPlay.sprite import *
from cfg import screen, player, hero, ms, pause, controls
import cfg

def drawing(dic):
    dic['img'].set_position(dic['posx'],dic['posy'])
    dic['img'].draw()
    return None

def drawingOver(dic):
    dic['img2'].set_position(dic['posx'],dic['posy'])
    dic['img2'].draw()
    return None



def saveArq(decs,chooseP):
    bd = open('forgKingSave.txt','w')
    bd.write(str(int(hero['posx']))+'#'+str(int(hero['posy']))+'\n')
    bd.write(str(int(hero['health']))+'#'+str(int(hero['mana']))+'#'+str(int(hero['agility']))+'#'+str(hero['strength'])+'#'+
             str(int(hero['manaLimit']))+'#'+str(hero['kills'])+'#'+str(int(hero['maxHealth']))+'\n')
    bd.write(str(hero['nAnim'])+'#'+str(hero['nDir'])+'\n')
    bd.write(str(int(cfg.currentCity['id'])) + '#' + str(cfg.currentCity['name']) + '\n')
    bd.write(str(cfg.currentEnemy['name'])+'\n')
    bd.write(str(int(cfg.currentEnemy['posx']))+'#'+str(int(cfg.currentEnemy['posy']))+'\n')
    bd.write(str(int(cfg.currentEnemy['health']))+'#'+str(int(cfg.currentEnemy['mana']))+'\n')
    bd.write(str(cfg.currentEnemy['nAnim'])+'#'+str(cfg.currentEnemy['nDir'])+'\n')
    bd.write(str(decs['cur'])+'#'+str(chooseP['total'])+'\n')
    for i in range(len(hero['isDead'])):
        if i==len(hero['isDead'])-1:
            bd.write(hero['isDead'][i])
        else:
            bd.write(hero['isDead'][i]+'#')
    bd.write('\n')
    bd.write(str(player['isInBattle']) + '#' + str(player['isInTown']))
    bd.close()
    return None


def pauseDraw(decs,chooseP):

    enemy = Sprite(cfg.currentEnemy['imgs'][0], 1)
    enemy.set_position(cfg.currentEnemy['posx'], cfg.currentEnemy['posy'])
    hero['spr'].set_position(hero['posx'],hero['posy'])
    hero['spr'].draw()
    drawing(pause['bg'])
    drawing(pause['save'])
    drawing(pause['quit'])
    drawing(pause['back'])
    drawing(pause['stats'])

    if ms.is_over_object(pause['back']['img']):
        drawingOver(pause['back'])
        if ms.is_button_pressed(1):
            player['hasPaused'] = False

    if ms.is_over_object(pause['quit']['img']):
        drawingOver(pause['quit'])
        if ms.is_button_pressed(1):
            screen.close()

    if ms.is_over_object(pause['stats']['img']):
        drawingOver(pause['stats'])
        if ms.is_button_pressed(1):
            player['isInStatsScreen'] = True

    if ms.is_over_object(pause['save']['img']):
        drawingOver(pause['save'])
        if ms.is_button_pressed(1):
            saveArq(decs, chooseP)


def statsDraw():
    screen.draw_text('Health: %d'%hero['health'], 410, 120, size=26, color=(0,0,0), font_name='Arial', bold=False, italic=False)
    screen.draw_text('Mana: %d'%hero['manaLimit'], 410, 170, size=26, color=(0,0,0), font_name='Arial', bold=False, italic=False)
    screen.draw_text('Strength: %d'%hero['strength'], 410, 220, size=26, color=(0,0,0), font_name='Arial', bold=False, italic=False)
    screen.draw_text('Agility: %d'%(hero['agility']//8), 410, 270, size=26, color=(0,0,0), font_name='Arial', bold=False, italic=False)
    drawing(controls['back'])
    example = Sprite('characters/Hero/example.png')
    example.set_position(40,100)
    example.draw()

    if ms.is_over_object(controls['back']['img']) and ms.is_button_pressed(1):
            player['isInStatsScreen'] = False
            path = cfg.cities[cfg.currentCity['name']]['path']
            image = 'Resources/' + path + 'bg.png'
            cfg.bg = GameImage(image)
