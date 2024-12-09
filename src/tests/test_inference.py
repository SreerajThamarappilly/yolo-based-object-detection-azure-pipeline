"""
test_inference.py

A simple test to verify the inference pipeline works.
"""

import os
import pytest
from ultralytics import YOLO
from src.detectors.yolo_detector import YOLODetector
from src.services.inference_service import InferenceService
from src.utils.image_utils import load_image_into_numpy_array

@pytest.mark.parametrize("sample_image", ["src/data/samples/sample_image.jpg"])
def test_inference_pipeline(sample_image):
    if not os.path.exists(sample_image):
        pytest.skip("Sample image does not exist.")
    
    img = load_image_into_numpy_array(sample_image)
    detector = YOLODetector()
    service = InferenceService(detector)
    detections = service.run_inference(img)
    # Just check if we get a list back
    assert isinstance(detections, list)
