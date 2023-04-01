from ursina import *

app = Ursina()
me = Animaion('assets\player', collider='box', y=5)
sky()
camera.orthographics = True
camera.fov = 20

Entity(
    model='quaid',
    texture='assets\BG',
    scale=36,
    z=1
)
def update():
    me.y += held_keys['w']*6*time.dt
    me.y -= held_keys['s']*6*time.dt
    a = held_keys['w']*-20
    b = held_keys['s']*20
    if a != 0:
        me.rotation_z = a
    else:
        me.rotation_z = b

    def input(key):
        if key == 'space':
            e = Entity(
                y=me.y,
                x=me.x+2,
                model='cube',
                texture
            )