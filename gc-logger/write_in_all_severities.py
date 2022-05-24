"""Write in log using all severity lvls"""

import logging

import setup_log

logger = logging.getLogger(__name__)
setup_log.setup_cloud_logging(logger)


def write() -> None:
    logger.info("Writing in all severities: ")
    logger.debug("This is DEBUG")
    logger.info("This is INFO")
    logger.warning("This is WARNING")
    logger.error("This is ERROR")
