__author__ = 'Peipei'

from nimble import cmds



from random import uniform as rand


def create_bubbles():
    size = rand(0.01,0.04)
    cmds.scale(0.1,0.3,0.1)
    cmds.move(0,0.4,0)
    cube = cmds.polyCube (w=5, d=5, h=4)
    cmds.move(0, 1.5, 0)


    cmds.sets( renderable=True, noSurfaceShader=True, empty=True, name='ph' + 'SG' )
    myShader = cmds.shadingNode( 'phongE', asShader=True, name='ph' )


    #cmds.shadingNode('lambert', name= 'ph', asShader= True)
    cmds.setAttr( myShader+'.color', 0, 1, 1, type='double3')
    cmds.setAttr (myShader+'.transparency', 1, 0.6, 0.6, type = 'double3')
    cmds.select(cube)
    cmds.hyperShade(assign= myShader)

    #cmds.displaySurface(xRay=True)
    #cmds.connectAttr('ph'+'.outColor', 'ph'+'SG.surfaceShader')
    #cmds.sets(cube, edit=True, forceElement='ph'+'SG')
    #cmds.move (0, 2, 0)

    for i in range (20):
        # set playback range

        cmds.playbackOptions( minTime=i+rand(1,4), maxTime='72' )
        bubble= cmds.polySphere( name='bubble'+str(i), radius = rand(0.2,0.4)) # create a sphere
        cmds.move(rand(-2,2),rand(-2,2), rand(-2,2))
        cmds.select('bubble'+str(i))
        cmds.lattice( dv=(5, 6, 5), oc=True)
        cmds.select('ffd'+str(i+1)+'Lattice.pt[0:3][0:1][2]','ffd'+str(i+1)+'Lattice.pt[4][1][2]', 'ffd'+str(i+1)+'Lattice.pt[0:4][2:5][2]', r= True)
        cmds.scale(0.33, 0.33, 0.33, relative = True)
        cmds.select('ffd'+str(i+1)+'Lattice.pt[0][1][3]', 'ffd'+str(i+1)+'Lattice.pt[2][3][4]', r=True)
        cmds.move(0, 0, -0.05, relative = True)
        cmds.select ('ffd'+str(i+1)+'Lattice.pt[2][3][0]')
        cmds.move(0, 0, 0.8, relative = True)
        #cmds.select('bubble'+str(i))



        for time in [1, 15, 30, 45, 60, 72]:        # for each frame calculate sub-steps

        #mc.setKeyframe( bubble, attribute='translateX', value=px, t=f )        # set keyframes
            cmds.setKeyframe( bubble, attribute='translateY',  value=0.002*time*i, t=time )
            cmds.setKeyframe( bubble, attribute='scaleX', value=size+0.001*time*i,  t=time )
            cmds.setKeyframe( bubble, attribute='scaleY', value=size+0.001*time*i,  t=time )
            cmds.setKeyframe( bubble, attribute='scaleZ', value=size+0.001*time*i,  t=time )


create_bubbles()