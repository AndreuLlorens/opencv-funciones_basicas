import cv2

escala_de_gris = 0 #cv2.IMREAD_GRAYSCALE imagen 2D
color = -1 #cv2.IMREAD_COLOR 
alpha = 1 #cv2.IMREAD_UNCHANGED imagen 3D

def cargar_imagen(url_path, escala_color_alpha):
    img = cv2.imread(url_path, escala_color_alpha)
    return img

def ensenyar_imagen(imagen):
    cv2.imshow('Image', imagen)

def reescalar_imagen(imagen_a_modificar):
    imagen_modificada = cv2.resize(imagen_a_modificar,(100, 400), fx = 0.5, fy = 2) # fx = ancho fy = altura 
    return imagen_modificada

def rotar_imagen(imagen_a_modificar):
    imagen_modificada = cv2.rotate(imagen_a_modificar, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return imagen_modificada

def copiar_imagen_modificada(imagen):
    cv2.imwrite('nueva_cebolla.png', imagen) #IMPORTANTE PONER EL TIPO DE FORMATO DE IMAGEN

def main():
    cebolla = cargar_imagen('VCO\Practicas\Imagen\imagen_cebolla.png', escala_de_gris) #Siempre en RELATIVE PATH
    cebolla = rotar_imagen(cebolla)
    cebolla = reescalar_imagen(cebolla)
    ensenyar_imagen(cebolla)
    #copiar_imagen_modificada(cebolla)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
main()