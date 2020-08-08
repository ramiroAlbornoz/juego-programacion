import pygame
def main():

    pygame.init()
    #ventana
    pantalla=pygame.display.set_mode([300,300a])
    pygame.display.set_caption("prueba pygame")
    (x,y)= (100,100)
    #colores
    blanco=(255,255,255)
    negro=(0,0,0)
    #varios
    reloj1=pygame.time.Clock()
    salir=False
    vx=0
    #imagenes
    fondo=pygame.image.load("C:/Users/ALUMNOs/Documents/programas/juego/fondo.png")
    personaje=pygame.image.load("C:/Users/ALUMNOs/Documents/programas/juego/personaje.png")
    personaje2=pygame.image.load("C:/Users/ALUMNOs/Documents/programas/juego/personaje2.png")
    #sprites
    sprite1=pygame.sprite.Sprite()
    sprite1.image=personaje
    sprite1.rect=personaje.get_rect()
    sprite1.rect.top=51
    sprite1.rect.left=57
    #------------------------------------
    #r1=pygame.Rect(50,50,45,45)
    #r2=pygame.Rect(100,100,45,45)
    #s1=pygame.Surface((100,150))
    #s1.fill(negro)
    #-------------------------------------
    while salir!=True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_d:
                    vx += 10
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    vx -= 10
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    vx=0
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_s:
                    vx=0
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_a:
                    vx=0
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_d:
                    vx=0
            #if event.type==pygame.MOUSEBUTTONDOWN:
                        #if r2.colliderect(r1):
                         #r1.inflate_ip(-1,-1)
        sprite1.rect.move_ip(vx,0)
        reloj1.tick(64)
        pantalla.fill(blanco)
        pantalla.blit(fondo,[0,0])
        pantalla.blit(sprite1.image,sprite1.rect)
        pygame.display.update()
        #-------------------------------------------
        #(xant,yant)=(r2.left,r2.top)
        #(r2.left,r2.top)=pygame.mouse.get_pos()
        #r2.left-=r2.width/2
        #r2.top-=r2.height/2
        #pygame.draw.rect(pantalla, negro, r1)
        #pygame.draw.rect(pantalla, negro, r2)
        #--------------------------------------
    pygame.quit()
main()