#import numpy as np
#from matplotlib import pyplot as plt 
import cv2 as cv 

#Inicia a captura de vídeo da câmera do notebook
webcam = cv.VideoCapture(0)  #"0" indica a câmera padrão (a do notebook)

#Verifica se a câmera foi aberta com sucesso
if not webcam.isOpened():
    print("Não é possível abrir a câmera")
    exit()

#Loop para capturar e processar cada quadro de vídeo
while True:
    #Captura o quadro (frame) atual da câmera
    ret, frame = webcam.read()
    
    #Se a captura falhar, ret será False
    if not ret:
        print("Não foi possível receber o quadro (fim da transmissão?). Saindo ...")
        break

    #Converte o quadro capturado para escala de cinza
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #Detecção de bordas
    deteccaoCanny = cv.Canny(gray, 100, 200)
    
    cv.imshow('Original', gray)
    
    #Exibe o quadro com a detecção de bordas em uma outra janela
    cv.imshow('Deteccao de Bordas', deteccaoCanny)

    #Verifica se a tecla 'q' foi pressionada para encerrar o programa
    if cv.waitKey(1) == ord('q'):
        break 

#Libera a câmera e fecha as janelas quando o loop termina
webcam.release()
cv.destroyAllWindows()
