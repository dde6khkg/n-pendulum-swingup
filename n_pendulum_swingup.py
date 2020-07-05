import pyglet

window_size = ()
window = pyglet.window.Window(*window_size)

label = pyglet.text.Label('Title')

@window.event
def on_draw():
    window.clear()
    label.draw()

if __name__ == '__main__':
    pyglet.app.run()
