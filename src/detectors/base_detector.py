"""
base_detector.py

Defines a base class for object detectors following the Strategy pattern.
All detectors should inherit from this base class and implement the infer method.
"""

from abc import ABC, abstractmethod
import numpy as np
from typing import List, Dict

class BaseDetector(ABC):
    @abstractmethod
    def infer(self, image: np.ndarray) -> List[Dict]:
        """
        Run inference on a given image and return a list of detections.
        Each detection is a dict with keys like 'label', 'confidence', 'bbox'.
        """
        pass
