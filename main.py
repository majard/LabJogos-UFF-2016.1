from menu import *
from hists import *
from fighting import *
from pauseMenu import *
import cfg
from towns import *

cfg.bg = GameImage('Bgs/menu.png')
screen.set_title('The Forgotten Kingdom')
cfg.currentEnemy = enemies['mattus']

#Game Loop--------------------------------------------------------------------------------------------------
while True:

    screen.set_background_color((0, 0, 0))
    cfg.bg.set_position(0, 0)
    cfg.bg.draw()


    if player['isInStatsScreen']:
        statsDraw()

    elif player['hasPaused']:
        pauseDraw(decs, chooseP)

    elif player['isInMenu']:
        audio.play()
        audio.set_volume(10)
        audio.set_repeat(True)
        menuDraw(decs,chooseP)

    elif player['isInTown']:
        town()


    elif player['isInControlsScreen']:
        controlsDraw(controls)

    elif player['isInBattle']:
        battle()

    elif player['isDeciding']:
        cfg.currentEnemy['spr'].draw()
        decsDraw(decs)

    elif player['gameIsOver']:
        gameOver['bg'].draw()
        gameOver['quit']['img'].set_position(gameOver['quit']['posx'],gameOver['quit']['posy'])
        gameOver['quit']['img'].draw()
        if ms.is_over_object(gameOver['quit']['img']) and ms.is_button_pressed(1):
            screen.close()

    elif player['isInStory']:
        histDraw()

    elif player['isChoosingPoints']:
        chooseP['count'] = choosingPoints(chooseP, chooseP['count'])
        hists['time'] = screen.time_elapsed()

    elif player['gameIsEnding']:
        audio.stop()
        audio2.set_volume(10)
        audio2.set_repeat(True)
        audio2.play()
        endGame['bg'].draw()
        endGame['quit']['img'].set_position(endGame['quit']['posx'],endGame['quit']['posy'])
        endGame['quit']['img'].draw()
        if ms.is_over_object(endGame['quit']['img']) and ms.is_button_pressed(1):
            screen.close()

    screen.update()
