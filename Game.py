import pygame, random, sys
from pygame.locals import *
import cv2
import numpy as np
import math
import sqlite3
from tkinter import *
from ctypes import windll
import time


def play():
        cap = cv2.VideoCapture('GAME.mp4')
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                cv2.imshow('frame', gray)
                # & 0xFF is required for a 64-bit system
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
            cv2.waitKey(20)
        cap.release()
        cv2.destroyAllWindows()


def decl():
        SetWindowPos = windll.user32.SetWindowPos

        
        conn = sqlite3.connect('snake.db')
        cap = cv2.VideoCapture(0)


        #---------------------------------------------MENU LOGIC------------------------------------------------------------------------------

        #conn.execute('''CREATE TABLE highscore(
        #   ID INTEGER PRIMARY KEY AUTOINCREMENT,
        #  NAME           TEXT      NOT NULL,
        #  score            INT       NOT NULL);''')


        res = False

        e='str'
        string='name'


        start = False
        xs1 = [290, 290, 290, 290, 290]
        ys1 = [290, 270, 250, 230, 210]
        dirs1 = 0
        score1 = 0
        applepos1 = (random.randint(0, 590), random.randint(0, 590))
        pygame.init()
        pygame.Color('black')
        s1=pygame.display.set_mode((600, 600))
        appleimage1 = pygame.Surface((10, 10))
        appleimage1.fill((0, 255, 0))
        img1 = pygame.Surface((20, 20))
        img1.fill((255, 0, 0))
        f1 = pygame.font.SysFont('Arial', 20)
        clock1 = pygame.time.Clock()




SetWindowPos = windll.user32.SetWindowPos


conn = sqlite3.connect('snake.db')
cap = cv2.VideoCapture(0)


#---------------------------------------------MENU LOGIC------------------------------------------------------------------------------

#conn.execute('''CREATE TABLE highscore(
#   ID INTEGER PRIMARY KEY AUTOINCREMENT,
#   NAME           TEXT      NOT NULL,
#   score            INT       NOT NULL);''')


res = False

e='str'
string='name'


start = False
xs1 = [290, 290, 290, 290, 290]
ys1 = [290, 270, 250, 230, 210]
dirs1 = 0
score1 = 0
applepos1 = (random.randint(0, 590), random.randint(0, 590))
pygame.init()
pygame.Color('black')
s1=pygame.display.set_mode((600, 600))
appleimage1 = pygame.Surface((10, 10))
appleimage1.fill((0, 255, 0))
img1 = pygame.Surface((20, 20))
img1.fill((255, 0, 0))
f1 = pygame.font.SysFont('Arial', 20)
clock1 = pygame.time.Clock()
pygame.draw.line(s1,(255,255,255),(5,0),(5,600),3)
 
#-----------------------------------------------------


def collide(x1, x2, y1, y2, w1, w2, h1, h2):
	if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:return True
	else:return False
def die(screen, score):

        global conn,score2,sc_list
        score2 = score
        f=pygame.font.SysFont('Arial', 30);t=f.render('Your score was: '+str(score), True, (255, 255, 255));screen.blit(t, (10, 270));pygame.display.update();pygame.time.wait(2000)
        
        time.sleep(3)
        

        pygame.display.quit()        
        cv2.destroyAllWindows()
        
        r2 = conn.execute("select score from highscore order by score desc limit 10")
        sc_list = list(r2.fetchall())
        print(" sc list : ", sc_list)
        if sc_list and score >= int(min(sc_list[9])):
                enter_name()
        conn.commit()
        cap.release()
        pygame.display.quit()
        sys.exit(0)
        main_menu()
        
def get_name():
    global string
    string = e.get() 
    root1.destroy()
    conn.execute("insert into highscore(name,score) values (?,?)",(string,45))
    conn.commit()
    return string


def enter_name():


        global e,root1
        root1 = Tk()
        root1.geometry('%dx%d+%d+%d' % (700,500, 640, 100))
        e = Entry(root1)
        e.place(x=250,y=150)
        e.focus_set()

        b = Button(root1,text='okay',command=get_name)
        b.place(x=300,y=200)


        root1.mainloop()
                        


#-----------------------------------------------------MAIN LOGIC----------------------------------------------------------------------


def game():

    decl()
    time.sleep(2)
    cap = cv2.VideoCapture(0)
        
    global start,xs1,ys1,dirs1,score1,applepos1,s1,appleimage1,img1,f1,clock1,res
    pygame.init()
    pygame.display.set_caption('Snake')
    SetWindowPos(pygame.display.get_wm_info()['window'], -1, 0, 10, 0, 0, 0x0001)

    while (cap.isOpened()):
        #s1.fill((0,0,0))

        #SNAKE'S EXECUTION
        #---------------------------------------------------------------------------------------
        #if(start == True):
        clock1.tick(1)
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit(0)
            '''
            elif e.type == KEYDOWN:
                if e.key == K_UP and dirs1 != 0:dirs1 = 2
                elif e.key == K_DOWN and dirs1 != 2:dirs1 = 0
                elif e.key == K_LEFT and dirs1 != 1:dirs1 = 3
                elif e.key == K_RIGHT and dirs1 != 3:dirs1 = 1
            '''

        i = len(xs1)-1
        while i >= 2:
            if collide(xs1[0], xs1[i], ys1[0], ys1[i], 20, 20, 20, 20):die(s1, score1) 

            i-= 1
        if collide(xs1[0], applepos1[0], ys1[0], applepos1[1], 20, 10, 20, 10):score1+=1;xs1.append(700);ys1.append(700);applepos1=(random.randint(0,590),random.randint(0,590))
        if xs1[0] < 0 or xs1[0] > 580 or ys1[0] < 0 or ys1[0] > 580:die(s1, score1)
        i = len(xs1)-1
        #print(xs1,i)

        while i >= 1:
            xs1[i] = xs1[i-1];ys1[i] = ys1[i-1];i -= 1

        if dirs1==0:
            #print("right")
            ys1[0] += 20
        elif dirs1==1:
            xs1[0] += 20
        elif dirs1==2:
            ys1[0] -= 20
        elif dirs1==3:
            xs1[0] -= 20
        s1.fill((0,0,0))
        for i in range(0, len(xs1)):
            s1.blit(img1, (xs1[i], ys1[i]))
        s1.blit(appleimage1, applepos1);t1=f1.render(str(score1), True, (255,255,255));s1.blit(t1, (10, 10));pygame.display.update()

        #---------------------------------------------------------------------------------------

        #DETECTION'S EXECUTION
        #---------------------------------------------------------------------------------------
        

        ret, img = cap.read()

        # get hand data from the rectangle sub window on the screen
        cv2.rectangle(img, (450,450), (200,200), (0,255,0),0)
        crop_img = img[200:450, 200:450]


        # convert to grayscale
        grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    
        # applying gaussian blur
        value = (35, 35)
        blurred = cv2.GaussianBlur(grey, value, 0)

        # thresholdin: Otsu's Binarization method
        _, thresh1 = cv2.threshold(blurred, 127, 255,
                               cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)



        # check OpenCV version to avoid unpacking error
        (version, _, _) = cv2.__version__.split('.')

        if version == '3':
            image, contours, hierarchy = cv2.findContours(thresh1.copy(), \
                   cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        elif version == '2' or version == "4":
            contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
                   cv2.CHAIN_APPROX_NONE)

        #self.contours = contours
        #get_center_of_mass(contours)
        # find contour with max area
        cnt = max(contours, key = lambda x: cv2.contourArea(x))

        # create bounding rectangle around the contour (can skip below two lines)
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(crop_img, (x, y), (x+w, y+h), (0, 0, 255), 0)

        # finding convex hull
        hull = cv2.convexHull(cnt)

        # drawing contours
        drawing = np.zeros(crop_img.shape,np.uint8)
        cv2.drawContours(drawing, [cnt], 0, (0, 255, 0), 0)
        cv2.drawContours(drawing, [hull], 0,(0, 0, 255), 0)

        # finding convex hull
        hull = cv2.convexHull(cnt, returnPoints=False)

        # finding convexity defects
        defects = cv2.convexityDefects(cnt, hull)
        count_defects = 0
        cv2.drawContours(thresh1, contours, -1, (0, 255, 0), 3)

        # applying Cosine Rule to find angle for all defects (between fingers)
        # with angle > 90 degrees and ignore defects
        
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]

            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])

            # find length of all sides of triangle
            a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)

            # apply cosine rule here
            angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57

            # ignore angles > 90 and highlight rest with red dots
            if angle <= 90:
                count_defects += 1
                cv2.circle(crop_img, far, 1, [0,0,255], -1)
            #dist = cv2.pointPolygonTest(cnt,far,True)

            # draw a line from start to end i.e. the convex points (finger tips)
            # (can skip this part)
            cv2.line(crop_img,start, end, [0,255,0], 2)
            #cv2.circle(crop_img,far,5,[0,0,255],-1)

        # define actions required
        if count_defects == 1 and dirs1 != 0:
            dirs1 = 2
            ##print('!!!!!!!!!1')        
            start=True
        elif count_defects == 2 and dirs1 != 2:
            dirs1 = 0
        elif count_defects == 3 and dirs1 != 1:
            dirs1 = 3
        elif count_defects == 4 and dirs1 != 3:
            dirs1 = 1
    
        all_img = np.hstack((drawing, crop_img))
        cv2.imshow('Contours', all_img)
        cv2.imshow('Thresholded', thresh1)

        # show appropriate images in windows
        cv2.imshow('Gesture', img)
        #cv2.resizeWindow('Gesture',800,800)
        cv2.moveWindow('Gesture',700,50)
        k = cv2.waitKey(10)
        if k == 27:
            break

def get_center_of_mass(contours):
        if len(contours) == 0:
            return None
        contours = np.array(contours,dtype=np.float32)
        print(type(contours))
        #print(contours)
        M = cv2.moments(contours)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        #print(cX,cY)
        return (cX, cY)
        
    #---------------------------------------------------------------------------------------

#--------------------------------------END OF MAIN LOGIC------------------------------------------------------------------------------


def highscore():

        global conn
        global root,w

        r = conn.execute('select * from highscore order by score desc limit 10')

        r1 = list(r.fetchall())

        w.create_rectangle(0, 0, 1300, 900, fill="black")
        
        #img = PhotoImage(file="bg.png")      
        #w.create_image(0,0, anchor=NW, image=img)  

        l1 = Label(root,text = 'RANK',bd=3,relief='solid',padx=100,pady=30,font=("Arial",20),background='#000000',foreground='red')
        l1.place(x = 00,y=00)


        l = Label(root,text = 'NAME',bd=3,relief='solid',padx=180,pady=30,font=("Arial",20),width=20,background='#000000',foreground='red')
        l.place(x = 270,y=00)

        l2 = Label(root,text = 'SCORE',bd=3,relief='solid',padx=155,pady=30,font=("Arial",20),width=9,background='#000000',foreground='red')
        l2.place(x = 840,y=00)




        y1=90

        c = 1
        for i in r1:

            l3 = Label(root,text = c,bd=3,relief='solid',padx=130,pady=10,font=("Arial",20),background='#000000',foreground='red')
            l3.place(x = 00,y=y1)


            l4 = Label(root,text = i[1],bd=3,relief='solid',padx=180,pady=10,font=("Arial",20),width=20,background='#000000',foreground='red')
            l4.place(x = 270,y=y1)

            l5 = Label(root,text = i[2],bd=3,relief='solid',padx=155,pady=10,font=("Arial",20),width=9,background='#000000',foreground='red')
            l5.place(x = 840,y=y1)

            y1+=55

            ##print(y1)

            c += 1
        #    #print(i[0])

        b2 = Button(root,text = 'BACK',fg='black',padx = 80, pady = 20,command=menu,background='#000000',foreground='red',bd=0)
        b2.place(x=600,y=650)

        root.mainloop()


def help_func():

        global root,w
        for w in root.winfo_children():
            #if(w != canvas):
            ##print(type(w))
            w.destroy()


        w = Canvas(root,width=1300,height=900)
        w.pack()
        img = PhotoImage(file="required_images/bg.png")      
        w.create_image(0,0, anchor=NW, image=img)  
        w.create_rectangle(0, 0, 1300, 900, fill="#ffffff")
        l5 = Label(root,text = 'NAVIGATION',bd=3,relief='solid',padx=400,pady=70,font=("Arial",70),width=9,background='#000000',foreground='red')
        l5.place(x = 0,y=0)
        a1 = Label(root,text = '1. SHOW 2 FINGERS TO GO UP',bd=3,relief='solid',padx=600,pady=30,font=("Arial",20),width=9,background='#000000',foreground='red')
        a1.place(x = 0,y=240)
        a2 = Label(root,text = '2. SHOW 3 FINGERS TO GO DOWN',bd=3,relief='solid',padx=600,pady=30,font=("Arial",20),width=9,background='#000000',foreground='red')
        a2.place(x = 0,y=320)
        a3 = Label(root,text = '3. SHOW 4 FINGERS TO GO LEFT',bd=3,relief='solid',padx=600,pady=30,font=("Arial",20),width=9,background='#000000',foreground='red')
        a3.place(x = 0,y=400)
        a4 = Label(root,text = '4. SHOW 5 FINGERS TO GO RIGGHT',bd=3,relief='solid',padx=600,pady=30,font=("Arial",20),width=9,background='#000000',foreground='red')
        a4.place(x = 0,y=480)


        hel = Button(root,text = 'BACK TO MAIN MENU',font=("Arial",50),fg='black',padx = 300, pady = 30,command = menu,background='#000000',foreground='red')
        hel.place(x=0,y=560)
                    


def rem():
    global root,w

def exit_func():
        global root,w

        root.destroy()
        pygame.display.quit()


def back():
        
        main_menu()


def menu():
        global root,w

        for w in root.winfo_children():
            #if(w != canvas):
            w.destroy()


        w = Canvas(root,width=1300,height=900)
        w.pack()

        #w.create_rectangle(0, 0, 1300, 900, fill="#ffffff")
        
        img = PhotoImage(file="required_images/bg.png")      
        w.create_image(0,0, anchor=NW, image=img)  
        #w.create_rectangle(0, 0, 1300, 900, fill="#ffffff")
        play1 = Button(root,text = 'PLAY',fg='black',padx = 80, pady = 20,command=game,background='#000000',foreground='red',bd=10,relief='raised')
        play1.place(x=600,y=120)

        menu = Button(root,text = 'HIGH SCORE',fg='black',padx = 60, pady = 20,command = highscore,background='#000000',foreground='red',bd=10,relief='raised')
        menu.place(x=600,y=220)
        hel = Button(root,text = 'HELP',fg='black',padx = 80, pady = 20,command = help_func,background='#000000',foreground='red',bd=10,relief='raised')
        hel.place(x=600,y=320)
        demo = Button(root,text = 'DEMO',fg='black',padx = 80, pady = 15,command = play,background='#000000',foreground='red',bd=10,relief='raised')
        demo.place(x=600,y=420)
        ex = Button(root,text = 'BACK',fg='black',padx = 80, pady = 20,command = back,background='#000000',foreground='red',bd=10,relief='raised')
        ex.place(x=600,y=520)


        #root.wm_attributes('-transparentcolor','#ffffff')

        root.mainloop()



def calc():

        ar = random.randint(0,5)
        br = random.randint(0,5)
        ar = max(ar,br)
        br= min(ar,br)

        cr = ar+br

        ##print(str(a),b,cr)

        res = False



        cap = cv2.VideoCapture(0)
        while(cap.isOpened()):

            if(res == True):
                ar = random.randint(0,49)
                br = random.randint(0,49)
                cr = ar+br
                ar = max(ar,br)
                br= min(ar,br)
                

            # read image

                
            ret, img = cap.read()


            # get hand data from the rectangle sub window on the screen
            cv2.rectangle(img, (600,400), (400,200), (0,255,0),0)
            crop_img = img[200:400, 400:600]

            cv2.rectangle(img, (300,400), (100,200), (0,255,0),0)
            crop_img2 = img[200:400, 100:300]



          #  #print(crop_img)
            # convert to grayscale
            grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
            grey2 = cv2.cvtColor(crop_img2, cv2.COLOR_BGR2GRAY)

            # applying gaussian blur
            value = (35, 35)
            blurred = cv2.GaussianBlur(grey, value, 0)

            value2 = (35, 35)
            blurred2 = cv2.GaussianBlur(grey2, value2, 0)

            # thresholdin: Otsu's Binarization method
            _, thresh1 = cv2.threshold(blurred, 127, 255,
                                       cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

            _, thresh2 = cv2.threshold(blurred2, 127, 255,
                                       cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)


            # show thresholded image
            cv2.imshow('Thresholded', thresh1)

            cv2.imshow('Thresholded', thresh2)

            # check OpenCV version to avoid unpacking error
            (version, _, _) = cv2.__version__.split('.')

            if version == '3':
                image, contours, hierarchy = cv2.findContours(thresh1.copy(), \
                       cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

                image2, contours2, hierarchy2 = cv2.findContours(thresh2.copy(), \
                       cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

            elif version == '2':

                contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
                       cv2.CHAIN_APPROX_NONE)

                contours2, hierarchy2 = cv2.findContours(thresh2.copy(),cv2.RETR_TREE, \
                       cv2.CHAIN_APPROX_NONE)

            # find contour with max area
            cnt = max(contours, key = lambda x: cv2.contourArea(x))

            cnt2 = max(contours2, key = lambda x: cv2.contourArea(x))

            # create bounding rectangle around the contour (can skip below two lines)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(crop_img, (x, y), (x+w, y+h), (0, 0, 255), 0)

            x2, y2, w2, h2 = cv2.boundingRect(cnt2)
            cv2.rectangle(crop_img2, (x2, y2), (x2+w2, y2+h2), (0, 0, 255), 0)

            # finding convex hull
            hull = cv2.convexHull(cnt)

            hull2 = cv2.convexHull(cnt2)

            # drawing contours
            drawing = np.zeros(crop_img.shape,np.uint8)
            cv2.drawContours(drawing, [cnt], 0, (0, 255, 0), 0)
            cv2.drawContours(drawing, [hull], 0,(0, 0, 255), 0)

            drawing2 = np.zeros(crop_img2.shape,np.uint8)
            cv2.drawContours(drawing2, [cnt2], 0, (0, 255, 0), 0)
            cv2.drawContours(drawing2, [hull2], 0,(0, 0, 255), 0)


            # finding convex hull
            hull = cv2.convexHull(cnt, returnPoints=False)

            hull2 = cv2.convexHull(cnt2, returnPoints=False)

            # finding convexity defects
            defects = cv2.convexityDefects(cnt, hull)
            count_defects = 0
            cv2.drawContours(thresh1, contours, -1, (0, 255, 0), 3)

            defects2 = cv2.convexityDefects(cnt2, hull2)
            count_defects2 = 0
            cv2.drawContours(thresh2, contours2, -1, (0, 255, 0), 3)

            # applying Cosine Rule to find angle for all defects (between fingers)
            # with angle > 90 degrees and ignore defects
            for i in range(defects.shape[0]):
                s,e,f,d = defects[i,0]

                start = tuple(cnt[s][0])
                end = tuple(cnt[e][0])
                far = tuple(cnt[f][0])

                # find length of all sides of triangle
                a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
                b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
                c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)

                # apply cosine rule here
                angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57

                # ignore angles > 90 and highlight rest with red dots
                if angle <= 90:
                    count_defects += 1
                    cv2.circle(crop_img, far, 1, [0,0,255], -1)
                #dist = cv2.pointPolygonTest(cnt,far,True)

                # draw a line from start to end i.e. the convex points (finger tips)
                # (can skip this part)
                cv2.line(crop_img,start, end, [0,255,0], 2)
                #cv2.circle(crop_img,far,5,[0,0,255],-1)


            for i in range(defects2.shape[0]):
                s2,e2,f2,d2 = defects2[i,0]

                start2 = tuple(cnt2[s2][0])
                end2 = tuple(cnt2[e2][0])
                far2 = tuple(cnt2[f2][0])

                # find length of all sides of triangle
                a2 = math.sqrt((end2[0] - start2[0])**2 + (end2[1] - start2[1])**2)
                b2 = math.sqrt((far2[0] - start2[0])**2 + (far2[1] - start2[1])**2)
                c2 = math.sqrt((end2[0] - far2[0])**2 + (end2[1] - far2[1])**2)

                # apply cosine rule here
                angle2 = math.acos((b2**2 + c2**2 - a2**2)/(2*b2*c2)) * 57

                # ignore angles > 90 and highlight rest with red dots
                if angle2 <= 90:
                    count_defects2 += 1
                    cv2.circle(crop_img2, far2, 1, [0,0,255], -1)
                #dist = cv2.pointPolygonTest(cnt,far,True)

                # draw a line from start to end i.e. the convex points (finger tips)
                # (can skip this part)
                cv2.line(crop_img2,start2, end2, [0,255,0], 2)
                #cv2.circle(crop_img,far,5,[0,0,255],-1)


            cr = ar + br
            s = str(ar) + '+' + str(br) + ' = ?'
            ##print(s,a,b)
            cv2.putText(img,s  , (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,255,0), 2)

                


            # define actions required

            if(cr%10 >5  or cr/10>5 or cr<10 or cr%10 == 0):
                res=True

                

            elif(cr == int(count_defects2  + 1)*10 + int(count_defects + 1)):
                
                res = True

            else:
                res=False

            # show appropriate images in windows
            cv2.imshow('Gesture', img)
            cv2.resizeWindow('Gesture',800,800)
            all_img = np.hstack((drawing, crop_img))
            cv2.imshow('Contours', all_img)

            k = cv2.waitKey(10)
            if k == 27:
                break



def main_menu():
    global root,w
    for w in root.winfo_children():
        #if(w != canvas):
        ##print(type(w))
        w.destroy()

        w = Canvas(root,width=1300,height=900)
        w.pack()
        print(" -------------- ")

    w.create_rectangle(0, 0, 1300, 900, fill="black")
    img = PhotoImage(file="required_images/bg.png")      
    w.create_image(0,0, anchor=NW, image=img)
    cal = Button(root,text = 'CALCULATOR',fg='black',command = calc,padx = 80, pady = 20,background='#000000',foreground='red',bd=10,relief='groove')
    cal.place(x=600,y=200)
        
    ga = Button(root,text = 'GAME',fg='black',command = menu,padx = 100, pady = 20,background='#000000',foreground='red',bd=10,relief='groove')
    ga.place(x=600,y=300)
    ex = Button(root,text = 'EXIT',fg='black',padx = 100, pady = 20,command = exit_func,background='#000000',foreground='red',bd=10,relief='groove')
    ex.place(x=600,y=400)
    # import time
    # time.sleep(50)
    


if __name__ == "__main__":
    root = Tk()
    root.geometry('1300x900')
    w = Canvas(root,width=1300,height=900)
    w.pack()


    decl()
    print("DEcl is completed")
    main_menu()
    print("main menu completed")
    root.mainloop()

    conn.commit()
