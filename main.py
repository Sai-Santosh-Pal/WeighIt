import tkinter
from tkinter import *
from tkinter.ttk import *


root = Tk()
root.title("Weight Calculator")
icon_path = r"C:\Python\Python-Projects\Weight-Converter\favicon.ico"
root.iconbitmap(icon_path)
root.geometry("750x750")


heading_label = Label(root, text="Weight Converter", font="Verdana 20 underline bold")
kg_label = Label(root, text="kg").grid(row=2, column=2)


weight = IntVar()
def back_end():
    weight_get = weight.get()

    weight_mercury = weight_get * 0.378
    weight_venus = weight_get * 0.907
    weight_earth = weight_get * 1
    weight_moon = weight_get * 0.166
    weight_mars = weight_get * 0.377
    weight_jupiter = weight_get * 2.364
    weight_saturn = weight_get * 0.916
    weight_uranus = weight_get * 0.889
    weight_neptune = weight_get * 1.125
    weight_pluto = weight_get * 0.067
    weight_sun = weight_get * 27.072

    sun = Label(root, text=f"Sun: {weight_sun} kg")
    mercury = Label(root, text=f"Mercury: {weight_mercury} kg")
    venus = Label(root, text=f"Venus: {weight_venus} kg")
    earth = Label(root, text=f"Earth: {weight_earth} kg")
    moon = Label(root, text=f"The Moon: {weight_moon} kg")
    mars = Label(root, text=f"Mars: {weight_mars} kg")
    jupiter = Label(root, text=f"Jupiter: {weight_jupiter} kg")
    saturn = Label(root, text=f"Saturn: {weight_saturn} kg")
    uranus = Label(root, text=f"Uranus: {weight_uranus} kg")
    neptune = Label(root, text=f"Neptune: {weight_neptune} kg")
    pluto = Label(root, text=f"Pluto: {weight_pluto} kg")

    sun.grid(row=5, column=0)
    mercury.grid(row=6, column=0)
    venus.grid(row=7, column=0)
    earth.grid(row=8, column=0)
    moon.grid(row=9, column=0)
    mars.grid(row=10, column=1)
    jupiter.grid(row=5, column=4)
    saturn.grid(row=6, column=4)
    uranus.grid(row=7, column=4)
    neptune.grid(row=8, column=4)
    pluto.grid(row=9, column=4)
    

    

  
 
l1 = Label(root, text = "Weight") 
 
  

l1.grid(row = 2, column = 0, sticky = W, pady = 2) 

  
e1 = Entry(root, textvariable=weight) 
e1.delete(3, 'end')
  
e1.grid(row = 2, column = 1, pady = 2) 

submit = Button(root, text="Submit", command=back_end)
submit.focus_set()
submit.grid(row=3, column=0)

heading_label.grid(row=0, column=7)

root.mainloop() 
