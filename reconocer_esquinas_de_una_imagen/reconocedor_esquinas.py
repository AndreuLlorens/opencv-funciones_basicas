import cv2 
import numpy as np 

def cargar_imagen(url_path):
    img = cv2.imread(url_path)
    return img

def ensenyar_imagen(imagen):
    cv2.imshow('Image', imagen)


def reescalar_imagen(imagen_a_modificar, ancho, alto):
    imagen_modificada = cv2.resize(imagen_a_modificar,(0, 0), fx = float(ancho), fy = float(alto)) # fx = ancho fy = altura 
    return imagen_modificada

def convertir_imagen_a_gris(imagen_a_modificar):
    imagen_a_modificar = cv2.cvtColor(imagen_a_modificar, cv2.COLOR_BGR2GRAY)
    return imagen_a_modificar 

            
def reconocer_esquina(imagen, maxNumerodeesquinas, minCalidadEsquinas, distancia_minima_entre_esquinas):
    esquinas = cv2.goodFeaturesToTrack(imagen, maxNumerodeesquinas, minCalidadEsquinas, float(distancia_minima_entre_esquinas)) #distancia euceldiana Raiz(x^2+y^2) x= x2-x1 y=y2-y1
    esquinas = esquinas.astype(np.int32) 
    return esquinas #me va a devolver un array donde estan la posicion de las esquinas 

def dibujar_circulos_en_las_esquinas(num_esquinas, imagen, radio, color, relleno):
    for num_esquinas in num_esquinas:
        #x = num_esquinas[0]
        #y = num_esquinas[1]
        x,y = num_esquinas.ravel() #[[1, 2], [2, 1] -< [1, 2, 2, 1]
        cv2.circle(imagen, (x, y), radio, color, relleno )
    return imagen

def cerrar_la_figura_acotada_por_los_circulos(imagen, num_esquinas):
    for i in range(len(num_esquinas)):
        for j in range(i + 1, len(num_esquinas)):
            esquina_1 = tuple(num_esquinas[i][0])
            esquina_2 = tuple(num_esquinas[j][0])
            color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size = 3)))
            cv2.line(imagen, esquina_1, esquina_2, color, 1)
    return imagen

def main():
    cebolla = cargar_imagen("VCO\opencv_funciones\Imagen_de_la_cebolla\imagen_cebolla.png")
    cebolla = reescalar_imagen(cebolla, 0.75, 0.75)
    cebolla = convertir_imagen_a_gris(cebolla)

    #para reconcer esquinas hay que convertir la imagen a escala de grises
    num_esquinas = reconocer_esquina(cebolla, 100, 0.01, 10)
    print(num_esquinas)

    cebolla = dibujar_circulos_en_las_esquinas(num_esquinas, cebolla, 5, (255, 0, 0), -1)
    cebolla = cerrar_la_figura_acotada_por_los_circulos(cebolla, num_esquinas)
    ensenyar_imagen(cebolla)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()