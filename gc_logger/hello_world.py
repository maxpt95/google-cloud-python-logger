"""Logs a Warning in Cloud Logging"""

import logging

import google.cloud.logging as cloud_logging

client = cloud_logging.Client()
logger = client.logger("python-logger-"+__name__)
logger.log_text("Warning World", severity="WARNING")
