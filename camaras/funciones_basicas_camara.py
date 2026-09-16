import cv2
import numpy as np


def inicializar_camara( num_camara):
    capturar_camara = cv2.VideoCapture(num_camara)
    return capturar_camara

def dibujar_lineas_en_la_imagen(frame_camara,punto_linea_incial, punto_linea_final, color, profundidad  ):

    img_a_dibujar = cv2.line(frame_camara, punto_linea_incial, punto_linea_final, color, profundidad  ) #las lineas van de 0 a -y e de 0 a +x
    return img_a_dibujar
#otras funciones 
""""
imagen = cv2.rectangle(En que variable voy a guardar  = (x, y), radio = (x, y), color = (0-256, 0-256, 0-256), profundidad (-1 sin relleno))
imagen = cv2.circle(imagen, LO MISMO QUE EL RECTANGULO, pero el radio es de 1D es decir r = x )
"""

def poner_texto_en_pantalla(valor_a_guardar, mensaje):
    font = cv2.FONT_HERSHEY_SIMPLEX
    return cv2.putText(valor_a_guardar, mensaje, (200, 32), font, 1, (0, 0, 0), 5, cv2.LINE_AA)

def encender_camara(camara):
    while True:
        funciona, frame = camara.read()
        ancho_marco = int(camara.get(3))
        alto_marco = int(camara.get(4))


        #ENSEÑAR CAMARA BASICO
        #cv2.imshow('pantalla_camara', frame)

        #enseñar la linea
        linea = dibujar_lineas_en_la_imagen(frame, (0, 0) ,(ancho_marco, alto_marco), (255, 0 , 0), 100)
        #para varias lineas 
        linea = dibujar_lineas_en_la_imagen(frame, (0, 0) ,(ancho_marco, -alto_marco), (255, 255 , 0), 100)
        linea = poner_texto_en_pantalla(linea, 'HOLA A TODOS')
        cv2.imshow('pantalla camara', linea) #si pongo linea se dibujaran las dos lineas
        #la variable linea es un array de elementos geometricos



        #abortar camara 
        if cv2.waitKey(1) == ord('q'): #Para salir del bucle infinito presionamos q
            break
    camara.release()

def main():
    camara_pc = inicializar_camara(0)
    encender_camara(camara_pc)
    
    cv2.destroyAllWindows()

main()