import tkinter as tk
pencere = tk.Tk()
entry = tk.Entry()
entry.pack()
pencere.title("WWW.ART PLUS.COM")
pencere.geometry("1000x1000")


labell = tk.Label(pencere, text="WELCOME TO ART PLUS...", font="Verdana 20")
labell.pack()
label00 = tk.Label(pencere, text="PLEASE SELECT THE ACTION YOU WISH TO DO...", font="Verdana 13")
label00.pack()

def buton():
    label = tk.Label(pencere, text="korayabaci67@GMAİL.COM")
    label.pack()
def buton1():
    label11 = tk.Label(pencere, text=" \n individual logo design \n institutional logo design \n purpose education logo desing")
    label11.pack()

def buton2():
    label22 = tk.Label(pencere, text=" \n starter packet 500 TL\n middle packet 1000TL\n Professional packet 2000TL")
    label22.pack()

def buton3():
    label33 = tk.Label(pencere, text="\n TESLA \n SPACEX \n ACUN MEDYA \n  SOSYAL MEDYA")
    label33.pack()

def buton4():
    label44 = tk.Label(pencere, text="The company is constantly growing")
    label44.pack()


label1 = tk.Label(pencere, text="CONTACT INFORMATION  ")
buton = tk.Button(pencere, text="click", fg="black", command=buton)
label1.pack()
buton.pack()


label2 = tk.Label(pencere, text="ORDER")
buton1 = tk.Button(pencere, text="click", fg="black", command=buton1)
label2.pack()
buton1.pack()

label3 = tk.Label(text="OUR PACKAGES ARE AS FOLLOWS")
buton2 = tk.Button(pencere, text="click", fg="black", command=buton2)
label3.pack()
buton2.pack()

label4 = tk.Label(pencere, text="CONTRACTED COMPANIES LIST")
buton3 = tk.Button(pencere, text="click", fg="black", command=buton3)
label4.pack()
buton3.pack()

label5 = tk.Label(pencere, text="COMPANY REPORT")
buton4 = tk.Button(pencere, text="click", fg="black", command=buton4)
label5.pack()
buton4.pack()

label6 = tk.Label(pencere, text="WRITE YOUR SUGGESTIONS AND COMPLAINTS HERE")
label6.pack()


def verial():
    label7["text"] = entry.get()
label7 = tk.Label(pencere, text="", fg="black")
buton5 = tk.Button(pencere, text="click", fg="black", command=verial)
buton5.pack()
label7.pack()
entry.place(x=430, y=400)

pencere.mainloop()
