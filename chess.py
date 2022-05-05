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

class Case: 
    def __init__(self,ecran,nom,x,y,couleur,piece):
        self.nom = nom
        self.x = x 
        self.y = y 
        self.piece = piece
        self.couleur =couleur
    


        pygame.draw.rect(ecran ,  (couleur),(x,y,dimensionCase,dimensionCase))
        txt= ""
        if (piece == 0 ): 
            return
        if (piece<0): #la pièce est blanche
            txt= "images/b_"
        if ((piece)>0):#la pièce est noire
            txt = "images/w_"
        if abs(piece)== 5 :
            txt= txt + "tower"
        if abs(piece)== 3:
            txt= txt + "bishop"
        if abs(piece)== 2:
            txt= txt + "knight"
        if abs(piece)== 9:
            txt = txt + "queen"
        if abs(piece)==50 :
            txt = txt + "king"
        if abs(piece)==1 :
            txt = txt + "pun"
        txt = txt+".png"
        
        piece = pygame.image.load(txt).convert_alpha()
        ecran.blit(piece, (self.x,self.y))
        pygame.display.flip()
        
    def getNom(self):
        return self.nom
    def activerCase(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                continuer = False
            if event.type == pygame.MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()
                print (x,y)                   
                if self.x <= x <= self.x+dimensionCase and self.y <= y <= self.y+dimensionCase:
                    print(self.nom)
                   


pygame.init()

#Constantes
dimensions =(700,700)
dimensionCase = 70
ecran = pygame.display.set_mode(dimensions)
continuer = True 
listeCases = []
nb=65
yInitial,xInitiale =100,100  # où commence le positionnement des picèces

pygame.draw.rect(ecran,(100,100,100), (0,0,800,800)) # fond d'écran 



y=yInitial
for i in range (7):
    
    x=xInitiale
    for j in range (7):
        if (i + j) %2 == 0 : couleur = (201,209,242)
        else : couleur = (89, 113, 212)
        nomCase= chr(nb)+str(j)
        case= Case(ecran,nomCase,x,y,couleur,board[i][j])
        case.activerCase()
        listeCases.append(case)
        
        # ecran.blit(piece,(x,y))#placer l'image de la pièce 
        pygame.display.flip()  # actualise    
        
        x+=dimensionCase
    nb+=1
    y+=dimensionCase
for i in range (len(listeCases)):
    print (listeCases[i].getNom)
while continuer:
    nb=65
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            continuer = False
       


pygame.quit()
