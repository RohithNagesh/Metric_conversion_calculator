from tkinter import *

root = Tk()
root.geometry('400x550')
root.title('USC')
Label(root, text= 'UNIT SYSTEM CONVERTER',font = 'arial 16 bold').pack()
Label(root, text = 'Click Any One :', font = 'arial 14 bold').pack()

def sitocgs():
    a=Entry(root,width=50)
    a.pack()
    a.insert(0,'"Clear Me and Enter parameter"')
    b=Entry(root,width=50)
    b.pack()
    b.insert(0,'"Clear Me and Enter value in SI units"')
    def results1():
        d=a.get()
        e=float(b.get())
        if d=='length' :
            labellength=Label(root,text=('In CGS unit syatem its',e*100,'centimeters'))
            labellength.pack()
        elif d=='mass' :
            lablemass=Label(root,text=('In CGS system its',e*1000,'grams'))
            lablemass.pack()
        elif d=='time' :
            labletime=Label(root,text=('Even in CGS unit system its',e,"seconds"))
            labletime.pack()
    Button(root,text='submit',command=results1).pack()
    
def sitofps():
    a=Entry(root,width=50)
    a.pack()
    a.insert(0,'"Clear Me and Enter parameter"')
    b=Entry(root,width=50)
    b.pack()
    b.insert(0,'"Clear Me and Enter value in SI units"')
    def results2():
        d=a.get()
        e=float(b.get())
        if d=='length' :
            labellength=Label(root,text=('In FPS unit syatem its',e*3.28084,'feet'))
            labellength.pack()
        elif d=='mass' :
            lablemass=Label(root,text=('In FPS system its',e*2.20462,'pounds'))
            lablemass.pack()
        elif d=='time' :
            labletime=Label(root,text=('Even in FPS unit system its',e,"seconds"))
            labletime.pack()
    Button(root,text='submit',command=results2).pack()

def cgstofps():
    a=Entry(root,width=50)
    a.pack()
    a.insert(0,'"Clear Me and Enter parameter"')
    b=Entry(root,width=50)
    b.pack()
    b.insert(0,'"Clear Me and Enter value in CGS units"')
    def results3():
        d=a.get()
        e=float(b.get())
        if d=='length' :
            labellength=Label(root,text=('In FPS unit syatem its',e*0.0328084,'feet'))
            labellength.pack()
        elif d=='mass' :
            lablemass=Label(root,text=('In FPS system its',e*0.00220462,'pounds'))
            lablemass.pack()
        elif d=='time' :
            labletime=Label(root,text=('Even in FPS unit system its',e,"seconds"))
            labletime.pack()
    Button(root,text='submit',command=results3).pack()

def cgstosi():
    a=Entry(root,width=50)
    a.pack()
    a.insert(0,'"Clear Me and Enter parameter"')
    b=Entry(root,width=50)
    b.pack()
    b.insert(0,'"Clear Me and Enter value in CGS units"')
    def results4():
        d=a.get()
        e=float(b.get())
        if d=='length' :
            labellength=Label(root,text=('In SI unit syatem its',e*0.01,'meters'))
            labellength.pack()
        elif d=='mass' :
            lablemass=Label(root,text=('In SI system its',e*0.001,'kilograms'))
            lablemass.pack()
        elif d=='time' :
            labletime=Label(root,text=('Even in SI unit system its',e,"seconds"))
            labletime.pack()
    Button(root,text='submit',command=results4).pack()

def fpstosi():
    a=Entry(root,width=50)
    a.pack()
    a.insert(0,'"Clear Me and Enter parameter"')
    b=Entry(root,width=50)
    b.pack()
    b.insert(0,'"Clear Me and Enter value in FPS units"')
    def results5():
        d=a.get()
        e=float(b.get())
        if d=='length' :
            labellength=Label(root,text=('In SI unit syatem its',e*0.3048,'meters'))
            labellength.pack()
        elif d=='mass' :
            lablemass=Label(root,text=('In SI system its',e*0.453592,'kilograms'))
            lablemass.pack()
        elif d=='time' :
            labletime=Label(root,text=('Even in SI unit system its',e,"seconds"))
            labletime.pack()
    Button(root,text='submit',command=results5).pack()

def fpstocgs():
    a=Entry(root,width=50)
    a.pack()
    a.insert(0,'"Clear Me and Enter parameter"')
    b=Entry(root,width=50)
    b.pack()
    b.insert(0,'"Clear Me and Enter value in FPS units"')
    def results6():
        d=a.get()
        e=float(b.get())
        if d=='length' :
            labellength=Label(root,text=('In CGS unit syatem its',e*30.48,'centimeters'))
            labellength.pack()
        elif d=='mass' :
            lablemass=Label(root,text=('In CGS system its',e*453.592,'grams'))
            lablemass.pack()
        elif d=='time' :
            labletime=Label(root,text=('Even in CGS unit system its',e,"seconds"))
            labletime.pack()
    Button(root,text='submit',command=results6).pack()

Button(root, text= 'SI to CGS',width=25,  command= sitocgs,height=2, bg = 'blue',fg='white').pack()
Button(root, text= 'SI to FPS',width=25,  command= sitofps,height=2, bg = 'blue',fg='white').pack()
Button(root, text= 'CGS to FPS',width=25, command= cgstofps,height=2, bg = 'blue',fg='white').pack()
Button(root, text= 'CGS to SI',width=25, command= cgstosi,height=2, bg = 'blue',fg='white').pack()
Button(root, text= 'FPS to SI',width=25, command= fpstosi,height=2, bg = 'blue',fg='white').pack()
Button(root, text= 'FPS to CGS',width=25, command= fpstocgs,height=2, bg = 'blue',fg='white').pack()
Button(root, text= 'STOP', width=25, command= root.destroy,height=2, bg= 'red').pack()

root.mainloop()
