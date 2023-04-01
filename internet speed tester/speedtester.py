from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+"Mbps"
    up = str(round(sp.upload() / (10 ** 6), 3)) + "Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = Tk()
sp.title(" Internet Speed Test ")
sp.geometry("500x650")
sp.config(bg="Blue")

lab = Label(sp,text=" Internet Speed Test ", font=("Time New Roman", 30),bg="Blue",fg="White")
lab.place(x=60,y=40,height=50,width=380)




lab = Label(sp,text=" Download Speed  ", font=("Time New Roman", 30),bg="Blue",fg="White")
lab.place(x=55,y=130)





lab_down = Label(sp,text=" 00 ", font=("Time New Roman", 30),bg="Blue",fg="White")
lab_down.place(x=55,y=200)




lab = Label(sp,text=" Upload Speed  ", font=("Time New Roman", 30), bg="Blue" , fg="White")
lab.place(x=55,y=290)





lab_up = Label(sp,text=" 00 ", font=("Time New Roman", 30),bg="Blue",fg="White")
lab_up.place(x=55,y=360)

button = Button(sp,text="Check Speed",font=("Time New Roman", 30), relief=RAISED,bg="Red", command=speedcheck )
button.place(x=60,y=460,height=50,width=380)


sp.mainloop()