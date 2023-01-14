import sys
import math
import pyautogui
import numpy as np
import tkinter as tk
from pynput.keyboard import Key, Listener, KeyCode

offx = 500
offy = 500

power = 100
angle = 90

root = tk.Tk()
root.attributes("-topmost", True)
root.attributes("-toolwindow", False)
root.attributes("-transparentcolor", "white")
root.state('zoomed')
root.attributes("-fullscreen", True)

canvas = tk.Canvas(root, bg='white', width=1920, height=1080)
canvas.pack()


def projectile_motion(power, angle):
    g = 20
    v0 = power
    theta = math.radians(angle)
    t = (2 * v0 * math.sin(theta))/g
    x_coordinates = np.linspace(0, 1000, 1000)
    x = v0 * math.cos(theta) * x_coordinates / 1000 
    y = v0 * math.sin(theta) * x_coordinates / 1000 - (0.1 * g * (x_coordinates / 100)**2)
    
    x = np.ceil( x*100 ).astype(int)
    y = np.ceil( y*100 ).astype(int)
    
    return x,y


def draw( tx , ty, offx, offy ):
    canvas.delete("all")
    canvas.create_oval( offx-3 , offy-3 , offx+3 , offy+3 , fill="green" )
    for i in range(0, tx.size - 400, 3 ):
        canvas.create_line( tx[i] + offx , offy + ty[i]*(-1) , tx[i+1] + offx , offy + ty[i+1]*(-1) , width=2, fill='red' )

def on_press(key):
    global offx
    global offy
    
    global power
    global angle
     
    print('pressed key {0}'.format(key))
    if key == Key.left:
        angle = angle + 1
    if key == Key.right:
        angle = angle - 1
    if key == Key.up:
        power = power + 1
    if key == Key.down:
        power = power - 1
    
    if key == KeyCode.from_char('f'):
        power = 100
        angle = 90
    if key == KeyCode.from_char('g'):
        offx , offy = pyautogui.position()
        #offy = offy - 31 + 7
        print(offx)
        print(offy)
    
    if power > 100:
        power = 100
    if power < 0:
        power = 0
        
            
            
    tx , ty = projectile_motion( power , angle )
    draw( tx , ty, offx, offy )


listener = Listener( on_press=on_press)
listener.start()


root.mainloop()
print("close")
sys.exit()

