import math
import pygame
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)

size = 1200,600
screen = pygame.display.set_mode((size))
screen.fill(WHITE)

#---------------------------------------------------------------------------
#Changable variables
ball_colour = (200,0,0)
ball_size = 20
pos  = [600,80] #starting positions of each ball
pos2 = [580,80]
pos3 = [540,80]
pos4 = [520,80]
velocity  = [0,0] #starting velocity of each ball
velocity2 = [0,0]
velocity3 = [0,0]
velocity4 = [0,0]
gravity = 0.075/2
time = 2 #delay between frames
l1x1,l1y1,l1x2,l1y2 = 600,550,1100,100 #line 1
l2x1,l2y1,l2x2,l2y2 = 600,550,100,100 #line 2
#---------------------------------------------------------------------------

def draw_ball(pos):
    pygame.draw.circle(screen,ball_colour,pos,ball_size)

def clear_screen(): #clears screen after every iteration of main game loop
    pygame.time.wait(time)
    pygame.display.flip()
    screen.fill(WHITE)
    pygame.draw.line(screen,BLACK,(l1x1,l1y1),(l1x2,l1y2))
    pygame.draw.line(screen,BLACK,(l2x1,l2y1),(l2x2,l2y2))

def update_position(position,velocity,gravity):
    position[0] += velocity[0]
    position[1] += velocity[1]
    velocity[1] += gravity

def dist(x1, y1, x2, y2, x3, y3): # finds distance from point to line segment, x3,y3 is the point
    u =  (((x3 - x1) * (x2-x1) + (y3 - y1) * (y2-y1)) / float((x2-x1)**2 + (y2-y1)**2))
    if u > 1:
        u = 1
    elif u < 0:
        u = 0
    return (((x1 + u * (x2-x1)) - x3)**2 + ((y1 + u * (y2-y1)) - y3)**2)**.5

def reflected_velocity(velocity,x1,y1,x2,y2): #determines velocity vector after bouncing off a line
    n = [y2-y1,-(x2-x1)]
    unitn = [n[0]/math.sqrt((n[0])**2+(n[1])**2),n[1]/math.sqrt((n[0])**2+(n[1])**2)]
    vdotn = velocity[0]*unitn[0]+velocity[1]*unitn[1]
    vec = [(2*vdotn)*unitn[0],(2*vdotn)*unitn[1]]
    return [velocity[0]-vec[0],velocity[1]-vec[1]]

def check_collision(velocity,pos,gx1,gy1,gx2,gy2,ball_size,gravity):
    new_velocity = velocity
    if dist(gx1,gy1,gx2,gy2,pos[0],pos[1])<ball_size+8: #if collison
        new_velocity=reflected_velocity(velocity,gx1,gy1,gx2,gy2)
        new_velocity[1]+=gravity
        velocity[0]=new_velocity[0]
        velocity[1]=new_velocity[1]

running = True
while running:
    #2 function calls per ball(draw_ball,update_position), +1 check_collision per ball for every line
    #1 clear_screen call per iteration

    draw_ball(pos)
    update_position(pos,velocity,gravity)
    check_collision(velocity,pos,l1x1,l1y1,l1x2,l1y2,ball_size,gravity)
    check_collision(velocity,pos,l2x1,l2y1,l2x2,l2y2,ball_size,gravity)

    draw_ball(pos2)
    update_position(pos2,velocity2,gravity)
    check_collision(velocity2,pos2,l1x1,l1y1,l1x2,l1y2,ball_size,gravity)
    check_collision(velocity2,pos2,l2x1,l2y1,l2x2,l2y2,ball_size,gravity)

    draw_ball(pos3)
    update_position(pos3,velocity3,gravity)
    check_collision(velocity3,pos3,l1x1,l1y1,l1x2,l1y2,ball_size,gravity)
    check_collision(velocity3,pos3,l2x1,l2y1,l2x2,l2y2,ball_size,gravity)

    draw_ball(pos4)
    update_position(pos4,velocity4,gravity)
    check_collision(velocity4,pos4,l1x1,l1y1,l1x2,l1y2,ball_size,gravity)
    check_collision(velocity4,pos4,l2x1,l2y1,l2x2,l2y2,ball_size,gravity)

    clear_screen()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
quit()