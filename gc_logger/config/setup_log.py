"""Setup Python logging to log on console and on Google Clode"""
import json
import logging
import logging.config
import os
from logging import Logger

import google.cloud.logging
from google.cloud.logging.handlers import CloudLoggingHandler


def setup_cloud_logging(logger: Logger):
    """Add Cloud Logging handler for logging on the cloud"""
    client = google.cloud.logging.Client()
    # Create a handler for Google Cloud Logging.
    cloud_handler = CloudLoggingHandler(client, name=logger.name)
    logger.addHandler(cloud_handler)


def setup_logging(path="./logging.json", default_level=logging.DEBUG):
    """Setup logging configuration"""
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
