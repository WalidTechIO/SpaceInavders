<!-- omit in toc -->
# Rapport de developpement SpaceInvaders EL OUAZIZI Walid
<!-- omit in toc -->
## Sommaire
- [Introduction](#introduction)
- [Points de développement sur le defender](#points-de-développement-sur-le-defender)
- [Points de développement sur les aliens](#points-de-développement-sur-les-aliens)
- [IA des aliens](#ia-des-aliens)
- [Conclusion](#conclusion)


## Introduction
Le jeu Space Invaders est un classique des jeux vidéo d'arcade des années 80.  
Il consiste à défendre sa base contre une invasion d' aliens en utilisant un vaisseau appelé "defender".  
Le but est de détruire tous les aliens avant qu'ils ne parviennent à atteindre le sol ou que le joueur ne perde toutes ses vies.
Dans ce rapport, nous allons présenter notre version du jeu Space Invaders en Python avec l'aide de la bibliothèque TKinter pour l' interface graphique. Nous allons également discuter de l'intelligence artificielle (IA) des aliens et des points de développement sur le defender et les aliens.

## Points de développement sur le defender
Nous avons ajouté plusieurs fonctionnalités au defender pour améliorer l'expérience de jeu. Tout d' abord, le defender peut maintenant tirer plusieurs missiles à la fois en appuyant sur la touche "espace" de façon continue. Cela permet au joueur de détruire plusieurs aliens à la fois et d'augmenter ses chances de gagner. De plus, le Defender a des points de vies, mais si il est touché de nombreuses fois par les tirs Alien, la partie est perdue

## Points de développement sur les aliens
Pour rendre les aliens plus difficiles à battre, nous avons ajouté plusieurs niveaux de vie à chaque alien. Lorsqu'un alien est touché par un missile du defender il perd 1 vie. Si les vies d'un Alien arrivent à 0 alors l'Alien est supprimé

## IA des aliens
L'IA des aliens dans notre version du jeu Space Invaders est conçue pour imiter le comportement des aliens dans le jeu original. Les aliens se déplacent en flotte(Fleet) en avançant vers le bas de l' écran et en changeant de direction lorsqu'ils atteignent les bords. Ils peuvent également tirer des missiles aléatoirement vers le defender.

## Conclusion
Notre version du jeu Space Invaders en Python avec TKinter est un projet passionnant qui nous a permis de mettre en pratique nos connaissances en programmation et en IA. L'IA des aliens est une des principales parties du jeu et nous avons travaillé dur pour qu' elle soit la plus réaliste possible. Nous avons également amélioré le defender en ajoutant des fonctionnalités telles que la possibilité de tirer plusieurs missiles à la fois.