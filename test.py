import pyglet
def show_gif(name):
    ag_file = name
    animation = pyglet.resource.animation(ag_file)
    sprite = pyglet.sprite.Sprite(animation)
    # create a window and set it to the image size
    win = pyglet.window.Window(width=sprite.width, height=sprite.height)
    # set window background color = r, g, b, alpha
    # each value goes from 0.0 to 1.0
    white = 1, 1, 1, 1
    pyglet.gl.glClearColor(*white)
    @win.event
    def on_draw():
        win.clear()
        sprite.draw()
    pyglet.app.run()

