"""
Créé par EL OUAZIZI Walid - L2 Info 5
"""

import Fleet as flt
import Defender as dfd
import Score as scr
import random

try:  
    import tkinter as tk
    import tkinter.messagebox as tkMessageBox
except:
    import Tkinter as tk
    import tkMessageBox

class Game(object):

    #Initalisation et installation de notre scene de jeu
    def __init__(self, mainClass, pseudo, health_point_alien, health_point_defender):
        self.mainClass = mainClass
        self.pseudo = pseudo
        self.frame = self.mainClass.getFrame()
        self.fleet = flt.Fleet(self, health_point_alien)
        self.defender = dfd.Defender(self, health_point_defender)
        self.height = 600
        self.width = 1024
        self.canvas = tk.Canvas(self.frame, width=self.width, height=self.height, bg='black', bd=0, highlightthickness=0)
        self.explosionList = []
        self.canvas.pack()
        self.defender.install_in()
        self.fleet.install_in()

    #Demarre l'animation
    def start_animation(self):
        self.canvas.after(10, self.animation)
        
    #Boucle d'animation
    def animation(self):
        self.move_bullets()
        self.move_aliens_fleet()
        self.alienShoot()
        self.fleet.manage_touched_aliens_by(self.defender)
        self.defender.touched_by_fleetShot()
        self.defender.updateScore()
        self.check_win()
        self.defender.manageDeath()
        self.fleet.manageDeath()
        self.removeAllExplosion()
        self.canvas.after(100, self.animation) # Boucle d'animation de la scene
        
    #Effecture l'animation de nos balles
    def move_bullets(self):
        for bullet in self.defender.fired_bullets:
            bullet.move_in(self.canvas)
        for alien in self.fleet.aliens_fleet:
            for bullet in alien.fired_bullets:
                bullet.move_in(self.canvas)
        
    #Effectue l'animation de notre flotte
    def move_aliens_fleet(self):
        self.fleet.move_in()
        
    #Si aucun alien de notre flotte n'est en vie cela signifie que la partie est gagnée, retour au menu ensuite
    def check_win(self):
        if(not self.fleet.fleet_alive()):
            tk.messagebox.showinfo("WIN !!!", "Bien joué ! - Score: " + str(self.defender.score))
            self.mainClass.clearFrame()
            self.mainClass.drawMenu()

    #Fais tirer nos aliens sur quelques frame
    def alienShoot(self):
        alienshoot = random.randint(0, 50)
        if(alienshoot % 49 == 0): self.fleet.alien_shoot(self.canvas) # 1 chance sur 50 pour que sur une frame un des Alien tire"""

    #Fonction qui recherche touts les sprite avec le tag explosion et les renvoie a la fonction
    # removeExplosion toutes les 10ms  
    def removeAllExplosion(self):
        allExplosionId = self.canvas.find_withtag('explosion')
        for explosionId in allExplosionId:
            self.canvas.after(10, self.removeExplosion(explosionId))

    #Fonction qui verifie si le sprite appartient a la collection a supprimer
    # Si oui il le supprime
    # Si non il l'ajoute a la collection afin de la supprimer le tour d'apres        
    def removeExplosion(self, id):
        if(id in self.explosionList):
            self.canvas.delete(id)
        else:
            self.explosionList.append(id)

    #Getter de canvas, defender, fleet, SpaceInvaders et Pseudo
    def getCanvas(self):
        return self.canvas

    def getDefender(self):
        return self.defender

    def getFleet(self):
        return self.fleet

    def getMainClass(self):
        return self.mainClass
    
    def getPseudo(self):
        return self.pseudo