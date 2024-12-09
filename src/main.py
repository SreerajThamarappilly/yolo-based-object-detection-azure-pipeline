"""
main.py

FastAPI application entrypoint. It uses the InferenceService and YOLODetector to serve inference requests.
"""

import io
from fastapi import FastAPI, File, UploadFile
from starlette.responses import JSONResponse

from src.detectors.yolo_detector import YOLODetector
from src.services.inference_service import InferenceService
from src.utils.image_utils import load_image_from_bytes
from src.utils.logging_utils import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title="Advanced YOLO-based Object Detection API",
    version="1.0.0",
    description="An advanced YOLO-based object detection service."
)

# Initialize detector and inference service
yolo_detector = YOLODetector()
inference_service = InferenceService(detector=yolo_detector)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/infer")
def infer(file: UploadFile = File(...)):
    """
    Inference endpoint. Upload an image and get detected objects.
    """
    logger.info("Received inference request.")
    image_bytes = file.file.read()
    image = load_image_from_bytes(image_bytes)
    detections = inference_service.run_inference(image)
    return JSONResponse(content={"detections": detections})
