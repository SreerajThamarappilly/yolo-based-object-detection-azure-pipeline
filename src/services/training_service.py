"""
training_service.py

Provides functionality to train or fine-tune the YOLO model on a custom dataset.
This script can be run standalone to train the model.
"""

import os
from ultralytics import YOLO
from src.config import configuration
from src.utils.logging_utils import get_logger

logger = get_logger(__name__)

if __name__ == "__main__":
    # Example: train on a custom dataset
    # Ensure that src/data/training_data/dataset.yaml is properly configured
    dataset_yaml = "src/data/training_data/dataset.yaml"

    if not os.path.exists(dataset_yaml):
        raise FileNotFoundError(f"Dataset config not found at {dataset_yaml}")

    logger.info("Loading YOLO model for training...")
    model = YOLO(configuration.MODEL_PATH)  # Load pretrained weights
    logger.info("Starting training...")
    model.train(data=dataset_yaml, epochs=5, imgsz=640)
    logger.info("Training completed. Check the runs directory for results.")
