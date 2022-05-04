import pygame

# initialisation du plateau
board =[[-5,-3,-3,-9,-50,-3,-3,-5],
        [-1,-1,-1,-1,-1,-1,-1,-1],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [5,3,3,50,9,3,3,5]]

pygame.init()
dimensions =(800,800)
ecran = pygame.display.set_mode(dimensions)

continuer = True 

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            continuer = False
    
    for i in range (8):
        for j in range (8):
            if ((board[i][j])<0):
                txt= "b_"
            if ((board[i][j])>0):
                txt = "w_"
            if ((board[i][j])== )
    pygame.display.update()
pygame.quit()
