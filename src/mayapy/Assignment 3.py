__author__ = 'Peipei'

from nimble import cmds
# Create a sphere, with 10 subdivisions in the X direction,
# and 15 subdivisions in the Y direction,
# the radius of the sphere is 20.
cmds.polySphere(sx=10, sy=15, r=2)

#translate the sphere to some location
cmds.move(4.0, 4.0, 0.0, relative=True)


import maya.cmds as mc        # import maya.cmds in order to access the Maya commands

for i in range(24):        # 24 steps in this staircase

    mc.polyCube(width=2)        # each step is 2 units wide
    mc.move(3, i, 0)        # move it over 3 in X and up in Y based on its index number
    mc.xform(ws=True, rotatePivot=(0,0,0))        # move its rotation pivot to the center of world space
    mc.rotate(0, 15*i, 0)        # rotate the step by 15 degrees times its index number


import maya.cmds as mc
from random import uniform as rand        # import python's random.uniform module and give it a nickname

for i in range(20):        # create 20 of these

mc.polySphere(radius=rand(0.2,1))        # create a sphere with random radius
mc.move(rand(-5,5),rand(-5,5), rand(-5,5))        # move to a random position within a 10x10x10 cube

#A bouncing ball
import maya.cmds as mc
mc.playbackOptions( minTime='0', maxTime='84' ) # set playback range

g = -0.3        # gravity
py = 12        # position
px = 0
pz = 0
vx = 1.0        # velocity
vy = 2.8
vz = 0.0
numSteps = 12        # number of sub-calculation steps (more steps = better accuracy)

ball = mc.polySphere( name = 'bouncing', radius = 2 ) # create a sphere
for f in range(84):        # for the first 84 frames (starting from 0 and ending with 83)

    for sub in range(numSteps):        # for each frame calculate sub-steps
        dt = 1.0/numSteps        # amount of time passed since last calculation
        t = f+dt*sub        # the current time
        vy = vy + g*dt        # adjust velocity with gravity
        if(py < 2.0):        # if ball hits the floor
           vy = -0.6*vy;
           vx = 0.75*vx;
           vz = 0.75*vz;
           py = 2.0;
        else:
           px = px + vx*dt        # adjust position with velocity
           pz = pz + vz*dt

        py = py + vy*dt

    mc.setKeyframe( ball, attribute='translateX', value=px, t=f )        # set keyframes
    mc.setKeyframe( ball, attribute='translateY', value=py, t=f )
    mc.setKeyframe( ball, attribute='translateZ', value=pz, t=f )



