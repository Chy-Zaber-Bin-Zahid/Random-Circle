from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

WINDOW_WIDTH  = 500
WINDOW_HEIGHT = 500

createdCircles = []
clickedX, clickedY, r = 0, 0, 0

class AABB:
    x = 0
    y = 0
    w = 0
    h = 0

    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
    
    def collides_with(self, other):
        return (self.x < other.x + other.w and # x_min_1 < x_max_2
                self.x + self.w > other.x  and # x_max_1 > m_min_2
                self.y < other.y + other.h and # y_min_1 < y_max_2
                self.y + self.h > other.y)     # y_max_1 > y_min_2
    
def is_circle_outside_window(circle,r):
    x, y = circle  
    if x<250 and y< 250:
        return x - r < 0 and x + r - 200 > WINDOW_WIDTH or y - r < 0 and y + r - 200 > WINDOW_HEIGHT
    elif x<250 and y>250:
        return x - r +400 < 0 and x + r  > WINDOW_WIDTH or y - r +400 < 0 and y + r > WINDOW_HEIGHT
    elif x>250 and y<250:
        return x - r +350 < 0 and x + r  > WINDOW_WIDTH or y - r +350 < 0 and y + r > WINDOW_HEIGHT
    else:
        return x - r < 0 and x + r - 400 > WINDOW_WIDTH or y - r < 0 and y + r - 400 > WINDOW_HEIGHT

def convert_coordinate(x, y):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    # Adjust the y-coordinate to match the expected coordinate system
    adjusted_y = WINDOW_HEIGHT - y
    return x, adjusted_y

def mouseListener(button, state, x, y):
    global clickedX, clickedY, r, createdCircles
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):  
            print("clicked")          
    if button==GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN: 	
            clickedX, clickedY = convert_coordinate(x,y)
            createdCircles.append((clickedX,clickedY))
    
    glutPostRedisplay()


def initialize():
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, WINDOW_WIDTH, 0.0, WINDOW_HEIGHT, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def circlePoints(x,y,cx,cy):
    glVertex2f(x + cx,y + cy)
    glVertex2f(y + cx,x + cy)

    glVertex2f(y + cx,-x + cy)
    glVertex2f(x + cx,-y + cy)

    glVertex2f(-x + cx,-y + cy)
    glVertex2f(-y + cx,-x + cy)

    glVertex2f(-y + cx,x + cy)
    glVertex2f(-x + cx,y + cy)

def midPointCircle(x1,y1,r):
    d = 1-r
    x = 0
    y = r
    circlePoints(x,y,x1,y1)
    
    while (x<y):
        if d<0:
            d=d+(2*x)+3        
        else:
            d=d+(2*x)-(2*y)+5
            y-=1
        x+=1
        circlePoints(x,y,x1,y1)


def drawLine(x,y,r):
    glBegin(GL_POINTS)
    midPointCircle(x,y,r)
    glEnd()


def show_screen():
    global clickedX, clickedY, r
    # clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # glColor3f(r, g, b)
    drawLine(clickedX, clickedY, r)


    glutSwapBuffers()




def animation():
    global clickedX, clickedY, r, createdCircles
    if clickedX != 0 or clickedY != 0: 
        r+=.5
        # remove_circles_outside_window()
        print(createdCircles)
    
        for i, circle in enumerate(createdCircles):
            if is_circle_outside_window(circle,r):
                createdCircles.pop()
                print(f"Circle {i + 1} outside the window: {circle}")



    glutPostRedisplay()



glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Make Circle!")

glutDisplayFunc(show_screen)
glutIdleFunc(animation)
glutMouseFunc(mouseListener)

# glutKeyboardFunc(keyboard_ordinary_keys)
# glutMouseFunc(mouse_click)

glEnable(GL_DEPTH_TEST)
initialize()
glutMainLoop()
