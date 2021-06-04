import tkinter as tk
from tkinter import font

#standard stats

window = tk.Tk()
window.geometry("500x700")
window.title("DWZ-Rechner")


#Elemente

label1 = tk.Label(text="Willkommen beim DWZ-Rechner:", font=20)
break1 = tk.Label(text="")

label2 = tk.Label(text="Alte DWZ:", font=20)
dwzalt = tk.Entry(font=20)
break2 = tk.Label(text="")

label3 = tk.Label(text="Punkte geholt:", font=20)
punkte = tk.Entry(font=20)
break3 = tk.Label(text="")

label4 = tk.Label(text="Anzahl Gegner:", font=20)
gegner = tk.Entry(font=20)
break4 = tk.Label(text="")

label5 = tk.Label(text="DWZ der Gegner:", font=20)
dwz1 = tk.Entry(font=20)
dwz2 = tk.Entry(font=20)
dwz3 = tk.Entry(font=20)
dwz4 = tk.Entry(font=20)
dwz5 = tk.Entry(font=20)
dwz6 = tk.Entry(font=20)
dwz7 = tk.Entry(font=20)
break5 = tk.Label(text="")

label6 = tk.Label(text="", font=20)

label7 = tk.Label(text="", font=20)


berechne = tk.Button(text="Jetzt Berechnen!", font=20)

break99 = tk.Label(text="")
end = tk.Button(text="End Applicatiom", command=window.quit)



#Elemente einfügen

label1.pack()
break1.pack()

label2.pack()
dwzalt.pack()
break2.pack()

label3.pack()
punkte.pack()
break3.pack()

label4.pack()
gegner.pack()
break4.pack()

label5.pack()
dwz1.pack()
dwz2.pack()
dwz3.pack()
dwz4.pack()
dwz5.pack()
dwz6.pack()
dwz7.pack()
break5.pack()

berechne.pack()
#u


break99.pack()
end.pack()


window.mainloop()