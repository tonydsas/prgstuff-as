from trender import trender

newScreen = trender.screen(8,8)
for i in range(8):
    newScreen.addString(0,i,"#      #")
newScreen.addString(0,0,"########")
newScreen.addString(0,7,"########")

newScreen.renderOutput()