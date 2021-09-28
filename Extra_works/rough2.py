# from OpenGL.GL import *
# from OpenGL.GLU import *     
# from OpenGL.GLUT import *    
# import sys
# import math



# def clearScreen():
#     glClearColor(0.0, 0.0, 0.0, 1.0)
#     gluOrtho2D(-1.0, 1.0,-1.0,1.0)



# def main():
#     glutInit(sys.argv)
#     glutInitDisplayMode(GLUT_RGB)
#     glutCreateWindow("Horizontal Line")
#     glutInitWindowSize(500, 500)
#     glutInitWindowPosition(50, 50)
#     glutDisplayFunc(lambda:drawClippingWindow(10,40,10,40))
#     clearScreen()
#     glutMainLoop()





# def drawClippingWindow(xWinMin, xWinMax, yWinMin, yWinMax):
#     edges = [
#         [0, 1],
#         [1, 2],
#         [2, 3],
#         [0, 3]
#     ]
#     points = [
#         [xWinMin, yWinMin],
#         [xWinMax, yWinMin],
#         [xWinMax, yWinMax],
#         [xWinMin, yWinMax]
#     ]
#     rgb = (1.0, 1.0, 1.0)

#     drawLines(edges, points, rgb)

# def drawLines(edges, points, rgb):

#     glColor3f(rgb[0], rgb[1], rgb[2])
#     for e in edges:
#         for v in e:
#             glVertex2fv(points[v])
xWinMin,yWinMin,xWinMax,yWinMax=10,10,40,40

points = [
        [xWinMin, yWinMin],
        [xWinMax, yWinMin],
        [xWinMax, yWinMax],
        [xWinMin, yWinMax]
    ]


edges = [
        [0, 1],
        [1, 2],
        [2, 3],
        [0, 3]
    ]
for e in edges:
        for v in e:
            print(points[v])


