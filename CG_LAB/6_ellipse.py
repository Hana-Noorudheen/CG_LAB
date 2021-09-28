from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math


def clearscreen():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-100, 100, -100, 100)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)


def setpixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def ellipse_polar(rx, ry, xc, yc):
    x, y = 0, ry
    angle = 0
    end_angle = (22/7)/2

    while angle<=end_angle:
        angle=angle+0.001

        x=math.cos(angle)*rx
        y=math.sin(angle)*ry

        
        setpixel(x+xc,y+yc)
        setpixel(-x+xc,y+yc)
        setpixel(-x+xc,-y+yc)
        setpixel(x+xc,-y+yc)    


def ellipse_nonPolar(a, b, xc, yc):
    x, y = 0, b

    while  x<=a:
        x=x+0.01
        y=b*(math.sqrt(abs(1-((x*x)/(a*a)))))

        setpixel(x+xc,y+yc)
        setpixel(-x+xc,y+yc)
        setpixel(-x+xc,-y+yc)
        setpixel(x+xc,-y+yc) 


def main():


    ch=0
    while(ch!=3):
        ch=int(input("Enter\n 1 for Ellipse polar Algorithm \n 2 for Ellipse NonPolar Algorithm\n"))

        if(ch==1 or ch==2 ):
            rx=int(input('rx='))
            ry=int(input('ry='))
            xc=int(input('xc='))
            yc=int(input('yc='))
    
            glutInit()
            glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
            glutInitWindowSize(500,500)
            glutInitWindowPosition(200,200)
    
    
            if int(ch)==1:
                glutCreateWindow("Polar algorithm")
                glutDisplayFunc(lambda: ellipse_polar(rx, ry, xc, yc))
                   
            if int(ch)==2:
    
                glutCreateWindow("Nonpolar algorithm")
                glutDisplayFunc(lambda: ellipse_nonPolar(rx, ry, xc, yc))
            clearscreen()
            glutMainLoop()    
            
        else:
            print("Invalid Choice")
           
main()



















