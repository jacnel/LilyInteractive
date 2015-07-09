import pyglet
from win32api import GetSystemMetrics
import math

screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)

def show_gif(filename):
        ag_file = filename
        animation = pyglet.resource.animation(ag_file)
        sprite = pyglet.sprite.Sprite(animation)
        #scale image
        scale_w = (screen_width/sprite.width)
        scale_h = (screen_height/sprite.height)
        sprite.scale = min(scale_w, scale_h)
        sprite.set_position((screen_width/2 - sprite.width/2), (screen_height/2 - sprite.height/2))
        #background image
        img = pyglet.image.load("ZooGifs/zoobackground.jpg")
        background = pyglet.sprite.Sprite(img)
        # create a window and set it to the image size
        win = pyglet.window.Window(width = screen_width, height = screen_height)
        win.set_location(0,20)
        #self.set_topmost(win)
        # set window background color = r, g, b, alpha
        # each value goes from 0.0 to 1.0
        white = 1, 1, 1, 1
        pyglet.gl.glClearColor(*white)
        @win.event
        def on_draw():
            win.clear()
            background.draw()
            sprite.draw()
        @sprite.event
        def on_animation_end():
            win.close()
        pyglet.app.run()

