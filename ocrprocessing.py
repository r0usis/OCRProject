import pytesseract as ocr
from PIL import Image
import os
import cv2

for _,_,arquivos in os.walk('./imagens'):
    print()

i = 0

while i < len(arquivos):
    imagem = cv2.imread('./imagens/' + str(arquivos[i]))

    #corta a imagem do ponto x1 ao x2 (x1:x2) e do ponto y1 ao y2 (y1:y2)
    imagemcortada = imagem[1:390, 1760:2400]
    ret, imagemlimiar = cv2.threshold(imagemcortada, 200, 255, cv2.THRESH_BINARY)
    
    textoOCR = ocr.image_to_string(imagemlimiar, lang='por')
    texto = textoOCR.split()

    numeros = []
    for palavra in texto:
        if palavra.isnumeric():
            numeros.append(int(palavra))
    
    a = numeros[0]
    numdoc = 0
    for numero in numeros:
        if numero >= a:
            numdoc = numero
        
    print("doc - " + str(numdoc))
    if numdoc != 0:
        nomeArquivo = './renomeadas/' + 'DHL_' + str(numdoc)
        cv2.imwrite('./cortadas/' + nomeArquivo + "limiar.jpg", imagemlimiar)
        cv2.imwrite(nomeArquivo + ".jpg", imagem)
    
    i+=1


    