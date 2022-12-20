# 15DaysOfChristmas
# Cooper Cross
# 12/2/19

import pygame,datetime,random,math,sys
lights = []
MAX_SNOW = 250
SNOW_SPEED = 2
treeStarCounter = 0
def draw_a_tree(surface,leaf_size,x,y,is_trunk=True):
    if is_trunk:
        rect=pygame.rect.Rect(x-25,y-30,50,60)
        pygame.draw.rect(surface,(102,68,34),rect)
        draw_a_tree(surface,leaf_size,x,y-30,False)
    elif leaf_size <= 2:
        return
    else:
        pygame.draw.polygon(surface,(0,134,0),((x-leaf_size/2,y),(x+leaf_size/2,y),(x,y-(2*leaf_size/3))))
        draw_a_tree(surface,3*leaf_size/4,x,y-leaf_size/3,False)
        # TREE LIGHT DRAW
        if leaf_size > 30:
            light_rect=pygame.rect.Rect((0,0),(1,1))
            light_rect.width = leaf_size
            light_rect.height = 2*leaf_size/3
            light_rect.bottom=y
            light_rect.centerx=x
            pygame.draw.arc(surface,(0,0,0),light_rect,math.radians(-143),math.radians(74-110),2)
            draw_a_light(surface,(int(x),int(y)))
            draw_a_light(surface,(int(x-leaf_size/4),int(y-leaf_size/20)))
            draw_a_light(surface,(int(x+leaf_size/4),int(y-leaf_size/20)))

def render_light(surface,pos):
    pygame.draw.circle(surface,pygame.color.THECOLORS[random.choice(list(pygame.color.THECOLORS.keys()))],pos,6)
def  update_lights():
    global updatedLights,lights
    for i in lights:
        render_light(updatedLights,i)
def draw_a_light(surface,pos):
    global lights
    render_light(surface,pos)
    lights.append(pos)
def rotatePointAroundCenter(point,center,degrees):
    displacement = (point[0]-center[0],point[1]-center[1])
    radians = math.radians(degrees)
    newPoint = [0,0]
    newPoint[0] = displacement[0]*math.cos(radians)+displacement[1]*math.sin(radians)
    newPoint[1] = displacement[1]*math.cos(radians)-displacement[0]*math.sin(radians)
    return newPoint
def draw_a_present(surface,x,y):
    (w,h)=random.choice([(100,50),(100,100),(75,75),(50,50)])
    present = pygame.surface.Surface((w,h))
    present.fill(pygame.color.THECOLORS[random.choice(list(pygame.color.THECOLORS.keys()))])
    ribboncolor = pygame.color.THECOLORS[random.choice(list(pygame.color.THECOLORS.keys()))]
    bowcolor = pygame.color.THECOLORS[random.choice(list(pygame.color.THECOLORS.keys()))]
    bowcolor2 = pygame.color.THECOLORS[random.choice(list(pygame.color.THECOLORS.keys()))]
    bowcolor3 = pygame.color.THECOLORS[random.choice(list(pygame.color.THECOLORS.keys()))]
    pygame.draw.line(present,ribboncolor,(0,h/2),(w,h/2),20)
    pygame.draw.line(present,ribboncolor,(w/2,h),(w/2,0),20)
    pygame.draw.circle(present,bowcolor,(int(w/2),int(h/2)),15)
    pygame.draw.circle(present,bowcolor2,(int(w/2),int(h/2)),8)
    pygame.draw.circle(present,bowcolor3,(int(w/2),int(h/2)),4)
    presentrect = present.get_rect()
    presentrect.bottom = y
    presentrect.centerx = x
    surface.blit(present,presentrect)
def initSnow(screen):
    global snow
    snow = []
    for i in range(MAX_SNOW):
        snowflake = [random.randrange(0,screen.get_width()-1),random.randrange(0,screen.get_height()-1)]
        snow.append(snowflake)
def moveAndDrawSnow(screen):
    global snow
    for snowflake in snow:
        snowflake[1] +=SNOW_SPEED
        if snowflake[1] >= screen.get_height():
            snowflake[1] = 0
            snowflake[0] = random.randrange(0,639)
        flakeSize = random.randint(0,4)
        pygame.draw.circle(screen,(255,255,255),snowflake,flakeSize)
def blink_tree_star():
    global treeStarCounter
    if treeStarCounter %2 == 0:
        treeStarColor = (255,235,1)
    else:
        treeStarColor = (255,255,132)
    treeStarCounter +=1
    pygame.draw.polygon(tree,treeStarColor,[(100,27),(108,47),(126,47),(112,60),(117,80),(100,68),(83,80),(88,60),(74,47),(93,47),(100,27)],0)
    pygame.draw.aalines(tree,(255,192,0),True,[(100,27),(108,47),(126,47),(112,60),(117,80),(100,68),(83,80),(88,60),(74,47),(93,47),(100,27)],3)
    
        
pygame.init()

pygame.init()
pygame.display.set_caption("Merry Christmas HHS CS!")
screen = pygame.display.set_mode((640,480))
# BACKGROUND DRAW
background = pygame.surface.Surface((640,480))
background.fill((255,0,0))
# floor
pygame.draw.polygon(background,(217,217,217),((0,480),(100,320),(540,320),(640,480)))
# side walls
pygame.draw.polygon(background,(204,153,255),((0,0),(100,0),(100,320),(0,480)))
pygame.draw.polygon(background,(204,153,255),((640,0),(540,0),(540,320),(640,480)))
# back wall
pygame.draw.polygon(background,(192,29,255),((100,0),(540,0),(540,320),(100,320)))
# window
pygame.draw.polygon(background,(255,255,117),[(550,200),(630,280),(630,80),(550,60)])
pygame.draw.line(background,(0,80,0),(590,70),(590,240),10)
pygame.draw.line(background,(0,80,0),(550,130),(630,180),10)
pygame.draw.lines(background,(0,80,0),True,[(550,200),(630,280),(630,80),(550,60)],10)
# PRESENT DRAW
presents = pygame.surface.Surface((640,480)).convert_alpha()
presents.fill((0,0,0,0))
draw_a_present(presents,500,400)
draw_a_present(presents,460,430)
draw_a_present(presents,70,420)
draw_a_present(presents,130,440)
# WALL LIGHTS DRAW
updatedLights = pygame.surface.Surface((640,480)).convert_alpha()
updatedLights.fill((0,0,0,0))
# LIGHTS DRAW
pygame.draw.arc(background,(0,0,0),pygame.rect.Rect((0,-30),(320,60)),-math.pi,0,5)
pygame.draw.arc(background,(0,0,0),pygame.rect.Rect((320,-30),(320,60)),-math.pi,0,5)
draw_a_light(background,(6,6))
draw_a_light(background,(80,25))
draw_a_light(background,(160,30))
draw_a_light(background,(240,25))
draw_a_light(background,(320,6))
draw_a_light(background,(400,25))
draw_a_light(background,(480,30))
draw_a_light(background,(560,25))
draw_a_light(background,(634,6))


# TREE DRAW
tree = pygame.surface.Surface((640,480)).convert_alpha()
tree.fill((0,0,0,0))
draw_a_tree(tree,200,100,360)

# CALENDAR DRAW
calendar = pygame.surface.Surface((189,150))
calendar.fill((0,255,0))
for i in range(0, 189, 27):
    pygame.draw.line(calendar, (255,255,255), (i,30), (i,150), 2)
for i in range(30, 151, 24):
    pygame.draw.line(calendar, (255,255,225), (0, i), (189,i),2)

cal_head_font = pygame.font.Font(None, 26)
cal_head_surface = cal_head_font.render("DECEMBER", True, (255,0,0))
cal_head_rect = cal_head_surface.get_rect()
cal_head_rect.center = (94.5, 15)
cal_num_font = pygame.font.Font(None, 20)

for i in range(1,32):
    cal_num_surface = cal_num_font.render(str(i), True,(255,0,0),(0,255,0))
    cal_num_rect = cal_num_surface.get_rect()
    cal_num_rect.center = (((i-1) % 7 * 27) + 13.5,((i-1) // 7 * 24) + 42)
    calendar.blit(cal_num_surface, cal_num_rect)

calendar.blit(cal_head_surface, cal_head_rect)

# CALENDAR CROSSOUT
today = datetime.datetime.now().day
for i in range(1, today):
    pygame.draw.line(calendar,(0,0,0),(((i-1)%7*27)+27,((i-1)//7*24)+30),(((i-1)%7*27),((i-1)//7*24)+54),3)
# SANTA DRAW
santa = pygame.surface.Surface((640,480)).convert_alpha()
santa.fill((0,0,0,0))
# L ARM DRAW
santasArm = pygame.surface.Surface((640,480)).convert_alpha()
santasArm.fill((0,0,0,0))
pygame.draw.polygon(santasArm,(255,0,0),((274,207),(264,197),(243,182),(226,168),(215,154),(212,153),(206,158),(192,155),(183,157),(182,172),(204,190),(219,208),(244,231),(261,245)))#ARM AND HAND
pygame.draw.polygon(santasArm,(255,255,255),((243,182),(242,176),(231,167),(226,168),(218,181),(204,190),(204,200),(212,208),(219,208),(232,197)))
# R ARM DRAW
santasRotArm = santasArm.subsurface(pygame.rect.Rect((182,153),(92,92)))
pygame.draw.polygon(santa,(255,0,0),((358,191),(405,202),(428,207),(448,212),(457,220),(459,226),(457,232),(444,236),(440,243),(421,237),(399,233),(389,233),(344,236)))# ARM AND HAND
pygame.draw.polygon(santa,(255,255,255),((428,207),(418,197),(406,197),(407,204),(400,215),(401,237),(421,238),(421,223)))
# L LEG DRAW
pygame.draw.polygon(santa,(255,0,0),((270,323),(268,345),(266,352),(305,361),(309,352),(317,326),(319,312),(272,306)))#leg
pygame.draw.polygon(santa,(102,68,34),((301,370),(266,361),(247,356),(231,357),(224,368),(227,380),(245,388),(272,386),(274,390),(295,391)))#boot
pygame.draw.polygon(santa,(255,255,255),((301,370),(312,355),(303,352),(293,348),(279,346),(268,342),(263,343),(266,361)))#fur
# R LEG DRAW
pygame.draw.polygon(santa,(255,0,0),((322,326),(330,352),(331,359),(372,350),(369,323),(367,311),(316,314)))#leg
pygame.draw.polygon(santa,(102,68,34),((340,369),(373,361),(396,356),(410,359),(415,375),(400,387),(366,386),(365,392),(347,393),(340,386)))#boot
pygame.draw.polygon(santa,(255,255,255),((373,361),(340,369),(334,368),(326,353),(345,348),(359,347),(375,343)))#fur

# BODY
pygame.draw.polygon(santa,(255,255,255),((234,289),(226,299),(230,316),(281,322),(304,327),(317,326),(333,322),(363,324),(408,304),(410,287),(402,275),(328,208),(281,207)))#VEST FUR
pygame.draw.polygon(santa,(255,0,0),((271,188),(245,231),(236,259),(234,272),(235,287),(241,295),(294,302),(300,298),(304,285),(298,217)))#VEST 1
pygame.draw.polygon(santa,(255,0,0),((326,235),(328,286),(330,295),(335,300),(369,297),(401,277),(389,234),(357,192),(334,197)))#VEST 2
pygame.draw.circle(santa,(0,0,0),(315,243),4)
pygame.draw.circle(santa,(0,0,0),(314,257),4)
pygame.draw.circle(santa,(0,0,0),(315,274),4)
pygame.draw.circle(santa,(0,0,0),(317,293),4)
# HEAD AND HAT
pygame.draw.polygon(santa,(255,255,255),((278,153),(272,188),(281,211),(300,232),(315,238),(326,232),(346,215),(357,191),(351,151),(278,153)))
# BEARD
pygame.draw.polygon(santa,(255,218,185),((282,151),(283,166),(309,178),(315,179),(321,177),(345,166),(346,152),(355,140),(310,133),(289,141)))
# HEAD
pygame.draw.polygon(santa,(255,0,0),((266,139),(278,123),(293,112),(315,110),(343,115),(312,85),(260,134)))
# HAT MAIN
pygame.draw.polygon(santa,(255,255,255),((346,152),(335,140),(310,133),(289,141),(282,151),(270,150),(261,146),(266,139),(278,123),(293,112),(315,110),(343,115),(357,132)))
# HAT RIM
pygame.draw.circle(santa,(255,255,255),(255,149),15)
# HAT BALL
# FACE
pygame.draw.circle(santa,(50,50,50),(307,151),3) #EYE
pygame.draw.circle(santa,(50,50,50),(319,151),3)#EYE
pygame.draw.polygon(santa,(255,255,255),((310,140),(310,141),(294,145),(294,149),(303,145),(309,144)))#EYEBROW
pygame.draw.polygon(santa,(255,255,255),((315,146),(324,146),(330,150),(331,146),(326,142),(317,140)))#EYEBROW
pygame.draw.polygon(santa,(255,255,255),((283,167),(287,177),(296,182),(311,176),(305,169)))#MUSTACHELET
pygame.draw.polygon(santa,(255,255,255),((344,168),(323,166),(319,176),(336,178)))#MUSTACHELET
pygame.draw.lines(santa,(245,208,175),False,((307,165),(307,169),(310,173),(321,171),(322,164)),2)#NOSE
initSnow(screen)
counter = 0
clock = pygame.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get(): #closes pygame window
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    screen.fill((0,0,0))
    if counter % 30 == 0:
        update_lights()
    if counter % 10 == 0:
        blink_tree_star()
    rotatedArm = pygame.transform.rotate(santasRotArm,math.sin(counter/5.0)*10-7)
    rotArmRect = rotatedArm.get_rect()
    rotArmPos = rotatePointAroundCenter((86,73),santasRotArm.get_rect().center,-math.sin(counter/5.0)*10+7)
    rotArmPos[0] += 190
    rotArmPos[1] += 180
    rotArmRect.center = rotArmPos
    screen.blit(background,(0,0))
    screen.blit(tree,(0,0))
    screen.blit(updatedLights,(0,0))
    screen.blit(presents,(0,0))
##    screen.blit(calendar,(400,20))
##    screen.blit(santasArm,(0,0))
    screen.blit(rotatedArm,rotArmRect)
    screen.blit(santa,(0,0))
    moveAndDrawSnow(screen)
    screen.blit(calendar,(400,20))
    pygame.display.flip()
    counter += 1
