from Graphics import *




class Rocket(object):
    def __init__(self, x, y, win):
        self.x = x
        self.y = y
        self.buildBooster(x,y, win)

    def buildBooster(self, x, y, win):
        body = Rectangle(Point(x,y),Point(x +55, y +275))
        body.setFill(color_rgb(95,95,95))
        engin = Polygon(Point(x,y +275),Point(x +55,y +275),Point(x +75,y +300),Point(x -25,y + 300))
        engin.setFill('black')
        cap = Polygon(Point(x,y),Point(x +25,y -25),Point(x +55,y))
        cap.setFill(color_rgb(63, 59, 59))
        body.draw(win)
        engin.draw(win)
        cap.draw(win)





class Capsule(object):
    def __init__(self,x,y,win):
        self.drawBody(win)
        self.drawEng(win)
        self.drawTop(win,x,y)
    def drawTop(self, win,x,y):
        cap = Polygon(Point(x,y),Point(x,y - 50),Point(x + 50,y - 100),Point(x + 100,y - 100),Point(x + 150,y - 50),Point(x + 150,y))
        cap.setFill(color_rgb(119, 23, 23))
        cap.draw(win)
        pole = Rectangle(Point(450,50), Point(500,150))
        pole.draw(win)
        pole.setFill(color_rgb(112, 14, 14))
        tri = Polygon(Point(450,50), Point(475,25), Point(500,50))
        tri.draw(win)
        tri.setFill(color_rgb(63, 59, 59))
    def drawBody(self, win):
        body = Rectangle(Point(400,250),Point(550,525))
        body.draw(win)
        body.setFill(color_rgb(124, 13, 13))
    def drawEng(self, win):
        eng1 = Rectangle(Point(400,525),Point(550,575))
        eng2 = Rectangle(Point(425,575),Point(525,600))
        eng1.draw(win)
        eng2.draw(win)
        eng1.setFill(color_rgb(178, 19, 19))
        eng2.setFill('black')





class RocketShip(object):
    def __init__(self,win):
        cap = Capsule(400,250,win)
        boost = Rocket(575,275,win)
        boost = Rocket(325,275, win)

