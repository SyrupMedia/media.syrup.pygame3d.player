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

obj = pywavefront.Wavefront('../Assets/Suzanne.obj', collect_faces=True)

windowWidth: int = 1366
windowHeight: int = 768

#endregion

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
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    Model()

    pygame.display.flip()  # Update the frames
    pygame.time.wait(10)


if __name__ == "__main__":
    # Pygame initialisation
    pygame.init()
    display = (int(windowWidth), int(windowHeight))
    # Enables OpenGL with *double buffering*
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

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

    glTranslatef(0, 0, -10)

    while True:
        # Check if the application should quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        Update()