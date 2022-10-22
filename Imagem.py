import os
from datetime import datetime

import cv2
import mediapipe as mp
from matplotlib import pyplot
from PIL import Image, ImageDraw, ImageFont


class Imagem():

    def __init__(self):
        self.face_detection = mp.solutions.face_detection

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
                        pyplot.imsave('Original.jpg', imagem)
                        pyplot.imsave('{}.jpg'.format(colaborador), rosto)
        except Exception as e:
            raise (print("Erro ao gerar a imagem: ", e))