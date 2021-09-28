from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*


def clearscreen():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-100, 100, -100, 100)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(5.0)

def setpixel(x,y):
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glFlush()

def Line_Midpoint(x1, y1, x2, y2):
    if x1 < x2:
        dx, dy = x2-x1, y2-y1
        x, y, xend = x1, y1, x2
    else:
        dx,dy=x1-x2,y1-y2
        x,y,xend=x2,y2,x1    

   
    setpixel(x,y)
    p=dy-(dx/2)

    while x<xend:
        x=x+1
        if p<0:
            p=p+dy
        else:
            y=y+1
            p=p+dy-dx
        setpixel(x,y)



def main():
    choice=0
   
    while(choice!=2):
        choice=int(input("Enter\n\t1.Plot a line \n\t2.exit\n"))
        if choice==1:
            x1=float(input('x1 Coordinate:'))
            x2=float(input('x2 Coordinate:'))
            y1=float(input("y1 Coordinate:"))
            y2=float(input("y2 Coordinate:"))
        
            glutInit()
            glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
            glutInitWindowSize(500,500)
            glutInitWindowPosition(200,200)
            glutCreateWindow("Line using Midpoint Algorithm")
            glutDisplayFunc(lambda: Line_Midpoint(x1, y1, x2, y2))
            glutIdleFunc(lambda: Line_Midpoint(x1, y1, x2, y2))
            clearscreen()
            glutMainLoop()
        else:
            print("Invalid Choice")    
main()   








