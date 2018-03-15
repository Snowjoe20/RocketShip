from RocketShip import *

window = GraphWin("RocketShip", 1000, 650,'white')
space = Image(Point(500, 325), "backround23.png")
space.draw(window)


def main():

    RocketShip(window)
    window.getMouse()
    window.close()

main()