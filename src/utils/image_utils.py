"""
image_utils.py

Utility functions for image processing, such as loading images
and preparing them for YOLO inference.
"""

import cv2
import numpy as np
from typing import Tuple

def load_image_into_numpy_array(image_path: str) -> np.ndarray:
    """Load an image from disk into a NumPy array."""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not load image at {image_path}")
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def load_image_from_bytes(image_bytes: bytes) -> np.ndarray:
    """Load an image from raw bytes into a NumPy array."""
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Could not decode image from bytes")
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
