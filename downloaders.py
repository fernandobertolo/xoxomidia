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


def encontra_e_salva_imagem(self, posicao_da_imagem=8):
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

    