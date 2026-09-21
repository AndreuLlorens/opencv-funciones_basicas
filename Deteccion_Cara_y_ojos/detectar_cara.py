import cv2
import numpy as np
import os
from collections import namedtuple

#estructura global de datos 
Elementos_cara = namedtuple('Elmentos_cara', ['cara', 'ojos'])

""""
SI SE USA EN OTRO DISPOSITIVO CAMBIAR LA RUTA.
EL FICHERO ESTA EN EL REPOSITORIO JUNTO AL CODIGO
https://github.com/opencv/opencv/tree/4.x 
"""


CARPETA_XML = MY_PATH
el = Elementos_cara(
    cv2.CascadeClassifier(CARPETA_XML + 'haarcascade_frontalface_default.xml'),
    cv2.CascadeClassifier(CARPETA_XML + 'haarcascade_eye.xml')
)




def inicializar_camara( num_camara):
    capturar_camara = cv2.VideoCapture(num_camara)
    return capturar_camara

def encender_camara(camara):
    while True:
        funciona, frame = camara.read()
        if not funciona:
            break

        #convierto la imagen de la camara en gris
        imagen_en_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        rectangulos_caras = el.cara.detectMultiScale(imagen_en_gris, 1.3, 5)
        for (x_rectangulo, y_rectangulo, w_rectangulo, h_rectangulo) in rectangulos_caras:
            cv2.rectangle(frame, (x_rectangulo, y_rectangulo), 
                        (x_rectangulo + w_rectangulo, y_rectangulo + h_rectangulo), (255,0,0), 5)
            roi_gray = imagen_en_gris[y_rectangulo:y_rectangulo+h_rectangulo, x_rectangulo:x_rectangulo + w_rectangulo]
            roi_color = frame[y_rectangulo:y_rectangulo+h_rectangulo, x_rectangulo:x_rectangulo + w_rectangulo]

            ojo = el.ojos.detectMultiScale(roi_gray, 1.3, 5)
            for (ojox, ojoy, ojow, ojoh) in ojo:
                cv2.rectangle(roi_color, (ojox, ojoy), (ojox + ojow, ojoy + ojoh), (0, 255, 0), 5)

        cv2.imshow('pantalla_camara', frame)

        #abortar camara 
        if cv2.waitKey(1) == ord('q'): #Para salir del bucle infinito presionamos q
            break
    camara.release()

def main(args = None):
    camara_pc = inicializar_camara(0)
    encender_camara(camara_pc)
        
    cv2.destroyAllWindows()

main()