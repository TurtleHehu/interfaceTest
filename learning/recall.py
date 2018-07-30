import easygui as g
import numpy as np

from PIL import Image
import matplotlib.image as mpimg

g.msgbox('欢迎',title='这仅仅是一个弹窗！')
choice = ['奥迪','捷豹']
g.choicebox(msg='请选择你最喜欢的车！',title='选车了',choices=choice)
g.ccbox(msg='喜欢这个封面么',title='投票',image='C:\\Users\\wildTurtle\\Desktop\\入职资料\\15118573895837797.gif')
img = Image.open('C:\\Users\\wildTurtle\\Desktop\\入职资料\\15118573895837797.gif')
img.show()
img.save('C:\\Users\\wildTurtle\\Desktop\\入职资料\\new.gif')

lena = mpimg.imread('C:\\Users\\wildTurtle\\Desktop\\入职资料\\new.gif')
im = Image.fromarray(np.uint8(lena*255))
im.show()