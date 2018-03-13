from RocketShip import *

window = GraphWin("RocketShip", 1000, 650,'white')


def main():

    RocketShip(window)
    window.getMouse()
    window.close()

main()