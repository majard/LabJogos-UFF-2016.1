from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.animation import *
from PPlay.keyboard import *
from random import randint
from PPlay.sound import *
#Variáveis Globais--------------------------------------------------------------------------------------
width = 640
height = 480
speed = 70
startTime = 0
startTimeEnemy = 0
attackTime = 0

#play mode:
player = dict(isInMenu=True,
              isInTown=False,
              isInBattle=False,
              isDeciding=False,
              gameIsOver=False,
              isInStory=False,
              isChoosingPoints=False,
              hasPaused=False,
              isInControlsScreen=False,
              gameIsEnding=False,
              isInStatsScreen=False)

#Criação da tela e background----------------------------------------------------------------------------
screen = Window(width, height)
audio = Sound('audioMed.ogg')
audio2 = Sound('malandra.ogg')
bg = 0

#Menu___________________________________________________________________________________
menu = dict(
            play = dict(img = Sprite('buttons/butPlay.png'),
                        posx = width  - 250,
                        posy = height/5),
            cont = dict(img = Sprite('buttons/butCont.png'),
                        posx = width - 250,
                        posy = height*2/5),
            controls = dict(img = Sprite('buttons/butControls.png'),
                            posx = width  - 250,
                            posy = height*(3/5)),
            quit = dict(img = Sprite('buttons/butQuit.png'),
                        posx = width - 250,
                        posy = height*(4/5)))


#Controls________________________________________________________________________________
controls = dict(bg = dict(img = GameImage('Bgs/controls.png'),
                          posx = 0,
                          posy = 0),
                back = dict(img = Sprite('buttons/butBack.png'),
                            posx = -15,
                            posy = -5))


#Histories_______________________________________________________________________________________
hists = dict(imgs = ['stories/story.png','stories/story1.png','stories/story2.png','stories/story3.png',
                     'stories/story3.png','stories/story3.png','stories/story3.png'],
             cur = 0,
             time = 0)

decs = dict(imgs = ['stories/dec1.png','stories/dec2.png','stories/dec3.png','stories/dec4.png','stories/dec5.png','stories/dec6.png','stories/dec7.png','stories/dec8.png','stories/dec9.png'],
            kill = dict(img = Sprite('buttons/butKill.png'),
                        img2 = Sprite('buttons/butKill2.png'),
                        posx = 70,
                        posy = 300),
            leave = dict(img = Sprite('buttons/butLeave.png'),
                         img2 = Sprite('buttons/butLeave2.png'),
                        posx = 350,
                        posy = 300),
            cur = 0)

chooseP = dict(img = 'Bgs/choosingPoints.png',
               total = 100,
               time = 0,
               count = 0)

pause = dict(bg = dict(img = GameImage('Bgs/menubg.png'),
                        posx = 0,
                        posy = 0),
             save = dict(img = Sprite('buttons/save1.png'),
                         img2 = Sprite('buttons/save2.png'),
                         posx = width/2 - 100,
                         posy = 150),
             quit = dict(img = Sprite('buttons/quit1.png'),
                         img2 = Sprite('buttons/quit2.png'),
                         posx = width/2 - 100,
                         posy = 350),
             back = dict(img = Sprite('buttons/backgame1.png'),
                         img2 = Sprite('buttons/backgame2.png'),
                         posx = width/2 - 100,
                         posy = 50),
             stats = dict(img = Sprite('buttons/stats1.png'),
                          img2 = Sprite('buttons/stats2.png'),
                          posx = width/2 - 100,
                          posy = 250))

gameOver = dict(bg = GameImage('Bgs/gameOver.png'),
                quit = dict(img = Sprite('buttons/butQuit.png'),
                        posx = width - 400,
                        posy = height-150))

endGame = dict(bg = GameImage('Bgs/endGame.png'),
                quit = dict(img = Sprite('buttons/butQuit.png'),
                        posx = width - 400,
                        posy = height-150))

dialog = dict(spr=0,
              n = 0)

cities = dict(piproor=dict(path='Piproor/',
                           char1='young woman.gif',
                           char2='old man.gif',
                           enemy='jinnyx'),
              zilennas=dict(path='Zilennas/',
                            char1='boy.gif',
                            char2='old woman.gif',
                            enemy='pennae'),
              ispelum=dict(path='Ispelum/',
                           char1='mage.gif',
                           char2='boy.gif',
                           enemy = 'circe'),
              pipreet=dict(path='Pipreet/',
                           char1='woman.gif',
                           char2='man.gif',
                           enemy='mattus'),
              swaard=dict(path='Swaard/',
                          char1='old woman.gif',
                          char2='man.gif',
                          enemy='arius'),
              maul=dict(path='Maul/',
                        char1='old man.gif',
                        char2='woman.gif',
                        enemy='donnahue'),
              kingsia=dict(path='kingsia/',
                           enemy = 'deimos'))

citiesOrder = ['pipreet', 'ispelum', 'zilennas', 'maul', 'piproor', 'swaard', 'kingsia']


currentCity = dict(name = 'pipreet',
                   id = 0)

#Criação dos personagens----------------------------------------------------------------------------------

#hero________________________________________________________
hero = dict(posx = randint(0, width/2),
            posy = randint(0, height),
            imgs = ['characters/Hero/bunekinDeFronte.png',
                    'characters/Hero/bunekinTras.png',
                    'characters/Hero/bunekinEsq.png',
                    'characters/Hero/bunekinDir.png'],
            anims = ['characters/Hero/animTras.png',
                     'characters/Hero/animDir.png',
                     'characters/Hero/animEsq.png',
                     'characters/Hero/animFrente.png'],
            duration = 250,
            health = 0,
            mana = 0,
            agility = 0,
            strength = 0,
            manaLimit = 0,
            recMana = 1000,
            nAnim = 30,
            nDir = 3,
            shot = dict(),
            frozen = False,
            burnt = False,
            paralyzed = False,
            statsTimer = dict(freeze = 0, burn = 0, paralyze = 0),
            kills = 0,
            isDead = [],
            playable = True)


hero['spr'] = Sprite(hero['imgs'][0],1)


#Inimigo------------------------------------------------------------------------------------------

enemies = dict(
            jinnyx = dict(
                spr = 0,
                name = 'Jinnyx',
                posx = randint(width/2,width-80),
                posy = randint(0,height-100),
                imgs = ['characters/Jynnyx/iniFront.png',
                    'characters/Jynnyx/iniTras.png',
                    'characters/Jynnyx/iniEsq.png',
                    'characters/Jynnyx/iniDir.png'],
                anims = ['characters/Jynnyx/iniAniTras.png',
                    'characters/Jynnyx/iniAniDir.png',
                    'characters/Jynnyx/iniAniEsq.png',
                    'characters/Jynnyx/iniAniFront.png'],
                frames = 3,
                framesMax = 4,
                duration = 250,
                health = 100,
                mana = 80,
                manaLimit = 80,
                recMana = 2000,
                agility =  1.3 * speed,
                strength = 8,
                nAnim = 30,
                nDir = 3,
                walkingTime =0,
                dodgingTime = 0,
                shootingTime = 0,
                objY = randint(100,height)-100,
                shot = dict(),
                vetAtt = [0,0,0,0,0,0,0,0,1,1],
                randTime = 0,
                attacks = ['fire'],
                verAtt = False,
                frozen = False,
                burnt = False,
                paralyzed = False,
                statsTimer = dict(freeze = 0, burn = 0, paralyze = 0),
                playable = False,
                item = 'm',
                itemVer = False),

            pennae = dict(
                spr = 0,
                name = 'Pennae',
                posx = randint(width/2,width-80),
                posy = randint(0,height-100),
                imgs = ['characters/Pennae/penDown.png',
                        'characters/Pennae/penUp.png',
                        'characters/Pennae/penLeft.png',
                        'characters/Pennae/penRight.png'],
                anims = ['characters/Pennae/penAnimUp.png',
                        'characters/Pennae/penAnimRight.png',
                        'characters/Pennae/penAnimLeft.png',
                        'characters/Pennae/penAnimDown.png'],
                frames = 2,
                framesMax = 2,
                duration = 250,
                health = 40,
                mana = 40,
                manaLimit = 40,
                recMana = 1000,
                agility = 1.6 * speed,
                strength = 6,
                nAnim = 30,
                nDir = 3,
                walkingTime =0,
                dodgingTime = 0,
                shootingTime = 0,
                objY = randint(100,height)-100,
                shot = dict(),
                vetAtt = [0,0,0,0,0,0,0,0,1,1],
                randTime = 0,
                attacks = ['bolt'],
                verAtt = False,
                curAttack = 0,
                frozen = False,
                burnt = False,
                paralyzed = False,
                statsTimer = dict(freeze = 0, burn = 0, paralyze = 0),
                playable = False,
                item = 'a',
                itemVer = False),

            circe = dict(
                spr = 0,
                name = 'Circe',
                posx = randint(width/2,width-80),
                posy = randint(0,height-100),
                imgs = ['characters/Circe/circDown.png',
                        'characters/Circe/circUp.png',
                        'characters/Circe/circLeft.png',
                        'characters/Circe/circRight.png'],
                anims = ['characters/Circe/circAnimUp.png',
                        'characters/Circe/circAnimRight.png',
                        'characters/Circe/circAnimLeft.png',
                        'characters/Circe/circAnimDown.png'],
                frames = 3,
                framesMax = 3,
                duration = 250,
                health = 50,
                mana = 80,
                manaLimit = 80,
                recMana = 500,
                agility = 1.2 * speed,
                strength = 5,
                nAnim = 30,
                nDir = 3,
                walkingTime =0,
                dodgingTime = 0,
                shootingTime = 0,
                objY = randint(100,height)-100,
                shot = dict(),
                vetAtt = [0,0,0,0,0,0,0,0,1,1],
                randTime = 0,
                attacks = ['fire'],
                verAtt = False,
                curAttack = 0,
                frozen = False,
                burnt = False,
                paralyzed = False,
                statsTimer = dict(freeze = 0, burn = 0, paralyze = 0),
                playable = False,
                 item = 'm',
                 itemVer = False),

            mattus = dict(
                spr = 0,
                name = 'Mattus',
                posx = randint(width/2,width-80),
                posy = randint(0,height-100),
                imgs = ['characters/Mattus/matDown.png',
                        'characters/Mattus/matUp.png',
                        'characters/Mattus/matLeft.png',
                        'characters/Mattus/matRight.png'],
                anims = ['characters/Mattus/matAnimUp.png',
                        'characters/Mattus/matAnimRight.png',
                        'characters/Mattus/matAnimLeft.png',
                        'characters/Mattus/matAnimDown.png'],
                frames = 4,
                framesMax = 4,
                duration = 250,
                health = 60,
                mana = 100,
                manaLimit = 100,
                recMana = 2000,
                agility = 0.9 * speed,
                strength = 8,
                nAnim = 30,
                nDir = 3,
                walkingTime =0,
                dodgingTime = 0,
                shootingTime = 0,
                objY = randint(100,height)-100,
                shot = dict(),
                vetAtt = [0,0,0,0,0,0,0,0,1,1],
                randTime = 0,
                attacks = ['ice'],
                verAtt = False,
                curAttack = 0,
                frozen = False,
                burnt = False,
                paralyzed = False,
                statsTimer = dict(freeze = 0, burn = 0, paralyze = 0),
                playable = False,
                  item = 'h',
                  itemVer = False),

            warmann = dict(
                spr = 0,
                name = 'Warmann',
                posx = randint(width/2,width-80),
                posy = randint(0,height-100),
                imgs = ['characters/Warmann/warDown.png',
                        'characters/Warmann/warUp.png',
                        'characters/Warmann/warLeft.png',
                        'characters/Warmann/warRight.png'],
                anims = ['characters/Warmann/warAnimUp.png',
                        'characters/Warmann/warAnimRight.png',
                        'characters/Warmann/warAnimLeft.png',
                        'characters/Warmann/warAnimDown.png'],
                frames = 3,
                framesMax = 3,
                duration = 250,
                health = 120,
                mana = 40,
                manaLimit = 40,
                recMana = 1000,
                agility = 1.4 * speed,
                strength = 14,
                nAnim = 30,
                nDir = 3,
                walkingTime =0,
                dodgingTime = 0,
                shootingTime = 0,
                objY = randint(100,height)-100,
                shot = dict(),
                vetAtt = [0,0,0,0,0,0,0,0,1,1],
                randTime = 0,
                attacks = ['bolt', 'fire'],
                verAtt = False,
                curAttack = 0,
                frozen = False,
                burnt = False,
                paralyzed = False,
                statsTimer = dict(freeze = 0, burn = 0, paralyze = 0),
                playable = False,
                item = 's',
                itemVer = False),

            arius = dict(
                spr = 0,
                name = 'Arius',
                posx = randint(width/2,width-80),
                posy = randint(0,height-100),
                imgs = ['characters/Arius/ariDown.png',
                        'characters/Arius/ariUp.png',
                        'characters/Arius/ariLeft.png',
                        'characters/Arius/ariRight.png'],
                anims = ['characters/Arius/ariAnimUp.png',
                        'characters/Arius/ariAnimRight.png',
                        'characters/Arius/ariAnimLeft.png',
                        'characters/Arius/ariAnimDown.png'],
                frames = 3,
                framesMax = 3,
                duration = 250,
                health = 130,
                mana = 30,
                manaLimit = 30,
                recMana = 1000,
                agility = 1.4 * speed,
                strength = 14,
                nAnim = 30,
                nDir = 3,
                walkingTime =0,
                dodgingTime = 0,
                shootingTime = 0,
                objY = randint(100,height)-100,
                shot = dict(),
                vetAtt = [0,0,0,0,0,0,0,0,1,1],
                randTime = 0,
                attacks = ['bolt', 'ice'],
                verAtt = False,
                curAttack = 0,
                frozen = False,
                burnt = False,
                paralyzed = False,
                statsTimer = dict(freeze = 0, burn = 0, paralyze = 0),
                playable = False,
                item = 's',
                itemVer = False),

            donnahue = dict(
                spr = 0,
                name = 'Donnahue',
                posx = randint(width/2,width-80),
                posy = randint(0,height-100),
                imgs = ['characters/New1/newDown.png',
                        'characters/New1/newUp.png',
                        'characters/New1/newLeft.png',
                        'characters/New1/newRight.png'],
                anims = ['characters/New1/newAnimUp.png',
                        'characters/New1/newAnimRight.png',
                        'characters/New1/newAnimLeft.png',
                        'characters/New1/newAnimDown.png'],
                frames = 4,
                framesMax = 4,
                duration = 250,
                health = 120,
                mana = 40,
                manaLimit = 100,
                recMana = 1000,
                agility = 1.2 * speed,
                strength = 20,
                nAnim = 30,
                nDir = 3,
                walkingTime =0,
                dodgingTime = 0,
                shootingTime = 0,
                objY = randint(100,height)-100,
                shot = dict(),
                vetAtt = [0,0,0,0,0,0,0,0,1,1],
                randTime = 0,
                attacks = ['bolt', 'fire', 'ice'],
                verAtt = False,
                curAttack = 0,
                frozen = False,
                burnt = False,
                paralyzed = False,
                statsTimer = dict(freeze = 0, burn = 0, paralyze = 0),
                playable = False,
                item = 'a',
                itemVer = False),

            deimos = dict(
                spr = 0,
                name = 'Deimos',
                posx = randint(width/2,width-80),
                posy = randint(0,height-100),
                imgs = ['characters/Deimos/deimDown.png',
                        'characters/Deimos/deimUp.png',
                        'characters/Deimos/deimLeft.png',
                        'characters/Deimos/deimRight.png'],
                anims = ['characters/Deimos/deimAnimUp.png',
                        'characters/Deimos/deimAnimRight.png',
                        'characters/Deimos/deimAnimLeft.png',
                        'characters/Deimos/deimAnimDown.png'],
                frames = 3,
                framesMax = 3,
                duration = 250,
                health = 250,
                mana = 100,
                manaLimit = 100,
                recMana = 1000,
                agility = 1.2 * speed,
                strength = 25,
                nAnim = 30,
                nDir = 3,
                walkingTime =0,
                dodgingTime = 0,
                shootingTime = 0,
                objY = randint(100,height)-100,
                shot = dict(),
                vetAtt = [0,0,0,0,0,0,0,0,1,1],
                randTime = 0,
                attacks = ['fire', 'ice', 'bolt'],
                verAtt = False,
                curAttack = 0,
                frozen = False,
                burnt = False,
                paralyzed = False,
                statsTimer = dict(freeze = 0, burn = 0, paralyze = 0),
                playable = False,
                item = ''),

            lilith = dict(spr = 0,
                name = 'Lilith',
                posx = randint(width/2,width-80),
                posy = randint(0,height-100),
                imgs = ['characters/Lilith/liliDown.png',
                        'characters/Lilith/liliUp.png',
                        'characters/Lilith/liliLeft.png',
                        'characters/Lilith/liliRight.png'],
                anims = ['characters/Lilith/liliAnimUp.png',
                        'characters/Lilith/liliAnimRight.png',
                        'characters/Lilith/liliAnimLeft.png',
                        'characters/Lilith/liliAnimDown.png'],
                frames = 3,
                framesMax = 3,
                duration = 250,
                health = 250,
                mana = 200,
                manaLimit = 200,
                recMana = 1000,
                agility = 1.2 * speed,
                strength = 25,
                nAnim = 30,
                nDir = 3,
                walkingTime =0,
                dodgingTime = 0,
                shootingTime = 0,
                objY = randint(100,height)-100,
                shot = dict(),
                vetAtt = [0,0,0,0,0,0,0,0,1,1],
                randTime = 0,
                attacks = ['fire', 'ice', 'bolt'],
                verAtt = False,
                curAttack = 0,
                frozen = False,
                burnt = False,
                paralyzed = False,
                statsTimer = dict(freeze = 0, burn = 0, paralyze = 0),
                playable = False,
                item = ''))




currentEnemy = 0

histories = dict(imgs = [])

#ATTACKS-------------------------------------------------------------------------------------------

attacks = dict(
    fire = dict(
        left = 'attacks/Fire/fireLeft.png',
        right = 'attacks/Fire/fireRight.png',
        up = 'attacks/Fire/fireUp.png',
        down = 'attacks/Fire/fireDown.png',
        damage = 0.5,
        manaSpent = 5,
        key = 'j',
        speed = 200),

    ice = dict(
        left = 'attacks/Ice/ice.png',
        right = 'attacks/Ice/ice.png',
        up = 'attacks/Ice/ice.png',
        down = 'attacks/Ice/ice.png',
        damage = 0.3,
        manaSpent = 5,
        key = 'k',
        speed = 150),

    bolt = dict(
        left = 'attacks/Bolt/boltLeft.png',
        right = 'attacks/Bolt/bolt.png',
        up = 'attacks/Bolt/boltUp.png',
        down = 'attacks/Bolt/boltDown.png',
        damage = 0.3,
        manaSpent = 6,
        key = 'l',
        speed = 300),

    swAttack = dict(
        left = Sprite('attacks/Sword/swordRight.png',4),
        right = Sprite('attacks/Sword/swordRight.png',4),
        up = Sprite('attacks/Sword/swordRight.png',4),
        down = Sprite('attacks/Sword/swordRight.png',4),
        damage = 0.5,
        manaSpent = 0,
        key = 'u',
        colTime = 0,
        drawTime = 0,
        nGif = 0,
        spr = 0))

#Keyboard & Mouse------------------------------------------------------------------------------------------------
kb = Window.get_keyboard()
ms = Window.get_mouse()