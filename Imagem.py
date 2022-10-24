import os
from datetime import datetime

import cv2
import mediapipe as mp
from matplotlib import pyplot
from PIL import Image, ImageDraw, ImageFont


class Imagem():

    def __init__(self):
        self.face_detection = mp.solutions.face_detection
        self.template = "Base/Template/Novo.png"

    def crop_face(self, imagem, colaborador) -> None:
        try:
            with self.face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
                imagem = pyplot.imread(imagem)
                results = face_detection.process(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
                if results.detections:
                    for detection in results.detections:
                        x = int(detection.location_data.relative_bounding_box.xmin * imagem.shape[1])
                        y = int(detection.location_data.relative_bounding_box.ymin * imagem.shape[0])
                        w = int(detection.location_data.relative_bounding_box.width * imagem.shape[1])
                        h = int(detection.location_data.relative_bounding_box.height * imagem.shape[0])
                        crop_img = imagem[y - int(h * 0.5):y + h + int(h * 0.5), x - int(w * 0.5):x + w + int(w * 0.5)]
                        rosto = cv2.resize(crop_img, (360, 360), interpolation=cv2.INTER_AREA)
                        pyplot.imsave(f"Base/Aniversariante/Rosto_{colaborador}.png", rosto)
                        if os.path.exists(f"Base/Aniversariante/Rosto_{colaborador}.png"):
                            return f"Base/Aniversariante/Rosto_{colaborador}.png"
        except Exception as e:
            raise (print("Erro ao gerar a imagem: ", e))

    def write_image(self, colaborador):
        try:
            imagem_base = Image.open(self.template)
            draw = ImageDraw.Draw(imagem_base)
            font_nome = ImageFont.truetype(r"Base\Fonts\NotoSansJP-Bold.otf", 83)
            font_data = ImageFont.truetype(r"Base\Fonts\NotoSansJP-Bold.otf", 70)
            text_width, text_height = draw.textsize(colaborador, font_nome)
            position_nome = ((1600-text_width)/2,(1200-text_height)/2)
            draw.text(position_nome, colaborador, font=font_nome, fill = (255, 255, 255), align="center")
            dia = datetime.now().day
            mes = datetime.now().month
            position_dia = ((800-text_width)/2,(450-text_height)/2)
            draw.text(position_dia, f"{dia}", font=font_data, fill = (0, 0, 0), align="center")
            position_mes = ((1050-text_width)/2,(340-text_height)/2)
            draw.text(position_mes, f"{mes}", font=font_data, fill = (0, 0, 0), align="center")
            imagem_base.save(f"Base/Aniversariante/Template_{colaborador}.png")
            if os.path.exists(f"Base/Aniversariante/Template_{colaborador}.png"):
                return f"Base/Aniversariante/Template_{colaborador}.png"
            else:
                return self.imagem_base
        except Exception as e:
            raise (print("Erro ao escrever a imagem: ", e))

    def join_image(self, base, face, colaborador):
        try:
            # ABRE AS IMAGENS
            imagem_base = Image.open(base)
            imagem_face = Image.open(face)
            # CONVERTE AS IMAGENS PARA RGBA
            imagem = Image.new("RGBA", imagem_base.size)
            imagem.paste(imagem_face, (105, 440), imagem_face)
            imagem.paste(imagem_base, (0, 0), imagem_base)
            imagem.save(f"Base/Aniversariante/{colaborador}.png")
            if os.path.exists(f"Base/Aniversariante/Rosto_{colaborador}.png"):
                os.remove(f"Base/Aniversariante/Rosto_{colaborador}.png")
            if os.path.exists(f"Base/Aniversariante/Template_{colaborador}.png"):
                os.remove(f"Base/Aniversariante/Template_{colaborador}.png")
        except Exception as e:
            raise (print("Erro ao juntar as imagens: ", e))
