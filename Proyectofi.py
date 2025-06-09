import pygame
import random
import time
import sys

pygame.init()

ancho, alto = 800, 700
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Menú")

titulo = pygame.font.SysFont("Arial", 32)
texto = pygame.font.SysFont("Arial", 28)
font_x = pygame.font.SysFont("Arial", 40, bold=True)

blanco = (255, 255, 255)
negro = (0, 0, 0)
gris = (200, 200, 200) 
azul = (50, 150, 255)
rojo = (255, 0, 0)
verde = (0, 200, 0)

reloj = pygame.time.Clock()

class CajaTexto:
    def __init__(self, x, y, ancho, alto, etiqueta):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color = gris
        self.texto = ''
        self.etiqueta = etiqueta
        self.activa = False

    def manejarevento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            self.activa = self.rect.collidepoint(evento.pos)
            self.color = azul if self.activa else gris
        if evento.type == pygame.KEYDOWN and self.activa:
            if evento.key == pygame.K_RETURN:
                return self.texto
            elif evento.key == pygame.K_BACKSPACE:
                self.texto = self.texto[:-1]
            else:
                if len(self.texto) < 20:
                    self.texto += evento.unicode
        return None

    def dibujar(self, superficie):
        pygame.draw.rect(superficie, self.color, self.rect)
        textorenderizado = texto.render(self.texto, True, negro)
        superficie.blit(textorenderizado, (self.rect.x + 10, self.rect.y + 10))
        etiquetarenderizada = titulo.render(self.etiqueta, True, negro)
        superficie.blit(etiquetarenderizada, (self.rect.x, self.rect.y - 35))
        pygame.draw.rect(superficie, negro, self.rect, 2)

cajastexto = [
    CajaTexto(250, 60, 300, 40, "Nombre del Jugador 1:"),
    CajaTexto(250, 140, 300, 40, "Nombre del Jugador 2:"),
    CajaTexto(250, 220, 300, 40, "Rondas por jugador:"),
    CajaTexto(250, 300, 300, 40, "Tamaño de cuadros de juego:")
]

tamanoboton = pygame.Rect(300, 400, 200, 50)

ejecutando = True
datosdelmenu = ["", "", "", ""]

while ejecutando:
    pantalla.fill(blanco)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for i, caja in enumerate(cajastexto):
            resultado = caja.manejarevento(evento)
            if resultado is not None:
                datosdelmenu[i] = resultado
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if tamanoboton.collidepoint(evento.pos):
                if all(d.strip() for d in datosdelmenu):
                    try:
                        int(datosdelmenu[2])
                        int(datosdelmenu[3])
                        ejecutando = False
                    except ValueError:
                        pass

    for caja in cajastexto:
        caja.dibujar(pantalla)

    pygame.draw.rect(pantalla, azul, tamanoboton)
    texto_boton = titulo.render("Iniciar Juego", True, blanco)
    pantalla.blit(texto_boton, (tamanoboton.x + 30, tamanoboton.y + 10))

    pygame.display.flip()
    reloj.tick(30)
