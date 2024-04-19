"""
Créé par EL OUAZIZI Walid - L2 Info 5
"""
try:  
    import tkinter as tk
    import tkinter.messagebox as tkMessageBox
except:
    import Tkinter as tk
    import tkMessageBox
    
import AlienBullet as alnblt

class Alien(object):
    #Initialise nos aliens
    def __init__(self, hp):
        self.id = None
        self.alive = True
        self.life = hp
        self.fired_bullets = []

    #Calcul pour savoir si projectile se trouve dans la hitbox de l'Alien    
    def touched_by(self, canvas, projectile):
        if(self.alive):
            if(projectile):
                xP, yP, xP1, yP1 = canvas.coords(projectile.id)
            xA, yA, xA1, yA1 = canvas.bbox(self.id)
            if(xP >= xA and xP <= xA1 and yP >= yA and yP <= yA1):
                return True
        
    #Installe un alien aux coords x y
    def install_in(self, canvas, x, y, image, tag):
        self.id = canvas.create_image(x, y, image=image, tags=tag)
      
    #Deplace un alien en fonction de dx et dy
    def move_in(self, canvas, dx, dy):
        canvas.move(self.id, dx, dy)
        
    #Fais tirer un alien    
    def fire(self, canvas):
        if(len(self.fired_bullets) <= 7):
            self.fired_bullets.append(alnblt.AlienBullet(self))
            bullet = self.fired_bullets[-1]
            bullet.install_in(canvas)