from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_WIDTH  = 500
WINDOW_HEIGHT = 500

createdCircles = []
stop = "water"

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
def is_circle_outside_window(circle):
    x, y, r = circle[0], circle[1], circle[2]
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
    global createdCircles, stop
    if stop == "water":
      if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
          x, y = convert_coordinate(x, y)
          createdCircles.append([x, y, 0.0])
    
    glutPostRedisplay()

def keyboardListener(key, x, y):
    global stop
    if key==b' ':
      if stop == "water":
          stop = "ice"
          print("Stop!")
      else:
          stop = "water"
          print("Resume!")


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


def drawLine(circle):
    glBegin(GL_POINTS)
    midPointCircle(circle[0], circle[1], circle[2])
    glEnd()

def drawCircles():
    for circle in createdCircles:
        drawLine(circle)


def show_screen():
    global clickedX, clickedY, r
    # clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    drawCircles()

    glutSwapBuffers()




def animation():
    global createdCircles, stop
    if stop == "water":
        for circle in createdCircles:
          circle[2] += 0.5
          if is_circle_outside_window(circle):
              createdCircles.remove(circle)
              print(f"{len(createdCircles)} circle remaining and {circle} removed!")

    glutPostRedisplay()



glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Make Circle!")

glutDisplayFunc(show_screen)
glutIdleFunc(animation)
glutMouseFunc(mouseListener)
glutKeyboardFunc(keyboardListener)

glEnable(GL_DEPTH_TEST)
initialize()
glutMainLoop()
