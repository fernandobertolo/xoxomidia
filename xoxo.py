import logging, composer
from PIL import Image, ImageDraw, ImageFont
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s- %(levelname)s- %(message)s')



img = Image.new("RGB", (800,800),"white")  # Cria o canvas
font = ImageFont.truetype('bureauGrot_medium.otf', 100) #Cria o objeto fonte
draw = ImageDraw.Draw(img)  # Gera objeto draw
draw.rectangle([(0, 0), (200, 200)], fill="Red", outline=None) #Desenha o retangulo usando o objeto draw
img.save('testebox2.jpg')



text = "É a segunda vez que a democracia tem assento junto com o inimigo no banco dos réus"
font = ImageFont.truetype('bureauGrot_medium.otf', 50) #Cria o objeto fonte




print(composer.createChunks(text, font))