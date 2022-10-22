from Imagem import *


def main(foto, colaborador):
    try:
        Imagem().crop_face(foto, colaborador)
        print("Imagem gerada com sucesso!")
    except Exception as e:
        print("Erro ao gerar a imagem: ", e)

if __name__ == '__main__':
    foto = "imagem.jpg"
    colaborador = "João"
    main(foto, colaborador)
