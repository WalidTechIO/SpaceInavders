"""
Créé par EL OUAZIZI Walid - L2 Info 5
"""

import Bullet as blt
import Score as scr

try:  
    import tkinter as tk
    import tkinter.messagebox as tkMessageBox
except:
    import Tkinter as tk
    import tkMessageBox

class Defender(object):
    #Initalise note defender
    def __init__(self, game, life):
        self.width = 20
        self.height = 20
        self.move_delta = 30
        self.id = None
        self.max_fired_bullets = 8
        self.fired_bullets = []
        self.score = 0
        self.pseudo = game.getPseudo()
        self.life = life
        self.game = game
    
    #Dessine notre defender a sa position initiale
    def install_in(self):
        canvas = self.game.getCanvas()
        x, y = int(canvas.cget('width'))/2, int(canvas.cget('height')) - 5 #Spawn au milieu de l'axe X a 5px du bord bas de la fenetre
        self.id = canvas.create_rectangle(x, y, x + self.width, y - self.height, fill='white')

    #Deplace le Defender a gauche si dx = -1 droite si dx = 1    
    def move_in(self, dx):
        canvas = self.game.getCanvas()
        x0, x1 = canvas.coords(self.id)[0], canvas.coords(self.id)[2]
        if not((dx > 0) and (x1 > 1023)) and not((dx < 0) and (x0 < 1)): #This line test if the Defender is not in a corner
            canvas.move(self.id, self.move_delta * dx, 0)
        
    #Permet de tirer une balle
    #Installation de la balle dans la scene + ajout au tableau des balles tirées
    def fire(self):
        canvas = self.game.getCanvas()
        if(len(self.fired_bullets) <= 7):
            self.fired_bullets.append(blt.Bullet(self))
            bullet = self.fired_bullets[-1]
            bullet.install_in(canvas)
    
    #Met a jour le score du joueur a chaque image
    def updateScore(self):
        score = scr.Score()
        scorelist = score.read()
        scorelist[self.pseudo] = self.score
        score.write(scorelist)

    #Calcul qui verifie si une bullet alien est dans la hitbox du Defender    
    def touched_by_fleetShot(self):
        xDefender, yDefender, xDefender1, yDefender1 = self.game.getCanvas().bbox(self.id)
        for alien in self.game.getFleet().aliens_fleet:
            for alien_bullet in alien.fired_bullets:
                x, y = self.game.getCanvas().coords(alien_bullet.id)[0], self.game.getCanvas().coords(alien_bullet.id)[3]
                if(x >= xDefender and x <= xDefender1 and y >= yDefender and y <= yDefender1):
                    self.life -= 1
                    self.game.getCanvas().delete(alien_bullet.id)
                    alien.fired_bullets.remove(alien_bullet)

    #Gere la mort et la defaite du defender en cas de tir alen                
    def manageDeath(self):
            if(self.life == 0):
                tk.messagebox.showinfo("Loose !!!", "Bien tenté ! - Score: " + str(self.game.getDefender().getScore()))
                self.game.getMainClass().clearFrame()
                self.game.getMainClass().drawMenu()

    #Renvoie le score        
    def getScore(self):
        return self.score