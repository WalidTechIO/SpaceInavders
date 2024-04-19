"""
Créé par EL OUAZIZI Walid - L2 Info 5
"""

import Bullet as blt

#Modification de la classe Bullet pour gerer les deplacement vers le bas
class AlienBullet(blt.Bullet):
    def __init__(self, shooter):
        super().__init__(shooter)
        self.color = "green"
        
    def move_in(self, canvas):
        yT = (canvas.coords(self.id)[1])
        if(yT > 599):
            canvas.delete(self.id)
            self.shooter.fired_bullets.remove(self)
        canvas.move(self.id, 0, self.speed)