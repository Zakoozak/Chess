import pygame

pygame.init()

dimensionCase= 70
class Case:
    def __init__(self,ecran,nom,x,y,couleur,piece):
        self.nom = nom
        self.x = x 
        self.y = y 
        self.piece = piece
        self.couleur =couleur
        if self.piece != "":
            image = pygame.image.load(piece).convert_alpha()
            ecran.blit(image,(self.x,self.y))#placer l'image

        pygame.draw.rect(ecran ,  (couleur),(x,y,dimensionCase,dimensionCase))

        if (piece<0): #la pièce est blanche
            txt= "images/b_"
        if ((piece)>0):#la pièce est noire
            txt = "images/w_"
        if (piece == 0 ): 
            txt = txt+"rien"
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
        
        pygame.draw.rect(ecran,(couleur),(x,y,70,70))
        pygame.display.flip()
    
    def activerCase(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()
                print (x,y)                   
                if self.x <= x <= self.x+dimensionCase and self.y <= y <= self.y+dimensionCase:
                    print (True) 


ecran = pygame.display.set_mode((700,700))

case = Case (ecran, 0,0,(100,100,100),"" )
case2 = Case (ecran, 100,100,(100,100,100),"" )

case.activerCase()
case2.activerCase()
continuer = True 
while continuer:
    case.activerCase()
    case2.activerCase()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            continuer = False
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()
            print (x,y)
    
pygame.quit()