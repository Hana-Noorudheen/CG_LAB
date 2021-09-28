from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math


def clearscreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-100, 100, -100, 100)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)


def setpixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def circle_midpoint(r, xc, yc):
    x, y = 0, r
    setpixel(x+xc, y+yc)
    setpixel(x+xc, -y+yc)
    setpixel(y+xc, x+yc)
    setpixel(-y+xc, x+yc)

    p = 1-r
    while x < y:
        x = x+1
        if p < 0:
            p = p+2*x+1
        else:
            y = y-1
            p = p+2*x-2*y+1

        setpixel(x+xc, y+yc)
        setpixel(-x+xc, y+yc)
        setpixel(-x+xc, -y+yc)
        setpixel(x+xc, -y+yc)
        setpixel(y+xc, x+yc)
        setpixel(-y+xc, x+yc)
        setpixel(-y+xc, -x+yc)
        setpixel(y+xc, -x+yc)


def circle_polar(r, xc, yc):
    x, y = 0, r
    angle = 0
    end_angle = (22/7)/4

    while angle <= end_angle:
        angle = angle+0.001
        x = math.cos(angle)*r
        y = math.sin(angle)*r

        setpixel(x+xc, y+yc)
        setpixel(-x+xc, y+yc)
        setpixel(-x+xc, -y+yc)
        setpixel(x+xc, -y+yc)
        setpixel(y+xc, x+yc)
        setpixel(-y+xc, x+yc)
        setpixel(-y+xc, -x+yc)
        setpixel(y+xc, -x+yc)


def circle_nonpolar(r, xc, yc):
    x, y = 0, r

    while x <= y:
        y = y-0.01
        x = math.sqrt(r*r-y*y)

        setpixel(x+xc, y+yc)
        setpixel(-x+xc, y+yc)
        setpixel(-x+xc, -y+yc)
        setpixel(x+xc, -y+yc)
        setpixel(y+xc, x+yc)
        setpixel(-y+xc, x+yc)
        setpixel(-y+xc, -x+yc)
        setpixel(y+xc, -x+yc)


def main():
    ch = 0
    while(ch != 4):
        ch = int(input("Enter\n 1 for Circle Mid point Algorithm \n 2 for Circle Polar Algorithm\n 3 for Circle NonPolar Algorithm\n 4.exit\n"))

        if(ch == 1 or ch == 2 or ch == 3):

            r = float(input("Radius:"))
            xc = float(input("xcoordinate:"))
            yc = float(input("ycoordinate:"))

            glutInit()
            glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
            glutInitWindowSize(500, 500)
            glutInitWindowPosition(200, 200)

            if int(ch) == 1:
                glutCreateWindow("Circle midpoint algorithm")
                glutDisplayFunc(lambda: circle_midpoint(r, xc, yc))

            if int(ch) == 2:
                glutCreateWindow("Polar algorithm")
                glutDisplayFunc(lambda: circle_polar(r, xc, yc))

            if int(ch) == 3:
                glutCreateWindow("Nonpolar algorithm")
                glutDisplayFunc(lambda: circle_nonpolar(r, xc, yc))
            clearscreen()
            glutMainLoop()

        else:
            print("Invalid Choice")


main()


