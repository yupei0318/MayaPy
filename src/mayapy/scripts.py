__author__ = 'Peipei'

Here goes another tool for productivity. No more scrolling in attr editor for pan/zoom :)

How to:
1. copy script to script editor in Python tab, select all text and then MM drag it to your shelf.
2. select a camera
3. hit the little icon with a looking glass over the viewport
4. press in your shelf button to launch
5. have fun



import maya.cmds as cmds

cam=cmds.ls(sl=True)
if len(cam)<1:
    cmds.confirmDialog(message="select a camera")
else:
    camShape=cmds.listRelatives(cam)

def reset():
    cmds.panZoom(camShape,abs=True,z=1)
    cmds.panZoom(camShape,abs=True,l=0)
    cmds.panZoom(camShape,abs=True,d=0)
    cmds.floatSliderGrp(valZ, edit=True, value=1)
    cmds.floatSliderGrp(valX, edit=True, value=0)
    cmds.floatSliderGrp(valY, edit=True, value=0)

def paniZoom():
    zoomRate=cmds.floatSliderGrp(valZ, query=True, value=True)
    cmds.panZoom(camShape,abs=True,z=zoomRate)

    widthRate=cmds.floatSliderGrp(valX, query=True, value=True)
    cmds.panZoom(camShape,abs=True,l=widthRate)

    depthRate=cmds.floatSliderGrp(valY, query=True, value=True)
    cmds.panZoom(camShape,abs=True,d=depthRate)

windowZ=cmds.window(title="Zoom/pan",w=350,h=250)
cmds.columnLayout(w=150,adj=True)
valZ=cmds.floatSliderGrp(label="Zoom", field=True,dc="paniZoom()",value=1,min=-0.001,max=1,pre=3)
valY=cmds.floatSliderGrp(label="Vertical Pan", field=True,dc="paniZoom()",value=0,min=-1,max=1,pre=3)
valX=cmds.floatSliderGrp(label="Horizontal Pan", field=True,dc="paniZoom()",value=0,min=-1,max=1,pre=3)

resetButton=cmds.button(label="reset", c="reset()")
cmds.showWindow(windowZ)
cmds.panZoom(camShape,abs=True,z=10)

reset()

##################################################
import maya.cmds as cmds

bubble = cmds.polySphere( name = 'bubble', radius = 0.2) # create a sphere
obj = cmds.camera()
cmds.rename(obj[0], "bubbleCam")
cmds.aimConstraint( "bubble", 'bubbleCam', skip=["x", "z"])

    #for f in range(72):        # for the first 84 frames (starting from 0 and ending with 83)

for time in [1, 15, 30, 45, 60, 72]:        # for each frame calculate sub-steps


        #mc.setKeyframe( bubble, attribute='translateX', value=px, t=f )        # set keyframes
    cmds.setKeyframe( bubble, attribute='translateY',  value=size+0.1*time, t=time )
    cmds.setKeyframe( bubble, attribute='scaleX', value=size+0.02*time,  t=time )
    cmds.setKeyframe( bubble, attribute='scaleY', value=size+0.02*time,  t=time )
    cmds.setKeyframe( bubble, attribute='scaleZ', value=size+0.02*time,  t=time )

    cmds.setKeyframe()



###############################

import maya.cmds as cmds

# To create a plugin of type "squash" on the selected object.
# First, load the plugin. The deformer command will not autoload
# your plugin. Then, select the geometries that you'd like to deform,
# and use the deformer command as follows. For example, to deform a
# cylinder with a squash:
#
cmds.cylinder( ax=(0, 1, 0), r=1, hr=10, d=3, s=8, nsp=20, ch=1 )
cmds.select( 'nurbsCylinder1', r=True )
cmds.deformer( type="squash" )

# To query the membership of the deformer
#
cmds.deformer( 'squash1',q=True, g=True )

# To add additional geometries from your deformer, type:
#
cmds.select( 'nurbsCylinder1', r=True )
cmds.duplicate()
# Result: nurbsCylinder2 #
cmds.move( -2.749017, 0, 0, r=True )
cmds.deformer( 'squash1', e=True, g='nurbsCylinder2' )

# To remove a geometry from your deformer, type:
#
cmds.deformer( 'squash1', e=True, rm=True, g='nurbsCylinder2' )


########################


#for maya
import maya.cmds as cmds
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

#cmds.rename(obj[1], "bubbleCamShape")


# Save the current position of the persp camera.
homeName = cmds.cameraView(camera='persp')

# Add this view to the persp bookmark menu.
cmds.cameraView( homeName, e=True, camera='bubbleCam', ab=True )

# Change the persp camera position.
cmds.dolly( 'bubbleCam', distance=-30 )

# Create another bookmark for the zoomed position.
cmds.cameraView( camera='bubbleCam', name='zoom', ab=True )

# Restore original camera position.
cmds.cameraView( homeName, e=True, camera='bubbleCam', sc=True )

# Save the current 2D pan/zoom attributes of the persp camera
panZoomBookmark = cmds.cameraView( camera='bubbleCam', ab=True, typ=1 )

# Enable 2D pan/zoom
cmds.setAttr( 'bubbleCamShape.panZoomEnabled', True )

# Pan right
cmds.panZoom( 'bubbleCam', r=0.6 )

# Restore original film position
#cmds.cameraView( panZoomBookmark, e=True, camera='persp', sc=True )






