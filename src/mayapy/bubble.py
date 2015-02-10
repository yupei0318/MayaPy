__author__ = 'Peipei'

from nimble import cmds

def create_bubble():
    cmds.playbackOptions( minTime='0', maxTime='71' ) # set playback range

    size=0.2

    bubble = cmds.polySphere( name = 'bubble', radius = 0.2) # create a sphere

    #for f in range(72):        # for the first 84 frames (starting from 0 and ending with 83)

    for time in [1, 15, 30, 45, 60, 72]:        # for each frame calculate sub-steps


        #mc.setKeyframe( bubble, attribute='translateX', value=px, t=f )        # set keyframes
        cmds.setKeyframe( bubble, attribute='translateY',  value=size+0.1*time, t=time )
        cmds.setKeyframe( bubble, attribute='scaleX', value=size+0.02*time,  t=time )
        cmds.setKeyframe( bubble, attribute='scaleY', value=size+0.02*time,  t=time )
        cmds.setKeyframe( bubble, attribute='scaleZ', value=size+0.02*time,  t=time )
        #mc.setKeyframe( bubble, attribute='translateZ', value=pz, t=f )



create_bubble()
