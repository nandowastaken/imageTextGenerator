from PIL import Image, ImageDraw, ImageFont, ImageOps

# configurações de tela
width = 512
height = 300
BORDERSIZE = 20

# configurações de mensagem
messages = ["Eletrotécnica", "Eletrônica", "Informática"] 
FONTSIZE = 44
imgNumber = 0


for message in messages:
    font = ImageFont.truetype("arial.ttf", size=FONTSIZE)
    img = Image.new('RGB', (width, height), color='white')
    imgDraw = ImageDraw.Draw(img)

    # centraliza o texto
    textwidth, textHeight = imgDraw.textsize(message, font=font)
    xText = (width - textwidth) / 2
    yText = (height - textHeight) / 2

    imgDraw.text((xText, yText), message, font=font, fill=(0, 0, 0))

    img = ImageOps.expand(img, border=BORDERSIZE, fill='black')

    img.save(f'images/image{imgNumber}.png')
    imgNumber += 1