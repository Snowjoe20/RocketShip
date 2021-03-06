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
        engin.setFill('white')
        cap = Polygon(Point(x,y),Point(x +25,y -25),Point(x +55,y))
        cap.setFill(color_rgb(63, 59, 59))
        body.draw(win)
        engin.draw(win)
        cap.draw(win)
        bar = Line(Point(380,400),Point(400,400))
        bar.setWidth(10)
        bar2 = Line(Point(550, 400), Point(575, 400))
        bar2.setWidth(10)
        bar.draw(win)
        bar2.draw(win)
        bar.setFill('white')
        bar2.setFill('white')




class Capsule(Rocket):
    def __init__(self,x,y,win):
        super(Capsule,self).__init__(x,y,win)
        self.drawBody(win)
        self.drawEng(win)
        self.drawTop(win,x,y)
    def drawTop(self, win,x,y):
        cap = Polygon(Point(self.x,self.y),Point(self.x,self.y - 50),Point(self.x + 50,self.y - 100),Point(self.x + 100,self.y - 100),Point(self.x + 150,self.y - 50),Point(self.x + 150,self.y))
        cap.setFill(color_rgb(119, 23, 23))
        cap.draw(win)
        pole = Rectangle(Point(450,50), Point(500,150))
        pole.draw(win)
        pole.setFill(color_rgb(112, 14, 14))
        tri = Polygon(Point(450,50), Point(475,25), Point(500,50))
        tri.draw(win)
        tri.setFill(color_rgb(63, 59, 59))
        image1 = Image(Point(475, 100), "capLogo.png")
        image1.draw(win)
    def drawBody(self, win):
        body = Rectangle(Point(400,250),Point(550,525))
        body.draw(win)
        body.setFill(color_rgb(124, 13, 13))
    def drawEng(self, win):
        eng1 = Rectangle(Point(400,525),Point(550,575))
        eng2 = Rectangle(Point(425,575),Point(525,600))
        eng1.draw(win)
        eng2.draw(win)
        eng1.setFill('grey')
        eng2.setFill('white')



class RocketShip(object):
    def __init__(self,win):
        cap = Capsule(400,250,win)
        boost = Rocket(575,275,win)
        boost = Rocket(325,275, win)

