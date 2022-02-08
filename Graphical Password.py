from tkinter import *
import random
start = Tk()

start.title("Graphical Password")
start.geometry('1000x500')

lbl = Label(start, text="Enter your Password to Login",font=('Arial Bold',"18"))
lbl.place(x=320, y=5)

button_x = Button(start, text="<",width = 5,height = 2,font=("Arial Bold", 10))
button_x.place(x = 130, y = 90)

button_x = Button(start, text="^",width = 5,height = 2,font=("Arial Bold", 10))
button_x.place(x = 200, y = 60)

button_x = Button(start, text=">",width = 5,height = 2,font=("Arial Bold", 10))
button_x.place(x = 270, y = 90)

button_x = Button(start, text="v",width = 5,height = 2,font=("Arial Bold", 10))
button_x.place(x = 200, y = 120)

password = Entry(start,width=30,borderwidth=5)
password.place(x=360, y=100)

button_x = Button(start, text="Backspace",width = 10,height = 2, bg= 'Red',fg='white',font=("Arial Bold", 10))
button_x.place(x = 590, y = 90)

button_x = Button(start, text="Login",width = 10,height = 2, bg= 'Green',fg='white',font=("Arial Bold", 10))
button_x.place(x = 700, y = 90)

characters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','@','#','$','%','&','_','*','^','+','=','(',')','/','?','!','<','>','-',',','.',';',':',' ','{','}','[',']','|',1,2,3,4,5,6,7,8,9,0]
colours = ['Red','Yellow','Blue','Green','Orange','Purple','Pink','Brown','Violet','Cyan','Grey']
line1 = LabelFrame(start,width=1000,height=340)
line1.place(x=0,y=200)
#outer_box.pack(side='bottom',fill='x')

column=0
for j in range(15):
    s=random.choice(colours)
    t=random.choice(characters)
    button_x = Button(line1, text=t,width = 7,height = 2, bg= s,fg='white',font=("Arial Bold", 10))
    button_x.place(x = column, y = 260)
    button_x.pack(side='left')
    column=column + 15*j
    characters.remove(t)
    
line2 = LabelFrame(start,width=1000,height=320)
line2.place(x=0,y=245)


column=0
for j in range(15):
    s=random.choice(colours)
    t=random.choice(characters)
    button_x = Button(line2, text=t,width = 7,height = 2, bg= s,fg='white',font=("Arial Bold", 10))
    button_x.place(x = column, y = 260)
    button_x.pack(side='left')
    column=column + 15*j
    characters.remove(t)
    
line3 = LabelFrame(start,width=1000,height=320)
line3.place(x=0,y=290)

column=0
for j in range(15):
    s=random.choice(colours)
    t=random.choice(characters)
    button_x = Button(line3, text=t,width = 7,height = 2, bg= s,fg='white',font=("Arial Bold", 10))
    button_x.place(x = column, y = 260)
    button_x.pack(side='left')
    column=column + 15*j
    characters.remove(t)
    
line4 = LabelFrame(start,width=1000,height=340)
line4.place(x=0,y=335)
#outer_box.pack(side='bottom',fill='x')

column=0
for j in range(15):
    s=random.choice(colours)
    t=random.choice(characters)
    button_x = Button(line4, text=t,width = 7,height = 2, bg= s,fg='white',font=("Arial Bold", 10))
    button_x.place(x = column, y = 260)
    button_x.pack(side='left')
    column=column + 15*j
    characters.remove(t)
    
line5 = LabelFrame(start,width=1000,height=320)
line5.place(x=0,y=380)


column=0
for j in range(15):
    s=random.choice(colours)
    t=random.choice(characters)
    button_x = Button(line5, text=t,width = 7,height = 2, bg= s,fg='white',font=("Arial Bold", 10))
    button_x.place(x = column, y = 260)
    button_x.pack(side='left')
    column=column + 15*j
    characters.remove(t)
    
line6 = LabelFrame(start,width=1000,height=320)
line6.place(x=0,y=425)

column=0
for j in range(15):
    s=random.choice(colours)
    t=random.choice(characters)
    button_x = Button(line6, text=t,width = 7,height = 2, bg= s,fg='white',font=("Arial Bold", 10))
    button_x.place(x = column, y = 260)
    button_x.pack(side='left')
    column=column + 15*j
    characters.remove(t)


start.mainloop()