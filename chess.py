from tkinter import E
import numpy as np
import pygame

# initialisation board

def emptyBoard():
    emptyBoard =  [[0, 0, 0, 0, 0, 0, 0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0], 
            
            [0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0]]
    return emptyBoard

def tradBoard(listeCases):
    emptyBoard= emptyBoard()
    return np.reshape(listeCases,8,8)

def initBoard() :  
    board =[[-5,-2,-3,-9,-50,-3,-2,-5],
            [-1,-1,-1,-1,-1,-1,-1,-1],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [5,2,3,50,9,3,2,5]]
    return board
board = initBoard()


def drawBoard(board):
    listeCases=[]
    letter=65 # ASCII CODE for letter A, will be usefull for piece name
    number=8  #number's name  of piece (will begin to A8, B8 , C8, ... ,A1)
    x,y= xInitiale,yInitial
    
    for i in range (8):
        x=xInitiale
        for j in range(8):
            
            if (i + j) %2 == 0 : couleur = (201,209,242) # color
            else : couleur = (89, 113, 212) # color
            
            nomCase= chr(letter)+str(number)## case name ( to get the name from A8 to H1)
            letter+=1 ##increase the letter for name 
            
            case= Case(ecran,nomCase,x,y,couleur,board[i][j]) #creation of the case
            listeCases.append(case)
            
            
            x+=dimensionCase #increase of case dimension for placement
            pygame.display.flip()  # actualise   
        number-=1  ## piece number update 
        y+=dimensionCase #y update  
        letter=65 #piece letter reinitialisation
    return listeCases

class Case: 
    def __init__(self,ecran,nom,x,y,color,piece):
        self.nom = nom
        self.x = x 
        self.y = y 
        self.piece = piece
        self.color =color

### load piece
        pygame.draw.rect(ecran ,  (color),(x,y,dimensionCase,dimensionCase)) #tuile color 
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
    
    def activeCase(self,event):
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            continuer = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()               
            if self.x <= x <= self.x+dimensionCase and self.y <= y <= self.y+dimensionCase: # if cursos in case , return the name of the case
                print(self.nom)

def deplacement(case1, case2):
    
    for i in range (len(listeCases)):
            if listeCases[i].nom == case1 :
                caseA=listeCases[i]
            elif listeCases[i].nom == case2 :
                caseB=listeCases[i]
    #A8
    caseC= caseA.piece
    caseA.piece=0  

    depart= None
    for i in range (len(listeCases)):
        if listeCases[i].nom== case1:
            depart =i
            break
    departX = depart//8 
    departy = depart%8
    board[departX][departy] = 0
    
    #A6
    arrive  = None
    caseB.piece= caseA.piece
    for i in range (len(listeCases)):
        if listeCases[i].nom== case2:
            arrive =i
            break
    arriveX = arrive//8 
    arriveY = arrive%8
    board[arriveX][arriveY] = caseC


pygame.init()

#Constantes
dimensions =(700,700)
dimensionCase = 70
ecran = pygame.display.set_mode(dimensions)
continuer = True 
listeCases = [] # array of cases I will create 
letter=65 # ASCII CODE for letter A, will be usefull for piece name
number=8  #number's name  of piece (will begin to A8, B8 , C8, ... ,A1)
yInitial,xInitiale =100,100  # where begins the piece's placement
pygame.draw.rect(ecran,(100,100,100), (0,0,800,800)) # background

listeCases = drawBoard(board)
while continuer:
    letter=65 # ASCII CODE for letter A, will be usefull for piece name
    number=8  #number's name  of piece (will begin to A8, B8 , C8, ... ,A1)
    x,y= xInitiale,yInitial
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == pygame.KEYDOWN:
            
            deplacement("A1","D4")
            drawBoard(listeCases)
        for case in listeCases : 
            case.activeCase(event)



pygame.quit()
