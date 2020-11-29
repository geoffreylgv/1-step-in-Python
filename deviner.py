#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random;

#! give me chance to be delighted in py 
# i'm A. Geoffrey Logovi, here i start in python program

print("\t\t\t\t\t\t OK WE GO");
print("\t\t===========================================================");
print("\t JEU DEVINER LE NOMBRE ECRIT EN PYTHON : RAPPEL PREMIER PAS AVEC PYTHON\n");

print(" Objectif : Trouver le nombre aléatoire entre 1 et 50");

print(" \n\t\t PS: Essaie illimités\n");

nombre_a = random.randint(1,50);
#print(nombre_a);
nombre_u = 0;

nombre_coup = 0;
nombre_vie = 10;
start = 0;

while nombre_u != nombre_a:
    
    
    nombre_tmp = input("Entrer votre nombre ");
    
    nombre_u = int(nombre_tmp);
    if nombre_a > nombre_u:
        print("C'est plus");
    elif nombre_a < nombre_u:
        print("C'est moins");
    else:
        print("Bravo ! Vous avez gagné");
    nombre_coup +=1;

print("\t===========Essaie en ", nombre_coup, "coups =====");    
print("\t================Fin=======");

