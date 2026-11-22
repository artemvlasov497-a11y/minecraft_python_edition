from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from time import sleep

app = Ursina()

plr = FirstPersonController(position=(5, 15, 5))

blocks = []

for x in range(0, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            block = Entity(model='cube', collider='box', position=(x, y, z), texture='dirt')
            blocks.append(block)

plr.speed = 10
plr.gravity = 1

Sky()
app.run()
