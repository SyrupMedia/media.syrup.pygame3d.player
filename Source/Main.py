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

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    pygame.display.flip()  # Update the frames
    pygame.time.wait(10)


if __name__ == "__main__":
    # Pygame initialisation
    pygame.init()
    display = (int(windowWidth), int(windowHeight))
    # Enables OpenGL with *double buffering*
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glLight(GL_LIGHT0, GL_POSITION,  (1, 5, 1, 0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (2, 2, 2, 1))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (2, 2, 2, 1))
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )


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

        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                glTranslatef(0, 0, -0.1)
            elif event.key == K_DOWN:
                glTranslatef(0, 0, 0.1)
            elif event.key == K_LEFT:
                glTranslatef(-0.1, 0, 0)
            elif event.key == K_RIGHT:
                glTranslatef(0.1, 0, 0)

        Update()