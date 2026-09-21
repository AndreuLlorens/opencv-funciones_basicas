import cv2
import numpy as np


def inicializar_camara( num_camara):
    capturar_camara = cv2.VideoCapture(num_camara)
    return capturar_camara


def encender_camara(camara):
    while True:
        funciona, frame = camara.read()
        ancho_marco = int(camara.get(3))
        alto_marco = int(camara.get(4))

        #poner imagen en hsv
        hsv_imagen_camara = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #cambio la imagen de la camara a HSV

        #arrays que indican color 
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])

        #variable sirve para filtrar pixeles (mask )
        parte_imagen = cv2.inRange(hsv_imagen_camara, lower_blue, upper_blue) #filtro solo los pixeles que sean azules para que aparezcan 

        result = cv2.bitwise_and(frame, frame, mask= parte_imagen)

        #cv2.imshow('pantalla_camara', hsv_imagen_camara) #Hay que decalar que imagen pillamos
        cv2.imshow('pantalla_camara', result) #devuelve los bits azules 

        if cv2.waitKey(1) == ord('q'): #Para salir del bucle infinito presionamos q
            break

    camara.release()


def main():
    camara_pc = inicializar_camara(0)
    encender_camara(camara_pc)
    
    cv2.destroyAllWindows()

main()