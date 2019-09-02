import logging
from PIL import Image, ImageDraw, ImageFont
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s- %(levelname)s- %(message)s')

def compoe_o_texto(frase, tam_caixa_de_texto, font):

    # tam_caixa_de_texto - tupla com dois valores
    # fon - objeto fonte, deve ser criado externamente
    larg_caixa, alt_caixa = tam_caixa_de_texto
    comp_final = ""
    comp_temp = ""

    while True:
        for palavra in frase.split():
            logging.debug("\nFinal: " + comp_final + "\nTemp: " + comp_temp)
            comp_temp += " " + palavra
            if font.getsize(comp_temp)[0] > larg_caixa:
                comp_final += "\n" + comp_temp
                comp_temp = ""
        if len(comp_temp) > 0:
            comp_final += "\n" + comp_temp
        break
    return comp_final

def escreve_em_espaço_xy(img, caixa_de_texto, texto, font, tam_fonte =50, alinhamento="center", cor='black', nome_de_saida='./img.jpg'):
    # img - imagem que será usada, abre-se ou cria-se a imagem fora da função
    # caixa_de_texto - tupla de 4 número
    # texto - String
    # font - objeto fonte

    #### Trecho que define o tamanho adequado ao quadro #####
    font = ImageFont.truetype(font, tam_fonte)  # Cria o objeto fonte
    tam_fonte = caixa_de_texto[3] - caixa_de_texto[1]
    while font.getsize(texto)[0] > caixa_de_texto[2] - caixa_de_texto[0]:
        tam_fonte -= 1
        logging.debug(tam_fonte)
        font = ImageFont.truetype(font, tam_fonte)  # Cria o objeto fonte

    ##### Trecho que encaixa a fonte sobre a imagem ####
    draw = ImageDraw.Draw(img)  # Cria o objeto draw, com o objeto imagem
    tam_texto = font.getsize(texto)

    altura_da_caixa = caixa_de_texto[3] - caixa_de_texto[1]
    largura_da_caixa = caixa_de_texto[2] - caixa_de_texto[0]
    calcula_altura_da_colagem = (altura_da_caixa - tam_texto[1]) / 2 + caixa_de_texto[1] * 0.95

    if alinhamento == "left":
        local_da_colagem = (caixa_de_texto[0], calcula_altura_da_colagem)

    elif alinhamento == "center":
        local_da_colagem = ((largura_da_caixa - tam_texto[0]) / 2 + caixa_de_texto[0], calcula_altura_da_colagem)

    elif alinhamento == "right":
        local_da_colagem = ((caixa_de_texto[2] - tam_texto[0]), calcula_altura_da_colagem)

    draw.text((local_da_colagem), texto, cor, font=font)  # A primeira tupla indica o canto superior esquerdo

    img.save(nome_de_saida)

def gradient_drawn(img):
    #Entra uma imagem, retorna uma imagem com o gradiente
    img = Image.open(img)  # cria o objeto imagem
    x , y  = img.size[0], img.size[1] - int(img.size[1]/3) # x - 800 | y - 534
    cor = [0,0,0]

    linha = 10

    for linha in range(y,img.size[1]):
        for coluna in range(0, img.size[0]):
            current_pixel = img.getpixel((coluna, linha))
            img.putpixel((coluna,linha),(current_pixel[0] - cor[0],
                                         current_pixel[1] - cor[1],
                                         current_pixel[2] - cor[2]))
        cor[0] += 1
        cor[1] += 1
        cor[2] += 1

    return img






img = Image.new("RGB", (800,800),"white")  # Cria o canvas
# draw = ImageDraw.Draw(img)  # Gera objeto draw
text = "Lorem ipsum dolum sit amer inaldso souy duosy fuosdy fuosyd uofsy duoyf suody fusoy duys uariu portarium assis"
font = ImageFont.truetype('bureauGrot_medium.otf', 100) #Cria o objeto fonte
text = compoe_o_texto(text, (400,800), font)
escreve_em_espaço_xy(img, (0,0,800,800), text, 'bureauGrot_medium.otf')
print(text)




