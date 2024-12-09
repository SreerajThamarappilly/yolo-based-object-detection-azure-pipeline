"""
yolo_detector.py

Implementation of a YOLO-based detector that uses the Ultralytics YOLOv5 model.
"""

from typing import List, Dict
import numpy as np
from ultralytics import YOLO
from src.detectors.base_detector import BaseDetector
from src.config import configuration

class YOLODetector(BaseDetector):
    def __init__(self, model_path: str = None):
        """
        YOLODetector is a concrete implementation of BaseDetector for YOLO.

        :param model_path: Path to the YOLO model weights.
        """
        self.model_path = model_path or configuration.MODEL_PATH
        self.model = YOLO(self.model_path)

    def infer(self, image: np.ndarray) -> List[Dict]:
        """
        Run inference using YOLOv5 model and return detections.

        :param image: A numpy array representing the image (RGB).
        :return: A list of detection dictionaries.
        """
        results = self.model.predict(image, verbose=False)
        detections = []
        for result in results:
            for box in result.boxes:
                detections.append({
                    "label": self.model.names[int(box.cls)],
                    "confidence": float(box.conf),
                    "bbox": box.xyxy[0].tolist()  # [x1, y1, x2, y2]
                })
        return detections
