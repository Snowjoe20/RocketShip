from Graphics import *




class Rocket(object):
    def __init__(self, x, y, color, win):
        self.x = x
        self.y = y
        self.color = color
        self.buildBooster(x,y, color, win)

    def buildBosster(self, x, y, color, win):
        body = Rectangle(Point(x,y),Point(x +55, y +275))
        body.setFill(color)
        engin = Polygon(Point(x,y +275),Point(x +50,y +275),Point(x +62.5,y +300),Point(x -25,y + 300))
        engin.setFill(color)
        cap = Polygon(Point(x,y),Point(x +25,y -25),Point(x +50,y))
        cap.setFill(color)
        body.draw(win)
        engin.draw(win)
        cap.draw(win)





class Capsule(object):
    def __init__(self,win):
        window = Circle(Point(475,200),10.5)
        cap = Polygon(Point(550,250),Point(550,200),Point(500,150),Point(450,150),Point(400,200),Point(400,250))
        cap.setFill('orange')
        cap.draw(win)
        body = Rectangle(Point(400,250),Point(550,525))
        body.draw(win)
        eng1 = Rectangle(Point(400,525),Point(550,575))
        eng2 = Rectangle(Point(425,575),Point(525,600))
        eng1.draw(win)
        eng2.draw(win)







class RocketShip(object):
    def __init__(self,win):
        cap = Capsule
        boost = Rocket(575,275,"red",win)
        boost = Rocket(325,275, "red", win)
        
