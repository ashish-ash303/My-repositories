from tkinter import *

root=Tk()
root.grometry=("1350+650+0+0")
root.title("Body Mass Index")
root.resizable(0,0)
def BMIcal():
        BHeight=float(heightvariable.get())
        BWeight=float(weightvariable.get())
        BMI=str('%.2f' %((BHeight* BHeight)/BWeight))
        lblResult.config(text=BMI)





weightvariable=StringVar()
heightvariable=StringVar()

Topframe =Frame(root,width=600,height=50,bd=6,relief="raise",bg="powder blue")
Topframe.pack(side=TOP)

Leftframe=Frame(root,width=600,height=1000,bd=18,relief="raise",bg="powder blue")
Leftframe.pack(side=LEFT)

Rightframe=Frame(root,width=400,height=400,bd=4,relief="raise",bg="powder blue")
Rightframe.pack(side=RIGHT)


Le=Frame(Leftframe,width=600,height=700,bd=20,relief="raise")
Le.pack(side=TOP)

le1=Frame(Leftframe,width=500,height=1500,bd=28,relief="raise")
le1.pack(side=TOP)

lblTitle=Label(Topframe,text=' Body Mass index', font=('arial',55,"italic"),padx=6,pady=1,bd=10,relief="raise",width=15,height=1,bg="cadet blue")
lblTitle.pack()

lblweight=Label(Le,text="select weight in kg",font=('arial',15,'bold'),bd=10 ,bg='cadet blue',padx=10,pady=12).grid(row=0,column=0)
Bodyweight=Scale(Le,variable=weightvariable,from_= 1,to=300,length=450,   tickinterval= 20,orient=HORIZONTAL,bg="cadet blue")
Bodyweight.grid(row=1,column=0)

lblheight=Label(le1,text="Enter your in cm",font=('arial',20,'bold'),bd=20 ,bg='cadet blue').grid(row=0,column=0)
txtheightt=Entry(le1,textvariable=heightvariable,font=('arial',20,'bold'),bd=20,width=45,justify='center',bg="cadet blue")
txtheightt.grid(row=1,column=0,pady=15,padx=15)

lblResult=Label(le1,padx=16,pady=16,bd=15,font=('arial',20,'bold'),bg='sky blue',relief='sunk',width=25,height=1)
lblResult.grid(row=2,column=0)

lblBMITable=Label(Rightframe,font=('arial',20,'bold'),text="BMI Table And Inches in Cm",bg='sky blue').grid(row=0,column=0)
txtlblBMITable=Text(Rightframe,height=14,width=22,bd=16,font=('arial',20,'bold'),bg='cadet blue')
txtlblBMITable.grid(row=1,column=0)

txtlblBMITable.insert(END,'Meaning:\t\t'+'\n\n')
txtlblBMITable.insert(END,'Normal weight:-\t\t'+'19-24\n\n')
txtlblBMITable.insert(END,'Overweight:- \t\t'+' 25-29\n\n')
txtlblBMITable.insert(END,'Obesity 1 lev:-\t\t'+'30-34\n\n')
txtlblBMITable.insert(END,'obesity lev 2:-\t\t'+' 35-39\n\n')
txtlblBMITable.insert(END,'obesity lev 3:-\t\t'+'40-45\n\n')
txtlblBMITable.insert(END,'ONE INCHES:-\t'+'2.54CM\n\n')
btnBMI=Button(Rightframe,font=('arial',20,'bold'),text="ClickToCheckBMI",padx=1,pady=1,bd=12,width=16,height=1,command=BMIcal,bg="cadet blue")
btnBMI.grid(row=2,column=0)







root.mainloop()