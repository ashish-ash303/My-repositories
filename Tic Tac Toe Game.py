from tkinter import *
import tkinter.messagebox

root=Tk()
root.title("Tic Tac Toe Game")
#root.title.pack()

root.geometry("1350x750+0+0")
root.configure(bg="cadet blue")
topframe=Frame(root,bg="cadet blue",padx=2,width=1350,height=100,relief=RIDGE)
topframe.grid(row=0,column=0)

lblTitle=Label(topframe,font=('arial',40,"bold"),text='Tic Tac Toe',bd=17,bg="cadet blue",fg="cornsilk",justify=CENTER)
lblTitle.grid(row=0,column=0)

Mainframe=Frame(root,bg="powder blue",bd=25,width=1350,height=600,relief=RIDGE)
Mainframe.grid(row=1,column=0)

Leftframe=Frame(Mainframe,bd=10,width=650,height=500,pady=2,padx=10,bg='cadet blue',relief=RIDGE)
Leftframe.pack(side=LEFT)
Rightframe=Frame(Mainframe,bd=10,width=650,height=500,pady=2,padx=10,bg='cadet blue',relief=RIDGE)
Rightframe.pack(side=RIGHT)

rightframe=Frame(Rightframe,bd=10,width=560,height=240,padx=10,pady=2,bg='cadet blue',relief=RIDGE)
rightframe.grid(row=0,column=0)

rightframe1=Frame(Rightframe,bd=10,width=560,height=240,padx=10,pady=2,bg='cadet blue',relief=RIDGE)
rightframe1.grid(row=1,column=0)

player1=IntVar()
player2=IntVar()

player1.set(0)
player2.set(0)

buttons=StringVar()
click= True

def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons['text']="x"
        click=False
        scorekeeper()
    elif buttons["text"] == " " and click == False:
        buttons['text']="o"
        click=True
        scorekeeper()
def scorekeeper():
    if (btn1['text'] == "x"and btn2['text'] == "x"and btn3['text'] == "x"):
        btn1.configure(bg="powder blue")
        btn2.configure(bg="powder blue")
        btn3.configure(bg="powder blue")
        n = float(player1.get())
        score = (n+1)
        player1.set(score)
        tkinter.messagebox.showinfo("player1","And The Winner is:- player1")

    if (btn4['text'] == "x"and btn5['text'] == "x"and btn6['text'] == "x"):
        btn4.configure(bg="cadet blue")
        btn5.configure(bg="cadet blue")
        btn6.configure(bg="cadet blue")
        n= float(player1.get())
        score=(n+1)
        player1.set(score)
        tkinter.messagebox.showinfo("player1","And The Winner is:- player1")
    if (btn7['text'] == "x" and btn8['text'] == "x" and btn9['text'] == "x"):
        btn7.configure(bg="gainsboro")
        btn8.configure(bg="gainsboro")
        btn9.configure(bg="gainsboro")
        n = float(player1.get())
        score = (n + 1)
        player1.set(score)
        tkinter.messagebox.showinfo("player1", "And The Winner is:- player1")
    if (btn3['text'] == "x" and btn5['text'] == "x" and btn7['text'] == "x"):
        btn3.configure(bg="red")
        btn5.configure(bg="red")
        btn7.configure(bg="red")
        n = float(player1.get())
        score = (n + 1)
        player1.set(score)
        tkinter.messagebox.showinfo("player1", "And The Winner is:- player1")
    if (btn1['text'] == "x" and btn5['text'] == "x" and btn9['text'] == "x"):
        btn1.configure(bg="blue")
        btn5.configure(bg="blue")
        btn9.configure(bg="blue")
        n = float(player1.get())
        score = (n + 1)
        player1.set(score)
        tkinter.messagebox.showinfo("player1", "And The Winner is:- player1")
    if (btn1['text'] == "x" and btn4['text'] == "x" and btn7['text'] == "x"):
        btn1.configure(bg="pink")
        btn4.configure(bg="pink")
        btn7.configure(bg="pink")
        n = float(player1.get())
        score = (n + 1)
        player1.set(score)
        tkinter.messagebox.showinfo("player1", "And The Winner is:- player1")

    if (btn2['text'] == "x" and btn5['text'] == "x" and btn8['text'] == "x"):
        btn2.configure(bg="gainsboro")
        btn5.configure(bg="gainsboro")
        btn8.configure(bg="gainsboro")
        n = float(player1.get())
        score = (n + 1)
        player1.set(score)
        tkinter.messagebox.showinfo("player1", "And The Winner is:- player1")

    if (btn3['text'] == "x" and btn6['text'] == "x" and btn9['text'] == "x"):
        btn3.configure(bg="orange")
        btn6.configure(bg="orange")
        btn9.configure(bg="orange")
        n = float(player1.get())
        score = (n + 1)
        player1.set(score)
        tkinter.messagebox.showinfo("player1", "And The Winner is:- player1")



    if (btn1['text'] == "o" and btn2['text'] == "o" and btn3['text'] == "o"):
        btn1.configure(bg="powder blue")
        btn2.configure(bg="powder blue")
        btn3.configure(bg="powder blue")
        n = float(player2.get())
        score = (n + 1)
        player2.set(score)
        tkinter.messagebox.showinfo("player2", "And The Winner is:- player2")
    if (btn4['text'] == "o" and btn5['text'] == "o" and btn6['text'] == "o"):
        btn4.configure(bg="cadet blue")
        btn5.configure(bg="cadet blue")
        btn6.configure(bg="cadet blue")
        n = float(player2.get())
        score = (n + 1)
        player2.set(score)
        tkinter.messagebox.showinfo("player2", "And The Winner is:- player2")
    if (btn7['text'] == "o" and btn8['text'] == "o" and btn9['text'] == "o"):
        btn7.configure(bg="black")
        btn8.configure(bg="black")
        btn9.configure(bg="black")
        n = float(player2.get())
        score = (n + 1)
        player2.set(score)
        tkinter.messagebox.showinfo("player2", "And The Winner is:- player2")
    if (btn3['text'] == "o" and btn5['text'] == "o" and btn7['text'] == "o"):
        btn3.configure(bg="brown")
        btn5.configure(bg="brown")
        btn7.configure(bg="brown")
        n = float(player2.get())
        score = (n + 1)
        player2.set(score)
        tkinter.messagebox.showinfo("player2", "And The Winner is:- player2")
    if (btn1['text'] == "o" and btn4['text'] == "o" and btn9['text'] == "o"):
        btn1.configure(bg="gainsboro")
        btn4.configure(bg="gainsboro")
        btn7.configure(bg="gainsboro")
        n = float(player2.get())
        score = (n + 1)
        player2.set(score)
        tkinter.messagebox.showinfo("player2", "And The Winner is:- player2")
    if (btn1['text'] == "o" and btn5['text'] == "o" and btn9['text'] == "o"):
        btn1.configure(bg="green")
        btn5.configure(bg="green")
        btn9.configure(bg="green")
        n = float(player2.get())
        score = (n + 1)
        player2.set(score)
        tkinter.messagebox.showinfo("player2", "And The Winner is:- player2")
    if (btn2['text'] == "o" and btn5['text'] == "o" and btn8['text'] == "o"):
        btn2.configure(bg="red")
        btn5.configure(bg="red")
        btn8.configure(bg="red")
        n = float(player2.get())
        score = (n + 1)
        player2.set(score)
        tkinter.messagebox.showinfo("player2", "And The Winner is:- player2")
    if (btn3['text'] == "o" and btn6['text'] == "o" and btn9['text'] == "o"):
        btn3.configure(bg="yellow")
        btn6.configure(bg="yellow")
        btn9.configure(bg="yellow")
        n = float(player2.get())
        score = (n + 1)
        player2.set(score)
        tkinter.messagebox.showinfo("player2", "And The Winner is:- player2")

    if (btn3['text'] == "o" and btn5['text'] == "o" and btn7['text'] == "o"):
        btn3.configure(bg="yellow")
        btn5.configure(bg="yellow")
        btn7.configure(bg="yellow")
        n = float(player2.get())
        score = (n + 1)
        player2.set(score)
        tkinter.messagebox.showinfo("player2", "And The Winner is:- player2")




def Reset():
    btn1['text'] = " "
    btn2['text'] = " "
    btn3['text'] = " "
    btn4['text'] = " "
    btn5['text'] = " "
    btn6['text'] = " "
    btn7['text'] = " "
    btn8['text'] = " "
    btn9['text'] = " "

    btn1.configure(bg="gainsboro")
    btn2.configure(bg="gainsboro")
    btn3.configure(bg="gainsboro")
    btn4.configure(bg="gainsboro")
    btn5.configure(bg="gainsboro")
    btn6.configure(bg="gainsboro")
    btn7.configure(bg="gainsboro")
    btn8.configure(bg="gainsboro")
    btn9.configure(bg="gainsboro")

def NewGame():
    Reset()
    player1.set(0)
    player2.set(0)






lblplayer1=Label(rightframe,text="Player 1 :-",font=('Times 20 bold'),height=3,width=8,bg="gainsboro",padx=2,pady=2)
lblplayer1.grid(row=0,column=0,sticky=W)
txtPlayer1 = Entry(rightframe, font=('arial', 30,'bold'), bg="gainsboro",bd=2,fg='black',textvariable=player1,width=22,justify=LEFT).grid(row=0, column=1)


lblplayer2=Label(rightframe,text="Player 2:- ",font=('Times 20 bold'),height=3,width=8,bg="gainsboro")
lblplayer2.grid(row=1,column=0)

txtPlayer2 = Entry(rightframe, font=('arial', 30, 'bold'), width=22, bg="gainsboro",bd=2,fg='black',textvariable=player2,justify=LEFT).grid(row=1, column=1)



btn1=Button(Leftframe,text=" ",font=('Times 26 bold'),height=3,width=8,bg="gainsboro",command=lambda:checker(btn1))
btn1.grid(row=1,column=0,sticky=S+N+W+E)

btn2=Button(Leftframe,text=" ",font=('Times 26 bold'),height=3,width=8,bg="gainsboro",command=lambda:checker(btn2))
btn2.grid(row=1,column=1,sticky=S+N+W+E)

btn3=Button(Leftframe,text=" ",font=('Times 26 bold'),height=3,width=8,bg="gainsboro",command=lambda:checker(btn3))
btn3.grid(row=1,column=2,sticky=S+N+W+E)

btn4=Button(Leftframe,text=" ",font=('Times 26 bold'),height=3,width=8,bg="gainsboro",command=lambda:checker(btn4))
btn4.grid(row=2,column=0,sticky=S+N+W+E)

btn5=Button(Leftframe,text=" ",font=('Times 26 bold'),height=3,width=8,bg="gainsboro",command=lambda:checker(btn5))
btn5.grid(row=2,column=1,sticky=S+N+W+E)

btn6=Button(Leftframe,text=" ",font=('Times 26 bold'),height=3,width=8,bg="gainsboro",command=lambda:checker(btn6))
btn6.grid(row=2,column=2,sticky=S+N+W+E)

btn7=Button(Leftframe,text=" ",font=('Times 26 bold'),height=3,width=8,bg="gainsboro",command=lambda:checker(btn7))
btn7.grid(row=3,column=0,sticky=S+N+W+E)

btn8=Button(Leftframe,text=" ",font=('Times 26 bold'),height=3,width=8,bg="gainsboro",command=lambda:checker(btn8))
btn8.grid(row=3,column=1,sticky=S+N+W+E)

btn9=Button(Leftframe,text=" ",font=('Times 26 bold'),height=3,width=8,bg="gainsboro",command=lambda:checker(btn9))
btn9.grid(row=3,column=2,sticky=S+N+W+E)

btnReset=Button(rightframe1,text="Reset",font=('Times 26 bold'),height=3,width=20,bg="gainsboro",command=Reset)
btnReset.grid(row=0,column=0,sticky=S+N+W+E)

btnNewGame=Button(rightframe1,text="New Game",font=('Times 26 bold'),height=3,width=20,bg="gainsboro",command=NewGame)
btnNewGame.grid(row=1,column=0,sticky=S+N+W+E)

root.mainloop()