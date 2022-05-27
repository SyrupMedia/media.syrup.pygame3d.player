#region Modules

# System management
import sys

# Pygame
import pygame 
from pygame.locals import *

# OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

# Model handling
import pywavefront

#endregion

#region Variables

windowWidth:int = 1366
windowHeight:int = 768 

# Example cube
"""
cubeVertices = ((1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1),(-1,-1,1),(-1, 1,-1))
cubeEdges = ((0,1),(0,3),(0,4),(1,2),(1,7),(2,5),(2,3),(3,6),(4,6),(4,7),(5,6),(5,7))
cubeQuads = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))
"""

#endregion

"""
def DrawCube():
    glBegin(GL_QUADS)
    for cubeQuad in cubeQuads:
        for cubeVertex in cubeQuad:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()
"""

def Model():
    glPushMatrix()
    glScalef(*obj_scale)
    glTranslatef(*obj_trans)

    for mesh in obj.mesh_list:
        glBegin(GL_TRIANGLES)
        for face in mesh.faces:
            for vertex_i in face:
                glVertex3f(*obj.vertices[vertex_i])
        glEnd()

    glPopMatrix()

def Update():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    Model()

    pygame.display.flip() # Update the frames
    pygame.time.wait(10)


if __name__ == "__main__":
    # Pygame initialisation
    pygame.init()
    display = (int(windowWidth), int(windowHeight))
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) # Enables OpenGL with *double buffering*

    obj = pywavefront.Wavefront('Suzanne.obj', collect_faces=True)
    obj_box = (obj.vertices[0], obj.vertices[0])

    for vertex in obj.vertices:
        min_v = [min(obj_box[0][i], vertex[i]) for i in range(3)]
        max_v = [max(obj_box[1][i], vertex[i]) for i in range(3)]
        obj_box = (min_v, max_v)

    obj_trans = [-(obj_box[1][i]+obj_box[0][i])/2 for i in range(3)]

    scaled_size = 5
    obj_size = [obj_box[1][i]-obj_box[0][i] for i in range(3)]
    max_obj_size = max(obj_size)
    obj_scale = [scaled_size/max_obj_size for i in range(3)]

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    glTranslatef(0, 0, -5)

    while True:
        # Check if the application should quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        """
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                glTranslatef(0, 0, -0.1)
            elif event.key == K_DOWN:
                glTranslatef(0, 0, 0.1)
            elif event.key == K_LEFT:
                glTranslatef(-0.1, 0, 0)
            elif event.key == K_RIGHT:
                glTranslatef(0.1, 0, 0)
        """

        Update()

