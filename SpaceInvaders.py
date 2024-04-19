"""
Créé par EL OUAZIZI Walid - L2 Info 5
"""

import Game as gm
import Score as scr

try:  
    import tkinter as tk
    import tkinter.messagebox as tkMessageBox
except:
    import Tkinter as tk
    import tkMessageBox

class SpaceInvaders(object):
    """
    Main Game Class
    """
    #On initialise notre jeu
    def __init__(self):
        #Variables dinstances de la classe principale
        self.root = tk.Tk()
        self.root.title("Space Invaders")
        self.root.geometry("1024x600")
        self.root.bind("<Key>", self.keypress)
        self.root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
        self.score = scr.Score()
        self.frame = tk.Frame(self.root)
        self.game = None
        
        #Dessin du menu
        self.drawMenu()
        
        
    #On definit les controles
    def keypress(self, event):
        if event.keysym == 'Left':
            self.game.defender.move_in(-1)
        if event.keysym == 'Right':
            self.game.defender.move_in(1)
        if event.keysym == 'space':
            self.game.defender.fire()
        if event.keysym == 'Escape':
            self.clearFrame()
            self.drawMenu()
        
    #On lance le mainloop
    def play(self):
        self.root.mainloop()
        
    #Code qui s'execute au click du bouton demarrer la partie
    def startGame(self):
        if(self.pseudo.get()):
            pseudo = self.pseudo.get()
        else:
            try:
                pseudo = self.scoreboard.get(self.scoreboard.curselection())
            except:
                pseudo = None
        health_point_alien = self.alien_health.get()
        health_point_defender = self.defender_health.get()
        #Le code ci-dessus 
        if(pseudo):
            self.clearFrame()  
            if(health_point_alien and health_point_defender):
                self.game = gm.Game(self, pseudo, int(health_point_alien), int(health_point_defender))
            elif(health_point_alien):
                self.game = gm.Game(self, pseudo, int(health_point_alien), 3)
            elif(health_point_defender):
                self.game = gm.Game(self, pseudo, 2, int(health_point_defender))
            else:
                self.game = gm.Game(self, pseudo, 2, 3)
            self.frame.pack(side="top", fill="both", expand="true")
            self.game.start_animation()
        else:
            tkMessageBox.showerror("Erreur", "Vous devez choisir un pseudo !")
        
    #Supprime tout ce qui est afficher (pour passer du menu a la partie et inversement)
    def clearFrame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.destroy()
        for widget in self.root.winfo_children():
            widget.destroy()
        self.frame = tk.Frame(self.root)
        
    #Genere la frame menu du jeu
    def drawMenu(self):
        self.frame.place(anchor='center', relx=.5, rely=.5)
        #Label
        tk.Label(self.root, text="Space Invaders", font=("Arial", 30)).pack(side='top')
        tk.Label(self.frame, text="Pseudonyme : ").grid(row="0")
        tk.Label(self.frame, text="Scoreboard").grid(row="1")
        tk.Label(self.frame, text="Points de vies Aliens : ").grid(row="2")
        tk.Label(self.frame, text="Points de vies Defender : ").grid(row="3")
        #Elements
        self.pseudo = tk.Entry(self.frame)
        self.pseudo.grid(row="0", column="1")
        self.scoreboard = tk.Listbox(self.frame)
        self.scoreboard.grid(row="1", column="1")
        self.scoreboard_score = tk.Listbox(self.frame)
        self.scoreboard_score.grid(row="1", column="2")
        self.scoreboard_score.configure(exportselection='False')
        self.alien_health = tk.Entry(self.frame)
        self.alien_health.grid(row="2", column="1")
        self.alien_health.insert(-1, "2")
        self.defender_health = tk.Entry(self.frame)
        self.defender_health.grid(row="3", column="1")
        self.defender_health.insert(-1, "3")
        self.demarrer = tk.Button(self.frame, command=self.startGame, text="Demarrer la partie").grid(row="4", column="1")
        
        i = 0
        scorelist = self.score.read()
        for score in sorted(scorelist, key=scorelist.get, reverse=True):
            self.scoreboard.insert(i, score)
            self.scoreboard_score.insert(i, str(scorelist[score]))
            i += 1
            
    #Renvoie la frame
    def getFrame(self):
        return self.frame