"""
Créé par EL OUAZIZI Walid - L2 Info 5
"""

import Alien as aln
import random

try:  
    import tkinter as tk
    import tkinter.messagebox as tkMessageBox
except:
    import Tkinter as tk
    import tkMessageBox

class Fleet(object):
    
    #Fonction d'initialisation
    def __init__(self, game, hp):
        self.aliens_lines = 5
        self.aliens_columns = 10
        self.aliens_inner_gap = 20
        self.alien_x_delta = 5
        self.alien_y_delta = 15
        self.alienImage = tk.PhotoImage(file='images/alien.gif')
        self.explosionImage = tk.PhotoImage(file='images/explosion.gif')
        self.start_x = self.aliens_inner_gap + int(self.alienImage.width()/2)
        self.start_y = self.aliens_inner_gap + int(self.alienImage.height()/2)
        fleet_size = self.aliens_lines * self.aliens_columns
        self.aliens_fleet = [None] * fleet_size
        self.hp = hp
        self.game = game
        
        
    #Fonction de creation des aliens de notre flotte + dessin
    def install_in(self):
        canvas = self.game.getCanvas()
        for i in range(self.aliens_lines):
            for j in range(self.aliens_columns):
                numAlien = (j*1) + (i*self.aliens_columns)
                self.aliens_fleet[numAlien] = aln.Alien(self.hp)
                x = self.start_x + (j * (self.alienImage.width() + self.aliens_inner_gap))
                y = self.start_y + (i * (self.alienImage.height() + self.aliens_inner_gap))
                self.aliens_fleet[numAlien].install_in(canvas, x, y, self.alienImage, 'alien' + str(numAlien))
    
    #Fonction qui determine les mouvements de la flotte et deplace les aliens en fonction calcul aussi quand la partie est perdue
    def move_in(self):
        canvas = self.game.getCanvas()
        maxX = 0
        minX = 1024
        maxY = 0
        minY = 600
        
        #On parcourt chaque alien et on releve le X et Y, maximum et minmum de notre flotte
        for alien in self.aliens_fleet:
            if(int(canvas.coords(alien.id)[0])+int(self.alienImage.width()/2) > maxX):
                maxX = int(canvas.coords(alien.id)[0])+int(self.alienImage.width()/2)
                
            if(int(canvas.coords(alien.id)[0])-int(self.alienImage.width()/2)-self.aliens_inner_gap < minX):
                minX = int(canvas.coords(alien.id)[0])-int(self.alienImage.width()/2)-self.aliens_inner_gap
                
            if(int(canvas.coords(alien.id)[1])+int(self.alienImage.height()/2)  > maxY):
                maxY = int(canvas.coords(alien.id)[1])+int(self.alienImage.height()/2)
                
            if(int(canvas.coords(alien.id)[1])-int(self.alienImage.height()/2)-self.aliens_inner_gap < minY):
                minY = int(canvas.coords(alien.id)[1])-int(self.alienImage.height()/2)-self.aliens_inner_gap
            
        
        #Si notre flotte colle a droite on descend et commence a partir vers la gauche
        if(maxX >= 1024):
            for alien in self.aliens_fleet:
                alien.move_in(canvas, -2*self.alien_x_delta, self.alien_y_delta)
                
        #Si notre flotte colle a gauche on descend et commence a partir vers la droite        
        if(minX < -10): 
            for alien in self.aliens_fleet:
                alien.move_in(canvas, 2*self.alien_x_delta, self.alien_y_delta)
                
        # 1 position en Y sur 2 on va vers la droite ou la gauche
        if(minY % 30 == 0): 
            for alien in self.aliens_fleet:
                alien.move_in(canvas, self.alien_x_delta, 0)
        else:
            for alien in self.aliens_fleet:
                alien.move_in(canvas, -self.alien_x_delta, 0)
        
        # Si ce maxY est atteint la partie est perdue
        if(maxY > 575):
            tk.messagebox.showinfo("Loose !!!", "Bien tenté ! - Score: " + str(self.game.getDefender().getScore()))
            self.game.getMainClass().clearFrame()
            self.game.getMainClass().drawMenu()
        
    #Pour chaque alien pour chaque balle tires on verifie la collision
    #Si il y'a collision alors on retire de la vie à l'alien, on suppr la balle et on spawn l'explosion
    def manage_touched_aliens_by(self, defender):
        canvas = self.game.getCanvas()
        for alien in self.aliens_fleet:
            for bullet in defender.fired_bullets:
                if(alien.touched_by(canvas, bullet)):
                    xBullet, yBullet, xBullet1, yBullet1 = canvas.bbox(bullet.id)
                    alien.life -= 1
                    canvas.delete(bullet.id)
                    defender.fired_bullets.remove(bullet)
                    explosionId = canvas.create_image(xBullet, yBullet, image=self.explosionImage, tags='explosion')
                    
    #Fais tirer un alien au hasard                
    def alien_shoot(self, canvas):
        if(self.fleet_alive):
            angryAlien = random.choice(self.aliens_fleet)
            if angryAlien.alive:
                angryAlien.fire(canvas)

    #Renvoie True si au moins 1 alien est encore en vie 0 sinon        
    def fleet_alive(self):
        anybodyAlive = False
        for alien in self.aliens_fleet:
            if alien.alive:
                anybodyAlive = True
        return anybodyAlive

    #Gere la mort d'un alien si il n'as plus de vie
    def manageDeath(self):
        canvas = self.game.getCanvas()
        defender = self.game.getDefender()
        for alien in self.aliens_fleet:
            if(alien.life < 1):
                alien.alive = False
                if(alien in self.aliens_fleet): #Parfois 2 bullet arrive en meme temps sur un Alien et le programme
                    for alienbullet in alien.fired_bullets: #essaye de le supprimer 2 fois on evite avec la condition
                        canvas.delete(alienbullet.id) #On supprime aussi les balles tires par l'alien mort
                    canvas.delete(alien.id)
                    self.aliens_fleet.remove(alien)
                    defender.score += 50