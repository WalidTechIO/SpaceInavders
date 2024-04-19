"""
Créé par EL OUAZIZI Walid - L2 Info 5
"""

import pickle

#Simple class permettant la lecture et l'ecriture de dictionnaire

class Score(object):
    
    #Lit un dictionnaire dans score.pkl et le renvoie
    def read(self):
        with open('score.pkl', 'rb') as file:
            return pickle.load(file)
    
    #Ecrit un disctionnaire dans score.pkl
    def write(self, data):
        with open('score.pkl', 'wb') as file:
            pickle.dump(data, file)