import pickle

#Permet simplement d'initialiser un tableau de score vide

with open('score.pkl', 'wb') as file:
    pickle.dump({}, file)
