# written by tonydsas
# https://www.github.com/tonydsas
# please see LICENSE for more info

doTerminalClears = True

class screen:
    def __init__(self,y,x):
        self.y = y
        self.x = x
        self.screenX = []
        self.screen = []
        for i in range(self.x):
            self.screenX.append(" ")
        for i in range(self.y):
            self.screen.append(self.screenX.copy())
    
    def renderOutput(self):
        for i in self.screen:
            outputString = ""
            for v in i:
                outputString += v
            print(outputString)
    
    def addOutput(self,xPos:int,yPos:int,character:int):
        if len(character) != 1:
            return
        if len(self.screen) < yPos:
            return
        if len(self.screen[yPos]) < xPos:
            return
        self.screen[yPos][xPos] = character
    
    def addString(self,xPos:int,yPos:int,string:str):
        if len(self.screen) < yPos:
            return
        if xPos + len(string) > len(self.screen[yPos]):
            return
        ptr = 0
        for i in string:
            self.screen[yPos][xPos+ptr] = i
            ptr += 1
    def debugOutput(self):
        print(self.screen)
