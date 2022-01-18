import core
from Pong.balle import Balle
from Pong.carte import Carte
from Pong.joueur import JoueurUn, JoueurDeux

def setup():
    print("Start Setup---------")

    core.fps = 30
    core.WINDOW_SIZE = [800, 800]
    core.memory("Balle", Balle())
    core.memory("JoueurUn", JoueurUn())
    core.memory("JoueurDeux", JoueurDeux())
    core.memory("Carte", Carte())

    print("END Setup---------")

def run():

    core.cleanScreen()

    core.memory("Balle").draw(core.screen)
    core.memory("Balle").move()
    core.memory("Balle").dead()
    core.memory("Balle").border()
    core.memory("JoueurUn").draw(core.screen)
    core.memory("JoueurDeux").draw(core.screen)

    if core.getKeyPressList("z"):
        core.memory("JoueurUn").moveup()
        core.memory("JoueurUn").borderup()

    if core.getKeyPressList("s"):
        core.memory("JoueurUn").movedown()
        core.memory("JoueurUn").borderdown()

    if core.getKeyPressList("o"):
        core.memory("JoueurDeux").moveup()
        core.memory("JoueurDeux").borderup()

    if core.getKeyPressList("l"):
        core.memory("JoueurDeux").movedown()
        core.memory("JoueurDeux").borderdown()

    if core.memory("Balle").position.x < 40 and core.memory("JoueurUn").positionh.y <= core.memory("Balle").position.y <= core.memory("JoueurUn").positionl.y:
        core.memory("Balle").bounce()

    if core.memory("Balle").position.x > 760 and core.memory("JoueurDeux").positionh.y <= core.memory("Balle").position.y <= core.memory("JoueurDeux").positionl.y:
        core.memory("Balle").bounce()

core.main(setup, run)