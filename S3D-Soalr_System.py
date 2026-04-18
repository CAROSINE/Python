from vpython import *

scene.background = color.black

sun = sphere(pos=vector(0,0,0), radius=1, color=color.yellow)
earth = sphere(pos=vector(3,0,0), radius=0.3, color=color.blue, make_tail= True)
mars = sphere(pos=vector(5,0,0), radius=0.5, color=color.red, make_tail= True)

t = 0
while True:
    rate(50)
    earth.pos = vector(3*cos(t), 3*sin(t), 0)
    mars.pos = vector(5*cos(t), 5*sin(t*0.8), 0)
    t += 0.05