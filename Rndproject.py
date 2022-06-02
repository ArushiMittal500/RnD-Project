#from ctypes.wintypes import PINT
from tkinter import *
import random
import itertools
from tkinter import messagebox
import pickle


global counter 
counter=0


def login():
    
    global loginpage, username1
    counter = 1
    loginpage = Tk()
    loginpage.title("Graphical Password")
    loginpage.geometry('500x300+350+200')
    loginpage.resizable(0,0)
    #loginpage.config(bg='#95b9c7')
    
    label0 = Label(loginpage,text="Login to use Virtual Keyboard",font=('Arial Bold',"20"),justify=CENTER)
    label0.place(x=0, y=0)
    label0.config(bg="#045f5f", fg="white",width=30,height=2)
    
    label4 = Label(loginpage,text="Username: ",font=('Arial Bold',"14"))
    label4.place(x=140, y=80)

    username1 = Entry(loginpage,width=35,borderwidth=5,font=("Arial Bold", 8),bg="#eeeade")
    username1.place(x=140, y=120)
    
    btn_start = Button(loginpage,text='Login',width = 21,height = 1, bg='#347c17',fg='white',font=("Arial Bold", 12),command=lambda:loginauth())
    btn_start.place(x=140,y=160)
    
    label7 = Label(loginpage,text="Doesn't Have an account?",font=('Arial Bold',"11"))
    label7.place(x=140, y=210)
    
    btn = Button(loginpage,text='SignUp',width = 21, bg='#cc5801',fg='white',font=("Arial Bold", 12),command=lambda:signup())
    btn.place(x=140,y=240)


    loginpage.mainloop()
    

def loginauth():
    global user
    fh = open("users.pkl", 'rb')
    users_chosen = pickle.load(fh)
    if(username1.get()==""):
        messagebox.showerror("Error","Please Enter Username",parent=loginpage)
    elif(username1.get() not in users_chosen):
        messagebox.showerror("Error","Username doesn't Exist, Please Sign Up First",parent=loginpage)
    else:
        user=username1.get()
        keyboard_display()

def signup():
    
    global graph, menu1, menu2, menu3, characters, username, loginpass, confpass
    
    graph = Tk()
    graph.title("Graphical Password")
    graph.geometry('900x500+200+100')
    graph.resizable(0,0)
    #graph.config(bg='white')
    
    characters = [1,2,3,4,5,6,7,8,9,0,'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L',';','Z','X','C','V','B','N','M','_','-','?','!','@','#','$','%','^','&','*','+','(']
    
    global keyboard
    
    global colours
    
    colours = ['Red','Yellow','Pink','Blue','Green','Cyan','Purple','Gray','Orange','violet','Brown','Maroon']
    characters = [1,2,3,4,5,6,7,8,9,0,'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L',';','Z','X','C','V','B','N','M','_','-','?','!','@','#','$','%','^','&','*','+','(']


    c1= Canvas(graph,width=160, height=160)
    c1.place(x=600,y=180)
    #c1.config(bg='white')
    
    x=0
    y=0
    arc=[0]*8

    for k in range(8):
        arc1 = c1.create_arc((10,10,150,150),fill=colours[k],start=x, extent=45)
        arc[k] = c1.create_arc((23,23,137,137),fill=colours[k], start=y, extent=45)
        x=x+45
        y=y+45


    c1.create_text((117,66),text='1',font=("Arial Bold", 18))
    c1.create_text((117,95),text='8',font=("Arial Bold", 18))
    c1.create_text((94,115),text='7',font=("Arial Bold", 18))
    c1.create_text((65,115),text='6',font=("Arial Bold", 18))
    c1.create_text((40,96),text='5',font=("Arial Bold", 18))
    c1.create_text((40,62),text='4',font=("Arial Bold", 18))
    c1.create_text((63,40),text='3',font=("Arial Bold", 18))
    c1.create_text((96,42),text='2',font=("Arial Bold", 18))
    

    label0 = Label(graph,text="Create an account to use Virtual Keyboard",font=('Arial Bold',"24"),justify=CENTER)
    label0.place(x=0, y=0)
    label0.config(bg="#045f5f", fg="white",width=48,height=2)
    
    label1 = Label(graph,text="Choose The Sector: ",font=('Arial Bold',"12"))
                   
    
    label2 = Label(graph,text="Outer Color: ",font=('Arial Bold',"12"))
    
    
    label3 = Label(graph,text="Inner Color:",font=('Arial Bold',"12"))
    
    label1.place(x=150, y=270)
    label2.place(x=210, y=320)
    label3.place(x=210, y=370)


    label4 = Label(graph,text="Username: ",font=('Arial Bold',"12"))
    label4.place(x=210, y=120)

    label5 = Label(graph,text="Password: ",font=('Arial Bold',"12"))
    label5.place(x=210, y=170)

    label6 = Label(graph,text="Confirm Password: ",font=('Arial Bold',"12"))
    label6.place(x=150, y=220)

    username = Entry(graph,width=35,borderwidth=5,font=("Arial Bold", 8),bg="#eeeade")
    username.place(x=310, y=120)

    loginpass = Entry(graph,show="*",width=35,borderwidth=5,font=("Arial Bold", 8),bg="#eeeade")
    loginpass.place(x=310, y=170)


    confpass = Entry(graph,show="*",width=35,borderwidth=5,font=("Arial Bold", 8),bg="#eeeade")
    confpass.place(x=310, y=220)

    menu1= IntVar()
    menu1.set("Select Any Sector")

    drop1= OptionMenu(graph,menu1,1,2,3,4,5,6,7,8)
    drop1.place(x=310, y=270)
    drop1.config(width = 30,bg="#eeeade")
    
    
    menu2= StringVar()
    menu2.set("Select Any Color")
    
    drop2= OptionMenu(graph, menu2,'Red','Yellow','Pink','Blue','Green','Cyan','Purple','Gray','Orange','violet','Brown','Maroon')
    drop2.place(x=310, y=320)
    drop2.config(width = 30,bg="#eeeade")
    
    menu3= StringVar()
    menu3.set("Select Any Color")
    
    drop3= OptionMenu(graph, menu3,'Red','Yellow','Pink','Blue','Green','Cyan','Purple','Gray','Orange','violet','Brown','Maroon')
    drop3.place(x=310, y=370)
    drop3.config(width = 30,bg="#eeeade")
    

    btn_start = Button(graph,text='Sign Up',width = 21,height = 1, bg='#347c17',fg='white',font=("Arial Bold", 12),command=lambda:signupauth())
    btn_start.place(x=315,y=420)
    
    label7 = Label(graph,text="Already Have an account?",font=('Arial Bold',"11"))
    label7.place(x=590, y=390)
    
    btn_start = Button(graph,text='Login',width = 12, bg='#cc5801',fg='white',font=("Arial Bold", 12),command=lambda:login())
    btn_start.place(x=615,y=420)
    
    global pin1
    
    pin1=StringVar()

    graph.mainloop()
    
def signupauth():
    global user
    fh = open("users.pkl", 'rb')
    users_chosen = pickle.load(fh)
    if(username.get()=="" or loginpass.get()=="" or confpass.get()=="" or menu1.get()=="Select Any Sector" or menu2.get()=="Select Any Color" or menu3.get()=="Select Any Color"):
        messagebox.showerror("Error","All Fields are required", parent=graph)
    elif(username.get() in users_chosen):
        messagebox.showerror("Error","This Username already exists, Choose the unique username", parent=graph)
    elif(loginpass.get()!=confpass.get()):
        messagebox.showerror("Error","Password and Confirm Password not match")
    else:
        sector_chosen = pickle.load(fh)
        outer_color_chosen = pickle.load(fh)
        inner_color_chosen = pickle.load(fh)
        fh.close()
        #print("inner= ",inner_color_chosen)
        #print(username.get())
        
        users_chosen.append(username.get())
        sector_chosen.append(menu1.get())
        outer_color_chosen.append(menu2.get())
        inner_color_chosen.append(menu3.get())
        
        fh = open("users.pkl", 'wb')
        pickle.dump(users_chosen, fh)
        pickle.dump(sector_chosen, fh)
        pickle.dump(outer_color_chosen, fh)
        pickle.dump(inner_color_chosen, fh)
        fh.close()
        
        user=username.get()
        
        keyboard_display()

def sector_list(total_outer_arc,total_inner_arc):
    sector_outer=[0]*8
    sector_inner=[0]*8
    for i in range(8):
        sector_outer[i]=[]
        sector_inner[i]=[]


    for j in range(50):
        for i in range(8):
            sector_outer[i].append(total_outer_arc[j][i])
            sector_inner[i].append(total_inner_arc[j][i])
            
    
def color_list(perm_comb_outer,perm_comb_inner):
    color_outer=[0]*8
    color_inner=[0]*8
    for i in range(8):
        color_outer[i]=[]
        color_inner[i]=[]


    for j in range(50):
        for i in range(8):
            color_outer[i].append(perm_comb_outer[j][i])
            color_inner[i].append(perm_comb_inner[j][i])   
    return color_outer,color_inner
    
    
def color_comb(color_outer,color_inner):
    characters = ['1','2','3','4','5','6','7','8','9','0','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L',';','Z','X','C','V','B','N','M','_','-','?','!','@','#','$','%','^','&','*','+','(']
    for i in range(len(characters)):
        if(color_outer[sector-1][i]==outer_choice and color_inner[sector-1][i]==inner_choice):
            return characters[i]
            

    
def random_display(comb_outer,comb_inner):
    x=0
    y=0
    t=0
    for j in range(5):
        for i in range(10):
            outer_arc=[0]*8
            inner_arc=[0]*8
            if(t==8):
                comb_outer=comb_outer[1:] + comb_outer[:1]
                t=0
            for k in range(8):
                outer_arc[k] = c.create_arc((10+(i*90),10+(j*90),100+(i*90),100+(j*90)),fill=comb_outer[k],start=x, extent=45)
                inner_arc[k] = c.create_arc((23+(i*90),23+(j*90),87+(i*90),87+(j*90)),fill=comb_inner[k], start=y, extent=45)
                x=x+45
                y=y+45
                
            t=t+1
            total_outer_arc.append(outer_arc)
            total_inner_arc.append(inner_arc)
            perm_comb_outer.append(comb_outer)
            perm_comb_inner.append(comb_inner)
            comb_inner=comb_inner[1:] + comb_inner[:1]
            
            
def outer_display(test_list,outer_arc):
    for i in range(8):
        c.itemconfig(outer_arc[i], fill=test_list[i])
        

def rotate_upper_clock():
    for i in range(len(perm_comb_outer)):
        test_list=perm_comb_outer[i]
        test_list = test_list[1:] + test_list[:1]
        perm_comb_outer[i]=test_list
        outer_display(test_list,total_outer_arc[i])

        
def rotate_upper_anticlock():
    for i in range(len(perm_comb_outer)):
        test_list=perm_comb_outer[i]
        test_list = test_list[-1:] + test_list[:-1]
        perm_comb_outer[i]=test_list
        outer_display(test_list,total_outer_arc[i])
        
        
def inner_display(test_list,inner_arc):
    for i in range(8):
        c.itemconfig(inner_arc[i], fill=test_list[i])

def rotate_lower_clock():
    for i in range(len(perm_comb_inner)):
        test_list=perm_comb_inner[i]
        test_list = test_list[1:] + test_list[:1]
        perm_comb_inner[i]=test_list
        inner_display(test_list,total_inner_arc[i])
    
def rotate_lower_anticlock():
    for i in range(len(perm_comb_inner)):
        test_list=perm_comb_inner[i]
        test_list = test_list[-1:] + test_list[:-1]
        perm_comb_inner[i]=test_list
        inner_display(test_list,total_inner_arc[i])
    
    
def keyboard_display():
    
    #graph.destroy()
    global sector, outer_choice, inner_choice
    global perm_comb_outer,perm_comb_inner,total_outer_arc,total_inner_arc,c
    global sector_outer,sector_inner,color_outer,color_inner
    global passwordfield,selected_color
    global button_caps,style_blue, style_white
    global button_copy
    
    graph.destroy()
    if(counter==1):
        loginpage.destroy()
    
    fh = open("users.pkl", 'rb')
    users_chosen = pickle.load(fh)
    sector_chosen = pickle.load(fh)
    outer_color_chosen = pickle.load(fh)
    inner_color_chosen = pickle.load(fh)
    
    index = users_chosen.index(user)
    

    sector=sector_chosen[index]
    outer_choice=outer_color_chosen[index]
    inner_choice=inner_color_chosen[index]
    
    print(sector)
    print(outer_choice)
    print(inner_choice)
    global start
    start = Tk()

    start.title("Enter Your Password To Login")
    start.geometry('930x630+200+50')
    start.resizable(0,0)
    #start.config(bg='white')
    
    c2= Canvas(start,width=110, height=110)
    c2.place(x=20,y=20)
    #c2.config(bg='white')


    button_caps = Button(start, text="Caps Lock",width = 12,height = 2,bg= 'White',fg='Black',font=("Arial Bold", 10),command=lambda:caps_lock())
    button_caps.place(x = 170, y = 90)

    button_x = Button(start, text="Rotate-Outer",width = 12,height = 1,bg= 'White',fg='Black',font=("Arial Bold", 10))
    button_x.place(x = 170, y = 20)
    
    button_x = Button(start, text="<",width = 4,height = 1,bg= 'White',fg='Black',font=("Arial Bold", 10),command=lambda:rotate_upper_anticlock())
    button_x.place(x = 170, y = 50)

    button_x = Button(start, text=">",width = 4,height = 1,bg= 'White',fg='Black',font=("Arial Bold", 10),command=lambda:rotate_upper_clock())
    button_x.place(x = 235, y = 50)

    button_x = Button(start, text="Rotate-Inner",width = 12,height = 1,bg= 'White',fg='Black',font=("Arial Bold", 10))
    button_x.place(x = 300, y = 20)
    
    button_x = Button(start, text="<",width = 4,height = 1,bg= 'White',fg='Black',font=("Arial Bold", 10),command=lambda:rotate_lower_anticlock())
    button_x.place(x = 300, y = 50)

    button_x = Button(start, text=">",width = 4,height = 1,bg= 'White',fg='Black',font=("Arial Bold", 10),command=lambda:rotate_lower_clock())
    button_x.place(x = 365, y = 50)

    passwordfield = Entry(start,show="*",width=30,borderwidth=5,textvariable=pin1,font=("Arial Bold", 8))
    passwordfield.place(x=430, y=70)

    button_x = Button(start, text="Select",width = 12,height = 2, bg= 'White',fg='Black',font=("Arial Bold", 10),command=lambda:select())
    button_x.place(x = 300, y = 90)

    button_x = Button(start, text="Backspace",width = 20,height = 2, bg= 'Red',fg='white',font=("Arial Bold", 10),command=lambda:backspace())
    button_x.place(x = 650, y = 20)

    button_copy = Button(start, text="Copy To Clipboard",width = 20,height = 2, bg= 'Green',fg='white',font=("Arial Bold", 10),command=lambda:copy())
    button_copy.place(x = 650, y = 90)
    
    style_blue = {'bg': '#1520A6','fg': 'White'}
    style_white = {'bg': 'White','fg': 'Black'}
    
    if(outer_choice!=inner_choice):
        selected_color = [outer_choice,inner_choice]
        colours.remove(outer_choice)
        colours.remove(inner_choice)
        for i in range(6):
            choice = random.choice(colours)
            selected_color.append(choice)
            colours.remove(choice)
    else:
        selected_color = [outer_choice]
        colours.remove(outer_choice)
        for i in range(7):
            choice = random.choice(colours)
            selected_color.append(choice)
            colours.remove(choice)
    

    perm1 = itertools.permutations(selected_color)
    perm = list(perm1)
    
    perm_comb_outer =[]
    perm_comb_inner =[]
    total_outer_arc=[]
    total_inner_arc=[]
    c= Canvas(start,width=930, height=470)
    c.pack(side=BOTTOM)
    #c.config(bg='white')

    comb1 = random.choice(perm)
    comb_outer = list(comb1)
    comb_inner = list(comb1)
    
    random_display(comb_outer,comb_inner)
    
    x=0
    y=0
    
    for k in range(8):
        arc1 = c2.create_arc((10,10,100,100),fill=selected_color[k],start=x, extent=45)
        arc1 = c2.create_arc((23,23,87,87),fill=selected_color[k], start=y, extent=45)
        x=x+45
        y=y+45
    
    
    c2.create_text((76,46),text='1',font=("Arial Bold", 13))
    c2.create_text((62,36),text='2',font=("Arial Bold", 13))
    c2.create_text((47,35),text='3',font=("Arial Bold", 13))
    c2.create_text((35,46),text='4',font=("Arial Bold", 13))
    c2.create_text((33,65),text='5',font=("Arial Bold", 13))
    c2.create_text((47,76),text='6',font=("Arial Bold", 13))
    c2.create_text((63,76),text='7',font=("Arial Bold", 13))
    c2.create_text((75,65),text='8',font=("Arial Bold", 13))
    

    
    for j in range(5):
        for i in range(10):
            z=characters[0]
            c.create_oval((35+(i*90),35+(j*90),75+(i*90),75+(j*90)),fill='white')
            c.create_text(55+(i*90),55+(j*90),text=z,font=("Arial Bold", 20))
            characters.remove(z)
   
    start.mainloop()


def select():
    sector_list(total_outer_arc,total_inner_arc)
    color_outer,color_inner=color_list(perm_comb_outer,perm_comb_inner)
    letter1=str(color_comb(color_outer,color_inner))
    print(button_caps.cget('bg'))
    if(button_caps.cget('bg')=='White'):
        letter = letter1.lower()
    else:
        letter=letter1
    print("letter ",letter)
    passwordfield.insert(END,letter)
    print(passwordfield.get())
    

def caps_lock():
    if(button_caps.cget('bg')=='White'):
        button_caps.configure(**style_blue)
    else:
        button_caps.configure(**style_white)
        
def backspace():
    password = passwordfield.get()
    passwordfield.delete((len(password)-1))
    print(passwordfield.get())
    
    
def copy():
    copied = passwordfield.get()
    print(copied)
    start.clipboard_clear()
    start.clipboard_append(copied)
    button_copy["text"]="Copied"
    

signup()

