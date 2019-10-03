import logging
from PIL import Image, ImageDraw, ImageFont
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s- %(levelname)s- %(message)s')


text = "É a segunda vez que a democracia tem assento junto com o inimigo no banco dos réus"


##################   objeto  ########################
# teste teste aknfpisudb fisunoj



#####################################################

def defineTextSize():
    pass

def createChunks(text, font, textBoxSize=(400,800)):
    # Entra um texto e um objeto fonte e saem duas listas:
    #   Lista 1. As palavras separadas
    #   Lista 2. Tuplas com os tamanhos de cada palavra,

    # Pametros da função:
    # Text - Ums string simples
    # Font, entra um objeto fonte, no futuro está será uma função interna, por isso o tamanho é definido fora da função
    # TextBixSize = tamanho da caixa de texto onde o texto será composto

    words = []                                          # lista simples com as palavras
    words = text.split()                                # Separa a frase na lista
    chunksSizes = []                                    # lista com o tam horizontal de cada chunk/palavra

    structuredWords = []                                # Uma linha de palavras
    structuredSizes = []                                # Cada lista indica uma linha com o tamanho dos chunks



    for i in range(0,len(words)):
        words[i] = words[i]+' '                         # Readciona o espaço ao final da palavra
        chunksSizes.append(font.getsize(words[i])[0])   # Gera a lista com a largura dos chunks. A altura é definida pelo tamanho da fonte

    currentWordLine = []
    currentChunkSize = []
    counter = 0

    while counter < len(words):                      # Este laço mede os chunks e separa-os em lista diferentes, para indicar as linhas
        currentWordLine.append(words[counter])
        currentChunkSize.append(chunksSizes[counter])

        if sum(currentChunkSize) >= textBoxSize[0]:         # Se o chunk atual for maior que o box "quebra a Linha" gerando uma nova lista
            del currentWordLine[-1]
            del currentChunkSize[-1]
            structuredWords.append(currentWordLine)
            structuredSizes.append(currentChunkSize)
            currentWordLine = []
            currentChunkSize= []
        else:
            counter += 1

    return structuredWords, structuredSizes

def writeTextInABox(img, text, fontSize, boxSize, fontColor = 'white'):
    # Entra uma imagem e um texto (que será separado e processado pela função "createchunks", e sai a imagem com o texto escrito

    # img - Objeto Img.
    # text - String simples.
    # fonteSize - Valor usado para calcular tamanho da fonte e a entrelinhas.
    # box - Tupla com quatro valores, 2 para coordenas do 'x' e 2 para o 'Y'

    anchorPoint = boxSize[1]
    font = ImageFont.truetype('bureauGrot_medium.otf', fontSize)  # Cria o objeto fonte
    structuredWords, structuredSizes = createChunks(text, font) # Cria uma lista com as palavras e uma com a largura das palavras

    textLineBreak = []


    for wordSize in structuredSizes:
        counter0 = 0
        textLineBreak[counter0].append(wordSize)


    for line in textLineBreak:
        draw.text((boxSize[0], anchorPoint), ''.join(line), fontColor, font=font)

        anchorPoint += fontSize

    img.save("opa.jpg")




img = Image.new("RGB", (800,800),"Black")  # Cria o canvas

writeTextInABox(img, text, 45, (50,50,450,750))
