from PIL import Image, ImageDraw, ImageFont
import numpy as np
import textwrap

colors = {
    0: {
        'first': (239,214,236),
        'second': (255,189,221),
        'third': (106,69,105)
    },
    1: {
        'first': (193,231,230),
        'second': (189,225,225),
        'third': (63,94,91)
    },
    2: {
        'first': (227,237,180),
        'second': (213,224,159),
        'third': (96,108,38)
    },
    3: {
        'first': (235,224,255),
        'second': (227,217,247),
        'third': (63,54,73)
    },
    4: {
        'first': (234,255,224),
        'second': (227,247,217),
        'third': (58,73,54)
    },
    5: {
        'first': (255,200,200),
        'second': (251,189,189),
        'third': (156,92,92)
    },
    6: {
        'first': (255,236,177),
        'second': (250,228,157),
        'third': (138,119,60)
    },
    7: {
        'first': (237,196,179),
        'second': (231,187,169),
        'third': (119,84,70)
    },
    8: {
        'first': (255,248,214),
        'second': (246,240,208),
        'third': (128,91,16)
    },
    9: {
        'first': (255,177,182),
        'second': (246,131,140),
        'third': (192,34,45)
    },
    10: {
        'first': (255,245,236),
        'second': (246,231,219),
        'third': (181,137,109)
    },
    11: {
        'first': (220,227,230),
        'second': (204,215,220),
        'third': (79,96,105)
    },
    12: {
        'first': (208,227,243),
        'second': (217,233,247),
        'third': (54,62,73)
    },
    13: {
        'first': (255,212,207),
        'second': (252,202,196),
        'third': (204,75,58)
    }
}



""" new = Image.new(mode="RGBA", size=(1920,1080), color='#efd6ec')
addImage("overlays/matematica.png", (255, 0 , 0))

addText('ACELERAÇÃO ESCALAR', 200)

addImage("overlays/overlay.png", 0)

new.show() """


def transformar_texto(texto):
    # Converter para minúsculas
    texto = texto.lower()

    # Substituir espaços por '-'
    texto = texto.replace(' ', '-')
    texto = texto.replace(',', '')
    texto = texto.replace(':', '')

    # Tratar caracteres especiais
    # Usando uma expressão regular para substituir caracteres especiais por seus equivalentes
    caracteres_especiais = {
        'ç': 'c',
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ã': 'a',
        'ª': 'a',
        'ê': 'e',
        'ó': 'o',
        'õ': 'o',
        'â': 'a'
        # Adicione mais substituições conforme necessário
    }
    
    for caracter_especial, substituto in caracteres_especiais.items():
        texto = texto.replace(caracter_especial, substituto)

    return texto

materia = 'matematica'

def salvarImagem(text, bg, second, third):
    def addImage(img, color):
        image = Image.open(img)
        image = image.convert("RGBA")
        if color != 0:
            substitute_color = color

            image_data = np.array(image)
            red, green, blue, alpha = image_data.T
            white_areas = (red == 0) & (blue == 0) & (green == 0)
            image_data[..., :-1][white_areas.T] = substitute_color

            image = Image.fromarray(image_data)

        new.paste(image, (0,0), image)

    def addText(info, pixels, color):
        def create_image(size, message, font, fontColor):
            W, H = size
            image = Image.new('RGBA', size)
            draw = ImageDraw.Draw(image)
            _, _, w, h = draw.textbbox((0, 100), message, font=font)
            draw.text(((W-w)/2, (H-h)/2), message, font=font, fill=fontColor, align='center')
            return image

        myFont = ImageFont.truetype('Roboto-Black.ttf', pixels)
        myMessage = info
        myMessageWrap = textwrap.wrap(myMessage, width=15)

        text = ''
        for line in myMessageWrap:
            text = text+'\n'+line
        text = text[1:]
        myImage = create_image((1920, 1080), text, myFont, color)
        new.paste(myImage, (0,0), myImage)
        
    new = Image.new(mode="RGBA", size=(1920,1080), color=bg)
    addImage("overlays/"+materia+".png", second)

    addText(text, 200, third)

    addImage("overlays/overlay.png", 0)

    new.save('output/'+transformar_texto(text)+'.png', 'PNG')

with open('lista.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

count = 0
for linha in linhas:
    salvarImagem(linha.strip(), colors[count]['first'], colors[count]['second'], colors[count]['third'])
    new = ''

    count = count + 1
    if(count >= len(colors)):
        count = 0
