"""
inference_service.py

Provides a service interface for running inference. Uses the Strategy pattern
to allow plugging in different detectors.
"""

import numpy as np
from typing import Dict, Any, List
from src.detectors.base_detector import BaseDetector

class InferenceService:
    def __init__(self, detector: BaseDetector):
        """
        InferenceService wraps a detector to run inference on images.
        
        :param detector: An instance of BaseDetector (e.g., YOLODetector).
        """
        self.detector = detector
    
    def run_inference(self, image: np.ndarray) -> List[Dict[str, Any]]:
        """
        Run inference using the configured detector.
        
        :param image: Numpy array of the image.
        :return: List of detections.
        """
        return self.detector.infer(image)
