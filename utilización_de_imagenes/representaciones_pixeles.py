import cv2
import random

def cargar_imagen(url_path, escala_color_alpha):
    img = cv2.imread(url_path, escala_color_alpha)
    return img

def ensenyar_imagen(imagen):
    cv2.imshow('Image', imagen)

def imprimir_valores_imgen(imagen):
    print(imagen)
    print(type(imagen))
    print(imagen.shape) #obtendremos altura, ancho y canales(espacio de colores) [filas, columnas, canales]

def acceder_valor_pixeles(imagen):
    print(imagen[257][45:400])

def cambiar_colores_de_los_pixeles_3D(imagen): #SOLO FUNCIONA EN 3D cuando en cargar imagen ponemos 1 IMAGEN A COLOR
    for i in range(100):
        for j in range(imagen.shape[1]):
            imagen[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

    return imagen

def cambiar_colores_de_los_pixeles_2D(imagen): #SOLO FUNCIONA EN 3D cuando en cargar imagen ponemos 0 ESCALA DE GRIS 
    for i in range(100):
        for j in range(imagen.shape[1]):
            imagen[i][j] = random.randint(0, 255)

    return imagen



def main():
    cebolla = cargar_imagen('VCO\Practicas\Imagen\imagen_cebolla.png',0)#Siempre en RELATIVE PATH SOLO FUNCIONA EN 1 
    imprimir_valores_imgen(cebolla)
    cebolla = cambiar_colores_de_los_pixeles_2D(cebolla)
    ensenyar_imagen(cebolla)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
main()