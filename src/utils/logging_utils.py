"""
logging_utils.py

Provides a simple utility function to configure and retrieve a logger.
"""

import logging
from src.config import configuration

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, configuration.LOG_LEVEL.upper(), logging.INFO))
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
    ch.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(ch)
    return logger
