"""
Créé par EL OUAZIZI Walid - L2 Info 5
"""

try:  
    import tkinter as tk
    import tkinter.messagebox as tkMessageBox
except:
    import Tkinter as tk
    import tkMessageBox

#Classe correspondant a une balle
class Bullet(object):
    def __init__(self, shooter):
        self.radius = 5
        self.color = "red"
        self.speed = 8
        self.id = None
        self.shooter = shooter
   
    #Installe le bullet dans un canvas
    def install_in(self, canvas): 
        xBS = canvas.coords(self.shooter.id)[0] + 10# For aesthetic spawn
        yBS = canvas.coords(self.shooter.id)[1] - 4 # Same
        self.id = canvas.create_oval(xBS - self.radius, yBS - self.radius, xBS + self.radius, yBS + self.radius, fill=self.color)     
    
    def move_in(self, canvas):
        yT = (canvas.coords(self.id)[1]) #Recupere le Y le plus bas de la bullet
        if(yT < 1):
            canvas.delete(self.id)
            self.shooter.fired_bullets.remove(self) #Supprime la bullet si elle sort de la scene
        else:
            canvas.move(self.id, 0, -1 * self.speed) #Deplace la bullet si elle est tjr dans la scene