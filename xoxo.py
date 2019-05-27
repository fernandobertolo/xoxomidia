import logging, requests, bs4
from PIL import Image, ImageDraw, ImageFont
import composer
import os
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s- %(levelname)s- %(message)s')

class xoxomidia():

    def __init__(self, url):
        self.titulo = ""
        self.texto = ""
        self.url = url
	
	def cria_canvas(self, tamanho = (800,800)):
		#Tamanho = um tupla com dois valores
		img = Image.new("RGBA", tamanho)
		return  img


    def extrai_titulo_linha_fina(self):
        pag = requests.get(self.url)
        pag.encoding = pag.apparent_encoding
        try:
            pag.raise_for_status()
        except:
            print("Download deu merda")

        sopa = bs4.BeautifulSoup(pag.text, features="html.parser")
        titulo = sopa.find(itemprop='headline').get_text()
        linha_fina = sopa.find(itemprop='description').get_text()

        self.titulo = titulo
        self.texto = linha_fina

    def encontra_e_salva_imagem(self, posicao_da_imagem = 8):
        pag = requests.get(self.url)
        pag.encoding = pag.apparent_encoding
        try:
            pag.raise_for_status()
        except:
            print("Download deu merda")

        sopa = bs4.BeautifulSoup(pag.text, features="html.parser")
        img = sopa.find_all("img")[posicao_da_imagem]  # Esta parte do código está bem frágil !!!!!!!!!
        img = "http:" + img.attrs["src"]
        logging.debug(img)
        f = open('./01234.jpg', 'wb')
        f.write(requests.get(img).content)
        f.close()

    def escreve_em_espaço_xy(self, imagem, caixa_de_texto, texto, font, alinhamento="center", nome_de_saida='./img.jpg'):
        img = Image.open(imagem)  # Cria o objeto imagem

        #### Trecho que define o tamanho adequado ao quadro #####
        tam_fonte = caixa_de_texto[3] - caixa_de_texto[1]
        fonte = ImageFont.truetype(font, tam_fonte)  # Cria o objeto fonte
        while fonte.getsize(texto)[0] > caixa_de_texto[2] - caixa_de_texto[0]:
            tam_fonte -= 1
            logging.debug(tam_fonte)
            fonte = ImageFont.truetype(font, tam_fonte)  # Cria o objeto fonte

        ##### Trecho que encaixa a fonte sobre a imagem ####
        draw = ImageDraw.Draw(img)  # Cria o objeto draw, com o objeto imagem
        tam_texto = fonte.getsize(texto)

        altura_da_caixa = caixa_de_texto[3] - caixa_de_texto[1]
        largura_da_caixa = caixa_de_texto[2] - caixa_de_texto[0]
        calcula_altura_da_colagem = (altura_da_caixa - tam_texto[1]) / 2 + caixa_de_texto[1] * 0.95

        if alinhamento == "left":
            local_da_colagem = (caixa_de_texto[0], calcula_altura_da_colagem)

        elif alinhamento == "center":
            local_da_colagem = ((largura_da_caixa - tam_texto[0]) / 2 + caixa_de_texto[0], calcula_altura_da_colagem)

        elif alinhamento == "right":
            local_da_colagem = ((caixa_de_texto[2] - tam_texto[0]), calcula_altura_da_colagem)

        draw.text((local_da_colagem), texto, 'white', font=fonte)  # A primeira tupla indica o canto superior esquerdo

        img.save(nome_de_saida)


def compoe_o_texto(frase, tam_caixa_de_texto, fonte, tamanho_da_fonte=50):
    #tam_caixa_de_texto = tupla com dois valores
    font = ImageFont.truetype(fonte, tamanho_da_fonte)  # Cria o objeto fonte
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

def escreve_o_texto(imagem, texto, coordenada, fonte, tam_fonte):
    #cordenada = Um tupla com 2 número marcando onde o texto começa
    img = Image.open(imagem)  # Cria o objeto imagem
    draw = ImageDraw.Draw(img)  # Cria o objeto draw, com o objeto imagem
    fonte = ImageFont.truetype(fonte, tam_fonte)  # Cria o objeto fonte
    draw.text((coordenada), texto, 'white', font=fonte)  # A primeira tupla indica o canto superior esquerdo
    img.save("zeeebra.jpg")

import logging
from PIL import Image
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s- %(levelname)s- %(message)s')



img = "001.jpg"

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


gradient_drawn(img).save("teste.jpg")



texto = "O Brasil caminha para ruina ambiental a paços largos"

texto = compoe_o_texto(texto, (300,400), "Gulim.ttf")
print(texto)


escreve_o_texto("img.jpg", texto, (-20,-30), "Gulim.ttf", 50)

