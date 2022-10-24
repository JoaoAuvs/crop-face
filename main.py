from Imagem import *


def main(foto, colaborador):
    try:
        face = Imagem().crop_face(foto, colaborador)
        template = Imagem().write_image(colaborador)
        Imagem().join_image(template, face, colaborador)
    except Exception as e:
        print("Erro ao gerar a imagem: ", e)

if __name__ == '__main__':
    foto = "imagem.jpg"
    colaborador = "João Neto"
    main(foto, colaborador)
