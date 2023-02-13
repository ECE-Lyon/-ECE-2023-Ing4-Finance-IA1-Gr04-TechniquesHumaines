#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 15:31:45 2023

@author: loreafernandez
"""
import numpy as np

f1 = open("Sudoku_Easy51c.txt" , "r")
f2 = open("Sudoku_hardestc.txt" , "r")
f3 = open("Sudoku_top95c.txt" , "r")


chaine11 = f1.read()  #contient les chiffres de tous les sudoku easy
chaine21 = f2.read()  # " " hardest
chaine31 = f3.read()  # " " top

for k in range(81,162):
    chaine12 ='' + chaine11[k]  #contient uniquement les chiffres de la seconde grille easy
    chaine22 ='' + chaine21[k]  # " " " hardest
    chaine32 ='' + chaine31[k]  # " " " top

for k in range(162,243):
    chaine13 ='' + chaine11[k]  #contient uniquement les chiffres de la troisieme grille easy
    chaine23 ='' + chaine21[k]  # " " " hardest
    chaine33 ='' + chaine31[k]  # " " " top


def generate_grid_easy(): #fct appelée lorsque l'utilisateur choisit le niveau facile
    #grid = [[0 for x in range(9)] for y in range(9)]
    grid=np.zeros([9,9], dtype=int)
    
    k=0
    while(k<81):
        for i in range(9):
            for j in range(9):
                 
                 #while True:
                
                   #num = random.randint(1, 9)
                    num = chaine11[k]
                   #if is_valid(grid, i, j, num):
                    grid[i][j] = num
                   
                    #break
                    k=k+1

    return grid

def generate_grid_hardest(): #fct appelée lorsque l'utilisateur choisit le niveau moyen
    grid=np.zeros([9,9], dtype = int)
    
    k=0
    while(k<81):
        for i in range(9):
            for j in range(9):
                    if(chaine21[k]=='.'): #tranformation des '.' en 0 car nous utilisons un tab d'entiers
                        num=0
                    else: 
                        num = chaine21[k]
                    grid[i][j] = num
                    k=k+1

    return grid

def generate_grid_top(): #fct appelée lorsque l'utilisateur choisit le niveau difficile
    grid=np.zeros([9,9], dtype = int)
    
    k=0
    while(k<81):
        for i in range(9):
            for j in range(9):
                    if(chaine31[k]=='.'): 
                        num=0
                    else: 
                        num = chaine31[k]
                    grid[i][j] = num
                    k=k+1

    return grid

f1.close()
f2.close()
f3.close()


"""
def is_valid(grid, row, col, num):
    # check row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # check column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # check 3x3 subgrid
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if grid[row_start + i][col_start + j] == num:
                return False

    return True


def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True


grid = generate_grid()
print("Grille générée:")
for row in grid:
    print(row)
print()

if solve(grid):
    print("Grille résolue:")
    for row in grid:
        print(row)
else:
    print("Impossible de résoudre la grille.")

"""