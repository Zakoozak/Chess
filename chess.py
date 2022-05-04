import pygame

# initialisation du plateau
def initBoard() :
    board =[[-5,-2,-3,-9,-50,-3,-2,-5],
            [-1,-1,-1,-1,-1,-1,-1,-1],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            
            [0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [5,2,3,50,9,3,2,5]]
    return board
board = initBoard()

pygame.init()
dimensions =(800,800)
ecran = pygame.display.set_mode(dimensions)
continuer = True 
y,x =100,100                    # où commence le positionnement des picèces
pygame.draw.rect(ecran,(100,100,100), (0,0,800,800))
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            continuer = False
    y,x =100,100    
    for i in range (7):
        x=0
        for j in range (7):
            if abs(board[i][j]==0): #la case est bide 
                x+=70
                continue 
            if ((board[i][j])<0): #la pièce est blanche
                txt= "images/b_"
            if ((board[i][j])>0):#la pièce est noire
                txt = "images/w_"
            if abs(board[i][j])== 5 :
                txt= txt + "tower"
            if abs(board[i][j])== 3:
                txt= txt + "bishop"
            if abs(board[i][j])== 2:
                txt= txt + "knight"
            if abs(board[i][j])== 9:
                txt = txt + "queen"
            if abs(board[i][j])==50 :
                txt = txt + "king"
            if abs(board[i][j])==1 :
                txt = txt + "pun"
    
            txt = txt+".png"
            piece = pygame.image.load(txt).convert_alpha()
            ecran.blit(piece,(x,y))#placer l'image
            pygame.display.flip()  #acctualiser    
            
            x+=70
        y+=70
            
pygame.quit()
